# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "orderId":"", # 押货或售后单id
    "content": f"同意这个退货申请" # 意见内容
}


def _mgmt_inventory_returnOrder_addOpinion(data=data, access_token=access_token):
    """
    后台押货退货添加审批意见
    /mgmt/inventory/returnOrder/addOpinion
    """

    url = f"{BASE_URL}/mgmt/inventory/returnOrder/addOpinion"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
