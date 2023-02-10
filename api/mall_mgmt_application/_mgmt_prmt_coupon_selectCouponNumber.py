# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests


params = {
    "couponNumber": couponNumber, # 优惠券编码
    "couponId": None
}

def _mgmt_prmt_coupon_selectCouponNumber(params=params, access_token=access_token):
    """
    查询优惠券编码是否已经存在
    /mgmt/prmt/coupon/selectCouponNumber
    """

    url = f"{BASE_URL}/mgmt/prmt/coupon/selectCouponNumber"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
