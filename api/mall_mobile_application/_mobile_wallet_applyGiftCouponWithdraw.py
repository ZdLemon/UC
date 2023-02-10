# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "giftCouponIdList":["1524174843472138240","1524174844310999040"] # 电子礼券id集合
}


def _mobile_wallet_applyGiftCouponWithdraw(data=data, access_token=access_token):
    """
    电子礼券申请提现
    /mobile/wallet/applyGiftCouponWithdraw
    """

    url = f"{BASE_URL}/mobile/wallet/applyGiftCouponWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r