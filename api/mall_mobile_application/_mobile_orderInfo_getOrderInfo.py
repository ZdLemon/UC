# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "orderNo": "SG942437220325000009", # 订单编号(必填)
}

def _mobile_orderInfo_getOrderInfo(params=params, access_token=access_token):
    """
    通过订单号查询客户端订单信息
    /mobile/orderInfo/getOrderInfo
    """

    url = f"{BASE_URL}/mobile/orderInfo/getOrderInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
