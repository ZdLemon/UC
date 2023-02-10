# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"id": "",
	"productType": 3,
	"productId": "",
	"versionStatus": 2,
	"serialNo": "M70355",
	"discountBoxNum": None,
	"catalogTitle": "化妆品(玛丽艳美容护肤品)",
	"catalogId": "3",
	"showIds": ["3"],
	"title": "玛丽艳活力精华露礼盒",
	"brandTitle": "玛丽艳",
	"brandId": "3",
	"meterUnit": "盒",
	"packing": "84瓶/盒*5盒",
	"boxNum": "420",
	"saleCompanyTitle": "完美中国",
	"saleCompanyId": "2",
	"propertyRights": "",
	"processMode": 1,
	"orderType": 1,
	"shippingTpl": "按订单金额收取运费",
	"shippingId": "1217978678543324234",
	"directSale": 0,
	"guarantee": "",
	"tags": [],
	"bundleProducts": [{
		"amount": 5,
		"productId": "232",
		"serialNo": "M7035",
		"title": "玛丽艳活力精华露",
		"retailPrice": 480,
		"versionId": "4237",
		"pv": 410,
		"subId": "232",
		"subVerId": "4237"
	}],
	"customProducts": [],
	"lclFeeId": "",
	"retailPrice": "1440",
	"securityPrice": 480,
	"groupPrice": 1123,
	"pv": "1230",
	"orderPrice": 1224,
	"activityPrice": "",
	"preDepositPrice": "",
	"depositDiscountPrice": "",
	"discountPrice": "",
	"attrs": "{}",
	"verMedais": [{
		"mediaType": 1,
		"sort": 1,
		"storageType": 1,
		"url": "https://uat-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-product/20220406101516ii1TS.png"
	}, {
		"mediaType": 1,
		"sort": 2,
		"storageType": 1,
		"url": "https://uat-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-product/20220406101520OupIa.png"
	}],
	"videoMedais": [],
	"imgMedais": [{
		"mediaType": 1,
		"sort": 1,
		"storageType": 1,
		"url": "https://uat-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-product/20220406101516ii1TS.png"
	}, {
		"mediaType": 1,
		"sort": 2,
		"storageType": 1,
		"url": "https://uat-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-product/20220406101520OupIa.png"
	}],
	"webContent": "",
	"appContent": "",
	"serveContent": "<p><span id=\"_mce_caret\" data-mce-bogus=\"1\" data-mce-type=\"format-caret\"><strong></strong></span></p><p><br data-mce-bogus=\"1\"></p>",
	"stopBatType": None,
	"stopBatTime": None,
	"isStopBat": 0,
	"isStopSale": 0,
	"isStopDiscountBat": 0,
	"isStopDiscountTransfer": 0,
	"isExchangeProduct": 0,
	"isInstall": 0,
	"isRepair": 0,
	"isReturnRepair": 0,
	"isConsumeStock": 0,
	"isInvoice": 1,
	"isOneOrder": 0,
	"isProductReturn": 1,
	"isDeliver": 1,
	"isActivateItem": 0,
	"isPreProduct": 0,
	"isIdentityLimit": 0,
	"isLimitNum": 0,
	"orderWay": 1,
	"deliverWay": 1,
	"saleTimeType": 1,
	"upSaleTime": None,
	"downSaleTime": None,
	"customerIdentityTypes": [],
	"customerCardTypes": []
}

def _mgmt_product_item_saveVersion(data=data, access_token=access_token):
    """
    添加商品
    /mgmt/product/item/saveVersion
    """

    url = f"{BASE_URL}/mgmt/product/item/saveVersion"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
