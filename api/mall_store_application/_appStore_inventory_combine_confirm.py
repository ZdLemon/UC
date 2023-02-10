# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh
import requests
import uuid
import time
from urllib.parse import urlencode


data = {
	"combineId": "", # 套装组合id
	"combineNum": None, # 套装组合数量
	"productCode": productCode_zh
}


def _appStore_inventory_combine_confirm(data=data, access_token=access_token):
    """
    确认套装组合
    /appStore/inventory/combine/confirm
    """

    url = f"{BASE_URL}/appStore/inventory/combine/confirm"
    headers = {"Authorization": f"bearer {access_token}", "content-type": "application/x-www-form-urlencoded"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
