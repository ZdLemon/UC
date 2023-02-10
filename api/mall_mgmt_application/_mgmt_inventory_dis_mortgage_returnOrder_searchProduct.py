# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time
import calendar


params = {
    "productCode": productCode, # 商品编号
    "storeCode": store_85
}

def _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params=params, access_token=access_token):
    """
    商品编码搜索退货商品信息
    /mgmt/inventory/dis/mortgage/returnOrder/searchProduct
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/searchProduct"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
