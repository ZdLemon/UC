# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "orderId": ""
}

def _mgmt_inventory_order_getOrderDetail(params=params, access_token=access_token):
    """
    后台获取押货单详情
    /mgmt/inventory/order/getOrderDetail
    """

    url = f"{BASE_URL}/mgmt/inventory/order/getOrderDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
