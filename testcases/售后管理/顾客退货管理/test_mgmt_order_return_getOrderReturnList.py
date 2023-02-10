# coding:utf-8

from api.mall_mgmt_application._mgmt_order_return_getOrderReturnList import params, _mgmt_order_return_getOrderReturnList

from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/getOrderReturnList")
class TestClass:
    """
    退货单列表
    /mgmt/order/return/getOrderReturnList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("退货单列表-成功路径: 查询退货单编号检查")
    def test_mgmt_order_return_getOrderReturnList(self):
            
        params = deepcopy(self.params)
        params["returnNo"] = "TSG03400022041900004201"               
        with _mgmt_order_return_getOrderReturnList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            

