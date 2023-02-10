# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


def _appStore_store_info(access_token=access_token):
    """
    服务中心查看基础信息
    /appStore/store/info
    """

    url = f"{BASE_URL}/appStore/store/info"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
