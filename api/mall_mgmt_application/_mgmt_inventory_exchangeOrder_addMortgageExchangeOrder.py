# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": "902804",
	"exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
	"orderFileUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706101541hHT3I.jpg", # 换货单附件，支持3个，用逗号隔开
	"productDisposalType": "", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
	"reasonFirst": "其他原因换货", # 一级原因
	"reasonFirstRemarks": "111111", # 一级原因备注
	"reasonSecond": "其他原因换货", # 二级原因
	"reasonSecondRemarks": "22222222", # 二级原因备注
	"productVoList": [{
		"productCode": "AG", # 物品编号
		"title": "完美芦荟胶",
		"packing": "40G/支",
		"meterUnit": "支  ",
		"retailPrice": 40, # 物品零售价
		"productNum": 2, # 物品换货数
		"productProductionDate": "20220101", # 物品生产日期
		"productBatch": "12345", # 批次号
		"productSn": "", # 物品序列号/二维码
		"productProblemDesc": "进水了", # 问题描述
		"firstUseTime": "", # 第一次使用的时间
		"dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
		"happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
		"securityPrice": 20,
		"productDisposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
	}],
	"orderFileName": "20220706101541hHT3I.jpg,20220706101547SIkgW.jpg,20220706101552twQcR.jpg" # 换货单附件名，支持3个，用逗号隔开
}


def _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(data, access_token=access_token):
    """
    后台申请添加押货换货单
    /mgmt/inventory/exchangeOrder/addMortgageExchangeOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/addMortgageExchangeOrder"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
