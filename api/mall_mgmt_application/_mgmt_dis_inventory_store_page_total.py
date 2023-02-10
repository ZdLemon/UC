# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"companyCode": "", # 分公司编号
	"storeCode": "", # 服务中心编号
    "operator": 0, # 零售价运算符: 0为=，1为'>='，2为'>'，3为'<=',4为'<'
    "retailPrice": None, # 零售价合计
	"pageNum": 1,
	"pageSize": 10,
    "currentPage": 1,
    "product": None
}

def _mgmt_dis_inventory_store_page_total(params=params, access_token=access_token):
    """
    库存合计（按服务中心维度）
    /mgmt/dis-inventory/store/total
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/store/total"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
