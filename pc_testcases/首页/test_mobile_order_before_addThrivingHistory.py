# coding:utf-8

from api.mall_mobile_application._mobile_order_before_addThrivingHistory import data, _mobile_order_before_addThrivingHistory
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    新增代客下单搜索历史记录
    /mobile/order/before/addThrivingHistory
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/order/before/addThrivingHistory")
    @allure.severity(P2)
    @allure.title("新增代客下单搜索历史记录-成功路径: 新增代客下单搜索历史记录检查")
    def test_mobile_order_before_addThrivingHistory(self):
        
        data = deepcopy(self.data)            
        with _mobile_order_before_addThrivingHistory(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json() == {
                    "code":200,
                    "message":"操作成功",
                    "data":"新增成功"
                }

