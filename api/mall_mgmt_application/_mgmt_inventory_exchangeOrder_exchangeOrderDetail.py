# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "orderId": None, # 
}


def _mgmt_inventory_exchangeOrder_exchangeOrderDetail(params=params, access_token=access_token):
    """
    后台押货换货单详情
    /mgmt/inventory/exchangeOrder/exchangeOrderDetail
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/exchangeOrderDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
