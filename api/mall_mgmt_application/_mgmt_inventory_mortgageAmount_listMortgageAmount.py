# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "storeCode":None, # 服务中心编号
    "companyCode":None, # 分公司编号
    "pageNum":1,
    "pageSize":10,
    "searchIsAll":True # 是否查询全部 标识 true 是 其他 否
}

def _mgmt_inventory_mortgageAmount_listMortgageAmount(data=data, access_token=access_token):
    """
    服务中心账款管理 -- 押货余额列表
    /mgmt/inventory/mortgageAmount/listMortgageAmount
    """

    url = f"{BASE_URL}/mgmt/inventory/mortgageAmount/listMortgageAmount"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
