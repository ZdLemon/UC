# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


data = {
    "storeCode": "", # 服务中心编号
    "pageSize": 10, 
    "pageNum": 1,
}


def _mgmt_inventory_disInventoryTransfer_inventoryTotalMsg(data=data, access_token=access_token):
    """
    库存信息合计
    /mgmt/inventory/disInventoryTransfer/inventoryTotalMsg
    """

    url = f"{BASE_URL}/mgmt/inventory/disInventoryTransfer/inventoryTotalMsg"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
