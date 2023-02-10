
from util.login_rsakey import login_rsakey
from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY, URL, JOB_USER, JOB_PASSWORD

import requests


def xxl_job_admin_login(username=JOB_USER, password=JOB_PASSWORD, ifRemember="on"):
    """定时调度任务登录接口

    Args:
        username (_type_, optional): _description_. Defaults to username.
        password (_type_, optional): _description_. Defaults to password.
        channel (_type_, optional): _description_. Defaults to CHANNEL01.
        authorization

    Returns:
        _type_: _description_
    """  
    url = f"{URL}/login"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "userName": username,
        "password": password,
        "ifRemember": ifRemember
    }

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:  
        logger.debug(data_msg(r, data))       
        return r


