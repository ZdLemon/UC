# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
    "companyCode":["34000"], # 分公司
    "storeCode": store_85, # 服务中心编号
    "pageNum":3,
    "pageSize":10
}


def _mgmt_inventory_disChargeDetail_pageList(data=data, access_token=access_token):
    """
    分页列表-手续费明细表
    /mgmt/inventory/disChargeDetail/pageList
    """

    url = f"{BASE_URL}/mgmt/inventory/disChargeDetail/pageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
