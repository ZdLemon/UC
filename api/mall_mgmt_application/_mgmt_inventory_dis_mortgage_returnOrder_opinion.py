# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time
import calendar


data = {
    "orderId":"", # 押货或售后单id
    "content":"" # 审批内容
}


def _mgmt_inventory_dis_mortgage_returnOrder_opinion(data=data, access_token=access_token):
    """
    添加审批意见
    /mgmt/inventory/dis/mortgage/returnOrder/opinion
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/opinion"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
