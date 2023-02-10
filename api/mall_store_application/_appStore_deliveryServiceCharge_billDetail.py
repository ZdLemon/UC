# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "month": time.strftime("%Y-%m",time.localtime(time.time())),
    "pageNum": 1,
    "pageSize": 10
}

def _appStore_deliveryServiceCharge_billDetail(params=params, access_token=access_token):
    """
    配送服务费扣补明细
    /appStore/deliveryServiceCharge/billDetail
    """

    url = f"{BASE_URL}/appStore/deliveryServiceCharge/billDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
