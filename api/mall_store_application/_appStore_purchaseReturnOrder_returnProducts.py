# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "product": productCode, # 产品名称/产品编号
    "pageNum": 1,
    "pageSize": 20
}

def _appStore_purchaseReturnOrder_returnProducts(params=params, access_token=access_token):
    """
    提交退货单页面的押货退货商品搜索
    /appStore/purchaseReturnOrder/returnProducts
    """

    url = f"{BASE_URL}/appStore/purchaseReturnOrder/returnProducts"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
