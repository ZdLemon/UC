# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
	"provinceCode": "460000000000", # 省编码
	"cityCode": "460100000000", # 市编码
	"districtCode": "460105000000", # 区县编码
	"streetCode": "460105002000", # 街道编码
	"checkList": [1], # 业务范围 1：B区域，2：C区域
	"isControl": 1, # 是否发货 0：不发货，1：发货
	"stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
	"timeUp": "", # 定时生效时间
	"timeOff": "", # 定时失效时间
	"provinceName": "海南省", # 省
	"cityName": "海口市", # 市
	"districtName": "秀英区", # 区
	"streetName": "海秀街道办", # 街道
	"stcwId": "1", # 交通管制提示语id
	"businessRange": 1 # 业务范围:1->B,2->C,3->B+C
}


def _mgmt_sys_traffic_addTrafficControl(data=data, access_token=access_token):
    """
    添加交通管制
    /mgmt/sys/traffic/addTrafficControl
    """

    url = f"{BASE_URL}/mgmt/sys/traffic/addTrafficControl"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
    
