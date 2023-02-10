# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "id": None, # 
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params=params, access_token=access_token):
    """
    详情
    /mgmt/inventory/dis/mortgage/exchangeOrder/detail/{id}
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/detail/{params['id']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
