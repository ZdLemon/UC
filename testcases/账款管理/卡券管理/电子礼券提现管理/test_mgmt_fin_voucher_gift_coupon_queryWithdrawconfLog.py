# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog import _mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog
from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/gift/coupon/queryWithdrawconfLog")
class TestClass:
    """
    电子礼券提现配置修改记录查询
    /mgmt/fin/voucher/gift/coupon/queryWithdrawconfLog
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("电子礼券提现配置修改记录查询")
    def test_mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog(self):
        
        @allure.step("电子礼券提现配置修改记录查询")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog():
                  
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_fin_voucher_gift_coupon_queryWithdrawconfLog()
