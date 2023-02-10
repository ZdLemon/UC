# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "promotionId":None,
    "examine":3, # 审核是否通过3通过4不通过
    "remarks":"我同意了", # 备注
    "enclosureVos":[], # 附件集合
    "couponId":"1270722876147919236" # 优惠券id
}

def _mgmt_prmt_coupon_examine(data=data, access_token=access_token):
    """
    优惠券审核
    /mgmt/prmt/coupon/examine
    """

    url = f"{BASE_URL}/mgmt/prmt/coupon/examine"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
