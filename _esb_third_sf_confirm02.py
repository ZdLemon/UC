# coding:utf-8

from util.login_rsakey import login_rsakey
from util.msg import data_msg
from util.logger import logger
from setting import CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY

import requests
import time
import random, string

BASE_URL = "https://uc-test.perfect99.com/api"


def _login(username="hewei02", password=PASSWORD, channel=CHANNEL01):
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


data = {
    "Body": {
        "WaybillRoute": [
            {
                "mailno": "",
                "acceptAddress": "test",
                "reasonName": None,
                # 押货换货单编号 + 经营模式 + 两位递增的序列 如HYH9305162211000001 + 13 + 01,如果同一张换货单上门取件取消后再申请(或修改)序列号要往上加1
                "orderid": "HYH90280422110000171302",
                "acceptTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), #"2022-11-24 08:38:58"
                "remark": "顾客已线下取消",
                "opCode": "70",
                "id": "166925037210410",
                "reasonCode": None
            }
        ]
    }
}

access_token = _login().json()["data"]["access_token"]


def _esb_third_sf_confirm(data=data, access_token=access_token):
    """
    顺丰物流揽件确认回调
    /esb/third/sf/confirm
    """

    url = f"{BASE_URL}/esb/third/sf/confirm"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


_esb_third_sf_confirm()