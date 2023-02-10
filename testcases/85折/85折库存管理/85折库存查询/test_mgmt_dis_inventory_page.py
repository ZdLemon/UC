# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_page import params ,_mgmt_dis_inventory_page
from api.mall_mgmt_application._mgmt_dis_inventory_detail import params as params02, _mgmt_dis_inventory_detail # 增减明细
from api.mall_mgmt_application._mgmt_dis_inventory_frozen_detail import params as params03, _mgmt_dis_inventory_frozen_detail # 冻结明细
from api.mall_mgmt_application._mgmt_product_item_listVersion import data as data02, _mgmt_product_item_listVersion # 产品信息

from setting import P1, P2, P3, productCode_zh, productCode, store_85
from util.logger import logger
from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import math


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/page")
class TestClass:
    """
    分页查询库存列表: 查询检查
    /mgmt/dis-inventory/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("分页查询库存列表-成功路径: 查询默认条件检查")
    def test_01_mgmt_dis_inventory_page(self):
            
        params = deepcopy(self.params)                 
        with _mgmt_dis_inventory_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("分页查询库存列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_page(self, companyCode):
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode                
        with _mgmt_dis_inventory_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("分页查询库存列表-成功路径: 查询服务中心编号检查")
    def test_03_mgmt_dis_inventory_page(self):
            
        params = deepcopy(self.params) 
        params["storeCode"] = store_85                 
        with _mgmt_dis_inventory_page(params, self.access_token) as r:
            for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                assert i == store_85

    @allure.severity(P2)
    @allure.title("分页查询库存列表-成功路径: 查询当前库存检查")
    @pytest.mark.parametrize("stockOperator,stock,ids", [
        (0, 10, "库存=10"), 
        (1, 10, "库存>=10"), 
        (2, 10, "库存>10"), 
        (3, 10, "库存<=10"), 
        (4, 10, "库存<10")
    ])
    def test_04_mgmt_dis_inventory_page(self, stockOperator, stock, ids):
            
        params = deepcopy(self.params)
        params["stockOperator"] = stockOperator
        params["stock"] = stock
        with _mgmt_dis_inventory_page(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if stockOperator == 0:
                        assert d["stock"] == 10
                    elif stockOperator ==1:
                        assert d["stock"] >= 10
                    elif stockOperator == 2:
                        assert d["stock"] > 10
                    elif stockOperator == 3:
                        assert d["stock"] <= 10
                    elif stockOperator == 4:
                        assert d["stock"] < 10
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/page")
class TestClass02:
    """
    分页查询库存列表: 列表各字段数据,增减明细详情,冻结明细合计数对比检查
    /mgmt/dis-inventory/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("分页查询库存列表-成功路径: 各字段和增减明细合计数相等检查")
    @pytest.mark.parametrize("bizType,ids", [(1, "押货数量"), (2, "押货退回"), (3, "交付数量"), (4, "交付退回"), (5, "库存调整")])
    def test_01_mgmt_dis_inventory_page(self, bizType, ids):
        
        inventory_page = None # M7035库存信息 
        
        @allure.step("分页查询库存列表:获取各字段信息")   
        def step_mgmt_dis_inventory_page():
            
            nonlocal inventory_page
            params = deepcopy(self.params) 
            params["storeCode"] = store_85
            params["product"] = productCode                
            with _mgmt_dis_inventory_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                inventory_page = r.json()["data"]["list"][0]
        
        @allure.step("查询库存明细")
        def step_mgmt_dis_inventory_detail():
            
            params = {
                "type": None, # 出入库：1入库 2出库
                "bizType": bizType, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                "beginMonth": "", #202204月份，格式为：yyyyMM
                "endMonth": "", # 202204月份，格式为：yyyyMM
                "storeCode": store_85, # 服务中心编号
                "productCode": productCode, # 产品编号
                "pageNum": 1,
                "pageSize": 10
            }
            with _mgmt_dis_inventory_detail(params, self.access_token) as r:
                if bizType == 1:
                    assert str(inventory_page["mortgageNum"]) == r.json()["data"]["count"]
                elif bizType == 2:
                    assert str(inventory_page["mortgageReturn"]) == r.json()["data"]["count"]
                elif bizType == 3:
                    BB = 0 # 补保单金额
                    if math.ceil(r.json()["data"]["page"]["total"] / r.json()["data"]["page"]["pageSize"]) > 1:
                        for i in range(math.ceil(r.json()["data"]["page"]["total"] / r.json()["data"]["page"]["pageSize"])):
                            params["storeCode"] = store_85
                            params["productCode"] = productCode
                            params["beginMonth"] = time.strftime("%Y%m",time.localtime(time.time()))
                            params["endMonth"] = time.strftime("%Y%m",time.localtime(time.time()))
                            params["bizType"] = bizType
                            params["pageSize"] = 100
                            params["pageNum"] = i + 1
                            with _mgmt_dis_inventory_detail(params, self.access_token) as r2:
                                for d in r2.json()["data"]["page"]["list"]:
                                    if d["bizNo"].startswith("BB"):                                       
                                        BB += int(d["diffNum"]) 
                                        logger(f"BB: {BB}")
                    else:
                        for d in r.json()["data"]["page"]["list"]:
                            if d["bizNo"].startswith("BB"):
                                BB += int(d["diffNum"]) 
                                               
                    assert inventory_page["orderNum"] == int(r.json()["data"]["count"]) + BB
                elif bizType == 4:
                    assert str(inventory_page["orderReturn"]) == r.json()["data"]["count"]
                elif bizType == 5:
                    assert str(inventory_page["adjustNum"]) == r.json()["data"]["count"]
   
        step_mgmt_dis_inventory_page()
        step_mgmt_dis_inventory_detail()

    @allure.severity(P1)
    @allure.title("分页查询库存列表-成功路径: 冻结库存和冻结明细合计数相等检查")
    def test_02_mgmt_dis_inventory_page(self):
        
        inventory_page = None # M7035产品库存信息
        
        @allure.step("分页查询库存列表")
        def step_mgmt_dis_inventory_page():
            
            nonlocal inventory_page
            params = deepcopy(self.params)  
            params["storeCode"] = store_85
            params["product"] = productCode          
            with _mgmt_dis_inventory_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                inventory_page = r.json()["data"]["list"][0]
        
        @allure.step("查询库存冻结明细")
        def step_mgmt_dis_inventory_frozen_detail():
            
            params = {
                "type": None, # 类型：1冻结 2解冻
                "beginMonth": None, #202204月份，格式为：yyyyMM
                "endMonth": None, # 202204月份，格式为：yyyyMM
                "storeCode": store_85, # 服务中心编号
                "productCode": productCode, # 产品编号
                "pageNum": 1,
                "pageSize": 10
            }       
            with _mgmt_dis_inventory_frozen_detail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert str(inventory_page["frozenStock"]) == r.json()["data"]["count"]
        
        step_mgmt_dis_inventory_page()
        step_mgmt_dis_inventory_frozen_detail()

    @allure.severity(P1)
    @allure.title("分页查询库存列表-成功路径: 各字段关系检查")
    def test_03_mgmt_dis_inventory_page(self):
        
        listVersion = None # 产品信息
        
        @allure.step("商品版本列表")
        def step_mgmt_product_item_listVersion():

            nonlocal listVersion
            data = deepcopy(self.data02)
            data["serialNo"] = productCode
            with _mgmt_product_item_listVersion(data, self.access_token) as r:
                listVersion = r.json()["data"]["list"][0]
                    
        @allure.step("分页查询库存列表")
        def step_mgmt_dis_inventory_page():
               
            params = deepcopy(self.params)  
            params["storeCode"] = store_85 
            params["product"] = productCode               
            with _mgmt_dis_inventory_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert sum([
                    r.json()["data"]["list"][0]["priorBalance"], 
                    r.json()["data"]["list"][0]["mortgageNum"],
                    r.json()["data"]["list"][0]["mortgageReturn"],
                    r.json()["data"]["list"][0]["orderNum"],
                    r.json()["data"]["list"][0]["orderReturn"],
                    r.json()["data"]["list"][0]["adjustNum"],
                    ]) == r.json()["data"]["list"][0]["stock"] # 当前库存
                assert r.json()["data"]["list"][0]["stock"] - r.json()["data"]["list"][0]["frozenStock"] == r.json()["data"]["list"][0]["availableStock"] # 可用库存
                assert r.json()["data"]["list"][0]["stock"] * float(listVersion["pv"]) == r.json()["data"]["list"][0]["pv"] # 当前PV合计
                assert r.json()["data"]["list"][0]["stock"] * float(listVersion["orderPrice"]) == r.json()["data"]["list"][0]["securityPrice"] # 当前押货价合计
                assert r.json()["data"]["list"][0]["stock"] * float(listVersion["retailPrice"]) == r.json()["data"]["list"][0]["retailPrice"] # 当前零售价合计
        
        step_mgmt_product_item_listVersion()
        step_mgmt_dis_inventory_page()
                
        



