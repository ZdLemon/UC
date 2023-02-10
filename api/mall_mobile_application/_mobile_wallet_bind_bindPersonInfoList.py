# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


def _mobile_wallet_bind_bindPersonInfoList(access_token=access_token):
    """
    绑定银行卡-获取绑定人信息
    /mobile/wallet/bind/bindPersonInfoList
    """

    url = f"{BASE_URL}/mobile/wallet/bind/bindPersonInfoList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r

