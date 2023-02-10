# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "verifyRemark": "", # 审核备注
    "verifyResult": 1, # 审核结果 1通过，2拒绝
    "show": True,
    "type": 2,    
    "id": "910",
    "updateTime": 1653192519000,
    "dealTime": 1653192519000,
    "del": 0,
    "waterNo": "YHK202205221208390001",
    "storeCode": "902804",
    "companyCode": "34000",
    "bankName": "邮政储蓄",
    "account": "666123456789",
    "receiptBankName": "中国工商银行",
    "receiptAccount": "2011054919200009545",
    "remitMoney": 1000.00,
    "sourceType": 8,
    "sourceTypeName": "手工增押货款",
    "changeReason": "汇押货款",
    "dealType": 2,
    "dealTypeName": "人为处理",
    "inputMan": "hewei01",
    "remark": "录入手工增押货款1000元",
    "createTime": 1653192520000,
    "createTimeExcel": "2022-05-22 12:08:40",
    "verifyer": None,
    "bankPaymentTime": None,
    "bankPaymentTimeName": None,
    "systemPaymentTime": None,
    "systemPaymentTimeExcel": None,
    "moneyFrom": 3,
    "storeName": "深圳市宝安区新桥斌美瑞商品信息咨询服务中心",
    "leaderName": "宋少美",
    "verifyStatus": 0,
    "verifyStatusName": "待审核",
    "verifyResult": 0,
    "verifyResultName": "",
    "verifyRemark": None
}

def _mgmt_inventory_remit_verifyManualInputRemit(params=params, access_token=access_token):
    """
    手工录入流水审核
    /mgmt/inventory/remit/verifyManualInputRemit
    """

    url = f"{BASE_URL}/mgmt/inventory/remit/verifyManualInputRemit"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
