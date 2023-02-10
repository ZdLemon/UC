# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {"id": None}

def _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token=access_token):
    """
    押货单详情(修改)
    /mgmt/inventory/dis/mortgage/order/detailForModify/{params[id]}
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/detailForModify/{params['id']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
