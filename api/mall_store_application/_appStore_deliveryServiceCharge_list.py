# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "month": time.strftime("%Y-%m",time.localtime(time.time())),
}

def _appStore_deliveryServiceCharge_list(params=params, access_token=access_token):
    """
    配送服务费列表
    /appStore/deliveryServiceCharge/list
    """

    url = f"{BASE_URL}/appStore/deliveryServiceCharge/list"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
