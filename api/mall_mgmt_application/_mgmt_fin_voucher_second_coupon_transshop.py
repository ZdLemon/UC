# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


data = {
	"secondCouponIdList": [], # 秒返券id集合
	"targetShopCode": "", # 转入服务中心编码
	"targetShopName": "" # 转入服务中心名称
}

def _mgmt_fin_voucher_second_coupon_transshop(data=data, access_token=access_token):
    """
    秒返券转店
    /mgmt/fin/voucher/second/coupon/transshop
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/transshop"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
