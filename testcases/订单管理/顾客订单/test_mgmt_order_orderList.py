# coding:utf-8

from api.mall_mgmt_application._mgmt_order_orderList import params ,_mgmt_order_orderList

from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/orderList")
class TestClass:
    """
    订单列表
    /mgmt/order/orderList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("订单列表-成功路径: 切换不同tab列表检查")
    # @pytest.mark.parametrize("orderStatusList", [1, 0, -3, "-1,-2", 2, 3, 99, 5, "4,98"])
    def test_01_mgmt_order_orderList(self):
            
        @allure.step("订单列表:待付款")
        def step_01_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 1 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 1   

        @allure.step("订单列表:待审核")
        def step_02_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 0 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 0   
                        
        @allure.step("订单列表:待支付定金")
        def step_03_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = -3 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == -3                           
                        
        @allure.step("订单列表:待支付尾款")
        def step_04_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = -1,-2 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == -1 or i == -2  
                        
        @allure.step("订单列表:待发货")
        def step_05_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 2 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 2                           
                        
        @allure.step("订单列表:待收货")
        def step_06_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 3 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 3  
                        
        @allure.step("订单列表:已完成")
        def step_07_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 99 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 99                         
                        
        @allure.step("订单列表:已退货")
        def step_08_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 5 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 5                        
                                 
        @allure.step("订单列表:已取消")
        def step_09_mgmt_order_orderList():
            
            params = deepcopy(self.params)
            params["orderStatusList"] = 4,98 # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成              
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["orderStatus"] for d in r.json()["data"]["list"]):
                        assert i == 4 or i == 98                         
                                                                                 
                                
        step_01_mgmt_order_orderList() 
        step_02_mgmt_order_orderList()           
        step_03_mgmt_order_orderList() 
        step_04_mgmt_order_orderList()                   
        step_05_mgmt_order_orderList() 
        step_06_mgmt_order_orderList()   
        step_07_mgmt_order_orderList() 
        step_08_mgmt_order_orderList()
        step_09_mgmt_order_orderList()    