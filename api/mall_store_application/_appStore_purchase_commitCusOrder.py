# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store

import requests
import uuid
import time


data = {
	"productList": [{
		"productCode": "DZZ91101", # 押货商品编码
		"productMortgagePrice": 167, # 商品押货价
		"productNum": 2, # 押货商品数量
		"productSecondCode": "DZ1" # 二级编码
	}],
	"transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
}

def _appStore_purchase_commitCusOrder(data=data, access_token=access_token):
    """
    提交定制品押货单
    /appStore/purchase/commitCusOrder
    """

    url = f"{BASE_URL}/appStore/purchase/commitCusOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
