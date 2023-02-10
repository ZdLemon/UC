# coding:utf-8

from api.mall_mgmt_application._mgmt_product_cfg_menu import params, _mgmt_product_cfg_menu

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/cfg/menu")
class TestClass:
    """
    菜单列表
    /mgmt/product/cfg/menu/{type}
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询所有的运费模板-成功路径: 查询所有的运费模板检查")
    @pytest.mark.parametrize("type", ["show", "catalog", "company", "brand", "tag"])
    def test_mgmt_product_cfg_menu(self, type):
        
        params = self.params
        params["type"] = type
        with _mgmt_product_cfg_menu(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

