# coding:utf-8

from api.mall_mobile_application._mobile_wallet_applyWalletWithdraw import data, _mobile_wallet_applyWalletWithdraw
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    申请钱包提现
    /mobile/wallet/applyWalletWithdraw
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["vip_token"]

    @allure.story("/mobile/wallet/applyWalletWithdraw")
    @allure.severity(P1)
    @allure.title("申请钱包提现-成功路径: 优惠顾客提现检查")
    def test_mobile_wallet_applyWalletWithdraw(self):
        
        data = deepcopy(self.data)         
        with _mobile_wallet_applyWalletWithdraw(data, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "提现申请成功"
