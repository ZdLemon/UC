# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "batchMonth":"202204", # 业绩月份YYYYMM
    "remark":"", # 备注
    "idList":["152"] # 主键id集合
}

def _mgmt_fin_voucher_second_coupon_acceptWithdraw(data=data, access_token=access_token):
    """
    秒返券提现受理接口
    /mgmt/fin/voucher/second/coupon/acceptWithdraw
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/second/coupon/acceptWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
