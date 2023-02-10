# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "orderId":"317", # 押货或售后单id
    "content":"222222222" # 审批内容
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, access_token=access_token):
    """
    添加审批意见
    /mgmt/inventory/dis/mortgage/exchangeOrder/opinion
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/opinion"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
