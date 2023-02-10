# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "storeCode":"", # 服务中心编号
    "leaderNo":None, # 负责人卡号
    "leaderName":None, # 负责人姓名
    "companyCode":None, # 分公司
    "moneyType":None, # 可用结余为负 0->是 1 ->否
    "pageNum":1,
    "pageSize":10
}

def _mgmt_inventory_deposit_sumDepositMsg(data=data, access_token=access_token):
    """
    85折账款管理 -- 押货保证列表统计信息
    /mgmt/inventory/deposit/sumDepositMsg
    """

    url = f"{BASE_URL}/mgmt/inventory/deposit/sumDepositMsg"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
