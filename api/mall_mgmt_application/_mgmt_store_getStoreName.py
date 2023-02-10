# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "storeCode" : "",
}

def _mgmt_store_getStoreName(params=params, access_token=access_token):
    """
    根据服务中心编号获取服务中心名称(正常服务中心)
    /mgmt/store/getStoreName
    """

    url = f"{BASE_URL}/mgmt/store/getStoreName"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
