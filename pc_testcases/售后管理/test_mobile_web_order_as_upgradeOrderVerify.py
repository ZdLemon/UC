# coding:utf-8

from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import data, _mobile_web_order_as_upgradeOrderVerify
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall-mobile-application")
@allure.story("/mobile/web/order/as/upgradeOrderVerify")
@pytest.mark.skip()
class TestClass:
    """
    升级单校验
    /mobile/web/order/as/upgradeOrderVerify
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.data = deepcopy(data)


    @allure.severity(P1)
    @allure.title("升级单校验-成功路径: 升级单校验检查")
    def test_mobile_web_order_as_upgradeOrderVerify(self):

        data = deepcopy(self.data)
        with _mobile_web_order_as_upgradeOrderVerify(data, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

                


