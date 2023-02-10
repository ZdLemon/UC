# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"orderId": "", # 退货单id
	"inspectStatus": 1, # 验货意见 0不通过 1通过
	"expressSubsidy": 100, # 运费补贴
	"inspectRemarks": "我验货通过了", # 验货备注
	"orderReturnRealAmount": "320.00", # orderReturnRealAmount
	"productList": [{
		"id": "", # 物品id
		"productRealNum": 2, # 物品实退数量
		"productRealAmount": 320.00 # 退货单实退金额总额
	}]
}


def _mgmt_inventory_returnOrder_inspectOrder(data=data, access_token=access_token):
    """
    后台押货退货验货
    /mgmt/inventory/returnOrder/inspectOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/returnOrder/inspectOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
