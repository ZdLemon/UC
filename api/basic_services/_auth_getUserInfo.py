# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _auth_getUserInfo(access_token=access_token):
    """
    获取当前用户登录缓存信息
    /auth/getUserInfo
    """

    url = f"{BASE_URL}/auth/getUserInfo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
