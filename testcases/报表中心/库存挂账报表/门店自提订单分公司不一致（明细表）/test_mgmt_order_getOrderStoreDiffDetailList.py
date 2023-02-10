# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getOrderStoreDiffDetailList import params, _mgmt_order_getOrderStoreDiffDetailList # 门店自提订单分公司不一致（明细表）-按订单
from api.mall_center_sys._mgmt_sys_getComByCodeOrPri import params as params02, _mgmt_sys_getComByCodeOrPri # 公司资料查询展示
from api.mall_mgmt_application._mgmt_order_orderList import params as params03, _mgmt_order_orderList # 订单列表

from setting import P1, P2, P3, username, store, username_vip, store_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderStoreDiffDetailList")
class TestClass:
    """
    门店自提订单分公司不一致（明细表）-按订单
    /mgmt/order/getOrderStoreDiffDetailList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（明细表）-按订单-成功路径: 查询付款/退款日期检查")
    def test_01_mgmt_order_getOrderStoreDiffDetailList(self):
        
        params = deepcopy(self.params)               
        with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["payTime"] for d in r.json()["data"]["list"]):
                    assert time.strftime("%Y-%m-%d",time.localtime(i / 1000)) == time.strftime("%Y-%m-%d",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（明细表）-按订单-成功路径: 查询订单财务分公司检查")
    def test_02_mgmt_order_getOrderStoreDiffDetailList(self):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]
        
        @allure.step("门店自提订单分公司不一致（明细表）")
        def step_mgmt_order_getOrderStoreDiffDetailList():        
        
            params = deepcopy(self.params)
            params["financeCompanyCode"] = getComByCodeOrPri["code"]               
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["financeCompanyName"] for d in r.json()["data"]["list"]):
                            assert i == getComByCodeOrPri["fullName"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getComByCodeOrPri()
        for getComByCodeOrPri in getComByCodeOrPris[1:]:
            step_mgmt_order_getOrderStoreDiffDetailList()

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（明细表）-按订单-成功路径: 查询服务中心所属分公司检查")
    def test_03_mgmt_order_getOrderStoreDiffDetailList(self):
        
        getComByCodeOrPris = [] # 公司资料查询展示
        
        @allure.step("公司资料查询展示")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal getComByCodeOrPris
            params = deepcopy(self.params02)                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getComByCodeOrPris = r.json()["data"]["list"]
        
        @allure.step("门店自提订单分公司不一致（明细表）")
        def step_mgmt_order_getOrderStoreDiffDetailList():        
        
            params = deepcopy(self.params)
            params["companyCode"] = getComByCodeOrPri["code"]               
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["companyName"] for d in r.json()["data"]["list"]):
                            assert i == getComByCodeOrPri["fullName"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getComByCodeOrPri()
        for getComByCodeOrPri in getComByCodeOrPris[1:]:
            step_mgmt_order_getOrderStoreDiffDetailList()

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（明细表）-按订单-成功路径: 仅支持精确查询服务中心编码检查")
    def test_04_mgmt_order_getOrderStoreDiffDetailList(self):
        
        getOrderSelfStoreDiffSumList = [] # 公司资料查询展示
        
        @allure.step("门店自提订单分公司不一致（明细表）-按订单:获取服务中心编码")
        def step_01_mgmt_order_getOrderStoreDiffDetailList():        
            
            nonlocal getOrderSelfStoreDiffSumList
            params = deepcopy(self.params) 
            params["beginDate"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-1 00:00:00" # 开始时间 默认当天2022-06-17 00:00:00 当月第一天
            params["endDate"] = f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))} 23:59:59", # 结束时间 默认当天2022-06-17 23:59:59                 
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderSelfStoreDiffSumList = r.json()["data"]["list"][0]

        @allure.step("门店自提订单分公司不一致（明细表）-按订单:精确查询服务中心编码")
        def step_02_mgmt_order_getOrderStoreDiffDetailList():        
            
            params = deepcopy(self.params)  
            params["storeCode"] = getOrderSelfStoreDiffSumList["storeCode"]
            params["beginDate"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-1 00:00:00" # 开始时间 默认当天2022-06-17 00:00:00 当月第一天
            params["endDate"] = f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))} 23:59:59", # 结束时间 默认当天2022-06-17 23:59:59    
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getOrderSelfStoreDiffSumList["storeCode"] in set(d["storeCode"] for d in r.json()["data"]["list"])

        step_01_mgmt_order_getOrderStoreDiffDetailList()
        step_02_mgmt_order_getOrderStoreDiffDetailList()   

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（明细表）-按订单-成功路径: 仅支持精确查询订单编码检查")
    def test_05_mgmt_order_getOrderStoreDiffDetailList(self):
        
        getOrderSelfStoreDiffSumList = [] # 公司资料查询展示
        
        @allure.step("门店自提订单分公司不一致（明细表）-按订单:获取订单编码")
        def step_01_mgmt_order_getOrderStoreDiffDetailList():        
            
            nonlocal getOrderSelfStoreDiffSumList
            params = deepcopy(self.params)              
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getOrderSelfStoreDiffSumList = r.json()["data"]["list"][0]

        @allure.step("门店自提订单分公司不一致（明细表）-按订单:精确查询订单编码")
        def step_02_mgmt_order_getOrderStoreDiffDetailList():        
            
            params = deepcopy(self.params)  
            params["orderNo"] = getOrderSelfStoreDiffSumList["orderNo"]
            params["beginDate"] = None
            params["endDate"] = None          
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getOrderSelfStoreDiffSumList["orderNo"] in set(d["orderNo"] for d in r.json()["data"]["list"])

        step_01_mgmt_order_getOrderStoreDiffDetailList()
        if getOrderSelfStoreDiffSumList:
            step_02_mgmt_order_getOrderStoreDiffDetailList()   

 
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderStoreDiffDetailList")
class TestClass02:
    """
    门店自提订单分公司不一致（明细表）-按订单:列表每条数据所有字段和订单数据对比校验
    /mgmt/order/getOrderStoreDiffDetailList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("门店自提订单分公司不一致（明细表）-按订单-成功路径: 各字段信息检查")
    def test_01_mgmt_order_getOrderStoreDiffDetailList(self):
        
        getOrderStoreDiffDetailList = [] # 门店自提订单分公司不一致（明细表）
        
        @allure.step("门店自提订单分公司不一致（明细表）")
        def step_mgmt_order_getOrderStoreDiffDetailList():
              
            nonlocal getOrderStoreDiffDetailList
            params = deepcopy(self.params)
            params["pageSize"] = 100              
            with _mgmt_order_getOrderStoreDiffDetailList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getOrderStoreDiffDetailList = r.json()["data"]["list"]
        
        @allure.title("订单列表-成功路径: 查询订单编号检查")
        def test_mgmt_order_orderList():
                
            params = deepcopy(self.params03)
            params["orderNo"] = getOrderStoreDiffDetail["orderNo"]               
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["orderStatus"] in [2, 3, 5, 99] # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
                assert r.json()["data"]["list"][0]["payTime"] == getOrderStoreDiffDetail["payTime"] # 付款日期/退款日期
                assert r.json()["data"]["list"][0]["storeCode"] == getOrderStoreDiffDetail["storeCode"] # 服务中心编号
                assert r.json()["data"]["list"][0]["companyName"] == getOrderStoreDiffDetail["companyName"] # 服务中心所属分公司
                assert r.json()["data"]["list"][0]["totalAmount"] == float(getOrderStoreDiffDetail["totalAmount"]) # 订单实付金额
                assert r.json()["data"]["list"][0]["financeCompanyName"] == getOrderStoreDiffDetail["financeCompanyName"] # 订单财务分公司
                       
        step_mgmt_order_getOrderStoreDiffDetailList()
        if getOrderStoreDiffDetailList:
            for getOrderStoreDiffDetail in getOrderStoreDiffDetailList:
                test_mgmt_order_orderList()
        