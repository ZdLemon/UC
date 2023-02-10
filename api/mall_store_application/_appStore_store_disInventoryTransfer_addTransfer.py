# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85
import requests
import uuid
import time


data = {
    "applyType": 1, # 提交途径 1门店提交 2后台提交
    "productList":[
        {
            "eightFivePrice":0, # 85折押货价
            "oneThreePrice":40, # 1:3押货价
            "productCode":"ACC", # 产品编号
            "transferNum":1 # 转移数量
        }
    ],
    "storeCode": store_85 # 服务中心编号
}


def _appStore_store_disInventoryTransfer_addTransfer(data=data, access_token=access_token):
    """
    新建库存转移记录
    /appStore/store/disInventoryTransfer/addTransfer
    """

    url = f"{BASE_URL}/appStore/store/disInventoryTransfer/addTransfer"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
