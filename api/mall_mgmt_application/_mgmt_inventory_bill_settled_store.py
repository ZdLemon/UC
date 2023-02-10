# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "companyCode": None, # 分公司编号
    "storeCode": None, # 服务中心编号
    "pageNum": 1,
    "pageSize": 10,
    "minMonth": f'{int(time.strftime("%Y")) - 1}11' if time.strftime("%Y%m").endswith("01") or time.strftime("%Y%m").endswith("02") else str(int(time.strftime("%Y%m")) - 2), # 月份最小值,格式：yyyyMM
    "maxMonth": f'{int(time.strftime("%Y")) - 1}11' if time.strftime("%Y%m").endswith("01") or time.strftime("%Y%m").endswith("02") else str(int(time.strftime("%Y%m")) - 2) # 月份最大值,格式：yyyyMM
} 


def _mgmt_inventory_bill_settled_store(params=params, access_token=access_token):
    """
    查询已月结服务中心13
    /mgmt/inventory/bill/settled-store
    """

    url = f"{BASE_URL}/mgmt/inventory/bill/settled-store"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
