# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests


params = {
    "storeCode": store
}

def _mgmt_inventory_common_getStoreInfo(params=params, access_token=access_token):
    """
    获取服务中心信息
    /mgmt/inventory/common/getStoreInfo
    """

    url = f"{BASE_URL}/mgmt/inventory/common/getStoreInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
