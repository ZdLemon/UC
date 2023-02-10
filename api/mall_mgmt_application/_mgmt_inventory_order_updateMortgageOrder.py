# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests


data = {
	"updateInvtMortgageOrderVO": {
		"orderRemarks": "", # 押货单备注
		"id": "1270744106308097292" # 押货单id
	},
	"invtMortgageProductVOList": [
        {
            "productCode": "M7035", # 物品编码
            "id": "1270744106313242269", # 物品id
            "productNum": 1, # 物品数量
            "productMortgagePrice": 160 # 物品押货价
        },
        {
            "productCode": "M70355",
            "id": "1270744106313242270",
            "productNum": 2,
            "productMortgagePrice": 480
        }
    ],
	"isBatchCancel": 0 # 批量取消标志
}


def _mgmt_inventory_order_updateMortgageOrder(data=data, access_token=access_token):
    """
    修改押货单
    /mgmt/inventory/order/updateMortgageOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/order/updateMortgageOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
