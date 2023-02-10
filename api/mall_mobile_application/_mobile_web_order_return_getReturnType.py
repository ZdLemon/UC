# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
}

def _mobile_web_order_return_getReturnType(params=params, access_token=access_token):
    """
    获取退货类型：1：当月退 2：隔月退
    /mobile/web/order/return/getReturnType
    """

    url = f"{BASE_URL}/mobile/web/order/return/getReturnType"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
