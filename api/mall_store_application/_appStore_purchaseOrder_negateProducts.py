# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _appStore_purchaseOrder_negateProducts(access_token=access_token):
    """
    提交押货单页面的负库存押货商品列表
    /appStore/purchaseOrder/negateProducts
    """

    url = f"{BASE_URL}/appStore/purchaseOrder/negateProducts"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
