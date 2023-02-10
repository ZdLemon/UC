# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "cardNo":"45722864",
    "serialNo":"AG",
    "sourceType":3
}



def _mobile_order_before_getLastMonth(data=data, access_token=access_token):
    """
    结算前销售调整,查询商品(模糊)
    /mobile/order/before/getLastMonth
    """

    url = f"{BASE_URL}/mobile/order/before/getLastMonth"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


