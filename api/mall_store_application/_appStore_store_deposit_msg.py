# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests


params = {
    "storeCode": store_85
}

def _appStore_store_deposit_msg(params=params, access_token=access_token):
    """
    获取服务中心可用押货保证金余额
    /appStore/store/deposit/msg
    """

    url = f"{BASE_URL}/appStore/store/deposit/msg"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
