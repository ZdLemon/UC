# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
	"checkList": [1], # 业务范围 1：B区域，2：C区域
	"isControl": 1, # 是否发货 0：不发货，1：发货
	"stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
	"timeUp": "", # 定时生效时间
	"timeOff": "", # 定时失效时间
	"stcwId": "1", # 交通管制提示语id
	"businessRange": 1, # 业务范围:1->B,2->C,3->B+C
	"id": None
}


def _mgmt_sys_traffic_updateTrafficControl(data=data, access_token=access_token):
    """
    更新交通管制
    /mgmt/sys/traffic/updateTrafficControl
    """

    url = f"{BASE_URL}/mgmt/sys/traffic/updateTrafficControl"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
    
