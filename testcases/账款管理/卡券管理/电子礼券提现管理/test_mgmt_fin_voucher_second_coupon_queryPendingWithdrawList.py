# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_gift_coupon_queryWithdrawList import data, _mgmt_fin_voucher_gift_coupon_queryWithdrawList
from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/gift/coupon/queryPendingWithdrawList")
class TestClass:
    """
    电子礼券提现列表(待受理)
    /mgmt/fin/voucher/gift/coupon/queryWithdrawList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("电子礼券提现列表（待受理不分页）: 仅支持精确查询会员卡号检查")
    def test_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（待受理不分页）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data)       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（待受理不分页）:精确查询会员卡号")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["cardNo"] = queryPendingWithdrawList["cardNo"]       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["cardNo"]
        
        @allure.step("电子礼券提现列表（待受理不分页）:模糊查询会员卡号")
        def step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["cardNo"] = queryPendingWithdrawList["cardNo"][:-1]   
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        if queryPendingWithdrawList:
            step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
            step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        
    @allure.severity(P2)
    @allure.title("电子礼券提现列表（待受理不分页）: 仅支持精确查询会员手机号检查")
    def test_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（待受理不分页）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data)       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（待受理不分页）:精确查询会员手机号")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["mobile"] = queryPendingWithdrawList["mobile"]       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["mobile"]
        
        @allure.step("电子礼券提现列表（待受理不分页）:模糊查询会员手机号")
        def step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["mobile"] = queryPendingWithdrawList["mobile"][:-1]   
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        if queryPendingWithdrawList:
            step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
            step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
   
    @allure.severity(P2)
    @allure.title("电子礼券提现列表（待受理不分页）-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType        
        with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
            if r.json()["data"]:
                for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                    assert i == memberType 
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("电子礼券提现列表（待受理不分页）: 查询提现时间检查")
    def test_04_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（待受理不分页）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data)       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（待受理不分页）:查询提现时间")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["withdrawStartTimeStr"] = queryPendingWithdrawList["withdrawTimeDesc"][:10] 
            data["withdrawEndTimeStr"] = queryPendingWithdrawList["withdrawTimeDesc"][:10]       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["withdrawTimeDesc"][:10] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["withdrawTimeDesc"][:10]
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        if queryPendingWithdrawList:
            step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/gift/coupon/queryPendingWithdrawList")
class TestClass02:
    """
    电子礼券提现列表（已受理）
    /mgmt/fin/voucher/gift/coupon/queryWithdrawList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已受理）: 仅支持精确查询会员卡号检查")
    def test_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（已受理）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销      
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（已受理）:精确查询会员卡号")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["cardNo"] = queryPendingWithdrawList["cardNo"] 
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["cardNo"]
        
        @allure.step("电子礼券提现列表（已受理）:模糊查询会员卡号")
        def step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["cardNo"] = queryPendingWithdrawList["cardNo"][:-1] 
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        
    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已受理）: 仅支持精确查询会员手机号检查")
    def test_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（已受理）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data) 
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（已受理）:精确查询会员手机号")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["mobile"] = queryPendingWithdrawList["mobile"] 
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["mobile"]
        
        @allure.step("电子礼券提现列表（已受理）:模糊查询会员手机号")
        def step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["mobile"] = queryPendingWithdrawList["mobile"][:-1]
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销    
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
   
    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已受理）-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType
        data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销         
        with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                    assert i == memberType 
            else:
                assert r.json()["data"] == []

    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已受理）: 查询提现时间检查")
    def test_04_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（已受理）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data) 
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（已受理）:查询提现时间")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["withdrawStartTimeStr"] = queryPendingWithdrawList["withdrawTimeDesc"][:10] 
            data["withdrawEndTimeStr"] = queryPendingWithdrawList["withdrawTimeDesc"][:10] 
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["withdrawTimeDesc"][:10] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["withdrawTimeDesc"][:10]
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/gift/coupon/queryPendingWithdrawList")
class TestClass03:
    """
    电子礼券提现列表（已撤销）
    /mgmt/fin/voucher/gift/coupon/queryPendingWithdrawList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已撤销）: 仅支持精确查询会员卡号检查")
    def test_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（已撤销理）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（已撤销）:精确查询会员卡号")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["cardNo"] = queryPendingWithdrawList["cardNo"] 
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销     
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["cardNo"]
        
        @allure.step("电子礼券提现列表（已撤销）:模糊查询会员卡号")
        def step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["cardNo"] = queryPendingWithdrawList["cardNo"][:-1] 
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        
    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已撤销）: 仅支持精确查询会员手机号检查")
    def test_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（已撤销）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data) 
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（已撤销）:精确查询会员手机号")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["mobile"] = queryPendingWithdrawList["mobile"] 
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销      
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["mobile"]
        
        @allure.step("电子礼券提现列表（已撤销）:模糊查询会员手机号")
        def step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["mobile"] = queryPendingWithdrawList["mobile"][:-1]
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销    
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_02_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
   
    @allure.severity(P3)
    @allure.title("电子礼券提现列表（已撤销）-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType
        data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销         
        with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
            if r.json()["data"]:
                for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                        assert i == memberType 
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("电子礼券提现列表（撤销）: 查询提现时间检查")
    def test_04_mgmt_fin_voucher_gift_coupon_queryWithdrawList(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表（撤销）")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data) 
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryPendingWithdrawList = r.json()["data"]["list"][0] 
        
        @allure.step("电子礼券提现列表（撤销）:查询提现时间")
        def step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList():
            
            data = deepcopy(self.data)
            data["withdrawStartTimeStr"] = queryPendingWithdrawList["withdrawTimeDesc"][:10] 
            data["withdrawEndTimeStr"] = queryPendingWithdrawList["withdrawTimeDesc"][:10] 
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销       
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["withdrawTimeDesc"][:10] for d in r.json()["data"]["list"]):
                    assert i == queryPendingWithdrawList["withdrawTimeDesc"][:10]
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawList()
        step_01_mgmt_fin_voucher_gift_coupon_queryWithdrawList()

      