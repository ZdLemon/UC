# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


data = {
    "customerCard":username,
    "sourceType":1,
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
    "storeCode":"942437"
}

def _mobile_order_carts_getSecondList(data=data, access_token=access_token):
    """
    获取购物秒返券券列表
    /mobile/order/carts/getSecondList
    """

    url = f"{BASE_URL}/mobile/order/carts/getSecondList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


response = {
	"code": 200,
	"message": "操作成功",
	"data": [
        {
            "secondCouponId": "1511629184500125696",
            "secondCouponCode": "MF202204061657360001",
            "secondCouponAmount": 2.00, # 秒返券金额
            "effectTime": 1649174400000,
            "effectTimeDesc": "2022-04-06 00:00:00",
            "invalidTime": 1680710399000,
            "invalidTimeDesc": "2023-04-05 23:59:59",
            "memberId": "826712599",
            "cardNo": "26712599",
            "mobile": "18818336838",
            "realname": "黄宇",
            "memberType": 2,
            "memberTypeDesc": "VIP会员",
            "sourceOrderNo": "SG902094220401000001",
            "soReturnFlag": None,
            "soReturnFlagDesc": "否",
            "sourceStoreCode": None,
            "sourceOrderWay": 1,
            "sourceOrderWayDesc": "自购订单",
            "sourceOrderMonth": "202204",
            "couponStatus": 2,
            "couponStatusDesc": "未使用",
            "couponStatusTime": 1649174400000,
            "couponStatusTimeDesc": "2022-04-06 00:00:00",
            "useOrderNo": None,
            "returnOrderNo": None,
            "diffFlag": None,
            "withdrawBatch": None,
            "getTime": None,
            "getTimeDesc": "",
            "isUsed": 0 # 是否可用，0:不可用 1:可用
        }
    ]
}
