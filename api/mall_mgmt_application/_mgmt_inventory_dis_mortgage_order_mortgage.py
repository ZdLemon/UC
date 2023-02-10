# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
	"storeCode": store_85, 
	"isDelivery": 1, # 是否发货
	"remarks": "", # 押货单备注
	"productList": [{ # 押货单商品列表信息
		"productCode": productCode, # 押货商品编码
		"mortgagePrice": 408, # 商品押货价
		"mortgageNum": 2 # 押货商品数量
	}],
	"transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
}


def _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token=access_token):
    """
    押货下单
    /mgmt/inventory/dis/mortgage/order/mortgage
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/mortgage"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
