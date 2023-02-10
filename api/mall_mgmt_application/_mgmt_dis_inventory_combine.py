# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"combineNum": None, # 组合数量
    "productCode": None, # 产品编号/名称
    "storeCode": None, # 服务中心编号
}


def _mgmt_dis_inventory_combine(data=data, access_token=access_token):
    """
    套装组合
    /mgmt/dis-inventory/combine
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/combine"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
