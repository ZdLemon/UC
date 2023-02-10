# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_combine_forward import params ,_mgmt_dis_inventory_combine_forward
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/combine/forward")
class TestClass:
    """
    套装组合展示
    /mgmt/dis-inventory/combine/forward
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("套装组合展示-成功路径: 套装组合展示检查")
    def test_mgmt_dis_inventory_combine_forward(self):
        
        params = deepcopy(self.params)
        params["productCode"] = productCode_zh
        params["storeCode"] = store_85
        with _mgmt_dis_inventory_combine_forward(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

 