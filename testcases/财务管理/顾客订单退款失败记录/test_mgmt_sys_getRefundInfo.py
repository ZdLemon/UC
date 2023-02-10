# coding:utf-8

from api.mall_center_sys._mgmt_sys_getRefundInfo import _mgmt_sys_getRefundInfo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getRefundInfo")
class TestClass:
    """
    查询有效退款阈值
    /mgmt/sys/getRefundInfo
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("查询有效退款阈值-成功路径: 查询有效退款阈值检查")
    def test_01_mgmt_sys_getRefundInfo(self):
                                 
        with _mgmt_sys_getRefundInfo(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"












