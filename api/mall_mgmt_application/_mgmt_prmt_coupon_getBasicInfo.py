# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "id": 1, # 优惠券id
}

def _mgmt_prmt_coupon_getBasicInfo(params=params, access_token=access_token):
    """
    优惠券详情-基础信息
    /mgmt/prmt/coupon/getBasicInfo
    """

    url = f"{BASE_URL}/mgmt/prmt/coupon/getBasicInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
