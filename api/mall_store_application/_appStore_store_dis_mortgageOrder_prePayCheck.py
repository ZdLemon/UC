# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests
import uuid


data = {
	"orderId": None, # 押货单id
	"oweDepositAmount": 0, # 押货保证金欠额
    "payAmount": None # 需支付金额
}

def _appStore_store_dis_mortgageOrder_prePayCheck(data=data, access_token=access_token):
    """
    押货单支付前的金额校验
    /appStore/store/dis/mortgageOrder/prePayCheck
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgageOrder/prePayCheck"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
