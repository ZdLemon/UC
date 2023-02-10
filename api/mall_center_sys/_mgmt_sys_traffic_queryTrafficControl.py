# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
    "pageNum":1,
    "pageSize":10,
    "provinceCode":"", # 省编码
    "cityCode":"", # 市编码
    "districtCode":"", # 区县编码
    "streetCode":"", # 街道编码
    "trafficControlStatus":None, # 状态 1：生效 0：待生效（默认）-1：失效
    "wordsType":None # 类型 0：不可发货 1：可发货但影响配送时效
}


def _mgmt_sys_traffic_queryTrafficControl(data=data, access_token=access_token):
    """
    分页查询交通管制
    /mgmt/sys/traffic/queryTrafficControl
    """

    url = f"{BASE_URL}/mgmt/sys/traffic/queryTrafficControl"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
    
