# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import datetime


data = {
    "walletCreditApplyIdList": [""], # 顾客信用额申请id集合
}


def _mgmt_fin_wallet_credit_deleteApply(data=data, access_token=access_token):
    """
    顾客信用额列表-删除
    /mgmt/fin/wallet/credit/deleteApply
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/credit/deleteApply"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
