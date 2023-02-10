# coding:utf-8

from api.mall_center_sys._mgmt_sys_getAllReNotice import _mgmt_sys_getAllReNotice
from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getAllReNotice")
class TestClass:
    """
    获取退货须知集合
    /mgmt/sys/getAllReNotice
    """
    def setup_class(self):
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("获取退货须知集合-成功路径: 85折订单退货时获取退货须知集合检查")
    def test_mgmt_sys_getAllReNotice(self):
              
        with _mgmt_sys_getAllReNotice(self.token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
