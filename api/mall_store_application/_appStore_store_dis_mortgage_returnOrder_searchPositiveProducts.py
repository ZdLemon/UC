# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "pageNum": 1,
    "pageSize": 20,
    "product": None # 商品
}

def _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts(params=params, access_token=access_token):
    """
    获取服务中心正库存的商品信息
    /appStore/store/dis/mortgage/returnOrder/searchPositiveProducts
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgage/returnOrder/searchPositiveProducts"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
