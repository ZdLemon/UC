# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getSecondCouponExplain import _mgmt_fin_wallet_getSecondCouponExplain
from setting import P1, P2, P3, username, store

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/getSecondCouponExplain")
class TestClass:
    """
    获取秒返券说明
    /mgmt/fin/wallet/getSecondCouponExplain
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("获取秒返券说明-成功路径: 获取秒返券说明检查")
    def test_mgmt_fin_wallet_getSecondCouponExplain(self):
                        
        with _mgmt_fin_wallet_getSecondCouponExplain(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

