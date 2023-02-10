# coding:utf-8

from api.mall_center_sys._mgmt_sys_lclFee_list import _mgmt_sys_lclFee_list

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/lclFee/list")
class TestClass:
    """
    获取拼箱费列表
    /mgmt/sys/lclFee/list
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("获取拼箱费列表-成功路径: 获取拼箱费列表检查")
    def test_mgmt_sys_lclFee_list(self):

        with _mgmt_sys_lclFee_list(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

