# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests



def _mobile_web_wallet_queryGiftCouponAmt(access_token=access_token):
    """
    可用电子礼券金额统计
    /mobile/web/wallet/queryGiftCouponAmt
    """

    url = f"{BASE_URL}/mobile/web/wallet/queryGiftCouponAmt"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
