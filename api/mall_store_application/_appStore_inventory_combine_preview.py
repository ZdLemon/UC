# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


params = {
    "id": "", # 套装组合id
    "combineNum": 7, # 套装组合数量
    "productCode": productCode_zh
}

def _appStore_inventory_combine_preview(params=params, access_token=access_token):
    """
    套装组合预览
    /appStore/inventory/combine/preview
    """

    url = f"{BASE_URL}/appStore/inventory/combine/preview"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
