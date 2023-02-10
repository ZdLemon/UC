# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "bankCardId":"1270738427215447494", # 主键id
    "withdrawAmount":"1.00" # 申请提现金额
}


def _mobile_wallet_applyWalletWithdraw(data=data, access_token=access_token):
    """
    申请钱包提现
    /mobile/wallet/applyWalletWithdraw
    """

    url = f"{BASE_URL}/mobile/wallet/applyWalletWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

response = {
	"code": 200,
	"message": "操作成功",
	"data": {
		"payOrderNo": "RC202203281016590001", # 交易编号
		"payInfo": "银行返回信息:成功", # 支付链接
		"payStatus": 2 # 支付订单状态,0-待支付,1-支付中,2-支付成功,3-支付失败,4-支付取消
	}
}