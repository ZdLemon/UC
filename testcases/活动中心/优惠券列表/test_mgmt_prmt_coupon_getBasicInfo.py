# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params ,_mgmt_prmt_coupon_getListPage
from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity
from api.mall_mgmt_application._mgmt_prmt_couponGrant_clearImportMember import _mgmt_prmt_couponGrant_clearImportMember
from api.mall_mgmt_application._mgmt_prmt_coupon_getBasicInfo import _mgmt_prmt_coupon_getBasicInfo

from setting import P1, P2, P3, couponName, couponNumber
from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/coupon/getBasicInfo")
class TestClass:
    """
    优惠券详情-基础信息
    /mgmt/prmt/coupon/getBasicInfo
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("清除缓存里导入的派发用户-成功路径: 派发优惠券时清除缓存里导入的派发用户检查")
    def test_mgmt_prmt_coupon_getBasicInfo(self):
        
        id = None # 优惠券id
        
        @allure.step("优惠券列表:获取id")
        def step_mgmt_prmt_coupon_getListPage():
            
            nonlocal id
            params = deepcopy(self.params)
            params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("获取所有顾客身份类型")                   
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == [
                    {
                        "code": 1,
                        "typeName": "会员"
                    }, 
                    {
                        "code": 2,
                        "typeName": "VIP会员"
                    }, 
                    {
                        "code": 3,
                        "typeName": "云商"
                    }, 
                    {
                        "code": 4,
                        "typeName": "微店"
                    }
                ]

        @allure.step("清除缓存里导入的派发用户")                   
        def step_mgmt_prmt_couponGrant_clearImportMember():
                           
            with _mgmt_prmt_couponGrant_clearImportMember(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("优惠券详情-基础信息")                   
        def step_mgmt_prmt_coupon_getBasicInfo():
            
            params ={"id": id}               
            with _mgmt_prmt_coupon_getBasicInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_prmt_coupon_getListPage()
        step_mgmt_prmt_getMemberIdentity()
        step_mgmt_prmt_couponGrant_clearImportMember()
        step_mgmt_prmt_coupon_getBasicInfo()
