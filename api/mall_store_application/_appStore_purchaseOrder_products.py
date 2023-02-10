# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "pageNum": 1,
    "pageSize": 40,
    "product": productCode
}

def _appStore_purchaseOrder_products(params=params, access_token=access_token):
    """
    提交押货单页面的押货商品搜索
    /appStore/purchaseOrder/products
    """

    url = f"{BASE_URL}/appStore/purchaseOrder/products"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
