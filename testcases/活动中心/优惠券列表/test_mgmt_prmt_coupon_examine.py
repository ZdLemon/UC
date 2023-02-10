# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_coupon_selectCouponNumber import _mgmt_prmt_coupon_selectCouponNumber # 查询优惠券编码是否已经存在
from api.mall_mgmt_application._mgmt_prmt_coupon_addCoupon import _mgmt_prmt_coupon_addCoupon # 新建优惠券
from api.mall_mgmt_application._mgmt_prmt_coupon_examine import _mgmt_prmt_coupon_examine # 优惠券审核
from setting import P1, P2, P3, couponNumber, couponName

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/coupon/examine")
class TestClass:
    """
    优惠券审核
    /mgmt/prmt/coupon/examine
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("优惠券审核-成功路径: 优惠券审核检查")
    def test_mgmt_prmt_coupon_examine(self):
        
        message = None
        id = None # 优惠券Id
        
        @allure.step("查询优惠券编码是否已经存在")
        def step_mgmt_prmt_coupon_selectCouponNumber():
            
            nonlocal message    
            params = {
                "couponNumber": couponNumber, # 优惠券编码
                "couponId": None
            }
            with _mgmt_prmt_coupon_selectCouponNumber(params, self.access_token) as r:
                assert r.status_code == 200
                message =  r.json()["message"]
        
        @allure.step("新建优惠券")
        def step_mgmt_prmt_coupon_addCoupon():
            
            nonlocal id
            data = {
                "orderWayList": [1, 2], # 下单限制1自购2代购
                "platforms": [1, 2, 4], # 限制平台1app2pc4小程序
                "limitStore": 0, # 是否限制门店0否1是2代购限门店
                "categoryIds": [], # 分类id集合
                "couponCount": 10, # 优惠券总量-1不限量
                "limitCount": None, # 可获得数量（null不限）
                "couponName": couponName, # 名称 通用10元券
                "couponNumber": couponNumber, # 编号 20220501 int(round(time.time() * 1000))
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
            with _mgmt_prmt_coupon_addCoupon(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"
                id = r.json()["data"]

        @allure.step("优惠券审核")
        def step_mgmt_prmt_coupon_examine():
            
            data = {
                "promotionId":None,
                "examine": 3, # 审核是否通过3通过4不通过
                "remarks":"我同意了", # 备注
                "enclosureVos":[], # 附件集合
                "couponId": id # 优惠券id
            }
            with _mgmt_prmt_coupon_examine(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"

        
        step_mgmt_prmt_coupon_selectCouponNumber()
        if message != "优惠券编码不能重复":
            step_mgmt_prmt_coupon_addCoupon()
            step_mgmt_prmt_coupon_examine()

            
