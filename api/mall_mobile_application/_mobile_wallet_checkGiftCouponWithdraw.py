# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mobile_wallet_checkGiftCouponWithdraw(access_token=access_token):
    """
    电子礼券提现校验
    /mobile/wallet/checkGiftCouponWithdraw
    """

    url = f"{BASE_URL}/mobile/wallet/checkGiftCouponWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
