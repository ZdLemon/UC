# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "orderId":"336", # 换货单id
    "deliverTime":"2022-07-07 11:52:53", # 发货时间
    "deliverType":2, # 发货方式 1顾客自提 2邮寄
    "expressCompany":"小河物流", # 新品配送物流公司
    "expressNo":"123456789" # 物流单号
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data=data, access_token=access_token):
    """
    发货
    /mgmt/inventory/dis/mortgage/exchangeOrder/deliver
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/deliver"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
