# coding:utf-8

from api.mall_mobile_application._mobile_product_discount_productList import data, _mobile_product_discount_productList
from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/product-discount/productList")
class TestClass:
    """
    查询85折转分商品
    /mobile/product-discount/productList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("查询85折转分商品-成功路径: 查询85折转分商品检查")
    def test_mobile_product_discount_productList(self):
        
        data = deepcopy(self.data)         
        with _mobile_product_discount_productList(data, self.token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
