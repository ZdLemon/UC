# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_home_getLogoConfig(access_token=access_token):
    """
    获取logo配置
    /mobile/home/getLogoConfig
    """

    url = f"{BASE_URL}/mobile/home/getLogoConfig"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
