# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "serialNo": productCode, # 产品编码
}

def _mobile_product_getStockInfo(params=params, access_token=access_token):
    """
    查询商品库存
    /mobile/product/getStockInfo
    """

    url = f"{BASE_URL}/mobile/product/getStockInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
