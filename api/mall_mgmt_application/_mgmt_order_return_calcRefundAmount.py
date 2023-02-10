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

def _mgmt_order_return_calcRefundAmount(params=params, access_token=access_token):
    """
    计算订单退款金额
    /mgmt/order/return/calcRefundAmount
    """

    url = f"{BASE_URL}/mgmt/order/return/calcRefundAmount"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
