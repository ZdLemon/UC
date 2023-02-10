# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


data = {
	"cardNo": username, # 用户卡号
	"serialNo": productCode # 商品编码
}

def _mobile_order_carts_canBuy(data=data, access_token=access_token):
    """
    根据用户卡号查询购买信息
    /mobile/order/carts/canBuy
    """

    url = f"{BASE_URL}/mobile/order/carts/canBuy"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
