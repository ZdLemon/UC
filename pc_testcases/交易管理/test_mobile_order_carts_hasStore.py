# coding:utf-8

from api.mall_mobile_application._mobile_order_carts_hasStore import _mobile_order_carts_hasStore
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    云商/微店是否已开通服务中心
    /mobile/order/carts/hasStore
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.story("/mobile/order/carts/hasStore")
    @allure.severity(P1)
    @allure.title("云商/微店是否已开通服务中心-成功路径: 云商是否已开通服务中心检查")
    def test_mobile_order_carts_hasStore(self):

        with _mobile_order_carts_hasStore(self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


