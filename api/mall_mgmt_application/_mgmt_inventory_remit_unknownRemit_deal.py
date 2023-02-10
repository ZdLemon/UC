# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": "902208", # 服务中心code
	"type": 2,
	"remark": None,
	"sourceType": 5, # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
	"businessMode": 2,
	"show": True,
	"sourceTypeList": [
        {
            "id": 5,
            "createTime": None,
            "updateTime": None,
            "del": 0,
            "type": 5,
            "name": "无法识别款确认押货款",
            "changeReason": "汇押货款",
            "bizType": 1,
            "bizName": "银行汇款",
            "detailType": 2
        }, 
        {
            "id": 6,
            "createTime": None,
            "updateTime": None,
            "del": 0,
            "type": 6,
            "name": "无法识别款退款",
            "changeReason": "无",
            "bizType": 1,
            "bizName": "银行汇款",
            "detailType": 2
        }, 
        {
            "type": 15,
            "name": "无法识别款不处理（需有批示或批文时可选择）",
            "changeReason": "无"
        }
    ],
	"id": "317", # 主键id
	"createTime": 1651238203000,
	"updateTime": 1651238202000,
	"del": 0,
	"waterNo": "HK1651238199",
	"companyCode": "34000", # 分公司code
	"bankName": "中国工商银行深圳华南城支行",
	"account": "622123456789951753",
	"receiptBankName": "中国工商银行",
	"receiptAccount": "2011054919200009545",
	"remitMoney": 10,
	"moneyFrom": 1,
	"storeName": "深圳市龙岗区金泽泰健康服务中心",
	"leaderName": "李哲",
	"dealChangeReason": None,
	"changeReason": "汇押货款", # 调整原因(款项类型对应交易类型名称)
	"dealType": 2,
	"dealTypeName": "人为处理",
	"dealMan": None,
	"dealTime": 1651238202000,
	"dealTimeExcel": None,
	"bankPaymentTime": [2022, 4, 29, 0, 0],
	"bankPaymentTimeStamp": "1651161600",
	"bankPaymentTimeExcel": "2022-04-29 00:00:00",
	"systemPaymentTime": [2022, 4, 29, 21, 16, 43],
	"systemPaymentTimeStamp": "1651238203",
	"systemPaymentExcel": "2022-04-29 21:16:43",
	"dealStatus": 0,
	"dealStatusName": "待处理",
	"dealRemark": "我是备注信息哦", # 处理备注
	"storeCodeSearch": True
}

def _mgmt_inventory_remit_unknownRemit_deal(data=data, access_token=access_token):
    """
    未知款项流水处理
    /mgmt/inventory/remit/unknownRemit/deal
    """

    url = f"{BASE_URL}/mgmt/inventory/remit/unknownRemit/deal"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
