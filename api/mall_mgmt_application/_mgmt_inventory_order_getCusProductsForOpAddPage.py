# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests
import time
import calendar


params = {
    "keyword": "", # 一或二级商品关键字
    "storeCode": store # 服务中心编号
}


def _mgmt_inventory_order_getCusProductsForOpAddPage(params=params, access_token=access_token):
    """
    运营后台提交定制品押货单页面的押货商品搜索列表
    /mgmt/inventory/order/getCusProductsForOpAddPage
    """

    url = f"{BASE_URL}/mgmt/inventory/order/getCusProductsForOpAddPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
