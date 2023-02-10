# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_returnOrder_listOrder import params ,_mgmt_inventory_returnOrder_listOrder # 后台查询押货后台查询押货退货单列表
from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/returnOrder/getOrderDetail")
class TestClass:
    """
    后台押货退货单详情
    /mgmt/inventory/returnOrder/getOrderDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("后台押货退货单详情-成功路径: 后台押货退货单详情检查")
    def test_mgmt_inventory_returnOrder_getOrderDetail(self):
            
        params = deepcopy(self.params) 
        orderSn = None 
        id = None
        productVoList = None # 押货退货单产品信息
        
        @allure.step("获取退货单号")
        def step_01_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal orderSn          
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderSn = r.json()["data"]["list"][0]["orderSn"]
        
        @allure.step("获取退货单id")
        def step_02_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]

        
        @allure.step("后台押货退货单详情")
        def step_mgmt_inventory_returnOrder_getOrderDetail():
            
            nonlocal productVoList
            params = {
                "orderId": id
            }
            with _mgmt_inventory_returnOrder_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList =  r.json()["data"]["productVoList"][0]
        
        step_01_mgmt_inventory_returnOrder_listOrder()
        step_02_mgmt_inventory_returnOrder_listOrder()
        step_mgmt_inventory_returnOrder_getOrderDetail()

 