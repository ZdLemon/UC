# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store

import requests
import uuid
import time


data = {
	"invtMortgageReturnOrderProductVOList": [{
		"productCode": "M7035", # 物品编号
		"productNum": 1 # 退货数量
	}],
	"invtMortgageReturnOrderVO": {
		"reasonFirst": "其他原因退货", # 一级原因
		"reasonFirstRemarks": "" # 一级原因备注
	}
}


def _appStore_purchaseReturnOrder_save(data=data, access_token=access_token):
    """
    提交退货单
    /appStore/purchaseReturnOrder/save
    """

    url = f"{BASE_URL}/appStore/purchaseReturnOrder/save"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
