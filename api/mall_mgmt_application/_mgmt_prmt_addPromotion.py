# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber, promotionCode, promotionName

import requests

data = {
    "startTime": None, # 开始时间时间戳1651507200000
    "endTime":  None, # 结束时间1651507200000
    "expireOption": 1, # 定金支付时效配置项:0-自定义,1-15分钟,2-30分钟,3-1小时
    "customDays": None, # 定金支付时效自定义(天)
    "customHours": None, # 定金支付时效自定义(时)
    "customMinutes": None, # 定金支付时效自定义(分)
    "payStartTime":  None, # 尾款支付开始时间1651507200000
    "payEndTime":  None, # 尾款支付结束时间1653926400000
    "remarks": "", 
    "configDto": {
        "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
        "limitNumber": 1, # 限购数量(-1不限,-2按需分配)
        "isNotice": 1, # 是否预告0预告1不预告
        "limitCustomer": 1, # 参与顾客设置1所有2顾客身份3顾客等级4导入
        "noticeTime": "", # 预告时间
        "limitType": 1, # 限购方式1不限量2独立限量3统一限量4按需导入5按阶梯配置独立限量6按阶梯配置统一限量
        "startCardTime": None,
        "endCardTime": None,
        "limitCardTime": 0,
        "limitMemberLevel": False, # 是否限制顾客等级
        "limitOrderTime": 0,
        "limitRegTime": 0,
        "memberLevelList": [],
        "regEndTime": None,
        "regStartTime": None,
        "orderEndTime": None,
        "orderStartTime": None
    },
	"productDtos": [{
		"id": None,
		"productId": "1728",
		"serialNo": "HD202201",
		"productName": "玛丽艳神仙露水",
		"specification": "50ml/瓶",
		"unit": "瓶",
		"activityPrice": 250,
		"retailPrice": 300,
		"productPv": 28,
		"productStatus": None,
		"promotionCode": None,
		"promotionName": None,
		"promotionId": None,
		"getCounts": None,
		"pointSteps": None,
		"preDepositPrice": 50,
		"depositDiscountPrice": 20,
		"deliveryDate": None
	}],
	"promotionCode": promotionCode, # 活动编码
    "promotionName": promotionName, # 活动名称
    "promotionState": 1, # 活动状态1待审核2待开始3进行中4已结束5已驳回6草稿
    "promotionType": 4, # 活动类型:1-活动,2-换购,4-预售
    "memberIdentities": []
}

def _mgmt_prmt_addPromotion(data=data, access_token=access_token):
    """
    保存新建的活动
    /mgmt/prmt/addPromotion
    """

    url = f"{BASE_URL}/mgmt/prmt/addPromotion"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
