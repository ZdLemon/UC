# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "orderNo": "",
}

def _mobile_web_order_as_returnMonthVerify(params=params, access_token=access_token):
    """
    隔月退货验证
    /mobile/web/order/as/returnMonthVerify
    """

    url = f"{BASE_URL}/mobile/web/order/as/returnMonthVerify"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
