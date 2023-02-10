# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "productCode": None, # 产品编号
    "storeCode": None, # 服务中心编号
}


def _mgmt_dis_inventory_combine_forward(params=params, access_token=access_token):
    """
    套装组合展示
    /mgmt/dis-inventory/combine/forward
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/combine/forward"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
