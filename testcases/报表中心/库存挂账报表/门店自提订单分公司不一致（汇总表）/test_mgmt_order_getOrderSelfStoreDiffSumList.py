# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getOrderStoreDiffSumList import params, _mgmt_order_getOrderStoreDiffSumList # 门店自提订单分公司不一致（汇总表）
from api.mall_center_sys._mgmt_sys_getComByCodeOrPri import params as params02, _mgmt_sys_getComByCodeOrPri # 公司资料查询展示
from api.mall_mgmt_application._mgmt_order_countOrderStoreDiffDetailByProList import params as params03, _mgmt_order_countOrderStoreDiffDetailByProList # 门店自提订单分公司不一致（明细表）- 按产品 统计

from setting import P1, P2, P3, username, store, username_vip, store_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderStoreDiffSumList")
class TestClass:
    """
    门店自提订单分公司不一致（汇总表）
    /mgmt/order/getOrderStoreDiffSumList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]

    
    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（汇总表）-成功路径: 查询月份检查")
    def test_01_mgmt_order_getOrderStoreDiffSumList(self):
        
        params = deepcopy(self.params)               
        with _mgmt_order_getOrderStoreDiffSumList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["month"] for d in r.json()["data"]["list"][:-1]):
                assert i == time.strftime("%Y-%m",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（汇总表）-成功路径: 查询服务中心所属分公司检查")
    def test_02_mgmt_order_getOrderStoreDiffSumList(self):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]
        
        @allure.step("门店自提订单分公司不一致（汇总表）")
        def step_mgmt_order_getOrderStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["companyCode"] = getComByCodeOrPri["code"]               
            with _mgmt_order_getOrderStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["companyName"] for d in r.json()["data"]["list"][:-1]):
                            assert i == getComByCodeOrPri["fullName"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getComByCodeOrPri()
        for getComByCodeOrPri in getComByCodeOrPris[1:]:
            step_mgmt_order_getOrderStoreDiffSumList()

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（汇总表）-成功路径: 查询订单财务分公司检查")
    def test_03_mgmt_order_getOrderStoreDiffSumList(self):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]
        
        @allure.step("门店自提订单分公司不一致（汇总表）")
        def step_mgmt_order_getOrderStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["financeCompanyCode"] = getComByCodeOrPri["code"]               
            with _mgmt_order_getOrderStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["financeCompanyName"] for d in r.json()["data"]["list"][:-1]):
                            assert i == getComByCodeOrPri["fullName"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getComByCodeOrPri()
        for getComByCodeOrPri in getComByCodeOrPris[1:]:
            step_mgmt_order_getOrderStoreDiffSumList()

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderStoreDiffSumList")
class TestClass02:
    """
    门店自提订单分公司不一致（汇总表）：合计列金额和明细表对比检查
    /mgmt/order/getOrderStoreDiffSumList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（汇总表）-成功路径: 查询服务中心所属分公司汇总数据=明细表汇总数据检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_01_mgmt_order_getOrderStoreDiffSumList(self, companyCode):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        countOrderStoreDiffDetailList = 0 # 门店自提订单分公司不一致（明细表）- 按订单统计
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]

        @allure.step("门店自提订单分公司不一致（明细表）- 按产品 统计")
        def step_mgmt_order_countOrderStoreDiffDetailByProList():        
        
            nonlocal countOrderStoreDiffDetailList
            params = deepcopy(self.params03)
            params["companyCode"] = companyCode               
            with _mgmt_order_countOrderStoreDiffDetailByProList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                countOrderStoreDiffDetailList = r.json()["data"]["internalAmount"]
        
        @allure.step("门店自提订单分公司不一致（汇总表）")
        def step_mgmt_order_getOrderStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["companyCode"] = companyCode               
            with _mgmt_order_getOrderStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["companyName"] == "合计":
                        assert i["internalAmount"] == countOrderStoreDiffDetailList

        step_mgmt_sys_getComByCodeOrPri()
        step_mgmt_order_countOrderStoreDiffDetailByProList()
        step_mgmt_order_getOrderStoreDiffSumList()

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（汇总表）-成功路径: 查询订单财务分公司汇总数据=明细表汇总数据检查")
    @pytest.mark.parametrize("financeCompanyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_order_getOrderStoreDiffSumList(self, financeCompanyCode):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        countOrderStoreDiffDetailList = 0 # 门店自提订单分公司不一致（明细表）- 按订单统计
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]

        @allure.step("门店自提订单分公司不一致（明细表）- 按产品 统计")
        def step_mgmt_order_countOrderStoreDiffDetailByProList():        
        
            nonlocal countOrderStoreDiffDetailList
            params = deepcopy(self.params03)
            params["financeCompanyCode"] = financeCompanyCode              
            with _mgmt_order_countOrderStoreDiffDetailByProList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                countOrderStoreDiffDetailList = r.json()["data"]["internalAmount"]
        
        @allure.step("门店自提订单分公司不一致（汇总表）")
        def step_mgmt_order_getOrderStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["financeCompanyCode"] = financeCompanyCode             
            with _mgmt_order_getOrderStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["companyName"] == "合计":
                        assert i["internalAmount"] == countOrderStoreDiffDetailList

        step_mgmt_sys_getComByCodeOrPri()
        step_mgmt_order_countOrderStoreDiffDetailByProList()
        step_mgmt_order_getOrderStoreDiffSumList()
