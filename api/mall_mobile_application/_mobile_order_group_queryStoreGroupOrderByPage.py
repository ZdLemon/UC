# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "pageSize": 10,
    "pageNum": 1
}

def _mobile_order_group_queryStoreGroupOrderByPage(params=params, access_token=access_token):
    """
    分页查询单位团购单
    /mobile/order/group/queryStoreGroupOrderByPage
    """

    url = f"{BASE_URL}/mobile/order/group/queryStoreGroupOrderByPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
