# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"companyCode": "", # 分公司编号
	"storeCode": "", # 服务中心编号
	"product": "", # 产品编号或名称
	"stockOperator": 1, # 库存运算符: 0为=，1为'>='，2为'>'，3为'<=',4为'<'
	"stock": None, # 库存
	"pageNum": 1,
	"pageSize": 100,
	"currentPage": 1
}

def _mgmt_dis_inventory_page(params=params, access_token=access_token):
    """
    分页查询库存列表
    /mgmt/dis-inventory/page
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
