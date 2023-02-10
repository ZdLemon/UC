# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


params = {
    "combineNum": 0, # 套装组合数量
    "productCode": productCode_zh  # 产品编号
}

def _appStore_dis_inventory_combine_preview(params=params, access_token=access_token):
    """
    套装组合预览
    /appStore/dis-inventory/combine/preview
    """

    url = f"{BASE_URL}/appStore/dis-inventory/combine/preview"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
