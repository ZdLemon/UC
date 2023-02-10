# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests



def _mobile_wallet_queryGiftCouponSurveyByMemberId(access_token=access_token):
    """
    电子礼券调查配置项显示
    /mobile/wallet/queryGiftCouponSurveyByMemberId
    """

    url = f"{BASE_URL}/mobile/wallet/queryGiftCouponSurveyByMemberId"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
