# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


params = {
    "type": 3, 
}

def _mgmt_inventory_common_getReason(params=params, access_token=access_token):
    """
    获取各种退换货原因
    /mgmt/inventory/common/getReason
    """

    url = f"{BASE_URL}/mgmt/inventory/common/getReason"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
