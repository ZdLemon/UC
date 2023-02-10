# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests
import uuid
import time


data = {
	"reasonFirst": "其他原因退货", # 一级原因
	"reasonFirstRemark": "", # 一级原因备注
	"productList": [{ # 押货单商品列表信息
		"productCode": "M7035", # 商品编码
		"productNum": 2,
		"productRemarks": "",
		"remark": "", # 商品备注
		"returnNum": 2 # 商品退货数量
	}], 
	"storeCode": store_85 # 服务中心编码
}

def _appStore_store_dis_mortgage_returnOrder_mortgageReturn(data=data, access_token=access_token):
    """
    押货退货下单
    /appStore/store/dis/mortgage/returnOrder/mortgageReturn
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgage/returnOrder/mortgageReturn"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
