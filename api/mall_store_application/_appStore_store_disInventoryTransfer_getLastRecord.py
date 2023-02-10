# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "storeCode": store_85
}


def _appStore_store_disInventoryTransfer_getLastRecord(params=params, access_token=access_token):
    """
    根据服务中心查询最新库存转移记录
    /appStore/store/disInventoryTransfer/getLastRecord
    """

    url = f"{BASE_URL}/appStore/store/disInventoryTransfer/getLastRecord"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
