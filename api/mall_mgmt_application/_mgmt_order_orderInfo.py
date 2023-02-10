# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import calendar
import time


params = {
    "orderNo": "", # 订单编号
}

def _mgmt_order_orderInfo(params=params, access_token=access_token):
    """
    订单信息
    /mgmt/order/orderInfo/{orderNo}
    """

    url = f"{BASE_URL}/mgmt/order/orderInfo/{params['orderNo']}"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
