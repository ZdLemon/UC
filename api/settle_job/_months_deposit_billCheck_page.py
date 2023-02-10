# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "companyCode": None, # 分公司编号
    "storeCode": None, # 服务中心编号
    "pageNum": 1,
    "pageSize": 10,
    "startMonth": f'{int(time.strftime("%Y")) - 1}11' if time.strftime("%Y%m").endswith("01") or time.strftime("%Y%m").endswith("02") else str(int(time.strftime("%Y%m")) - 2), # 月份最小值,格式：yyyyMM, 上个月
    "endMonth": f'{int(time.strftime("%Y")) - 1}11' if time.strftime("%Y%m").endswith("01") or time.strftime("%Y%m").endswith("02") else str(int(time.strftime("%Y%m")) - 2), # 月份最小值,格式：yyyyMM 上个月
}


def _months_deposit_billCheck_page(data=data, access_token=access_token):
    """
    押货保证金月结列表
    /months/deposit/billCheck/page
    """

    url = f"{BASE_URL}/months/deposit/billCheck/page"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
