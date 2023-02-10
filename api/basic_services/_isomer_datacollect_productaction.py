# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "memberId":"1270780218333982428", # 用户ID
    "productCodes":["M7035"], # 产品编码集合
    "source":1, # 来源1->WEB商城 2->APP商城 3->小程序商城 4->系统下单 5->商城1.0
    "type":1 # 0:加购产品;1:访问产品;2:分享产品;3:收藏产品;4:取消收藏藏品
}

def _isomer_datacollect_productaction(data=data, access_token=access_token):
    """
    商品行为数据采集
    /isomer/datacollect/productaction
    """

    url = f"{BASE_URL}/isomer/datacollect/productaction"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
