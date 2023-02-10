# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"status": "2",
	"auditRemark": "22222",
	"companyNo": "34000",
	"memberId": "1270780218333982428",
	"cardNo": "3000002095",
	"realname": "李思",
	"adjustType": 1,
	"adjustTypeDesc": "还欠款",
	"adjustAmount": 1,
	"updaterName": "test01",
	"updateTime": 1648716413000,
	"updateTimeDesc": "2022-03-31 16:46:53",
	"adjustReason": "还欠款申请",
	"auditorName": None,
	"auditTime": None,
	"auditTimeDesc": "",
	"adjustStatus": 1,
	"adjustStatusDesc": "待审核",
	"mobile": None,
	"entryTime": 1648716413000,
	"entryTimeDesc": None,
	"entryPersonId": "1256132947821634662",
	"entryPersonName": "test01",
	"adjustAuditDtos": [{
		"adjustNo": None,
		"adjustStatus": 1,
		"adjustStatusDesc": "待审核",
		"remark": None,
		"auditorId": None,
		"auditorName": None,
		"auditTime": None,
		"auditTimeDesc": None
	}],
	"walletAdjustId": "577"
}

def _mgmt_fin_wallet_auditAdjust(data=data, access_token=access_token):
    """
    手工录入款项审核-审核
    /mgmt/fin/wallet/auditAdjust
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/auditAdjust"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
