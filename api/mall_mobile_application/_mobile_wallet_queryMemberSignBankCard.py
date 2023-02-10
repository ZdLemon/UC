# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _mobile_wallet_queryMemberSignBankCard(access_token=access_token):
    """
    获取用户签约的银行卡及详情信息
    /mobile/wallet/queryMemberSignBankCard
    """

    url = f"{BASE_URL}/mobile/wallet/queryMemberSignBankCard"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.post(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r))     
        return r
