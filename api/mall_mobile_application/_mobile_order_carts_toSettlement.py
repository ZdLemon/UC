# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests


data = {
    "addressId":None,
    "customerCard":"3000002095", # 给某个顾客下单的会员卡号
    "customerId":"1270780218333982428", # 给某个顾客下单的会员ID
    "expressType":1, # 配送方式 1->服务中心自提 2->公司配送
    "orderAmount":480,
    "productList":[
        {
            "releList":None,
            "imgUrl":"https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
            "title":"玛丽艳活力精华露",
            "serialNo":"M7035",
            "activityPrice":480,
            "quantity":1,
            "pv":410,
            "productType":1,
            "isActivateItem":0,
            "retailPrice":480,
            "isActivity":0,
            "number":1
        }
    ],
    "orderInvoice":None,
    "couponList":[],
    "giftList":[],
    "freightList":[],
    "secondCouponList":[],
    "storeCode":store,
    "ownerId":"",
    "pv":410,
    "remarks":"",
    "returnRate":0.12,
    "sharerId":None,
    "sourceType":1 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
}

def _mobile_order_carts_toSettlement(data=data, access_token=access_token):
    """
    选择商品去结算
    /mobile/order/carts/toSettlement
    """

    url = f"{BASE_URL}/mobile/order/carts/toSettlement"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


response = {
	"code": 200,
	"message": "操作成功",
	"data": {
		"saleCompanyId": "2",
		"saleCompanyTitle": "完美中国",
		"expressType": 1,
		"productList": [{
			"checked": 1,
			"saleCompanyId": "2",
			"saleCompanyTitle": "完美中国",
			"productId": "232",
			"serialNo": "M7035",
			"cusSerialNo": None,
			"catalogId": "3",
			"title": "玛丽艳活力精华露",
			"shippingId": "1217978678543324234",
			"shippingTpl": "按订单金额收取运费",
			"productType": 1,
			"quantity": 1,
			"pv": 410,
			"picture": "https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
			"retailPrice": 480.00,
			"exchangePrice": None,
			"originalPrice": None,
			"subtotal": 480.00,
			"pvSubtotal": 410,
			"expressAmount": None,
			"isActivity": 0,
			"limitBuy": 0,
			"limitNumber": -1,
			"availableNumber": -1,
			"addCartTime": 1648202353764,
			"isConsumeStock": 0,
			"availableStock": -72088,
			"invalid": 0,
			"lastModify": "1640154067000",
			"isExchange": 0,
			"isPvExchange": None,
			"isAmExchange": None,
			"isMonExchange": None,
			"exchangeSize": None,
			"meterUnit": "瓶",
			"packing": "30ml/瓶",
			"versionId": "5059",
			"orderType": 1,
			"isExchangeProduct": 0,
			"isPvExchangeProduct": 0,
			"promotionId": None,
			"promotionName": None,
			"pvPromotionId": None,
			"pvPromotionName": None,
			"amPromotionId": None,
			"amPromotionName": None,
			"monPromotionId": None,
			"monPromotionName": None,
			"isInvoice": 1,
			"isOneOrder": 0,
			"orderWay": 99,
			"deliverWay": 99,
			"showInfos": [{
				"id": "3",
				"showId": "3",
				"title": "化妆品 (玛丽艳美容护肤品)",
				"cfgStatus": 1
			}],
			"isStopDiscountTransfer": 1,
			"isActivateItem": 0,
			"purchaseLimitType": 0,
			"purchaseLimitNum": None,
			"isIdentityLimit": 0,
			"customerIdentityTypes": [],
			"customerCardTypes": [],
			"isPreProduct": 0,
			"preDepositPrice": None,
			"depositDiscountPrice": None,
			"activityPrice": None,
			"isShowStock": 0,
			"deliveryDate": None,
			"balancePayDate": None,
			"exchangeList": []
		}],
		"lackInventoryProductList": None,
		"pvExchangeInfoList": None,
		"amExchangeInfoList": None,
		"monExchangeInfoList": None,
		"pvPromotionId": None,
		"pvPointStep": None,
		"amPromotionId": None,
		"amPointStep": None,
		"monPromotionId": None,
		"monPointStep": None,
		"isPvExchangeQualify": None,
		"isAmExchangeQualify": None,
		"isMonExchangeQualify": None,
		"customerMemberId": "1270780218333982428",
		"customer": "李思",
		"customerCard": "3000002095",
		"customerType": 3,
		"customerPhone": "13632353252",
		"price": {
			"totalPrice": 480.00,
			"productPrice": 480.00,
			"expressAmount": 0,
			"pv": 410,
			"goldAmount": 480.00,
			"returnRate": 0.12,
			"returnAmount": 49,
			"preDepositPrice": 0,
			"depositDiscountPrice": 0,
			"balancePayment": 0,
			"cumulativePv": 6223.00,
			"discountAmount": 0,
			"promotionDiscount": 0,
			"payPrice": 480.00,
			"couponAmount": 0,
			"giftCouponAmount": 0,
			"freightCouponAmount": 0,
			"secCouponAmount": 0,
			"useCouponList": [],
			"useGiftList": [],
			"useFreightList": [],
			"useSecList": [],
			"balancePayDate": None
		},
		"addCartTime": 1648202353781,
		"invalid": 0,
		"checked": 1,
		"sharerId": None,
		"sourceType": 1,
		"checkoutVO": {
			"expressType": 1,
			"addressId": None,
			"storeCode": "942437",
			"remark": None,
			"clientType": None,
			"orderInvoiceVo": None,
			"ownerId": None,
			"storeVO": {
				"id": "1270698371432237244",
				"phone": None,
				"shopkeeperId": "1270780218333982428",
				"shopkeeperNo": None,
				"name": "何伟零号店铺",
				"leaderId": "1261577260381675971",
				"leaderNo": "3000002095",
				"leaderName": "李思",
				"email": None,
				"fax": None,
				"zipCode": None,
				"postCode": None,
				"shopType": 1,
				"remarks": "",
				"isMainShop": 1,
				"level": 1,
				"companyCode": "34000",
				"companyName": "完美（中国）有限公司中山分公司",
				"openDate": None,
				"ratifyDate": 1630339200000,
				"decorationInfo": None,
				"extraInfo": None,
				"code": "942437",
				"isServiceShop": None,
				"isSignContract": None,
				"provinceCode": "440000000000",
				"provinceName": "广东省",
				"cityCode": "440100000000",
				"cityName": "广州市",
				"deliveryInfo": "广东省 广州市 海珠区 琶洲街道 琶洲新村001号  ",
				"shopStatus": 0,
				"permission": "1,2,3,4,5",
				"areaCode": "440105000000",
				"areaName": "海珠区",
				"streetName": "琶洲街道",
				"streetCode": "440105015000",
				"detailAddress": "琶洲新村001号",
				"lng": "113.383170",
				"lat": "23.100386",
				"del": 0,
				"wechat": None,
				"businessMode": 1,
				"isHighPriority": 2,
				"discountPermission": "",
				"isSettledAccount": 2,
				"normalStore": True,
				"ucongNo": None,
				"disqualified": False,
				"disableLogin": False,
				"selfOrder": True,
				"agentOrder": True
			},
			"isStock": 1,
			"addressVO": None,
			"ownerVO": None,
			"deliverWay": None
		},
		"recommendCoupon": None,
		"isFiveStar": 0,
		"cardStatus": 0,
		"cancelDate": None,
		"isInvoice": 1,
		"storeCode": "942437",
		"orderNo": None,
		"isOldOrder": False
	}
}




