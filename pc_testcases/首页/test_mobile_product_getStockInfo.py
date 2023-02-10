# coding:utf-8

from api.mall_mobile_application._mobile_product_getStockInfo import params, _mobile_product_getStockInfo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    查询商品库存
    /mobile/product/getStockInfo
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.token = os.environ["token"]

    @allure.story("/mobile/product/getStockInfo")
    @allure.severity(P1)
    @allure.title("查询商品库存-成功路径: 查询商品库存检查")
    def test_mobile_product_getStockInfo(self):
        
        params = deepcopy(self.params)            
        with _mobile_product_getStockInfo(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["data"]["serialNo"] == "M7035"

