# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "storeCode": store_85,
    "keyword": "", # 关键字
    "pageSize": 20,
    "pageNum": 1
}

def _mgmt_inventory_dis_mortgage_order_searchProductPage(params=params, access_token=access_token):
    """
    关键字搜索可押货商品分页
    /mgmt/inventory/dis/mortgage/order/searchProductPage
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/searchProductPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
