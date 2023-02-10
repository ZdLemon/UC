# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
	"mortgageItemReqDtoList": [
		{
			"itemCode": "", # 商品编号
			"num": 0, # 数量
			"skuCode": ""
		}
	],
	"mortgageOrderNo": "", # 押货单号
	"optime": "",
	"status": 2,
	"type": 5 # 1:3是2,85折是5
}

def _esb_third_mortgage_syncDeliveryInfo(data=data, access_token=access_token):
    """
    同步仓库中心的发货信息 押货发货
    /esb/third/mortgage/syncDeliveryInfo
    """

    url = f"{BASE_URL}/esb/third/mortgage/syncDeliveryInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
