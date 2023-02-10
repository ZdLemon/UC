# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "storeCode": "902063"  # str服务中心编号
}

def _mgmt_store_searchByStoreCode(params=params, access_token=access_token):
    """
    通过storeCode获取相关信息(新建合同搜索需要)
    /mgmt/store/searchByStoreCode
    """

    url = f"{BASE_URL}/mgmt/store/searchByStoreCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
