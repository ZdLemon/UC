# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mobile_order_carts_getCartProductNum(access_token=access_token):
    """
    获取购物车产品数量和选中结算产品数量
    /mobile/order/carts/getCartProductNum
    """

    url = f"{BASE_URL}/mobile/order/carts/getCartProductNum"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
