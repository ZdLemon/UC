# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_wallet_getBankCardInfo(access_token=access_token):
    """
    获取用户绑定的银行卡及详情信息
    /mobile/wallet/getBankCardInfo
    """

    url = f"{BASE_URL}/mobile/wallet/getBankCardInfo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
