# coding:utf-8

from util.login_rsakey import login_rsakey
from util.msg import params_msg, data_msg
from util.logger import logger
from setting import CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY

import requests
import time

BASE_URL = "https://uc-uat.perfect99.com/api"


def _login(username=USERNAME, password=PASSWORD, channel=CHANNEL01):
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
params = {
    "amount": 53,  # 金额
    "memberId": 831450008,  #  int顾客id
    "beginTime": "2023-02-01 00:00:00",
    "endTime": "2024-02-01 00:00:00",
    "num": 1
}

def _fin_api_voucher_voucher_generate(params=params, access_token=access_token):
    """
    给会员生成电子礼券，方便测试
    /fin/api/voucher/voucher/generate
    """

    url = f"{BASE_URL}/fin/api/voucher/voucher/generate"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r


_fin_api_voucher_voucher_generate() 