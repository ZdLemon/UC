# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "actualAmt": "501.00", # 实付金额 税率为零时等于应付金额,不为零时,实付金额=订单应付金额+订单应付金额*费率信息
    "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
    "orderNoList": ["SG003000220624000079"],
    "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
    "payableAmt": "501.00", # 订单应付金额
    "feeRate": 0, # 手续费率
    "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false", # 支付成功前端跳转地址,微信支付必传字段信息
    "walletPassword": "" # 钱包密码,非免密必传字段
}   


def _mobile_payment_singlePay(data=data, access_token=access_token):
    """
    单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    /mobile/payment/singlePay
    """

    url = f"{BASE_URL}/mobile/payment/singlePay"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


