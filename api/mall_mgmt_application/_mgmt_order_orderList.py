# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"pageNum": 1,
    "pageSize": 10,
    "orderNo": "" # 订单号
}

def _mgmt_order_orderList(params=params, access_token=access_token):
    """
    订单列表
    /mgmt/order/orderList
    """

    url = f"{BASE_URL}/mgmt/order/orderList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
