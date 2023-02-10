# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import datetime


data = {
    "auditStatus": None, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
    "auditRemark": "同意信用额申请", # 审批备注
    "walletCreditApplyIdList": [""], # 顾客信用额申请id集合
    "creditEffectTime": (datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S") # 生效时间"2022-06-10 14:00:00"
}


def _mgmt_fin_wallet_credit_auditApply(data=data, access_token=access_token):
    """
    顾客信用额列表-审核
    /mgmt/fin/wallet/credit/auditApply
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/credit/auditApply"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
