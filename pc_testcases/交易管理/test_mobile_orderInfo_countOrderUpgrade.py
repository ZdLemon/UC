# coding:utf-8

from api.mall_mobile_application._mobile_orderInfo_countOrderUpgrade import params, _mobile_orderInfo_countOrderUpgrade
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    统计用户待升级订单
    /mobile/orderInfo/countOrderUpgrade
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)

    @allure.story("/mobile/orderInfo/countOrderUpgrade")
    @allure.severity(P2)
    @allure.title("统计用户待升级订单-成功路径: 统计云商待升级订单检查")
    def test_mobile_orderInfo_countOrderUpgrade(self, login_oauth_token):

        params = deepcopy(self.params)
        params["customerId"] = login_oauth_token["data"]["userId"]
        with _mobile_orderInfo_countOrderUpgrade(params, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


