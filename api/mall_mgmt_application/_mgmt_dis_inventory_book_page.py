# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


params = {
    "companyCode": "", # 分公司编号
    "storeCode": "", # 服务中心编号
    "catalogId": None, # 产品类型（商品分类Id）
    "product": "", # 产品编码/名称
    "beginMonth": "",
    "endMonth": "",
    "productCode": "",
    "pageNum": 1,
    "pageSize": 10,
}

def _mgmt_dis_inventory_book_page(params=params, access_token=access_token):
    """
    85折查询实时库存台账
    /mgmt/dis-inventory/book/page
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/book/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
