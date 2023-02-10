# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"transId": "KEY_902804_1657436021991", # 业务id
	"isDelivery": 1, # 店铺中心无需填写 0不需要发货 1需要发货
	"storeCode": "902804",
	"orderRemarks": "", # 备注 店铺中心无需填写
	"productList": [{
		"productCode": "DINGZHI13", # 押货商品编码
		"productSecondCode": "D1", # 押货商品二级编码
		"productMortgagePrice": 1, # 商品押货价
		"productNum": 2 # 押货商品数量
	}]
}


def _mgmt_inventory_order_addCustomOrder(data=data, access_token=access_token):
    """
    添加定制品押货单
    /mgmt/inventory/order/addCustomOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/order/addCustomOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
