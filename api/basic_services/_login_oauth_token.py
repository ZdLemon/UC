
from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, username

import requests


def _login_oauth_token(username=username, password="888888"):
    """登录接口

    Args:
        username (_type_, optional): _description_. Defaults to username.
        password (_type_, optional): _description_. Defaults to password.
        channel (_type_, optional): _description_. Defaults to CHANNEL01.

    Returns:
        _type_: _description_
    """  
    url = f"{BASE_URL}/login/oauth/token"
    headers = {"Authorization": "Basic cG9ydGFsX2FwcDpwZXJmZWN0X3BvcnRhbA==", "Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": username, "password": password, "grant_type": "password"}

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:  
        logger.debug(data_msg(r, data))
        return r

