# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "serviceNo":"DTSG90280422052500316901", # 退货/换货单号
    "comment":"我同意这个代客售后申请", # 留言内容
    "id":"" # 留言id
}

def _mgmt_order_return_saveComment(data=data, access_token=access_token):
    """
    新增/修改留言
    /mgmt/order/return/saveComment
    """

    url = f"{BASE_URL}/mgmt/order/return/saveComment"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
