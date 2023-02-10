# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"id": "1270733832147098701",
	"exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
	"auditFileUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706123344Db36p.jpg", # 审批附件
	"auditFileName": "20220706123344Db36p.jpg", # 审批附件名称
	"auditRemark": "222222222222", # 审批备注
	"auditResult": "1", # 审批意见 0不通过 1通过
	"productDisposalType": "1", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
	"reasonFirst": "其他原因换货", # 一级原因
	"reasonFirstRemarks": "我是一级原因的备注信息哦", # 一级原因备注
	"reasonSecond": "其他原因换货", # 二级原因
	"reasonSecondRemarks": "我是二级原因的备注信息哦", # 二级原因备注
	"productVoList": [{
		"id": "1270733832150244533", # 物品记录id
		"productNum": 2, # 物品换货数
		"dailyUseType": None,
		"firstUseTime": "",
		"happenType": None,
		"productBatch": "12345", # 批次号
		"productProblemDesc": "进水了", # 问题描述
		"productProductionDate": "20220101", # 物品生产日期
		"productSn": "", # 物品序列号/二维码
		"productDisposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
	}],
	"returnInfo": "何伟广州仓" # 退回信息
}


def _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder(data, access_token=access_token):
    """
    后台审批押货换货单
    /mgmt/inventory/exchangeOrder/auditMortgageExchangeOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/auditMortgageExchangeOrder"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
