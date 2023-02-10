# coding:utf-8

from api.mall_mobile_application._mobile_order_before_thrivingHistoryList import data, _mobile_order_before_thrivingHistoryList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    查询代客下单搜索历史记录
    /mobile/order/before/thrivingHistoryList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/order/before/thrivingHistoryList")
    @allure.severity(P2)
    @allure.title("查询代客下单搜索历史记录-成功路径: 查询代客下单搜索历史记录检查")
    def test_mobile_order_before_thrivingHistoryList(self):
        
        data = deepcopy(self.data)             
        with _mobile_order_before_thrivingHistoryList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["message"] == "操作成功"

