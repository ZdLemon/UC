# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "cardNo":None, # 会员卡号
    "sourceOrderNo":None, # 来源订单号
    "diffWay":None, # 处理方案，1：扣减相应金额；2：补回相应金额
    "pageNum":1,
    "pageSize":10
}


def _mgmt_fin_voucher_second_coupon_queryDiffSum(data, access_token=access_token):
    """
    秒返券调差列表金额合计
    /mgmt/fin/voucher/second/coupon/queryDiffSum
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/queryDiffSum"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
