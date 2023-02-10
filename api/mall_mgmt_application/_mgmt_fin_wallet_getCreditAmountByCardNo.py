# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


params = {
	"cardNo": username
}


def _mgmt_fin_wallet_getCreditAmountByCardNo(params=params, access_token=access_token):
    """
    根据会员卡号获取顾客姓名和现有信用额
    /mgmt/fin/wallet/getCreditAmountByCardNo
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getCreditAmountByCardNo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
