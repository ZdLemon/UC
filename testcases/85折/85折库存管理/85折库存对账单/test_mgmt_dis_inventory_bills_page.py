# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_settled_scope import _mgmt_dis_inventory_settled_scope
from api.mall_mgmt_application._mgmt_dis_inventory_bills_page import params, _mgmt_dis_inventory_bills_page
from setting import P1, P2, P3, productCode_zh, productCode, store_85, storeName_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/bills/page")
class TestClass:
    """
    分页查询库存对账单
    /mgmt/dis-inventory/bills/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("分页查询库存对账单-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_01_mgmt_dis_inventory_bills_page(self, companyCode):
            
        maxMonth = None # 最近的月结月份
        
        @allure.step("获取月结完成时间范围")
        def step_mgmt_dis_inventory_settled_scope():
            
            nonlocal maxMonth           
            with _mgmt_dis_inventory_settled_scope(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                maxMonth = r.json()["data"]["maxMonth"]
        
        @allure.step("分页查询库存列表")
        def step_mgmt_dis_inventory_bills_page():
            
            params = deepcopy(self.params) 
            params["minMonth"] = maxMonth
            params["maxMonth"] = maxMonth
            params["companyCode"] = companyCode     
            with _mgmt_dis_inventory_bills_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["page"]["list"]:
                    for i in set(d["companyCode"] for d in r.json()["data"]["page"]["list"]):
                        assert i == companyCode
                else:
                    assert r.json()["data"]["page"]["list"] == []
                            
        step_mgmt_dis_inventory_settled_scope()
        step_mgmt_dis_inventory_bills_page()

    @allure.severity(P2)
    @allure.title("分页查询库存对账单-成功路径: 查询服务中心编号检查")
    def test_02_mgmt_dis_inventory_bills_page(self):
            
        maxMonth = None # 最近的月结月份
        
        @allure.step("获取月结完成时间范围")
        def step_mgmt_dis_inventory_settled_scope():
            
            nonlocal maxMonth           
            with _mgmt_dis_inventory_settled_scope(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                maxMonth = r.json()["data"]["maxMonth"]
        
        @allure.step("分页查询库存列表")
        def step_mgmt_dis_inventory_bills_page():
            
            params = deepcopy(self.params) 
            params["minMonth"] = maxMonth
            params["maxMonth"] = maxMonth
            params["storeCode"] = store_85    
            with _mgmt_dis_inventory_bills_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["page"]["list"]:
                    for i in set(d["storeCode"] for d in r.json()["data"]["page"]["list"]):
                        assert i == store_85
                else:
                    assert r.json()["data"]["page"]["list"] == []
                            
        step_mgmt_dis_inventory_settled_scope()
        step_mgmt_dis_inventory_bills_page()









