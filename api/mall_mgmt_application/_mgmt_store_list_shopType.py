# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "pageSize": 20,
    "pageNum": 1
}

def _mgmt_store_list_shopType(params=params, access_token=access_token):
    """
    网点类型列表
    /mgmt/store/list/shopType
    """

    url = f"{BASE_URL}/mgmt/store/list/shopType"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
