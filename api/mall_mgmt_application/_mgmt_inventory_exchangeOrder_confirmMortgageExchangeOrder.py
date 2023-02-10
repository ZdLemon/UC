# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"id": "1270733832147098709", # 换货单id
}


def _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder(data, access_token=access_token):
    """
    后台押货换确认收货
    /mgmt/inventory/exchangeOrder/confirmMortgageExchangeOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/confirmMortgageExchangeOrder"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
