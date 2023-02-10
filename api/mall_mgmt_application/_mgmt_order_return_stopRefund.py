# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "orderNo":"", # 订单编号
    "returnNo":"" # 退货单号
}


def _mgmt_order_return_stopRefund(data=data, access_token=access_token):
    """
    终止退款，改为直接退钱包
    /mgmt/order/return/stopRefund
    """

    url = f"{BASE_URL}/mgmt/order/return/stopRefund"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.get(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
