# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "pageNum": 1,
    "pageSize": 20,
    "combineBegin": "",
    "combineEnd": ""
}


def _appStore_dis_inventory_combine_record_page(params=params, access_token=access_token):
    """
    套装组合记录列表
    /appStore/dis-inventory/combine/record/page
    """

    url = f"{BASE_URL}/appStore/dis-inventory/combine/record/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
