# coding:utf-8

from api.mall_mobile_application._mobile_product_getProductDetail import params, _mobile_product_getProductDetail
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    商品详情
    /mobile/product/getProductDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.token = os.environ["token"]

    @allure.story("/mobile/product/getProductDetail")
    @allure.severity(P1)
    @allure.title("商品详情-成功路径: 商品详情检查")
    def test_mobile_product_getProductDetail(self):
        
        params = deepcopy(self.params)            
        with _mobile_product_getProductDetail(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["data"]["serialNo"] == "M7035"

