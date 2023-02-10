# coding:utf-8

from api.mall_store_application._appStore_deliveryServiceCharge_list import params, _appStore_deliveryServiceCharge_list
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/deliveryServiceCharge/list")
class TestClass:
    """
    配送服务费列表
    /appStore/deliveryServiceCharge/list
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("配送服务费列表-成功路径:配送服务费列表检查")
    def test_appStore_deliveryServiceCharge_list(self):
        
        params = deepcopy(self.params)
        with _appStore_deliveryServiceCharge_list(params, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



