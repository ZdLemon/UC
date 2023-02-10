# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests
import time


params = {
	"combineState": None, # 组合状态：1未组合、2已组合
    "companyCode": "", # 分公司编号
    "productCode": "", # 产品编号
    "storeCode": "", # 服务中心编号
    "combineBegin": "", # 组合开始时间
    "combineEnd": "", # 组合结束时间
	"pageNum": 1,
	"pageSize": 10
}


def _mgmt_inventory_combine_page(params=params, access_token=access_token):
    """
    分页查询套装组合列表
    /mgmt/inventory/combine/page
    """

    url = f"{BASE_URL}/mgmt/inventory/combine/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
