# coding:utf-8

from api.mall_mgmt_application._mgmt_product_bundle_getSaleOffBundleList import data, _mgmt_product_bundle_getSaleOffBundleList # 查询拆分套装列表
from api.mall_mgmt_application._mgmt_product_bundle_splitBundlePreview import _mgmt_product_bundle_splitBundlePreview # 拆分单个套装确认页
from api.mall_mgmt_application._mgmt_product_bundle_splitPreview import _mgmt_product_bundle_splitPreview # 批量/单独拆分前明细预览
from api.mall_mgmt_application._mgmt_product_bundle_splitBundle import _mgmt_product_bundle_splitBundle # 拆分单个套装
from api.mall_mgmt_application._mgmt_product_bundle_splitDetailCount import _mgmt_product_bundle_splitDetailCount # 拆分明细数量统计--拆分后
from api.mall_mgmt_application._mgmt_product_bundle_splitDetail import _mgmt_product_bundle_splitDetail # 拆分明细

from setting import P1, P2, P3, productCode_zh

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/bundle/splitBundle")
class TestClass:
    """
    拆分单个套装
    /mgmt/product/bundle/splitBundle
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("拆分单个套装-成功路径: 套装拆分检查")
    def test_mgmt_product_bundle_splitBundle(self, auditMortgageOrder_zh, offSaleVersion):
            
        getSaleOffBundleList = None # 查询拆分套装列表
        splitBundlePreview = None # 拆分单个套装确认页
        splitDetail = [] # 拆分明细
        
        @allure.step("获取套装拆分Id") 
        def  step_mgmt_product_bundle_getSaleOffBundleList(): 
             
            nonlocal getSaleOffBundleList
            data = deepcopy(self.data)
            data["serialNo"] = productCode_zh 
            data["splitStatus"] = 1  # 拆分状态，1-未拆分，2-已拆分             
            with _mgmt_product_bundle_getSaleOffBundleList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getSaleOffBundleList = r.json()["data"]["list"][0]
                
        @allure.step("拆分单个套装确认页") 
        def  step_mgmt_product_bundle_splitBundlePreview(): 
            
            nonlocal splitBundlePreview
            data = {
                "productId" : getSaleOffBundleList["productId"],  # 套装id
            }                           
            with _mgmt_product_bundle_splitBundlePreview(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                splitBundlePreview = r.json()["data"]

        @allure.step("批量/单独拆分前明细预览") 
        def  step_mgmt_product_bundle_splitPreview(): 
            
            data = {
                "productIds" : getSaleOffBundleList["productId"],  # 套装id
            }                           
            with _mgmt_product_bundle_splitPreview(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("拆分单个套装") 
        def  step_mgmt_product_bundle_splitBundle(): 
            
            data = {
                "splitId" : getSaleOffBundleList["id"],  #拆分id
            }                           
            with _mgmt_product_bundle_splitBundle(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == {"successCount": splitBundlePreview["suitCount"], "failCount":0}

        @allure.step("拆分明细数量统计--拆分后") 
        def  step_mgmt_product_bundle_splitDetailCount(): 
            
            data = {
                "splitId" : getSaleOffBundleList["id"],  #拆分id
            }                           
            with _mgmt_product_bundle_splitDetailCount(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == {"storeCount": splitBundlePreview["storeCount"],"suitCount": splitBundlePreview["suitCount"]}

        @allure.step("拆分明细") 
        def  step_mgmt_product_bundle_splitDetail(): 
            
            nonlocal splitDetail
            data = {
                "splitId": getSaleOffBundleList["id"], # 拆分id
                "pageNum": 1,
                "pageSize": 100000
            }                          
            with _mgmt_product_bundle_splitDetail(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                splitDetail = r.json()["data"]["list"]

        step_mgmt_product_bundle_getSaleOffBundleList()
        step_mgmt_product_bundle_splitBundlePreview()
        step_mgmt_product_bundle_splitPreview()
        step_mgmt_product_bundle_splitBundle()
        step_mgmt_product_bundle_splitDetailCount()
        step_mgmt_product_bundle_splitDetail()





