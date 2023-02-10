# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85, storeName

import requests


data = {
	"accountName": storeName, # 户名不能为空
	"bankAccount": "4000050909100468735", # 代扣账户不能为空
	"bankName": "工商银行", # 开户银行名称
	"businessType": 3, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
	"payAmount": 1, # 充值金额
	"payChannel": "WEB", # 充值渠道 WEB/APP
	"payType": 2, # 2->工行签约代扣 3->建行签约代扣
	"storeCode": store_85, # 店铺编号
	"userId": "814498218" # 用户ID
}

def _appStore_invest(data=data, access_token=access_token):
    """
    充值
    /appStore/invest
    """

    url = f"{BASE_URL}/appStore/invest"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
