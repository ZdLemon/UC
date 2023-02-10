# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests


params = {
    "storeCode": store,
    "keyword": productCode,
    "pageSize": 20,
    "pageNum": 1,
}

def _mgmt_inventory_order_searchProductsForAddPage(params=params, access_token=access_token):
    """
    新增押货单页面:根据产品关键字搜索普通商品列表
    /mgmt/inventory/order/searchProductsForAddPage
    """

    url = f"{BASE_URL}/mgmt/inventory/order/searchProductsForAddPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
