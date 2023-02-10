# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"orderWayList": [1, 2], # 下单限制1自购2代购
	"platforms": [1, 2, 4], # 限制平台1app2pc4小程序
	"limitStore": 0, # 是否限制门店0否1是2代购限门店
	"categoryIds": [], # 分类id集合
	"couponCount": 10, # 优惠券总量-1不限量
	"limitCount": None, # 可获得数量（null不限）
	"couponName": "通用10元券", # 名称 通用10元券
	"couponNumber": "20220501", # 编号 20220501 int(round(time.time() * 1000))
	"couponState": 1, # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
	"couponType": 1, # 优惠券类型1立减券2满减券3叠加满减券4堆叠满减券
	"endTime": None, # 失效时间（不填表示一直有效）
	"endType": 2, # 失效方式1定时失效2不限制3N个自然日
	"faceValue": 10, # 面值
	"grantCount": 0, # 已发放数量
	"isGenerateCode": 0, # 是否生成优惠码0不生成1生成
	"isStacked": 0, # 是否可叠加0不可叠加1可叠加
	"minAmount": None, # 使用条件
	"promotionIds": [], # promotionIds
	"remarks": "小薇薇新建的优惠券", # 说明
	"serialNos": [], # 可用商品集合
	"disableSerialNos": [], # 不可用商品集合
	"startTime": int(round(time.time() * 1000)), # 1651305600000,生效时间 13位时间戳
	"startTimeType": 0, 
	"useRange": 1, # 使用范围1所有产品2指定产品3指定不适用产品4指定产品分类5指定活动
	"usedCount": 0, # 已核销数量
	"stackTimes": "", # stackTimes
	"activeDay": 1, # 有效天数
	"startType": 1 # 开始生效方式1定时生效2派发后生效
}

def _mgmt_prmt_coupon_addCoupon(data=data, access_token=access_token):
    """
    保存新建的优惠券
    /mgmt/prmt/coupon/addCoupon
    """

    url = f"{BASE_URL}/mgmt/prmt/coupon/addCoupon"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
