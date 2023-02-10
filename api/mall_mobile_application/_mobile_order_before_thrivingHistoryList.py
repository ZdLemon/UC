# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "cardNo": productCode,  # 开单人卡号
    "from": "",
    "pageNum": 1,
    "pageSize": 99999
}

def _mobile_order_before_thrivingHistoryList(data=data, access_token=access_token):
    """
    查询代客下单搜索历史记录
    /mobile/order/before/thrivingHistoryList
    """

    url = f"{BASE_URL}/mobile/order/before/thrivingHistoryList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
