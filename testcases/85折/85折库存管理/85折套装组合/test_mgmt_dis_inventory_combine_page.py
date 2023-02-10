# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_combine_page import params ,_mgmt_dis_inventory_combine_page

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/combine/page")
class TestClass:
    """
    分页查询套装组合列表
    /mgmt/dis-inventory/combine/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("分页查询套装组合列表-成功路径: 默认查询检查")
    def test_01_mgmt_dis_inventory_combine_page(self):
        
        params = deepcopy(self.params)
        with _mgmt_dis_inventory_combine_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_combine_page(self, companyCode):
        
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode                  
        with _mgmt_dis_inventory_combine_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []


    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_03_mgmt_dis_inventory_combine_page(self, storeCode):
        
        params = deepcopy(self.params) 
        params["storeCode"] = storeCode                  
        with _mgmt_dis_inventory_combine_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 支持模糊查询产品编号检查")
    @pytest.mark.parametrize("product", [productCode_zh, productCode_zh[:-1]], ids=["正确的产品编号", "产品编号的一部分"])
    def test_04_mgmt_dis_inventory_combine_page(self, product, onSaleVersion):
        
        params = deepcopy(self.params) 
        params["product"] = product                  
        with _mgmt_dis_inventory_combine_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["productCode"] for d in r.json()["data"]["list"]):
                    assert product in i
            else:
                assert r.json()["data"]["list"] == []





