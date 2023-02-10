# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_split_page import data, _mgmt_dis_inventory_split_page
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/split/page")
class TestClass:
    """
    查询套装拆分列表
    /mgmt/dis-inventory/split/page
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询套装拆分列表-成功路径: 默认查询检查")
    def test_01_mgmt_dis_inventory_split_page(self):
        
        data = deepcopy(self.data)
        with _mgmt_dis_inventory_split_page(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.severity(P2)
    @allure.title("查询套装拆分列表-成功路径: 支持模糊查询产品编码检查")
    @pytest.mark.parametrize("product,ids", [(productCode_zh, "产品编号"), (productCode_zh[:-1], "产品编号的一部分")])
    def test_02_mgmt_dis_inventory_split_page(self, product, ids):
        
        data = deepcopy(self.data)
        data["product"] = product
        with _mgmt_dis_inventory_split_page(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                assert product in d["productCode"]
                
    @allure.severity(P2)
    @allure.title("查询套装拆分列表-成功路径: 支持模糊查询产品名称检查")
    @pytest.mark.parametrize("product,ids", [(productCode_zh_title, "产品名称"), (productCode_zh_title[:-1], "产品名称的一部分")])
    def test_03_mgmt_dis_inventory_split_page(self, product, ids):
        
        data = deepcopy(self.data)
        data["product"] = product
        with _mgmt_dis_inventory_split_page(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                assert product in d["productName"]
