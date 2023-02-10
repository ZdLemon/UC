# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


data = [{
	"accountName": "深圳市龙岗区金泽泰健康服务中心",
    "accountNo": '4000050909100468735',
    "bankName": "中国工商银行深圳华南城支行",
    "busiTime": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))}T00:00:00.261+0800",
    "companyNo": '34000',
    "receiptAccount": '2011054919200009545',
    "receiptBankName": "中国工商银行",
    "remark": None,
    "tradeAmount": '10',
    "tradeOrderNo": f"HK{str(time.time() * 1000)[:13]}",
}]

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
