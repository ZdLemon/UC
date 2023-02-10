# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "stockType": "0", # 库存类型,0-全部,1-限量,2-非限量
    "pageNum": 1,
    "pageSize": 10,
    "serialNo": "", # 产品编码
    "productTitle": "" # 产品名称
}


def _mgmt_product_stock_list(data=data, access_token=access_token):
    """
    库存列表
    /mgmt/product/stock/list
    """

    url = f"{BASE_URL}/mgmt/product/stock/list"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
