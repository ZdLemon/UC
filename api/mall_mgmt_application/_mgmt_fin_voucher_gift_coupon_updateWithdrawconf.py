# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests

data = {
    "id":"1",
    "minAmount":10, # 单次提现合计金额下限
    "remark":"一二三四五六七八九十" # 提现说明
}


def _mgmt_fin_voucher_gift_coupon_updateWithdrawconf(data=data, access_token=access_token):
    """
    电子礼券提现配置修改
    /mgmt/fin/voucher/gift/coupon/updateWithdrawconf
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/gift/coupon/updateWithdrawconf"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
