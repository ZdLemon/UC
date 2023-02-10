# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, name

import requests


data = {
	"cardNo": "", # 会员卡号
	"applyAmount": 10, # 调整新增信用额度
	"instalment": 0, # 是否分期，1：是，0：否
	"realname": name,
	"creditAmount": None, # 已有信用额
	"isCommit": None # 是否提交审核，1：是，0:否
}


def _mgmt_fin_wallet_credit_addApply(data, access_token=access_token):
    """
    顾客信用额列表-新增
    /mgmt/fin/wallet/credit/addApply
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/credit/addApply"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
