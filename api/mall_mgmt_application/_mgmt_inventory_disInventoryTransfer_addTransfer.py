# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


data = {
    "applyType": "2", # 提交途径 1门店提交 2后台提交
    "storeCode": store_85, # 服务中心编号
    "productList":[
        {
            "transferNum":1, # 转移数量
            "oneThreePrice":25, # 1:3押货价
            "eightFivePrice":64, # 85折押货价
            "productCode":"ACC" # 产品编号
        }
    ]
}


def _mgmt_inventory_disInventoryTransfer_addTransfer(data=data, access_token=access_token):
    """
    新建库存转移
    /mgmt/inventory/disInventoryTransfer/addTransfer
    """

    url = f"{BASE_URL}/mgmt/inventory/disInventoryTransfer/addTransfer"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
