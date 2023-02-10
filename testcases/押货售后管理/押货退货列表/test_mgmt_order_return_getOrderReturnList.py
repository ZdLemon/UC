# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_returnOrder_listOrder import params ,_mgmt_inventory_returnOrder_listOrder

from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/returnOrder/listOrder")
class TestClass:
    """
    后台查询押货后台查询押货退货单列表
    /mgmt/inventory/returnOrder/listOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 默认查询本月检查")
    def test_01_mgmt_inventory_returnOrder_listOrder(self):
            
        params = deepcopy(self.params)              
        with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_02_mgmt_inventory_returnOrder_listOrder(self):
            
        params = deepcopy(self.params) 
        storeCode = None 
        
        @allure.step("获取服务中心编号")
        def step_01_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal storeCode           
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeCode = r.json()["data"]["list"][0]["storeCode"]
        
        @allure.step("精确查询服务中心编号")
        def step_02_mgmt_inventory_returnOrder_listOrder():
            
            params["storeCode"] = storeCode
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
        
        @allure.step("模糊查询服务中心编号")
        def step_03_mgmt_inventory_returnOrder_listOrder():
            
            params["storeCode"] = storeCode[:-1]
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_returnOrder_listOrder()
        step_02_mgmt_inventory_returnOrder_listOrder()
        step_03_mgmt_inventory_returnOrder_listOrder()

    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 仅支持精确查询退货单号检查")
    def test_03_mgmt_inventory_returnOrder_listOrder(self):
            
        params = deepcopy(self.params) 
        orderSn = None 
        
        @allure.step("获取退货单号")
        def step_01_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal orderSn          
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderSn = r.json()["data"]["list"][0]["orderSn"]
        
        @allure.step("精确查询退货单号")
        def step_02_mgmt_inventory_returnOrder_listOrder():
            
            params["orderSn"] = orderSn
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["orderSn"] for d in r.json()["data"]["list"]):
                    assert i == orderSn
        
        @allure.step("模糊查询退货单号")
        def step_03_mgmt_inventory_returnOrder_listOrder():
            
            params["storeCode"] = orderSn[:-1]
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_returnOrder_listOrder()
        step_02_mgmt_inventory_returnOrder_listOrder()
        step_03_mgmt_inventory_returnOrder_listOrder()

    @allure.severity(P3)
    @allure.title("后台查询押货退货单列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_04_mgmt_inventory_returnOrder_listOrder(self, companyCode):
                    
        params["companyCode"] = companyCode
        with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                assert i == companyCode
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询押货退货单标识检查")
    @pytest.mark.parametrize("orderMark,ids", [(1, "普通押货退货"), (2, "套装组合退货"), (3, "套装拆分退货"), (4, "押货修改退")])
    def test_05_mgmt_inventory_returnOrder_listOrder(self, orderMark, ids):
                    
        params["orderMark"] = orderMark # 押货退货单标识 1普通押货退货 2套装组合退货 3套装拆分退货 4押货修改退
        with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["orderMark"] for d in r.json()["data"]["list"]):
                assert i == orderMark
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询押货退货单来源检查")
    @pytest.mark.parametrize("orderSource,ids", [(1, "服务中心退货"), (2, "运营后台退货")])
    def test_06_mgmt_inventory_returnOrder_listOrder(self, orderSource, ids):
                    
        params["orderSource"] = orderSource # 退货单来源 1服务中心退货 2运营后台退货
        with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["orderSource"] for d in r.json()["data"]["list"]):
                assert i == orderSource
        







