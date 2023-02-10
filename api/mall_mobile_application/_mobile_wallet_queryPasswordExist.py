# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_wallet_queryPasswordExist(access_token=access_token):
    """
    是否设置了支付密码
    /mobile/wallet/queryPasswordExist
    """

    url = f"{BASE_URL}/mobile/wallet/queryPasswordExist"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
