# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username, username_85

import requests


params = {
    "pageNum": 1,
    "pageSize": 6,
    "state": 1, # 使用状态1未使用2已使用3已作废4已失效5占用中
    "selectType": 1 # 筛选条件1全部2快过期3立减券4满减券
}


def _mobile_coupon_selectMemberCoupons(params=params, access_token=access_token):
    """
   	查询用户优惠券发放信息
    /mobile/coupon/selectMemberCoupons
    """

    url = f"{BASE_URL}/mobile/coupon/selectMemberCoupons"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
