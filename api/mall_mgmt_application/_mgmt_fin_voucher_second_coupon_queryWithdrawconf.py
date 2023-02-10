# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_fin_voucher_second_coupon_queryWithdrawconf(access_token=access_token):
    """
    秒返券提现配置查询
    /mgmt/fin/voucher/second/coupon/queryWithdrawconf
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/queryWithdrawconf"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
