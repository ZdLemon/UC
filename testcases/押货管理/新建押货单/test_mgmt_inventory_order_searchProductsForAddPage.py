# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表

from setting import P1, P2, P3, productCode_zh, productCode, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/searchProductsForAddPage")
class TestClass:
    """
    新增押货单页面:根据产品关键字搜索普通商品列表
    /mgmt/inventory/order/searchProductsForAddPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("根据产品关键字搜索普通商品列表-成功路径: 新建押货单时根据产品关键字搜索普通商品列表检查")
    def test_mgmt_inventory_order_searchProductsForAddPage(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
        
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"]
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal getAvailableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAvailableAmount = r.json()["data"]
        
        @allure.step("根据产品关键字搜索普通商品列表")
        def step_mgmt_inventory_order_searchProductsForAddPage():  
            
            nonlocal searchProductsForAddPage
            params = deepcopy(self.params)
            params["storeCode"] = store
            params["keyword"] = productCode
            with _mgmt_inventory_order_searchProductsForAddPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:   
                        searchProductsForAddPage = d
        
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_searchProductsForAddPage()
