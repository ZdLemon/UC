# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "remark":"我同意您提现了", # 备注
    "idList":["39"] # 主键id集合
}


def _mgmt_fin_voucher_gift_coupon_acceptWithdraw(data=data, access_token=access_token):
    """
    电子礼券提现受理接口
    /mgmt/fin/voucher/gift/coupon/acceptWithdraw
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/gift/coupon/acceptWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
