# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username_vip

import requests


data = {
    "cardNo": username_vip # 会员编号
}

def _mobile_order_before_addThrivingHistory(data=data, access_token=access_token):
    """
    新增代客下单搜索历史记录
    /mobile/order/before/addThrivingHistory
    """

    url = f"{BASE_URL}/mobile/order/before/addThrivingHistory"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
