# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests
import uuid


data = {
	"isDelivery": True, # 是否发货
	"productList": [
		{
			"mortgageNum": 0, # 押货商品数量
			"mortgagePrice": 0, # 商品押货价
			"productCode": "" # 押货商品编码
		}
	],
	"storeCode": "", # 服务中心编码
	"transId": f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
}

def _appStore_store_dis_mortgageOrder_mortgage(data=data, access_token=access_token):
    """
    押货下单
    /appStore/store/dis/mortgageOrder/mortgage
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgageOrder/mortgage"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
