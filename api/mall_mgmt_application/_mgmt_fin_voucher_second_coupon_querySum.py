# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


data = {
    "cardNo":"",
    "mobile":None,
    "memberType":None,
    "sourceOrderNo":"",
    "withdrawBatch":None,
    "sourceStoreCode":None,
    "couponStatusList":None,
    "soReturnFlag":None,
    "pageNum":1,
    "pageSize":10,
    "sourceOrderStartMonth":None,
    "sourceOrderEndMonth":None,
    "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
    "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
}

def _mgmt_fin_voucher_second_coupon_querySum(data=data, access_token=access_token):
    """
    秒返券列表金额合计
    /mgmt/fin/voucher/second/coupon/querySum
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/querySum"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
