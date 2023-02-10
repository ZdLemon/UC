# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": None,
	"cardNo": "", # 会员卡号
	"auditStatus": None, # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
	"effectStatus": None, # 生效状态，1：未生效，2：已生效
	"effectTime": None, # 调整时间
	"pageNum": 1,
	"pageSize": 10
}


def _mgmt_fin_wallet_credit_getApplyList(data=data, access_token=access_token):
    """
    顾客信用额列表-列表
    /mgmt/fin/wallet/credit/getApplyList
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/credit/getApplyList"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
