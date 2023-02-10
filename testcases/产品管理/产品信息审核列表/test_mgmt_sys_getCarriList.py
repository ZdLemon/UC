# coding:utf-8

from api.mall_center_sys._mgmt_sys_getCarriList import _mgmt_sys_getCarriList

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getCarriList")
class TestClass:
    """
    查询所有的运费模板
    /mgmt/sys/getCarriList
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询所有的运费模板-成功路径: 查询所有的运费模板检查")
    def test_mgmt_sys_getCarriList(self):

        with _mgmt_sys_getCarriList(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

