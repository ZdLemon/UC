# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": "", # 店铺编号
	"storeName": "", # 店铺名称
	"companyCode": "", # 分公司code
	"companyName": "", # 分公司名称
	"leaderName": "",
	"changeReason": "",
	"payAccount": "", # 付款账号
	"payAccountBankName": "", # 付款银行名称
	"receiptAccount": "",  # 收款账号
	"receiptBankName": "", # 收款银行名称
	"remitMoney": "", # 款项金额
	"sourceType": 3, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
	"inputRemark": "小何录入款项" # 录入备注
}


def _mgmt_inventory_disManualInputRemit_add(data=data, access_token=access_token):
    """
    85折手工录入流水
    /mgmt/inventory/disManualInputRemit/add
    """

    url = f"{BASE_URL}/mgmt/inventory/disManualInputRemit/add"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
