# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"id": 1,
	"maxNum": 100, # 每月提现次数上限
	"minAmount": 10, # 单次提现合计金额下限
	"remark": "" # 提现说明
}

def _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data=data, access_token=access_token):
    """
    秒返券提现配置修改
    /mgmt/fin/voucher/second/coupon/updateWithdrawconf
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/updateWithdrawconf"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
