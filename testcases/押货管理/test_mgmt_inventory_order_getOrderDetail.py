# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params ,_mgmt_inventory_order_listMortgageOrder
from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import params as params02, _mgmt_inventory_order_getOrderDetail
from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/getOrderDetail")
class TestClass:
    """
    后台获取押货单详情
    /mgmt/inventory/order/getOrderDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
        

    @allure.severity(P1)
    @allure.title("后台获取押货单详情-成功路径: 后台获取押货单详情检查")
    def test_mgmt_inventory_order_getOrderDetail(self):
            
        params = deepcopy(self.params) 
        orderSn = None
        id = None
        productNum = None
        
        @allure.step("获取退货单号")
        def step_01_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal orderSn          
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderSn = r.json()["data"]["list"][0]["orderSn"]
        
        @allure.step("获取id")
        def step_02_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productNum
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productNum = r.json()["data"]["productVoList"][0]["productNum"]
        
        step_01_mgmt_inventory_order_listMortgageOrder()
        step_02_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()

  