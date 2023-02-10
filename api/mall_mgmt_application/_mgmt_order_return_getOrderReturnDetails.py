# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "returnNo": "902063", # 退货单号
}

def _mgmt_order_return_getOrderReturnDetails(params=params, access_token=access_token):
    """
    退货详情
    /mgmt/order/return/getOrderReturnDetails
    """

    url = f"{BASE_URL}/mgmt/order/return/getOrderReturnDetails"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
