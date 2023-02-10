# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_product_cfg_getPrice(access_token=access_token):
    """
    价格参数查询
    /mgmt/product/cfg/getPrice
    """

    url = f"{BASE_URL}/mgmt/product/cfg/getPrice"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
