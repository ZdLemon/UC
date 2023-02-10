# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_combine_page import params, _mgmt_inventory_combine_page

from setting import P1, P2, P3, store

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/combine/page")
class TestClass:
    """
    分页查询套装组合列表
    /mgmt/inventory/combine/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 查询默认条件检查")
    def test_00_mgmt_inventory_combine_page(self):
            
        params = deepcopy(self.params)
        with _mgmt_inventory_combine_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_01_mgmt_inventory_combine_page(self, companyCode):
             
        params = deepcopy(self.params)                
        params["companyCode"] = companyCode           
        with _mgmt_inventory_combine_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []  
       
    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 查询组合时间检查")
    def test_02_mgmt_inventory_combine_page(self):
        
        combineTime = None
        
        @allure.step("获取组合时间") 
        def  step_01_mgmt_inventory_combine_page(): 
             
            nonlocal combineTime
            params = deepcopy(self.params) 
            params["combineState"] = 2 # 组合状态：1未组合、2已组合            
            with _mgmt_inventory_combine_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                combineTime = r.json()["data"]["list"][0]["combineTime"]
                
        @allure.step("查询组合时间") 
        def  step_02_mgmt_inventory_combine_page(): 
             
            params = deepcopy(self.params) 
            params["combineBegin"] = f"{combineTime[:4]}580800000"
            params["combineEnd"] = f"{combineTime[:4]}580800000"                           
            with _mgmt_inventory_combine_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["combineTime"][:4] == combineTime[:4]     
                
        step_01_mgmt_inventory_combine_page()
        step_02_mgmt_inventory_combine_page()                       
                     
    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 查询组合状态下拉选项检查")
    @pytest.mark.parametrize("combineState,ids", [(1, "未组合"), (2, "已组合")])
    def test_02_mgmt_inventory_combine_page(self, combineState, ids):
             
        params = deepcopy(self.params)                
        params["combineState"] = combineState  # 组合状态：1未组合、2已组合             
        with _mgmt_inventory_combine_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["state"] for d in r.json()["data"]["list"]):
                assert i == combineState  
                   
    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode,ids", [(store, "精确的服务中心编号"), (store[:-1], "模糊的服务中心编号")])
    def test_04_mgmt_inventory_combine_page(self, storeCode, ids):
            
        params = deepcopy(self.params)
        params["storeCode"] = storeCode                
        with _mgmt_inventory_combine_page(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []
                
    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 仅支持精确查询产品编号检查")
    def test_05_mgmt_inventory_combine_page(self):
        
        serialNo = None
        
        @allure.step("获取产品编号") 
        def  step_01_mgmt_inventory_combine_page(): 
             
            nonlocal serialNo
            params = deepcopy(self.params)               
            with _mgmt_inventory_combine_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                serialNo = r.json()["data"]["list"][0]["productCode"]
                
        @allure.step("支持精确查询产品编号") 
        def  step_02_mgmt_inventory_combine_page(): 
             
            params = deepcopy(self.params) 
            params["productCode"] = serialNo                            
            with _mgmt_inventory_combine_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["productCode"] for d in r.json()["data"]["list"]):
                    assert i == serialNo      
        
        @allure.step("不支持模糊查询产品编号") 
        def  step_03_mgmt_inventory_combine_page(): 
             
            params = deepcopy(self.params) 
            params["productCode"] = serialNo[:-1]                              
            with _mgmt_inventory_combine_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
                
        step_01_mgmt_inventory_combine_page()
        step_02_mgmt_inventory_combine_page()        
        step_03_mgmt_inventory_combine_page()                
                     


