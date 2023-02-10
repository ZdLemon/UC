# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "id": None
}


def _appStore_dis_inventory_combine_detail(params=params, access_token=access_token):
    """
    套装组合明细
    /appStore/dis-inventory/combine/detail
    """

    url = f"{BASE_URL}/appStore/dis-inventory/combine/detail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
