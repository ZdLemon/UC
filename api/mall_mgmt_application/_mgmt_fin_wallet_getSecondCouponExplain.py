# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_fin_wallet_getSecondCouponExplain(access_token=access_token):
    """
    获取秒返券说明
    /mgmt/fin/wallet/getSecondCouponExplain
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getSecondCouponExplain"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
    
