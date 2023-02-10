# coding:utf-8

from api.mall_mobile_application._mobile_order_carts_getCartProductNum import _mobile_order_carts_getCartProductNum
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取购物车产品数量和选中结算产品数量
    /mobile/order/carts/getCartProductNum
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.story("/mobile/order/carts/getCartProductNum")
    @allure.severity(P2)
    @allure.title("获取购物车产品数量和选中结算产品数量-成功路径: 获取购物车产品数量和选中结算产品数量检查")
    def test_mobile_order_carts_getCartProductNum(self):

        with _mobile_order_carts_getCartProductNum(self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


