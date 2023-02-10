# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username, username_85

import requests


params = {
    "queryName": None, # 搜索字段 服务中心名称/编号
    "cityCode": None, # 城市code
    "address": None,
    "pageSize": 10,
    "pageNum": 1,
    "sort": 1
}


def _mobile_order_checkout_params_getWebSearchStoreList(params=params, access_token=access_token):
    """
   	WEB搜索服务中心
    /mobile/order/checkout-params/getWebSearchStoreList
    """

    url = f"{BASE_URL}/mobile/order/checkout-params/getWebSearchStoreList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
