# coding:utf-8

from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取钱包首页相关信息
    /mobile/wallet/getDetail
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.story("/mobile/wallet/getDetail")
    @allure.severity(P1)
    @allure.title("获取钱包首页相关信息-成功路径: 获取钱包首页相关信息检查")
    def test_mobile_wallet_getDetail(self):
                  
        with _mobile_wallet_getDetail(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

