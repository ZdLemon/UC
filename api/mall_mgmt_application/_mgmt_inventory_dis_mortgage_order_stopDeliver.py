# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
	"orderSn": "" # 押货单编号
}


def _mgmt_inventory_dis_mortgage_order_stopDeliver(params, access_token=access_token):
    """
    押货单欠货停发
    /mgmt/inventory/dis/mortgage/order/stopDeliver
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/stopDeliver"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    params = params

    with requests.post(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
