# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"month": 202204, # 月份
    "productCode": None, # 分公司
	"pageNum": 1,
	"pageSize": 10,
}

def _mgmt_inventory_bill_product_page(params=params, access_token=access_token):
    """
    分页查询库存历史列表（产品维度）
    /mgmt/inventory/bill/product/page
    """

    url = f"{BASE_URL}/mgmt/inventory/bill/product/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
