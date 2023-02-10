# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "pageNum": 1,
    "pageSize": 20
}

def _appStore_purchaseReturnOrder_list(params=params, access_token=access_token):
    """
    押货退货单列表（分页）
    /appStore/purchaseReturnOrder/list
    """

    url = f"{BASE_URL}/appStore/purchaseReturnOrder/list"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
