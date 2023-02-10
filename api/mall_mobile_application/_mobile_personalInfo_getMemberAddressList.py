# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_personalInfo_getMemberAddressList(access_token=access_token):
    """
    获取当前登录用户的配送地址列表接口
    /mobile/personalInfo/getMemberAddressList
    """

    url = f"{BASE_URL}/mobile/personalInfo/getMemberAddressList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
