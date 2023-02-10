# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "id": ""
}


def _mgmt_fin_voucher_gift_coupon_revokeWithdraw(data=data, access_token=access_token):
    """
    电子礼券提现撤销接口
    /mgmt/fin/voucher/gift/coupon/revokeWithdraw
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/gift/coupon/revokeWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
