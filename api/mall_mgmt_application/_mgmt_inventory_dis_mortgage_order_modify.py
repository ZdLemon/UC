# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
	"orderSn": "", # 押货单编号
	"productList": [
		{
			"mortgageNum": None, # 押货商品数量
			"mortgagePrice": None, # 商品押货价
			"productCode": productCode # 商品编码
		}
	]
}


def _mgmt_inventory_dis_mortgage_order_modify(data, access_token=access_token):
    """
    押货单修改
    /mgmt/inventory/dis/mortgage/order/modify
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/modify"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
