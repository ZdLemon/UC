# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"actualAmt": "480.00", # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
	"channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
	"orderNoList": ["SG942437220325000009"],
	"payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
	"payableAmt": "480.00", # 订单总应付金额
	"feeRate": 0, # 手续费率
	"jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false", # 支付成功前端跳转地址,微信支付必传字段信息
	"walletPassword": "", # 钱包充值密码,非免密必传字段
	"sourceType": 1 # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
}

def _mobile_payment_associationPay(data=data, access_token=access_token):
    """
    组合支付,【适用于云商,微店（云+）,云商/微店的子账号,店员
    当钱包可用余额足够支付,二选一，钱包支付或者第三方支付；
    当钱包可用余额不足以支付，选择钱包+第三方。店员需具备支付权限
    /mobile/payment/associationPay
    """

    url = f"{BASE_URL}/mobile/payment/associationPay"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r




