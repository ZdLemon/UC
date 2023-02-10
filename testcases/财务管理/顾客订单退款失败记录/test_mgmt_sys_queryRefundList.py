# coding:utf-8

from api.mall_center_sys._mgmt_sys_queryRefundList import _mgmt_sys_queryRefundList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getRefundInfo")
class TestClass:
    """
    查询退款阈值修改记录
    /mgmt/sys/queryRefundList
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("查询退款阈值修改记录-成功路径: 查询退款阈值修改记录检查")
    def test_01_mgmt_sys_queryRefundList(self):
                                 
        with _mgmt_sys_queryRefundList(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"












