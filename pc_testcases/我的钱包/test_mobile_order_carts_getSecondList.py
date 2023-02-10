# coding:utf-8

from api.mall_mobile_application._mobile_wallet_recharge import data, _mobile_wallet_recharge
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    个人钱包充值
    /mobile/wallet/recharge
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/wallet/recharge")
    @allure.severity(P1)
    @allure.title("个人钱包充值-成功路径: 云商邮储银行充值检查")
    def test_mobile_wallet_recharge(self):
        
        data = deepcopy(self.data)         
        with _mobile_wallet_recharge(data, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2
