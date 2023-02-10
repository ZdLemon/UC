# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"companyCode": "", # 分公司编号
    "storeCode": "", # 服务中心编号
    "minMonth": "", # 月份最小值,格式：yyyyMM
    "maxMonth": "", # 月份最大值,格式：yyyyMM
    "pageNum": 1,
    "pageSize": 15,
    "productCode": "" # 产品编号
}

def _mgmt_dis_inventory_bills_page(params=params, access_token=access_token):
    """
    分页查询库存对账单
    /mgmt/dis-inventory/bills/page
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/bills/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
