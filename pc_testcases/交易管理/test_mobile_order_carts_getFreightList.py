# coding:utf-8

from api.mall_mobile_application._mobile_order_carts_getFreightList import data, _mobile_order_carts_getFreightList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取运费补贴券券列表
    /mobile/order/carts/getFreightList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/order/carts/getFreightList")
    @allure.severity(P1)
    @allure.title("获取运费补贴券券列表-成功路径: 获取运费补贴券券列表检查")
    def test_mobile_order_carts_getFreightList(self):
        
        data = deepcopy(self.data)         
        with _mobile_order_carts_getFreightList(data, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
