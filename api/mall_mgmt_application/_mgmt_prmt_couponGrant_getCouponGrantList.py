# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "pageNum": 1,
    "pageSize": 10,
    "grantWay": 1 # 派发类型1普通派发2转赠派发
}

def _mgmt_prmt_couponGrant_getCouponGrantList(params=params, access_token=access_token):
    """
    优惠券派发列表-分页查询派发记录
    /mgmt/prmt/couponGrant/getCouponGrantList
    """

    url = f"{BASE_URL}/mgmt/prmt/couponGrant/getCouponGrantList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
