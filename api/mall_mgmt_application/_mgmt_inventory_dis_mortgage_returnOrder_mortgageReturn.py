# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time
import calendar


data = {
	"productList": [{
		"productCode": productCode, # 商品编号
		"productName": "玛丽艳活力精华露", # 商品名称
		"packing": "30ml/瓶",
		"unit": "瓶",
		"pieceBoxNorm": None,
		"pieceBoxPrice": None,
		"mortgagePrice": 408, # 85折押货价
		"retailPrice": 480, # 零售价
		"inventoryNum": 254, # 库存数量
		"returnNum": 1, # 退货数量
		"remark": ""
	}],
	"orderMark": 0,
	"reasonFirst": "其他原因退货",
	"reasonFirstRemark": "",
	"reasonSecond": "特批退货",
	"reasonSecondRemark": "",
	"storeCode": "902208"
}
def _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn(data=data, access_token=access_token):
    """
    押货退货下单
    /mgmt/inventory/dis/mortgage/returnOrder/mortgageReturn
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/mortgageReturn"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
