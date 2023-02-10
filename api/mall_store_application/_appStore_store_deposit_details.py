# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests
import uuid
import time


data = {
	"mortgageOrderNoOrBusinessNo": "", # 押货单号or流水号
	"endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 交易结束月份yyyyMM
	"pageNum": 1,
	"pageSize": 20,
	"startMonth": time.strftime("%Y%m",time.localtime(time.time())), # 交易开始月份yyyyMM
	"storeCode": store_85 # 服务中心编号
}

def _appStore_store_deposit_details(data=data, access_token=access_token):
    """
    获取服务中心押货保证金增减明细
    /appStore/store/deposit/details
    """

    url = f"{BASE_URL}/appStore/store/deposit/details"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
