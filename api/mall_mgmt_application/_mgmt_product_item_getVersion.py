# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {"verId": None}

def _mgmt_product_item_getVersion(params, access_token=access_token):
    """
    查询商品
    /mgmt/product/item/getVersion
    """

    url = f"{BASE_URL}/mgmt/product/item/getVersion"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
