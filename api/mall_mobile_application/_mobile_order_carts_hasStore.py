# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mobile_order_carts_hasStore(access_token=access_token):
    """
    云商/微店是否已开通服务中心
    /mobile/order/carts/hasStore
    """

    url = f"{BASE_URL}/mobile/order/carts/hasStore"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
