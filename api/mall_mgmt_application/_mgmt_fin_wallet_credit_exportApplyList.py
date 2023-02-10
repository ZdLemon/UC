# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "storeCode":None,
    "cardNo":None,
    "auditStatus":None, # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
    "effectStatus":None, # 生效状态，1：未生效，2：已生效
    "effectTime": None, # [1654876800000,1654934400000]
    "pageNum":1,
    "pageSize":10,
    "effectStartTime": None, # 新增调整开始时间 2022-06-11 00:00:00
    "effectEndTime": None # 新增调整结束时间 2022-06-11 16:00:00
}


def _mgmt_fin_wallet_credit_exportApplyList(data=data, access_token=access_token):
    """
    导出信用额申请列表
    /mgmt/fin/wallet/credit/exportApplyList
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/credit/exportApplyList"
    headers = {
        "Authorization": f"bearer {access_token}", 
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
