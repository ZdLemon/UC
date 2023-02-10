# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "status":1,
    "mortgageOrderNo":"SG002000220211000109", # 订单号
    "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 物流单号
    "shippingCompany":"小何物流", # 物流公司
    "deliverTime":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) #"2022-02-11 16:25:40" 发货时间YYYY-MM-DD HH:MM:SS
}


def _esb_third_order_saveDeliveryInfo(data=data, access_token=access_token):
    """
    仓库系统-订单发货状态回传给商城
    /esb/third/order/saveDeliveryInfo
    """

    url = f"{BASE_URL}/esb/third/order/saveDeliveryInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
