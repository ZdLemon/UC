# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


data = {
    "pageNum":1,
    "pageSize":10,
    "couponStatusList":[2] # 使用状态集合，商城使用，比如：未使用传[2]；占用中传[3]；已使用传[1]；已失效传[4,5]；已提现传[6,7]
}

def _mobile_wallet_getSecondCouponList(data=data, access_token=access_token):
    """
    秒返券列表
    /mobile/wallet/getSecondCouponList
    """

    url = f"{BASE_URL}/mobile/wallet/getSecondCouponList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
