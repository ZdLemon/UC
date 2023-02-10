# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "orderId": "1270733832147098701", # 押货或售后单id
    "content": "1111111111111111111111" # 审批内容
}


def _mgmt_inventory_exchangeOrder_addOpinion(data=data, access_token=access_token):
    """
    后台押货换货添加审批意见
    /mgmt/inventory/exchangeOrder/addOpinion
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/addOpinion"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
