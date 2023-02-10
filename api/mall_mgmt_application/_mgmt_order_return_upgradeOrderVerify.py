# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
from urllib.parse import urlencode


data = {
    "orderNo":"", # 订单编号
    "applySource": 0, # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
}

def _mgmt_order_return_upgradeOrderVerify(data=data, access_token=access_token):
    """
    升级单校验
    /mgmt/order/return/upgradeOrderVerify
    """

    url = f"{BASE_URL}/mgmt/order/return/upgradeOrderVerify"
    headers = {"Authorization": f"bearer {access_token}", "content-type": "application/x-www-form-urlencoded"}
    data = urlencode(data)

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

