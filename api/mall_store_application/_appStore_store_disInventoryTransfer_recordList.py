# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85
import requests
import uuid
import time


data = {
    "storeCode": store_85,
    "pageNum":1,
    "pageSize":20
}


def _appStore_store_disInventoryTransfer_recordList(data=data, access_token=access_token):
    """
    库存转移记录列表
    /appStore/store/disInventoryTransfer/recordList
    """

    url = f"{BASE_URL}/appStore/store/disInventoryTransfer/recordList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
