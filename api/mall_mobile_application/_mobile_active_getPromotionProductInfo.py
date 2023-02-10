# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


params = {
    "serialNo": productCode, # 产品编码
    "cardNo": username, # 顾客卡号
    "platform": 2 # 请求平台:1-APP,2-PC,4-小程序
}

def _mobile_active_getPromotionProductInfo(params=params, access_token=access_token):
    """
    获活动商品详情以及已购买数量
    /mobile/active/getPromotionProductInfo
    """

    url = f"{BASE_URL}/mobile/active/getPromotionProductInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r

response = {
    "code":200,
    "message":"操作成功",
    "data":{
        "serialNo":None,
        "isPromotion":0, # 是否在活动中0否 1是
        "isCanBuy":1, # 是否可以购买0否 1是
        "limitType":None,
        "limitNumber":-1, # 限购数量(-1不限)
        "retailPrice":None,
        "exchangePrice":None,
        "originalPrice":None,
        "activityPrice":None,
        "preDepositPrice":None,
        "depositDiscountPrice":None,
        "balancePayment":None,
        "productPv":None,
        "startTime":None,
        "endTime":None,
        "expireMinutes":None,
        "payStartTime":None,
        "payEndTime":None,
        "deliveryDate":None,
        "limitCustomer":None,
        "promotionId":None,
        "promotionName":None,
        "picture":None,
        "title":None,
        "payMinute":None,
        "productId":None,
        "payLimitTime":None,
        "promotionType":None,
        "exchangeType":None,
        "limitProduct":None,
        "serialNos":None,
        "buyCount":0, # 已购买数量
        "promotionState":None,
        "isNewCard":None,
        "showEndTime":None,
        "limitCardTime":None,
        "startCardTime":None,
        "endCardTime":None,
        "shelvesCoupons":[
            {
                "shelvesId":"78", # 优惠券上架id
                "couponId":"1270722876147919149", # 优惠券id
                "couponNumber":"testlqzx003", # 优惠券编号
                "couponName":"领券中心测试003", # 优惠券名称
                "useRange":1, # 使用范围:1-所有产品,2-指定产品,3-指定不适用产品,4-指定产品分类,5-指定活动
                "faceValue":1.00, # 优惠券面值
                "couponType":2, # 优惠券类型:1-立减券,2-满减券,3-叠加满减券
                "minAmount":1.00, # 使用条件
                "received":False, # 是否已领取
                "receiveCount":-1, # 领取总量:-1不限制
                "receivedCount":22, # 已领取数量
                "finished":False, # 是否已领完
                "showOrder":1,
                "couponPrice":479.00 # 券后价
            }
        ],
        "exchangeInfo":None
    }
}