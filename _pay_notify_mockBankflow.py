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

data = [
    {
	"accountName": "柠檬服务中心",
    "accountNo": '6221234569874521',
    "bankName": "中国银行解放路支行",
    "busiTime": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))}T00:00:00.261+0800",
    "companyNo": '02000',
    "receiptAccount": '3602028919200120721',
    "receiptBankName": "中国工商银行",
    "remark": None,
    "tradeAmount": '5000',
    "tradeOrderNo": f"HKT{str(time.time() * 1000)[:13]}",
    },
    ]

def _pay_notify_mockBankflow(data=data, access_token=access_token):
    """
    模拟线下汇款
    /pay/notify/mockBankflow
    """

    url = f"{BASE_URL}/pay/notify/mockBankflow"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

_pay_notify_mockBankflow()
        


 