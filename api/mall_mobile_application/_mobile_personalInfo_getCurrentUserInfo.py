# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mobile_personalInfo_getCurrentUserInfo(access_token=access_token):
    """
    个人用户信息接口
    /mobile/personalInfo/getCurrentUserInfo
    """

    url = f"{BASE_URL}/mobile/personalInfo/getCurrentUserInfo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r