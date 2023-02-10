# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog(access_token=access_token):
    """
    电子礼券提现配置修改记录查询
    /mgmt/fin/voucher/gift/coupon/queryWithdrawconfLog
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/gift/coupon/queryWithdrawconfLog"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
