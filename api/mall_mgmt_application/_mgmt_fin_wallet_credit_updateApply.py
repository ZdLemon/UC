# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, name

import requests


data = {
	"cardNo": "14498218", # 会员卡号
	"storeCode": "902208",
	"shopType": 1,
	"shopTypeDesc": "正式网点",
	"realname": "李哲",
	"applyAmount": 11, # 调整新增信用额度
	"currentApplyAmount": 72,
	"adjustedApplyAmount": 82,
	"creditEffectTime": None, # 调整新增时间
	"creditInvalidTime": None,
	"applyTime": 1654853701000,
	"instalmentDesc": "否", # 是否分期: 是 | 否
	"auditorName": None,
	"auditStatus": 7,
	"auditStatusDesc": "待提交",
	"auditRemark": None,
	"auditTime": None,
	"effectStatusDesc": "未生效",
	"walletCreditApplyId": "1269",
	"instalment": 0, # 是否分期，1：是，0：否
	"creditAmount": 72,
	"creditApplyId": "1269", # 顾客信用额ID，新增不传，修改必传
	"isCommit": 0 # 是否提交审核，1：是，0:否
}


def _mgmt_fin_wallet_credit_updateApply(data=data, access_token=access_token):
    """
    顾客信用额列表-修改
    /mgmt/fin/wallet/credit/updateApply
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/credit/updateApply"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
