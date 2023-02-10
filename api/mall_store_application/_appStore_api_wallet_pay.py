# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests
import uuid


data = {
	"accountName": "", # 户名(仅钱包支付不用传)
	"bankAccount": "", # 代扣账户(仅钱包支付不用传)
	"bankName": "", # 开户银行名称(仅钱包支付不用传)
	"businessType": 0, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
	"depositAmount": 0, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
	"extJson": "", # 扩展参数
	"payAmount": 0,
	"payChannel": "", # 支付渠道 WEB/APP
	"payType": 0, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
	"pxAmount": 0, # 拼箱费
	"storeCode": "", # 店铺编号
	"uniqueFlagNo": "", # 订单唯一标识
	"userId": "", # 用户ID
 	"yfAmount": 0 # 运费
}

def _appStore_api_wallet_pay(data=data, access_token=access_token):
    """
    支付
    /appStore/api/wallet/pay
    """

    url = f"{BASE_URL}/appStore/api/wallet/pay"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
