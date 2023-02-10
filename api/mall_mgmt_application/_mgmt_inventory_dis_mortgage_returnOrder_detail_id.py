# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


params = {
    "id": None, 
}

def _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params=params, access_token=access_token):
    """
    押货退详情
    /mgmt/inventory/dis/mortgage/returnOrder/detail/{id}
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/detail/{params['id']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
