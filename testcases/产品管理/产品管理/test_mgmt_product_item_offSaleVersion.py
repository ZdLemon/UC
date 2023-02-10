# coding:utf-8

from api.mall_mgmt_application._mgmt_product_item_listVersion import data, _mgmt_product_item_listVersion
from api.mall_mgmt_application._mgmt_product_item_offSaleVersion import params, _mgmt_product_item_offSaleVersion

from setting import P1, P2, P3, productCode_zh, productCode_zh_title

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/offSaleVersion")
class TestClass:
    """
    商品版本下架
    /mgmt/product/item/offSaleVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title(" 商品版本下架-成功路径:  商品版本下架检查")
    def test_mgmt_product_item_offSaleVersion(self):
        
        product = None # 商品信息
        
        @allure.step("商品版本列表, 获取商品Id, 确认商品是否已上架")
        def step_mgmt_product_item_listVersion():
            
            nonlocal product
            data = deepcopy(self.data)
            data["serialNo"] = productCode_zh                   
            with _mgmt_product_item_listVersion(data, self.access_token) as r:
                product = r.json()["data"]["list"][0]
        
        @allure.step("商品版本下架")
        def step_mgmt_product_item_offSaleVersion():
            
            nonlocal product
            params = deepcopy(self.params)
            params["productId"] = product["productId"]                   
            with _mgmt_product_item_offSaleVersion(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "下架成功"
        
        step_mgmt_product_item_listVersion()
        if product["versionStatus"] == 7: # # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
            step_mgmt_product_item_offSaleVersion()
        
        


