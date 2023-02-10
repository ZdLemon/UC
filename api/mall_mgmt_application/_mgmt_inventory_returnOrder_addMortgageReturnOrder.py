# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"invtMortgageReturnOrderProductVOList": [{
		"productCode": "M7035",
		"productSecCode": None,
		"productName": "玛丽艳活力精华露",
		"productSecName": None,
		"productPacking": "30ml/瓶",
		"productUnit": "瓶",
		"productBoxNum": 84,
		"productMortgagePrice": 160,
		"productRetailPrice": 480,
		"currentStock": 12,
		"canMortgageNum": 0,
		"productPv": 410,
		"isStopBat": 0,
		"picUrl": None,
		"productNum": 2,
		"productRemarks": "我是产品退货备注哦哦哦"
	}],
	"invtMortgageReturnOrderVO": {
		"orderMark": 0,
		"reasonFirst": "其他原因退货", # 一级原因
		"reasonFirstRemarks": "我是一级备注原因哦哦哦哦哦哦", # 一级原因备注
		"reasonSecond": "特批退货", # 二级原因
		"reasonSecondRemarks": "我是二级备注原因哦哦哦哦哦哦", # 二级原因备注
		"storeCode": "902804"
	}
}

def _mgmt_inventory_returnOrder_addMortgageReturnOrder(data=data, access_token=access_token):
    """
    后台申请添加押货退货单
    /mgmt/inventory/returnOrder/addMortgageReturnOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/returnOrder/addMortgageReturnOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
