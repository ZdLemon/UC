# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _appStore_purchase_balanceAmount(access_token=access_token):
    """
    押货金额
    /appStore/purchase/balanceAmount
    """

    url = f"{BASE_URL}/appStore/purchase/balanceAmount"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
