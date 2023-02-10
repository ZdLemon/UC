# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_order_return_getReturnReasonByType(access_token=access_token):
    """
    退货/退款原因列表
    /mobile/order/return/getReturnReasonByType
    """

    url = f"{BASE_URL}/mobile/order/return/getReturnReasonByType"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
