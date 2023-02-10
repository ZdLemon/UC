# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "withdrawId": None, # 
}

def _mgmt_fin_voucher_gift_coupon_queryWithdrawdtlList(params=params, access_token=access_token):
    """
    电子礼券提现详情查询
    /mgmt/fin/voucher/gift/coupon/queryWithdrawdtlList
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/gift/coupon/queryWithdrawdtlList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
