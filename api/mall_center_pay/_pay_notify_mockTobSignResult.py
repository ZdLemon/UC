# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"accName": "科技公司测试使用勿动",
	"accNo": "622123456789951357",
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
