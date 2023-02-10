# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


params = {
    "payType": "PC", # 客户端
}

def _mobile_wallet_rechargeMethod(params=params, access_token=access_token):
    """
    获取充值方式列表
    /mobile/wallet/rechargeMethod
    """

    url = f"{BASE_URL}/mobile/wallet/rechargeMethod"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r

response = {
	"code": 200,
	"message": "操作成功",
	"data": [
        {
            "payPartnerId": "203",
            "paywayName": "邮政储蓄银行",
            "transCardType": 2,
            "bankType": "PSBC",
            "bankAccount": "666123456789",
            "bankName": "邮政储蓄银行",
            "bankBranchName": "",
            "defaultSignAccount": 1,
            "rate": 0.00
        }, 
        {
            "payPartnerId": "202",
            "paywayName": "建设银行",
            "transCardType": None,
            "bankType": None,
            "bankAccount": None,
            "bankName": None,
            "bankBranchName": None,
            "defaultSignAccount": None,
            "rate": 0.00
        },
        {
            "payPartnerId": "103",
            "paywayName": "银联",
            "transCardType": None,
            "bankType": None,
            "bankAccount": None,
            "bankName": None,
            "bankBranchName": None,
            "defaultSignAccount": None,
            "rate": 0.00
        },
        {
            "payPartnerId": "101",
            "paywayName": "微信支付",
            "transCardType": None,
            "bankType": None,
            "bankAccount": None,
            "bankName": None,
            "bankBranchName": None,
            "defaultSignAccount": None,
            "rate": 0.00
        },
        {
            "payPartnerId": "102",
            "paywayName": "支付宝支付",
            "transCardType": None,
            "bankType": None,
            "bankAccount": None,
            "bankName": None,
            "bankBranchName": None,
            "defaultSignAccount": None,
            "rate": 0.00
        }
    ]
}




