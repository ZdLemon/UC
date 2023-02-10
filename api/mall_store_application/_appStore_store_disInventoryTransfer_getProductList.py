# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "id": ""
}


def _appStore_store_disInventoryTransfer_getProductList(params=params, access_token=access_token):
    """
    根据记录id查询转移记录的商品明细
    /appStore/store/disInventoryTransfer/getProductList
    """

    url = f"{BASE_URL}/appStore/store/disInventoryTransfer/getProductList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
