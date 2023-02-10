# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "keyword": None # 一或二级商品关键字
}

def _appStore_purchaseOrder_getCusProductsForWebAddPage(params=params, access_token=access_token):
    """
    提交定制品押货单页面的押货商品搜索列表
    /appStore/purchaseOrder/getCusProductsForWebAddPage
    """

    url = f"{BASE_URL}/appStore/purchaseOrder/getCusProductsForWebAddPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
