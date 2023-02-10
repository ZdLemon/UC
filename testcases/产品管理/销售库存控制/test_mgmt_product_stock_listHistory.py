# coding:utf-8

from api.mall_mgmt_application._mgmt_product_stock_list import data, _mgmt_product_stock_list
from api.mall_mgmt_application._mgmt_product_stock_listHistory import data as data02, _mgmt_product_stock_listHistory
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/listHistory")
class TestClass:
    """
    库存历史
    /mgmt/product/stock/listHistory
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("库存历史-成功路径: 完美运营后台押货数据检查")
    def test_01_mgmt_product_stock_listHistory(self):

        stockId = None
        
        @allure.step("库存列表-获取id")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stockId
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                stockId = r.json()["data"]["list"][0]["stockId"]
        
        @allure.step("库存历史")
        def step_mgmt_product_stock_listHistory():
            
            data = deepcopy(self.data02)
            data["stockId"] = stockId
            with _mgmt_product_stock_listHistory(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
    
