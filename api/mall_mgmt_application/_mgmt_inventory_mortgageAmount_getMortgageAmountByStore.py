# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests


params = {
    "storeCode": store
}

def _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params=params, access_token=access_token):
    """
    根据storeCode查询押货余额主表数据
    /mgmt/inventory/mortgageAmount/getMortgageAmountByStore
    """

    url = f"{BASE_URL}/mgmt/inventory/mortgageAmount/getMortgageAmountByStore"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
