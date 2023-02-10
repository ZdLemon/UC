# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_store_page import params, _mgmt_dis_inventory_store_page
from api.mall_mgmt_application._mgmt_dis_inventory_total import params as params02, _mgmt_dis_inventory_total
from api.mall_mgmt_application._mgmt_product_item_listVersion import data as data02, _mgmt_product_item_listVersion # 产品信息
from api.mall_mgmt_application._mgmt_dis_inventory_page import params as params03, _mgmt_dis_inventory_page # 库存列表

from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/store/page")
class TestClass:
    """
    分页查询库存列表-按服务中心维度：搜索检查
    /mgmt/dis-inventory/store/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("分页查询库存列表-按服务中心维度-成功路径: 查询默认条件检查")
    def test_01_mgmt_dis_inventory_store_page(self):
            
        params = deepcopy(self.params)                 
        with _mgmt_dis_inventory_store_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("分页查询库存列表-按服务中心维度-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_store_page(self, companyCode):
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode                
        with _mgmt_dis_inventory_store_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("分页查询库存列表-按服务中心维度-成功路径: 查询服务中心编号检查")
    def test_03_mgmt_dis_inventory_store_page(self):
            
        params = deepcopy(self.params) 
        params["storeCode"] = store_85                 
        with _mgmt_dis_inventory_store_page(params, self.access_token) as r:
            for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                assert i == store_85

    @allure.severity(P2)
    @allure.title("分页查询库存列表-按服务中心维度-成功路径: 查询店零售价合计检查")
    @pytest.mark.parametrize("operator,retailPrice,ids", [
        (0, 10000, "店零售价合计=10"), 
        (1, 10000, "店零售价合计>=10"), 
        (2, 10000, "店零售价合计>10"), 
        (3, 10000, "店零售价合计<=10"), 
        (4, 10000, "店零售价合计<10")
    ])
    def test_04_mgmt_dis_inventory_store_page(self, operator, retailPrice, ids):
            
        params = deepcopy(self.params)
        params["operator"] = operator
        params["retailPrice"] = retailPrice
        with _mgmt_dis_inventory_store_page(params, self.access_token) as r:
            # # 零售价运算符: 0为=，1为'>='，2为'>'，3为'<=',4为'<'
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if operator == 0:
                        assert d["totalRetail"] == 10000
                    elif operator ==1:
                        assert d["totalRetail"] >= 10000
                    elif operator == 2:
                        assert d["totalRetail"] > 10000
                    elif operator == 3:
                        assert d["totalRetail"] <= 10000
                    elif operator == 4:
                        assert d["totalRetail"] < 10000
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/store/page")
class TestClass02:
    """
    分页查询库存列表-按服务中心维度（按服务中心维度）:各字段信息和产品维度列表合计数相等检查
    /mgmt/dis-inventory/store/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("分页查询库存列表-按服务中心维度-成功路径: 各字段信息和产品维度列表合计数相等检查")
    def test_mgmt_dis_inventory_store_page(self):
        
        total = None # 服务中心库存合计信息
        inventory_page = None # 获取服务中心库存所有商品信息
        priorBalance = [] # 上期结存信息["M7035", 0, 480]
        mortgageNum_orderReturn = [] # 押货+交付退回数量["M7035", 0, 480]
        mortgageReturn_orderNum = [] # 押货退回+交付数量数量["M7035", 0, 480]

        @allure.step("分页查询库存列表，获取所有商品编码")
        def step_mgmt_dis_inventory_page():
            
            nonlocal inventory_page   
            params = deepcopy(self.params)  
            params["storeCode"] = store_85               
            with _mgmt_dis_inventory_page(params, self.access_token) as r:
                assert r.json()["data"]["total"] <= 100 # 商品≤100个
                inventory_page = r.json()["data"]["list"]
                            
        @allure.step("商品版本列表,获取各商品的零售价")
        def step_mgmt_product_item_listVersion():

            nonlocal priorBalance, mortgageNum_orderReturn, mortgageReturn_orderNum                                                                                                                           
            data = deepcopy(self.data02)
            for i in inventory_page:
                data["serialNo"] = i["productCode"]
                with _mgmt_product_item_listVersion(data, self.access_token) as r:
                    priorBalance.append([i["productCode"], i["priorBalance"], float(r.json()["data"]["list"][0]["retailPrice"])])
                    mortgageNum_orderReturn.append([i["productCode"], i["mortgageNum"] + i["orderReturn"], float(r.json()["data"]["list"][0]["retailPrice"])])
                    mortgageReturn_orderNum.append([i["productCode"], i["mortgageReturn"] + i["orderNum"], float(r.json()["data"]["list"][0]["retailPrice"])])
        
        @allure.step("库存合计")
        def step_mgmt_dis_inventory_total():  
            
            nonlocal total  
            params = deepcopy(self.params) 
            params["storeCode"] = store_85                
            with _mgmt_dis_inventory_total(params, self.access_token) as r:
                total = r.json()["data"]
        
        @allure.step("分页查询库存列表-按服务中心维度")
        def step_mgmt_dis_inventory_store_page():  
              
            params = deepcopy(self.params) 
            params["storeCode"] = store_85                 
            with _mgmt_dis_inventory_store_page(params, self.access_token) as r:
                # assert r.json()["data"]["list"][0]["priorRetail"] == sum([i[1] * i[2] for i in priorBalance]) # 上期库存结存零售金额
                # assert r.json()["data"]["list"][0]["increaseRetail"] == sum([i[1] * i[2] for i in mortgageNum_orderReturn]) # 本期增加库存零售金额
                # assert r.json()["data"]["list"][0]["decreaseRetail"] == sum([i[1] * i[2] for i in  mortgageReturn_orderNum]) # 本期减少库存零售金额
                assert r.json()["data"]["list"][0]["totalRetail"] == total["retailPrice"] # 本期结余库存零售金额
                assert r.json()["data"]["list"][0]["totalPv"] == total["pv"] # 当前结余库存PV合计
                assert r.json()["data"]["list"][0]["totalSecurity"] == total["securityPrice"]# 当前结余库存押货价合计
        
        step_mgmt_dis_inventory_page()
        step_mgmt_product_item_listVersion()
        step_mgmt_dis_inventory_total()
        step_mgmt_dis_inventory_store_page()

