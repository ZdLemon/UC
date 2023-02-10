# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"combineIds": [],
	"pageNum": 1,
	"pageSize": 100000
}


def _mgmt_dis_inventory_combine_detail(data=data, access_token=access_token):
    """
    分页查询套装组合明细
    /mgmt/dis-inventory/combine/detail
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/combine/detail"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
