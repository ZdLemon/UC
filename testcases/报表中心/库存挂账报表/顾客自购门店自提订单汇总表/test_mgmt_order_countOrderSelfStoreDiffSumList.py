# coding:utf-8

from api.mall_mgmt_application._mgmt_order_countOrderSelfStoreDiffSumList import params, _mgmt_order_countOrderSelfStoreDiffSumList # 顾客自购门店自提订单分公司不一致（汇总表）统计统计
from api.mall_center_sys._mgmt_sys_getComByCodeOrPri import params as params02, _mgmt_sys_getComByCodeOrPri # 公司资料查询展示
from api.mall_mgmt_application._mgmt_order_countOrderStoreDiffDetailList import params as params03, _mgmt_order_countOrderStoreDiffDetailList # 门店自提订单分公司不一致（明细表）- 按产品 统计
from api.mall_mgmt_application._mgmt_order_getOrderStoreDiffDetailList import params as params04, _mgmt_order_getOrderStoreDiffDetailList # 门店自提订单分公司不一致（明细表）-按订单
from setting import P1, P2, P3, username, store, username_vip, store_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/countOrderSelfStoreDiffSumList")
class TestClass:
    """
    顾客自购门店自提订单分公司不一致（汇总表）统计
    /mgmt/order/countOrderSelfStoreDiffSumList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("业务分公司不为财务分公司的订单总金额=门店自提订单分公司不一致（明细表）按订单-订单实付金额合计检查")
    @pytest.mark.parametrize("financeCompanyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_01_mgmt_order_countOrderSelfStoreDiffSumList(self, financeCompanyCode):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        countOrderStoreDiffDetailList = 0 # 门店自提订单分公司不一致（明细表）- 按订单 统计
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]

        @allure.step("门店自提订单分公司不一致（明细表）- 按订单 统计")
        def step_mgmt_order_countOrderStoreDiffDetailList():        
        
            nonlocal countOrderStoreDiffDetailList
            params = deepcopy(self.params03)
            params["financeCompanyCode"] = financeCompanyCode             
            with _mgmt_order_countOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    countOrderStoreDiffDetailList = float(r.json()["data"]["totalAmount"])
        
        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）统计")
        def step_mgmt_order_countOrderSelfStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["financeCompanyCode"] = financeCompanyCode             
            with _mgmt_order_countOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["totalAmount"]:
                    assert r.json()["data"]["companyNeqAmount"] == countOrderStoreDiffDetailList
                else:
                    assert r.json()["data"]["companyNeqAmount"] is None and countOrderStoreDiffDetailList == 0
        
        step_mgmt_sys_getComByCodeOrPri()
        step_mgmt_order_countOrderStoreDiffDetailList()
        step_mgmt_order_countOrderSelfStoreDiffSumList()

    @allure.severity(P2)
    @allure.title("业务分公司不为财务分公司的订单总数=门店自提订单分公司不一致（明细表）按订单-订单数检查")
    @pytest.mark.parametrize("financeCompanyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_order_countOrderSelfStoreDiffSumList(self, financeCompanyCode):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        getOrderStoreDiffDetailList = 0 # 门店自提订单分公司不一致（明细表）- 按订单
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]

        @allure.step("门店自提订单分公司不一致（明细表）-按订单")
        def step_mgmt_order_getOrderStoreDiffDetailList():        
        
            nonlocal getOrderStoreDiffDetailList
            params = deepcopy(self.params03)
            params["financeCompanyCode"] = financeCompanyCode             
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getOrderStoreDiffDetailList = r.json()["data"]["total"]
        
        @allure.step("顾客自购门店自提订单分公司不一致（汇总表）统计")
        def step_mgmt_order_countOrderSelfStoreDiffSumList():        
        
            params = deepcopy(self.params)
            params["financeCompanyCode"] = financeCompanyCode             
            with _mgmt_order_countOrderSelfStoreDiffSumList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["totalAmount"]:
                    assert r.json()["data"]["companyNeqQty"] == getOrderStoreDiffDetailList
                else:
                    assert r.json()["data"]["companyNeqQty"] is None and getOrderStoreDiffDetailList == 0
        
        step_mgmt_sys_getComByCodeOrPri()
        step_mgmt_order_getOrderStoreDiffDetailList()
        step_mgmt_order_countOrderSelfStoreDiffSumList()




