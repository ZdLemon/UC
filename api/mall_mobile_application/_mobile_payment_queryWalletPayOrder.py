# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username, username_85

import requests


params = {
    "payNo": "", # 支付流水号
}

def _mobile_payment_queryWalletPayOrder(params=params, access_token=access_token):
    """
   	查询支付成功信息
    /mobile/payment/queryWalletPayOrder
    """

    url = f"{BASE_URL}/mobile/payment/queryWalletPayOrder"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
