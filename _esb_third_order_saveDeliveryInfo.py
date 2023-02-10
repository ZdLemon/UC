# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from util.login_rsakey import login_rsakey
from setting import CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY

import requests
import time


BASE_URL = "https://uc-uat.perfect99.com/api"


def _login(username="hewei01", password=PASSWORD, channel=CHANNEL01):
    """登录接口

    Args:
        username (_type_, optional): _description_. Defaults to username.
        password (_type_, optional): _description_. Defaults to password.
        channel (_type_, optional): _description_. Defaults to CHANNEL01.
        authorization

    Returns:
        _type_: _description_
    """  
    url = f"{BASE_URL}/login"
    headers = {"Authorization": Authorization}
    data = login_rsakey(username, password, channel)

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:  
        logger.debug(data_msg(r, data))       
        return r


access_token = _login().json()["data"]["access_token"]
data = {
    "status":1,
    "mortgageOrderNo":"SG034000221226000021", # 订单号
    # "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 物流单号
    "deliveryCode": f"shunfeng122601", # 物流单号
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


_esb_third_order_saveDeliveryInfo()