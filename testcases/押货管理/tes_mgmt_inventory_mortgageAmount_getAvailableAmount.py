# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额

from setting import P1, P2, P3, productCode_zh, productCode, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/mortgageAmount/getAvailableAmount")
class TestClass:
    """
    根据storeCode查询押货余额
    /mgmt/inventory/mortgageAmount/getAvailableAmount
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("根据storeCode查询押货余额-成功路径: 新建押货单时根据storeCode查询押货余额检查")
    def test_mgmt_inventory_mortgageAmount_getAvailableAmount(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        
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
        
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
