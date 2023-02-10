# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "pageNum":1,
    "pageSize":20,
    "stockId":"26", # 库存id
    "startTime":"", # 开始时间时间戳
    "endTime":"" # 结束时间时间戳
}

def _mgmt_product_stock_listHistory(data=data, access_token=access_token):
    """
    库存历史
    /mgmt/product/stock/listHistory
    """

    url = f"{BASE_URL}/mgmt/product/stock/listHistory"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
