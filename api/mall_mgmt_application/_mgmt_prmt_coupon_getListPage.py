# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "pageNum": 1,
    "pageSize": 10,
    "platforms": None # 限制平台结果累加1app2pc4小程序
}

def _mgmt_prmt_coupon_getListPage(params=params, access_token=access_token):
    """
    分页获取优惠券列表
    /mgmt/prmt/coupon/getListPage
    """

    url = f"{BASE_URL}/mgmt/prmt/coupon/getListPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
