# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "storeCode": None, # 服务中心编号
} 


def _mgmt_inventory_common_getStoreSimpleInfo(params=params, access_token=access_token):
    """
    获取服务中心简单信息
    /mgmt/inventory/common/getStoreSimpleInfo
    """

    url = f"{BASE_URL}/mgmt/inventory/common/getStoreSimpleInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
