# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "returnType": 1, # 退换货类型：1.商城退货，2.商城换货，3.服务中心押货退货，4.服务中心押货换货，5.展业包订货退货，6.展业包订货换货
}

def _sys_api_getAllReturnReasonByType(params=params, access_token=access_token):
    """
    通过退换货类型获取 一级,二级层级原因
    /sys/api/getAllReturnReasonByType
    """

    url = f"{BASE_URL}/sys/api/getAllReturnReasonByType"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
