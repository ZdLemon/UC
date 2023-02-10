# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


data = {
	"secondCouponIdList": []
}

def _mobile_wallet_applySecondCouponWithdraw(data=data, access_token=access_token):
    """
    秒返券申请提现
    /mobile/wallet/applySecondCouponWithdraw
    """

    url = f"{BASE_URL}/mobile/wallet/applySecondCouponWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
