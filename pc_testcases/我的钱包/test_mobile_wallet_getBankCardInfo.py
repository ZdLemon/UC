# coding:utf-8

from api.mall_mobile_application._mobile_wallet_getBankCardInfo import _mobile_wallet_getBankCardInfo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取用户绑定的银行卡及详情信息
    /mobile/wallet/getBankCardInfo
    """
    def setup_class(self):
        self.token = os.environ["vip_token"]

    @allure.story("/mobile/wallet/rechargeMethod")
    @allure.severity(P1)
    @allure.title("获取用户绑定的银行卡及详情信息-成功路径: 优惠顾客提现时获取用户绑定的银行卡及详情信息检查")
    def test_mobile_wallet_getBankCardInfo(self):

        with _mobile_wallet_getBankCardInfo(self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


