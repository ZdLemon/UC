# coding:utf-8

from api.mall_mgmt_application._mgmt_product_item_listVersion import data ,_mgmt_product_item_listVersion
from api.mall_mgmt_application._mgmt_product_item_getVersion import params ,_mgmt_product_item_getVersion

from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/getVersion")
class TestClass:
    """
    查询商品:详情
    /mgmt/product/item/getVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询商品-成功路径: 查询组合产品检查")
    def test_mgmt_product_item_getVersion(self):
        
        verid = None
        
        @allure.step("商品版本列表,获取verid")
        def step_mgmt_product_item_listVersion():
            
            nonlocal verid
            data = deepcopy(self.data)
            data["serialNo"] = productCode_zh                  
            with _mgmt_product_item_listVersion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                verid = r.json()["data"]["list"][0]["id"]
        
        @allure.step("查询商品")
        def step_mgmt_product_item_getVersion():
            
            params = deepcopy(self.params)
            params["verId"] = verid                  
            with _mgmt_product_item_getVersion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["bundleProductInfos"][0]["serialNo"] == productCode

