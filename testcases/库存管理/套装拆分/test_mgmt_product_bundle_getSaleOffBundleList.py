# coding:utf-8

from api.mall_mgmt_application._mgmt_product_bundle_getSaleOffBundleList import data, _mgmt_product_bundle_getSaleOffBundleList

from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/bundle/getSaleOffBundleList")
class TestClass:
    """
    查询拆分套装列表
    /mgmt/product/bundle/getSaleOffBundleList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 查询默认条件检查")
    def test_01_mgmt_product_bundle_getSaleOffBundleList(self):
            
        data = deepcopy(self.data)
        with _mgmt_product_bundle_getSaleOffBundleList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 仅支持精确查询套装产品编号检查")
    def test_02_mgmt_product_bundle_getSaleOffBundleList(self):
        
        serialNo = None
        
        @allure.step("获取套装产品编号") 
        def  step_01_mgmt_product_bundle_getSaleOffBundleList(): 
             
            nonlocal serialNo
            data = deepcopy(self.data)               
            with _mgmt_product_bundle_getSaleOffBundleList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                serialNo = r.json()["data"]["list"][0]["serialNo"]
                
        @allure.step("支持精确查询套装产品编号") 
        def  step_02_mgmt_product_bundle_getSaleOffBundleList(): 
             
            data = deepcopy(self.data) 
            data["serialNo"] = serialNo                             
            with _mgmt_product_bundle_getSaleOffBundleList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["serialNo"] for d in r.json()["data"]["list"]):
                    assert i == serialNo      
        
        @allure.step("不支持模糊查询套装产品编号") 
        def  step_03_mgmt_product_bundle_getSaleOffBundleList(): 
             
            data = deepcopy(self.data) 
            data["serialNo"] = serialNo[:-1]                              
            with _mgmt_product_bundle_getSaleOffBundleList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
                
        step_01_mgmt_product_bundle_getSaleOffBundleList()
        step_02_mgmt_product_bundle_getSaleOffBundleList()        
        step_03_mgmt_product_bundle_getSaleOffBundleList()                

    @allure.severity(P2)
    @allure.title("查询拆分套装列表-成功路径: 查询拆分状态下拉选项检查")
    @pytest.mark.parametrize("splitStatus,ids", [(1, "未拆分"), (2, "已拆分")])
    def test_03_mgmt_product_bundle_getSaleOffBundleList(self, splitStatus, ids):
             
        data = deepcopy(self.data)                
        data["splitStatus"] = splitStatus  # 拆分状态，1-未拆分，2-已拆分              
        with _mgmt_product_bundle_getSaleOffBundleList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["splitStatus"] for d in r.json()["data"]["list"]):
                assert i == splitStatus  
            
              

