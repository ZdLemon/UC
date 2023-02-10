# coding:utf-8

from api.mall_mobile_application._mobile_wallet_rechargeMethod import params, _mobile_wallet_rechargeMethod
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取充值方式列表
    /mobile/wallet/rechargeMethod
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)

    @allure.story("/mobile/wallet/rechargeMethod")
    @allure.severity(P1)
    @allure.title("获取充值方式列表-成功路径: 获取充值方式列表检查")
    def test_mobile_wallet_rechargeMethod(self):

        params = deepcopy(self.params)
        with _mobile_wallet_rechargeMethod(params, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


