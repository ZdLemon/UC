# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
	"combineState": None,
    "companyCode": None, # 分公司编号
    "product": None, # 产品编号/名称
    "storeCode": None, # 服务中心编号
    "combineBegin": None,
    "combineEnd": None,
    "pageNum": 1,
    "pageSize": 10,
}


def _mgmt_dis_inventory_combine_page(params=params, access_token=access_token):
    """
    分页查询套装组合列表
    /mgmt/dis-inventory/combine/page
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/combine/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
