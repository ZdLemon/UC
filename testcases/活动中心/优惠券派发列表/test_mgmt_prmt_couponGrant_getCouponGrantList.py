# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_couponGrant_getCouponGrantList import params ,_mgmt_prmt_couponGrant_getCouponGrantList

from setting import P1, P2, P3, couponName, couponNumber

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/couponGrant/getCouponGrantList")
class TestClass:
    """
    优惠券派发列表-分页查询派发记录
    /mgmt/prmt/couponGrant/getCouponGrantList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 查询默认条件检查")
    def test_01_mgmt_prmt_couponGrant_getCouponGrantList(self):
            
        params = deepcopy(self.params)             
        with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 支持模糊查询优惠券名称检查")
    @pytest.mark.parametrize("couponName", [couponName, couponName[:-1]], ids=["优惠券完整名称", "优惠券名称的一部分"])
    def test_02_mgmt_prmt_couponGrant_getCouponGrantList(self, couponName):
            
        params = deepcopy(self.params)
        params["couponName"] = couponName       
        with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert couponName in d["couponName"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 支持模糊查询优惠券编号检查")
    @pytest.mark.parametrize("couponNumber", [couponNumber, couponNumber[:-1]], ids=["优惠券完整编号", "优惠券编号的一部分"])
    def test_03_mgmt_prmt_couponGrant_getCouponGrantList(self, couponNumber):
            
        params = deepcopy(self.params)
        params["couponNumber"] = couponNumber       
        with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert couponNumber in d["couponNumber"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 查询派发创建时间检查")
    def test_04_mgmt_prmt_couponGrant_getCouponGrantList(self):
        
        createTime = None
        
        @allure.step("获取创建时间")
        def step_01_mgmt_prmt_couponGrant_getCouponGrantList():    
            
            nonlocal createTime
            params = deepcopy(self.params)      
            with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
                createTime = r.json()["data"]["list"][0]["createTime"][:10]
        
        @allure.step("查询派发创建时间")
        def step_02_mgmt_prmt_couponGrant_getCouponGrantList():    
            
            params = deepcopy(self.params) 
            params["createTimeMin"] = f"{createTime} 00:00:00"
            params["createTimeMax"] = f"{createTime} 23:59:59"
            with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert d["createTime"][:10] == createTime
        
        step_01_mgmt_prmt_couponGrant_getCouponGrantList()
        step_02_mgmt_prmt_couponGrant_getCouponGrantList()

    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 查询派发对象检查")
    @pytest.mark.parametrize("grantTarget", [2, 4], ids=["顾客身份", "自由导入"])
    def test_05_mgmt_prmt_couponGrant_getCouponGrantList(self, grantTarget):
            
        params = deepcopy(self.params)
        params["grantTarget"] = grantTarget       
        with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["grantTarget"] for d in r.json()["data"]["list"]):
                    assert i == grantTarget
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 查询派发对象检查")
    @pytest.mark.parametrize("grantType", [1, 2, 3, 4], ids=["即时派发", "定时派发", "每日循环派发", "每月定时派发"])
    def test_06_mgmt_prmt_couponGrant_getCouponGrantList(self, grantType):
            
        params = deepcopy(self.params)
        params["grantType"] = grantType # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
        with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["grantType"] for d in r.json()["data"]["list"]):
                    assert i == grantType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券派发列表-成功路径: 查询发放状态检查")
    @pytest.mark.parametrize("state", [1, 2, 3, 4, 5, 6], ids=["待审核", "派发中", "已完成", "已驳回", "草稿", "已停止"])
    def test_07_mgmt_prmt_couponGrant_getCouponGrantList(self, state):
            
        params = deepcopy(self.params)
        params["state"] = state # 发放状态1待审核2派发中3已完成4已驳回5草稿6已停止
        with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["state"] for d in r.json()["data"]["list"]):
                    assert i == state
            else:
                assert r.json()["data"]["list"] == []












