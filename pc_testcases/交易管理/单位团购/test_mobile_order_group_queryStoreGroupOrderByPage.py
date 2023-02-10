# coding:utf-8

from api.mall_mobile_application._mobile_order_group_queryStoreGroupOrderByPage import params, _mobile_order_group_queryStoreGroupOrderByPage
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/order/group/queryStoreGroupOrderByPage")
class TestClass:
    """
    分页查询单位团购单
    /mobile/order/group/queryStoreGroupOrderByPage
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)

    @allure.severity(P1)
    @allure.title("分页查询单位团购单-成功路径: 分页查询单位团购单检查")
    def test_mobile_order_group_queryStoreGroupOrderByPage(self):

        @allure.step("分页查询单位团购单")
        def step_mobile_order_group_queryStoreGroupOrderByPage():

            params = deepcopy(self.params)
            with _mobile_order_group_queryStoreGroupOrderByPage(params, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mobile_order_group_queryStoreGroupOrderByPage()
                    


