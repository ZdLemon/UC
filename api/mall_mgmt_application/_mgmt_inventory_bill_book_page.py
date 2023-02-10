# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar
import datetime


params = {
    "companyCode": "", # 分公司编号
    "storeCode": "", # 服务中心编号
    "catalogId": None, # 产品类型（商品分类Id）
    "product": "", # 产品编码/名称
    "beginMonth": (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y%m"), # 上个月份202204月份，格式为：yyyyMM
    "endMonth": (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y%m"), # 上个月份202204月份，格式为：yyyyMM
    "productCode": "",
    "pageNum": 1,
    "pageSize": 10,
}

def _mgmt_inventory_bill_book_page(params=params, access_token=access_token):
    """
    查询库存月结台账
    /mgmt/inventory/bill/book/page
    """

    url = f"{BASE_URL}/mgmt/inventory/bill/book/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
