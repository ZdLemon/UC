# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests
import time


data = {
	"serialNo": None, # 套装产品编码
	"stopTime": [],
	"splitStatus": None, # 拆分状态，1-未拆分，2-已拆分
	"pageNum": 1,
	"pageSize": 10
}


def _mgmt_product_bundle_getSaleOffBundleList(data=data, access_token=access_token):
    """
    查询拆分套装列表
    /mgmt/product/bundle/getSaleOffBundleList
    """

    url = f"{BASE_URL}/mgmt/product/bundle/getSaleOffBundleList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
