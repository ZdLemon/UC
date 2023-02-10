# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "storeCode": store_85  # str服务中心编号
}


def _mgmt_inventory_disInventoryTransfer_getLastRecord(params=params, access_token=access_token):
    """
    根据服务中心查询最新库存转移记录
    /mgmt/inventory/disInventoryTransfer/getLastRecord
    """

    url = f"{BASE_URL}/mgmt/inventory/disInventoryTransfer/getLastRecord"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
