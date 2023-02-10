# coding:utf-8

from api.mall_mgmt_application._mgmt_product_cfg_getPrice import _mgmt_product_cfg_getPrice

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/cfg/getPrice")
class TestClass:
    """
    价格参数查询
    /mgmt/product/cfg/getPrice
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("价格参数查询-成功路径: 价格参数查询检查")
    def test_mgmt_product_cfg_getPrice(self):

        with _mgmt_product_cfg_getPrice(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

