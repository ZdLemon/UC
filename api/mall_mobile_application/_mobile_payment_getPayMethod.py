# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "orderNoList":["SG942437220325000009"], # 订单号集合
    "payType":"PC", # 支付类型,H5、APP、PC、PROGRAM
    "sourceType":1 # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
}

def _mobile_payment_getPayMethod(data=data, access_token=access_token):
    """
    获取支付方式
    /mobile/payment/getPayMethod
    """

    url = f"{BASE_URL}/mobile/payment/getPayMethod"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r




