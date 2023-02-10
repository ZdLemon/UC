# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": "902804",
	"exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
	"reasonFirst": "其他原因换货", # 一级原因
	"reasonFirstRemark": "111111", # 一级原因备注
	"reasonSecond": "其他原因换货", # 二级原因
	"reasonSecondRemark": "22222222", # 二级原因备注
	"productList": [{
		"productCode": "AG", # 商品编号
		"productName": "完美芦荟胶",
		"packing": "40G/支",
		"unit": "支  ",
		"retailPrice": 40, # 零售价
		"exchangeNum": 2, # 数量
		"productionDate": "20220101", # 物品生产日期
		"productBatch": "12345", # 批次号
		"productSn": "", # 物品序列号/二维码
		"problemDesc": "进水了", # 问题描述
		"firstUseTime": "", # 第一次使用的时间
		"dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
		"happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
		"mortgagePrice": 34, # 85折押货价
		"disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
	}],
	"files": [ 
		{
			"fileUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/202207061549235J52k.jpg",
			"fileName": "202207061549235J52k.jpg"
		},
		{
			"fileUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706154927jbxTm.jpg",
			"fileName": "20220706154927jbxTm.jpg"
		},
		{
			"fileUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/202207061549326y4OD.jpg",
			"fileName": "202207061549326y4OD.jpg"
		}
    ] # 换货单附件，支持3个
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, access_token=access_token):
    """
    押货换货下单
    /mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
