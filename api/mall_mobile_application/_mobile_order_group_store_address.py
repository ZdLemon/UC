# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_order_group_store_address(access_token=access_token):
    """
    获取服务中心收货信息
    /mobile/order/group/store-address
    """

    url = f"{BASE_URL}/mobile/order/group/store-address"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
