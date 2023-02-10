# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "customerId": 1270780218333982428, # 用户Id
}

def _mobile_orderInfo_countOrderUpgrade(params=params, access_token=access_token):
    """
    统计用户待升级订单
    /mobile/orderInfo/countOrderUpgrade
    """

    url = f"{BASE_URL}/mobile/orderInfo/countOrderUpgrade"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
