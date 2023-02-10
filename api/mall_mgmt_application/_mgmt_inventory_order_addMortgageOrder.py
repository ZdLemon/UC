# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests
import time


data = {
	"invtMortgageOrderVO": {
		"storeCode": store,
		"isDelivery": 1, # 0不需要发货 1需要发货
		"remarks": "" # 押货备注
	},
	"invtMortgageOrderProductVOList": [
		{
			"productCode": productCode, # 物品编号
			"productMortgagePrice": 160, # 物品押货价
			"productNum": 2 # 数量
		}
    ],
    "transId": f"KEY_{store}_{int(round(time.time() * 1000))}"
}


def _mgmt_inventory_order_addMortgageOrder(data=data, access_token=access_token):
    """
    运营后台添加押货单
    /mgmt/inventory/order/addMortgageOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/order/addMortgageOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
