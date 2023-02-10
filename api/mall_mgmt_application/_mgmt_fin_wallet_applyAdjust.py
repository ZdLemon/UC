# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"walletId": "1422106423658958848", # 钱包id
	"companyCode": "34000", # 分公司
	"type": 1, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
	"adjustAmount": "1000", # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
	"adjustReason": "还欠款1000元"
}


def _mgmt_fin_wallet_applyAdjust(data=data, access_token=access_token):
    """
    手工录入款项审核-提交
    /mgmt/fin/wallet/applyAdjust
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/applyAdjust"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
