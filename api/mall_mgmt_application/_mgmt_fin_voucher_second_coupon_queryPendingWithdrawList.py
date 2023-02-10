# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "cardNo":None, # 会员卡号
    "mobile":None, # 会员手机号
    "memberType":None, # 顾客类型
    "withdrawBatch":None, # 批次号
    "withdrawTime":None, # 提现时间yyyy-MM，提供给APP和小程序使用
    "withdrawStatus":1, # 提现状态，1：待受理；2：已受理；3：已撤销
    "pageNum":1,
    "pageSize":10
}

def _mgmt_fin_voucher_second_coupon_queryPendingWithdrawList(data=data, access_token=access_token):
    """
    秒返券提现列表（待受理不分页）
    /mgmt/fin/voucher/second/coupon/queryPendingWithdrawList
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/queryPendingWithdrawList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
