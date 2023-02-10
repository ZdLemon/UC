# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests
import time


data = {
	"storeCode": "902804", # 店铺编号
	"storeName": "深圳市宝安区新桥斌美瑞商品信息咨询服务中心",
	"leaderName": "宋少美",
	"companyCode": "34000", # 分公司code
	"sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
	"changeReason": "汇押货款", # 调整原因
	"remitMoney": "10000", # 汇款金额
	"account": "", # 付款账号
	"bankName": "", # 付款银行名称
	"remark": "11111111", # 备注
	"receiptAccount": "2011054919200009545", # 收款账号
	"receiptBankName": "中国工商银行" # 收款银行名称
}

def _mgmt_inventory_remit_addManualInputRemit(data=data, access_token=access_token):
    """
    手工录入流水
    /mgmt/inventory/remit/addManualInputRemit
    """

    url = f"{BASE_URL}/mgmt/inventory/remit/addManualInputRemit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
