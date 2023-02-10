# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "returnNo": "TGH90220822081800001701", # 退货单号
}

def _appStore_orderReturn_details(params=params, access_token=access_token):
    """
    售后详情
    /appStore/orderReturn/details
    """

    url = f"{BASE_URL}/appStore/orderReturn/details"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
