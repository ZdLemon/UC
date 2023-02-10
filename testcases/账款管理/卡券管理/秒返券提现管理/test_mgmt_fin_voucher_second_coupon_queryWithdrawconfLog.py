# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawconfLog import _mgmt_fin_voucher_second_coupon_queryWithdrawconfLog
from setting import P1, P2, P3, username, store, username_vip
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryWithdrawconfLog")
class TestClass:
    """
    秒返券提现配置修改记录查询
    /mgmt/fin/voucher/second/coupon/queryWithdrawconfLog
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("秒返券提现配置修改记录查询-成功路径: 修改记录查询检查")
    def test_mgmt_fin_voucher_second_coupon_queryWithdrawconfLog(self):
 
            with _mgmt_fin_voucher_second_coupon_queryWithdrawconfLog(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        

