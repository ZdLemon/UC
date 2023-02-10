# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"orderId": "1270733832147098713", # 换货单id
	"deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
	"deliverType": 2, # 发货方式 1顾客自提 2邮寄
	"expressCompany": "小河物流", # 新品配送物流公司
	"expressNo": "xh123456" # 物流单号
}


def _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder(data, access_token=access_token):
    """
    后台押货换货单发货
    /mgmt/inventory/exchangeOrder/deliverMortgageExchangeOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/deliverMortgageExchangeOrder"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
