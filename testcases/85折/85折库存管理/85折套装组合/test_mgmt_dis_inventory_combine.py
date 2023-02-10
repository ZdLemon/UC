# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_combine import data, _mgmt_dis_inventory_combine
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/combine")
class TestClass:
    """
    套装组合
    /mgmt/dis-inventory/combine
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("套装组合-成功路径: 85折套装组合检查")
    def test_mgmt_dis_inventory_combine(self, onSaleVersion):
        
        data = deepcopy(self.data)
        data["productCode"] = productCode_zh
        data["storeCode"] = store_85
        data["combineNum"] = 2
        with _mgmt_dis_inventory_combine(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["combineNum"] == 2

 