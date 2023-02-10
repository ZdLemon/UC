# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store

import requests
import uuid
import time


data = {
	"list": [{
		"mortgagePrice": 160, # 商品押货价
		"productCode": productCode, # 押货商品编码
		"productNum": 2 # 押货商品数量
	}],
	"transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
}

def _appStore_purchase_commit(data=data, access_token=access_token):
    """
    提交押货单
    /appStore/purchase/commit
    """

    url = f"{BASE_URL}/appStore/purchase/commit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
