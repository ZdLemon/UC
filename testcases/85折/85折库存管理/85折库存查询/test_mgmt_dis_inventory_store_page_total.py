# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_store_page_total import params, _mgmt_dis_inventory_store_page_total

from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter

# TODO
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/store/total")
class TestClass:
    """
    库存合计（按服务中心维度）
    /mgmt/dis-inventory/store/total
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("库存合计-按服务中心维度-成功路径: 查询默认条件检查")
    def test_01_mgmt_dis_inventory_store_page_total(self):
            
        params = deepcopy(self.params)                 
        with _mgmt_dis_inventory_store_page_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("库存合计-按服务中心维度-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_store_page_total(self, companyCode):
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode                
        with _mgmt_dis_inventory_store_page_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("库存合计-按服务中心维度-成功路径: 查询服务中心编号检查")
    def test_03_mgmt_dis_inventory_store_page_total(self):
            
        params = deepcopy(self.params) 
        params["storeCode"] = store_85                 
        with _mgmt_dis_inventory_store_page_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("库存合计-按服务中心维度-成功路径: 查询店零售价合计检查")
    @pytest.mark.parametrize("operator,retailPrice,ids", [
        (0, 10000, "店零售价合计=10"), 
        (1, 10000, "店零售价合计>=10"), 
        (2, 10000, "店零售价合计>10"), 
        (3, 10000, "店零售价合计<=10"), 
        (4, 10000, "店零售价合计<10")
    ])
    def test_04_mgmt_dis_inventory_store_page_total(self, operator, retailPrice, ids):
            
        params = deepcopy(self.params)
        params["operator"] = operator
        params["retailPrice"] = retailPrice
        with _mgmt_dis_inventory_store_page_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200


