# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
from urllib.parse import urlencode


data = {
    "orderId": "", 
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data=data, access_token=access_token):
    """
    确认收货
    /mgmt/inventory/dis/mortgage/exchangeOrder/confirm
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/confirm"
    headers = {"Authorization": f"bearer {access_token}", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
