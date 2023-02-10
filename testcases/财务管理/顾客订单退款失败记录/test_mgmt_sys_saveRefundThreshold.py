# coding:utf-8

from api.mall_center_sys._mgmt_sys_saveRefundThreshold import params, _mgmt_sys_saveRefundThreshold
from api.mall_center_sys._mgmt_sys_getRefundInfo import _mgmt_sys_getRefundInfo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/saveRefundThreshold")
class TestClass:
    """
    设置自动退款阈值
    /mgmt/sys/saveRefundThreshold
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("设置自动退款阈值-成功路径: 设置自动退款阈值检查")
    def test_01_mgmt_sys_saveRefundThreshold(self, login_2):
        @allure.step("设置自动退款阈值")
        def step_mgmt_sys_saveRefundThreshold():
            
            params = deepcopy(self.params)
            params["days"] = 2
            with _mgmt_sys_saveRefundThreshold(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"
        
        @allure.step("查询有效退款阈值,确认设置成功")
        def step_mgmt_sys_getRefundInfo():
                                 
            with _mgmt_sys_getRefundInfo(self.access_token) as r:
                assert r.json()["data"]["refundDays"] == 2
                assert r.json()["data"]["editor"] == login_2["data"]["username"]
        
        step_mgmt_sys_saveRefundThreshold()
        step_mgmt_sys_getRefundInfo()