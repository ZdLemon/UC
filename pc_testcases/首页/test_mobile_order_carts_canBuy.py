# coding:utf-8

from api.mall_mobile_application._mobile_order_carts_canBuy import data, _mobile_order_carts_canBuy
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    根据用户卡号查询购买信息
    /mobile/order/carts/canBuy
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/order/carts/canBuy")
    @allure.severity(P1)
    @allure.title("根据用户卡号查询购买信息-成功路径: 根据用户卡号查询购买信息检查")
    def test_mobile_order_carts_canBuy(self):
        
        data = deepcopy(self.data)             
        with _mobile_order_carts_canBuy(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["data"]["cardNo"] == data["cardNo"]

