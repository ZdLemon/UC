# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


data = {
	"institution": "天下第一武道大会",
	"institutionAddr": {
		"address": "武道一路1号",
		"province": "440000000000",
		"city": "440300000000",
		"district": "440303000000",
		"town": "440303001000"
	},
	"receiveType": 2,
	"consigneeName": "李哲",
	"consigneeMobile": "13827493388",
	"consigneeAddr": {
		"address": "新木社区新木路321-4号新木半里大厦D座127",
		"province": "440000000000",
		"city": "440300000000",
		"district": "440307000000",
		"town": "440307003000"
	},
	"remitType": 2,
	"remittance": "40000.00",
	"remitCredentials": [{
		"name": "身份证正面.png",
		"url": "https://uat-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-finance/20220504125417fAXMi.png"
	}],
	"needInvoice": 0,
	"invoiceType": 1,
	"contracts": None,
	"commitment": {
		"name": "押货换货附件1.jpg",
		"url": "https://uat-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-finance/202205041254273Dw73.jpg"
	},
	"remark": "",
	"bankAccount": "4000050909100468735",
	"bankName": " 深圳市龙岗区金泽泰健康服务中心",
	"invoice": None,
	"products": [{
		"productId": "232",
		"serialNo": "M7035",
		"title": "M7035 玛丽艳活力精华露",
		"catalogTitle": "化妆品(玛丽艳美容护肤品)",
		"catalogId": "3",
		"showList": [{
			"showId": "3",
			"title": "化妆品 (玛丽艳美容护肤品)"
		}],
		"retailPrice": 480,
		"underlinedPrice": 480,
		"groupPrice": "400",
		"pv": 410,
		"securityPrice": 160,
		"activityPrice": None,
		"preDepositPrice": None,
		"depositDiscountPrice": None,
		"imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
		"orderType": 1,
		"isExchangeProduct": 0,
		"isPreProduct": 0,
		"productType": 1,
		"isActivateItem": 0,
		"purchaseLimitType": 0,
		"purchaseLimitNum": None,
		"isIdentityLimit": 0,
		"customerIdentityTypes": [0],
		"customerCardTypes": [0],
		"stock": 100,
		"productCode": "M7035",
		"groupPricex": 374
	}]
}

def _mobile_order_group_appendGroupOrder(data=data, access_token=access_token):
    """
    新增单位团购单
    /mobile/order/group/appendGroupOrder
    """

    url = f"{BASE_URL}/mobile/order/group/appendGroupOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
