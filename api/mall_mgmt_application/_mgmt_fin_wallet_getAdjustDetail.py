# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"id": 577
}

def _mgmt_fin_wallet_getAdjustDetail(params=params, access_token=access_token):
    """
    手工录入款项审核-详情
    /mgmt/fin/wallet/getAdjustDetail
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getAdjustDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.post(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
response = {
	"code": 200,
	"message": "操作成功",
	"params": {
		"companyNo": "34000",
		"memberId": "1270780218333982428",
		"cardNo": "3000002095",
		"realname": "李思",
		"adjustType": 1,
		"adjustTypeDesc": "还欠款",
		"adjustAmount": 1.00,
		"updaterName": "test01",
		"updateTime": 1648716413000,
		"updateTimeDesc": "2022-03-31 16:46:53",
		"adjustReason": "还欠款申请",
		"auditorName": None,
		"auditTime": None,
		"auditTimeDesc": "",
		"adjustStatus": 1,
		"adjustStatusDesc": "待审核",
		"auditRemark": None,
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
		}]
	}
}
