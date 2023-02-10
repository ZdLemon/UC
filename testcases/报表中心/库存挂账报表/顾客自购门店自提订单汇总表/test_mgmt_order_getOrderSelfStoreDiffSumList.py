# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getOrderSelfStoreDiffSumList import params, _mgmt_order_getOrderSelfStoreDiffSumList # 顾客自购门店自提订单分公司不一致（汇总表）
from api.mall_center_sys._mgmt_sys_getComByCodeOrPri import params as params02, _mgmt_sys_getComByCodeOrPri # 公司资料查询展示

from setting import P1, P2, P3, username, store, username_vip, store_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSelfStoreDiffSumList")
class TestClass:
    """
    顾客自购门店自提订单分公司不一致（汇总表）
    /mgmt/order/getOrderSelfStoreDiffSumList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]

    
    @allure.severity(P2)
    @allure.title("顾客自购门店自提订单分公司不一致（汇总表）-成功路径: 查询月份检查")
    def test_01_mgmt_order_getOrderSelfStoreDiffSumList(self):
        
        params = deepcopy(self.params)               
        with _mgmt_order_getOrderSelfStoreDiffSumList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["month"] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("顾客自购门店自提订单分公司不一致（汇总表）-成功路径: 查询订单财务分公司检查")
    def test_02_mgmt_order_getOrderSelfStoreDiffSumList(self):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]
        
        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）")
        def step_mgmt_order_getOrderSelfStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["financeCompanyCode"] = getComByCodeOrPri["code"]               
            with _mgmt_order_getOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["financeCompanyName"] for d in r.json()["data"]["list"]):
                            assert i == getComByCodeOrPri["fullName"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getComByCodeOrPri()
        for getComByCodeOrPri in getComByCodeOrPris[1:]:
            step_mgmt_order_getOrderSelfStoreDiffSumList()

    @allure.severity(P2)
    @allure.title("顾客自购门店自提订单分公司不一致（汇总表）-成功路径: 仅支持精确查询卡号/姓名检查")
    def test_03_mgmt_order_getOrderSelfStoreDiffSumList(self):
        
        getOrderSelfStoreDiffSumList = [] # 公司资料查询展示
        
        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）:获取会员卡号姓名")
        def step_01_mgmt_order_getOrderSelfStoreDiffSumList():        
            
            nonlocal getOrderSelfStoreDiffSumList
            params = deepcopy(self.params)              
            with _mgmt_order_getOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderSelfStoreDiffSumList = r.json()["data"]["list"][0]

        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）:精确查询会员卡号")
        def step_02_mgmt_order_getOrderSelfStoreDiffSumList():        
            
            params = deepcopy(self.params)  
            params["customerCard"] = getOrderSelfStoreDiffSumList["customerCard"]           
            with _mgmt_order_getOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getOrderSelfStoreDiffSumList["customerCard"] in set(d["customerCard"] for d in r.json()["data"]["list"])

        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）:精确查询会员姓名")
        def step_03_mgmt_order_getOrderSelfStoreDiffSumList():        
            
            params = deepcopy(self.params)  
            params["customerCard"] = getOrderSelfStoreDiffSumList["customerName"]           
            with _mgmt_order_getOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getOrderSelfStoreDiffSumList["customerName"] in set(d["customerName"] for d in r.json()["data"]["list"])

        step_01_mgmt_order_getOrderSelfStoreDiffSumList()
        step_02_mgmt_order_getOrderSelfStoreDiffSumList()
        step_03_mgmt_order_getOrderSelfStoreDiffSumList()     


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSelfStoreDiffSumList")
class TestClass02:
    """
    顾客自购门店自提订单分公司不一致（汇总表）:订单总数=业务分公司为财务分公司的订单总数+业务分公司不为财务分公司的订单总数检查
    /mgmt/order/getOrderSelfStoreDiffSumList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("顾客自购门店自提订单分公司不一致（汇总表）: 订单总数=业务分公司为财务分公司的订单总数+业务分公司不为财务分公司的订单总数检查")
    def test_01_mgmt_order_getOrderSelfStoreDiffSumList(self):
        
        getOrderSelfStoreDiffSumList = [] # 公司资料查询展示
        
        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）:获取会员卡号姓名")
        def step_01_mgmt_order_getOrderSelfStoreDiffSumList():        
            
            nonlocal getOrderSelfStoreDiffSumList
            params = deepcopy(self.params)
            params["pageSize"] = 100            
            with _mgmt_order_getOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["totalQty"] == i["companyEqQty"] + i["companyNeqQty"]
                    assert i["totalAmount"] == i["companyEqAmount"] + i["companyNeqAmount"]

        step_01_mgmt_order_getOrderSelfStoreDiffSumList()

