# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "combineId": "", # 套装组合id
    "combineNum": 2 # 套装组合数量
}


def _mgmt_inventory_combine(data=data, access_token=access_token):
    """
    套装组合
    /mgmt/inventory/combine
    """

    url = f"{BASE_URL}/mgmt/inventory/combine"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
