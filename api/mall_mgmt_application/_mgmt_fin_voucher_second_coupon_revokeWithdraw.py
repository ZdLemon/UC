# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"id": None
}


def _mgmt_fin_voucher_second_coupon_revokeWithdraw(data=data, access_token=access_token):
    """
    秒返券提现撤销
    /mgmt/fin/voucher/second/coupon/revokeWithdraw
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/revokeWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
