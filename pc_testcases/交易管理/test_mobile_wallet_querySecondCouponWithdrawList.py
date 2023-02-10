# coding:utf-8

from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawList import _mobile_wallet_querySecondCouponWithdrawList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/wallet/querySecondCouponWithdrawList")
class TestClass:
    """
    秒返券提现列表
    /mobile/wallet/querySecondCouponWithdrawList
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.severity(P1)
    @allure.title("秒返券提现列表-成功路径: 秒返券提现列表检查")
    def test_mobile_wallet_querySecondCouponWithdrawList(self):
            
        with _mobile_wallet_querySecondCouponWithdrawList(access_token=self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
