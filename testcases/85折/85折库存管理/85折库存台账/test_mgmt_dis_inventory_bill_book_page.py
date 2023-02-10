# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_bill_book_page import params, _mgmt_dis_inventory_bill_book_page
from api.mall_mgmt_application._mgmt_product_cfg_menu_catalog import _mgmt_product_cfg_menu_catalog
from setting import P1, P2, P3, productCode, productCode_title, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/bill/book/page")
class TestClass:
    """
    85折85折查询库存月结台账
    /mgmt/dis-inventory/bill/book/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询默认条件检查")
    def test_01_mgmt_dis_inventory_bill_book_page(self):
            
        params = deepcopy(self.params) 
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["minMonth"] == int(time.strftime("%Y%m", time.localtime(time.time())))
                    assert d["maxMonth"] == int(time.strftime("%Y%m", time.localtime(time.time())))
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_bill_book_page(self, companyCode):
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"              
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["companyCode"] == companyCode
                    assert d["minMonth"] == 202203
                    assert d["maxMonth"] == 202203
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询服务中心编号检查")
    def test_03_mgmt_dis_inventory_bill_book_page(self):
            
        params = deepcopy(self.params) 
        params["storeCode"] = store_85 
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"               
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert d["storeCode"] == store_85
                assert d["minMonth"] == 202203
                assert d["maxMonth"] == 202203

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询产品类型检查")
    def test_04_mgmt_dis_inventory_bill_book_page(self):
        
        id = [] # 产品类型id
        
        @allure.step("获取产品类型")    
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal id
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["childList"]:
                    id.append(d["id"])
        
        @allure.step("查询产品类型")    
        def step_mgmt_dis_inventory_bill_book_page():
                        
            params = deepcopy(self.params) 
            params["beginMonth"] = "202203"
            params["endMonth"] = "202203" 
            for i in id:
                params["catalogId"] = i  # [10, 5, 6, 7, 8, 9, 2, 3, 4, 12, 11, 13, 14], ids=["小型厨具", "健康食品", "服务中心物料", "服务中心赠品", "辅销资料", "积分换购", "保洁用品及个人护理品", "化妆品（玛丽艳美容护肤品）", "保健器材", "赠送资料", "辅销品"])        
                with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        assert d["minMonth"] == 202203
                        assert d["maxMonth"] == 202203
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_dis_inventory_bill_book_page()

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 支持模糊查询产品编码检查")
    @pytest.mark.parametrize("product", [productCode, productCode[:-1]], ids=["精确产品编码", "产品编码的一部分"])
    def test_05_mgmt_dis_inventory_bill_book_page(self, product):
            
        params = deepcopy(self.params) 
        params["product"] = product
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"              
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert product in d["productCode"]
                assert d["minMonth"] == 202203
                assert d["maxMonth"] == 202203

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 支持模糊查询产品名称检查")
    @pytest.mark.parametrize("product", [productCode_title, productCode_title[:-1]], ids=["精确产品名称", "产品名称的一部分"])
    def test_06_mgmt_dis_inventory_bill_book_page(self, product):
            
        params = deepcopy(self.params) 
        params["product"] = product
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"             
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert productCode in d["productCode"]
                assert d["minMonth"] == 202203
                assert d["maxMonth"] == 202203


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/bill/book/page")
class TestClass02:
    """
    85折查询库存月结台账-各字段逻辑关系检查
    /mgmt/inventory/bill/book/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询默认条件时各字段逻辑关系检查")
    def test_01_mgmt_dis_inventory_bill_book_page(self):
            
        params = deepcopy(self.params) 
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["priorBalance"] + d["stockIn"] - d["stockOut"] == d["stock"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询分公司编号时各字段逻辑关系检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_bill_book_page(self, companyCode):
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"              
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["companyCode"] == companyCode
                    assert d["minMonth"] == 202203
                    assert d["maxMonth"] == 202203
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询服务中心编号时各字段逻辑关系检查")
    def test_03_mgmt_dis_inventory_bill_book_page(self):
            
        params = deepcopy(self.params) 
        params["store_85Code"] = store_85 
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"               
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["priorBalance"] + d["stockIn"] - d["stockOut"] == d["stock"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 查询产品类型时各字段逻辑关系检查")
    def test_04_mgmt_dis_inventory_bill_book_page(self):
        
        id = [] # 产品类型id
        
        @allure.step("获取产品类型")    
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal id
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["childList"]:
                    id.append(d["id"])
        
        @allure.step("查询产品类型")    
        def step_mgmt_dis_inventory_bill_book_page():
                        
            params = deepcopy(self.params) 
            params["beginMonth"] = "202203"
            params["endMonth"] = "202203" 
            for i in id:
                params["catalogId"] = i  # [10, 5, 6, 7, 8, 9, 2, 3, 4, 12, 11, 13, 14], ids=["小型厨具", "健康食品", "服务中心物料", "服务中心赠品", "辅销资料", "积分换购", "保洁用品及个人护理品", "化妆品（玛丽艳美容护肤品）", "保健器材", "赠送资料", "辅销品"])        
                with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
                    if r.json()["data"]["list"]:
                        for d in r.json()["data"]["list"]:
                            assert d["priorBalance"] + d["stockIn"] - d["stockOut"] == d["stock"]
                    else:
                        assert r.json()["data"]["list"] == []

        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_dis_inventory_bill_book_page()

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 支持模糊查询产品编码时各字段逻辑关系检查")
    @pytest.mark.parametrize("product", [productCode, productCode[:-1]], ids=["精确产品编码", "产品编码的一部分"])
    def test_05_mgmt_dis_inventory_bill_book_page(self, product):
            
        params = deepcopy(self.params) 
        params["product"] = product
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"              
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["priorBalance"] + d["stockIn"] - d["stockOut"] == d["stock"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折查询库存月结台账-成功路径: 支持模糊查询产品名称时各字段逻辑关系检查")
    @pytest.mark.parametrize("product", [productCode_title, productCode_title[:-1]], ids=["精确产品名称", "产品名称的一部分"])
    def test_06_mgmt_dis_inventory_bill_book_page(self, product):
            
        params = deepcopy(self.params) 
        params["product"] = product
        params["beginMonth"] = "202203"
        params["endMonth"] = "202203"             
        with _mgmt_dis_inventory_bill_book_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["priorBalance"] + d["stockIn"] - d["stockOut"] == d["stock"]
            else:
                assert r.json()["data"]["list"] == []


