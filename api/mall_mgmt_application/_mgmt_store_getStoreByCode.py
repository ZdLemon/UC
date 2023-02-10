# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "code" : store_85,  # 服务中心编号
}

def _mgmt_store_getStoreByCode(params=params, access_token=access_token):
    """
    根据服务中心编号获取服务中心
    /mgmt/store/getStoreByCode
    """

    url = f"{BASE_URL}/mgmt/store/getStoreByCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
