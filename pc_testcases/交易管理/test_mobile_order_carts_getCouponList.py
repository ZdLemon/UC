# coding:utf-8

from api.mall_mobile_application._mobile_order_carts_getCouponList import data, _mobile_order_carts_getCouponList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取选中结算分组的可用和不可用优惠券列表
    /mobile/order/carts/getCouponList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/order/carts/getCouponList")
    @allure.severity(P1)
    @allure.title("获取选中结算分组的可用和不可用优惠券列表-成功路径: 获取选中结算分组的可用和不可用优惠券列表检查")
    def test_mobile_order_carts_getCouponList(self):
        
        data = deepcopy(self.data)         
        with _mobile_order_carts_getCouponList(data, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
