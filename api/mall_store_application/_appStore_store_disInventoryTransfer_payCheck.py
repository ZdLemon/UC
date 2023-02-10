# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "uniqueFlagNo": ""
}

def _appStore_store_disInventoryTransfer_payCheck(params=params, access_token=access_token):
    """
    支付前的校验:押货价有变动amountIsUpdate=true
    /appStore/store/disInventoryTransfer/payCheck
    """

    url = f"{BASE_URL}/appStore/store/disInventoryTransfer/payCheck"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
