# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"actualRechargeAmt": 10, # 实付金额
	"channelCode": 203, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
	"feeRate": 0, # 费率
	"payType": "PC", # 支付类型,H5、APP、PC
	"rechargeAmount": 10, # 充值金额
	"walletPassword": "123456", # 钱包充值密码(传加密后数据),非免密必传字段
	"jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
}

def _mobile_wallet_recharge(data=data, access_token=access_token):
    """
    个人钱包充值
    /mobile/wallet/recharge
    """

    url = f"{BASE_URL}/mobile/wallet/recharge"
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