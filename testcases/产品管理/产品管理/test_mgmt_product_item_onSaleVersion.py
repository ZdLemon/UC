# coding:utf-8

from api.mall_mgmt_application._mgmt_product_item_listVersion import data ,_mgmt_product_item_listVersion
from api.mall_mgmt_application._mgmt_product_item_onSaleVersion import _mgmt_product_item_onSaleVersion

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/onSaleVersion")
@pytest.mark.skip()
class TestClass:
    """
    商品版本上架
    /mgmt/product/item/onSaleVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("商品版本上架-成功路径: 组合产品上架检查")
    def test_mgmt_product_item_onSaleVersion(self):

        productId = None # 商品Id
        
        @allure.step("商品版本列表: 获取商品Id")
        def step_mgmt_product_item_listVersion():
            
            nonlocal productId
            data = deepcopy(self.data)
            data["serialNo"] = productCode_zh
            with _mgmt_product_item_listVersion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productId = r.json()["data"]["list"][0]["productId"]
        
        @allure.step("商品版本上架")
        def step_mgmt_product_item_onSaleVersion():
            
            params = {"productId": productId}
            with _mgmt_product_item_onSaleVersion(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "上架成功"
        
        step_mgmt_product_item_listVersion()
        step_mgmt_product_item_onSaleVersion()


