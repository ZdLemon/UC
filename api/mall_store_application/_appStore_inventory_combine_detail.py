# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


params = {
    "id": ""
}


def _appStore_inventory_combine_detail(params=params, access_token=access_token):
    """
    套装组合明细
    /appStore/inventory/combine/detail
    """

    url = f"{BASE_URL}/appStore/inventory/combine/detail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
