# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "pageNum": 1,
    "pageSize": 20 
}

def _appStore_dis_inventory_combine_page(params=params, access_token=access_token):
    """
    套装组合列表
    /appStore/dis-inventory/combine/page
    """

    url = f"{BASE_URL}/appStore/dis-inventory/combine/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
