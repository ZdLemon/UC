# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = [ # 85押货单下单商品明细
	{
		"mortgageNum": 0, # 押货商品数量
		"mortgagePrice": 0, # 商品押货价
		"productCode": "" # 押货商品编码
	}
]

def _appStore_store_dis_mortgageOrder_pushProductsToCart(data=data, access_token=access_token):
    """
    推送购物车数据
    /appStore/store/dis/mortgageOrder/pushProductsToCart
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgageOrder/pushProductsToCart"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
