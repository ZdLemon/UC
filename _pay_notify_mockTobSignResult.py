# coding:utf-8

from util.login_rsakey import login_rsakey
from util.msg import params_msg, data_msg
from util.logger import logger
from setting import CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY

import requests
import time


BASE_URL = "https://uc-test.perfect99.com/api"


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

data = {
	"accName": "东莞市黄江怡健日用品经营部",
	"accNo": "2010025509200239610",
	"signFlag": "0",
	"channelCode": "ICBC_TOB_WITHHOLD",
	"mobile": "",
	"rsv": "",
	"userCode": "",
	"address": ""
}

def _pay_notify_mockTobSignResult(data=data, access_token=access_token):
    """
    模拟发送工行企业代扣签约
    /pay/notify/mockTobSignResult
    """

    url = f"{BASE_URL}/pay/notify/mockTobSignResult"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


_pay_notify_mockTobSignResult()
        


 