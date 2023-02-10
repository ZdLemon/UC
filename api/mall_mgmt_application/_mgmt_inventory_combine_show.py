# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "id" : ""
}

def _mgmt_inventory_combine_show(params=params, access_token=access_token):
    """
    套装组合展示
    /mgmt/inventory/combine/show
    """

    url = f"{BASE_URL}/mgmt/inventory/combine/show"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
