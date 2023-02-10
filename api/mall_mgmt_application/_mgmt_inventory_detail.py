# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests
import time
import calendar


params = {
    "outIn": None, # 出入库：1入库 2出库
    "source": 3, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
    "monthTime": None, # 月份，格式为：yyyyMM
    "storeCode": store, # 服务中心编号
    "productCode": productCode, # 产品编号
    "pageNum": 1,
    "pageSize": 10,
}


def _mgmt_inventory_detail(params=params, access_token=access_token):
    """
    查询库存明细
    /mgmt/inventory/detail
    """

    url = f"{BASE_URL}/mgmt/inventory/detail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
