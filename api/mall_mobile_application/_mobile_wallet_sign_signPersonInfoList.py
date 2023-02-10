# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_wallet_sign_signPersonInfoList(access_token=access_token):
    """
    签约银行卡-获取签约人信息
    /mobile/wallet/sign/signPersonInfoList
    """

    url = f"{BASE_URL}/mobile/wallet/sign/signPersonInfoList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
