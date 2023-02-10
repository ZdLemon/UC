# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
    "ids": [], # 主键id集合
    "stcType": "",
    "stcwId": None, # 交通管制提示语id
}


def _mgmt_sys_traffic_batchCencelTrafficControl(data=data, access_token=access_token):
    """
    批量取消交通管制
    /mgmt/sys/traffic/batchCencelTrafficControl
    """

    url = f"{BASE_URL}/mgmt/sys/traffic/batchCencelTrafficControl"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
    
