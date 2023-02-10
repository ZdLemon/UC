# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85
import requests
import uuid
import time


data = {
    "storeCode": store_85, # 服务中心编号
    "query":"", # 搜索条件
    "pageNum":1,
    "pageSize":10000,
    "productNumQuery": 2 # 传1大于0;0等于0;-1小于0;2不为0;不传为查全部
}


def _appStore_store_disInventoryTransfer_addTransferList(data=data, access_token=access_token):
    """
    库存列表
    /appStore/store/disInventoryTransfer/addTransferList
    """

    url = f"{BASE_URL}/appStore/store/disInventoryTransfer/addTransferList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
