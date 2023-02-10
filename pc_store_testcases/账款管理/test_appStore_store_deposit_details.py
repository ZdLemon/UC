# coding:utf-8

from api.mall_store_application._appStore_store_deposit_details import data, _appStore_store_deposit_details
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/deposit/details")
class TestClass:
    """
    获取服务中心押货保证金增减明细
    /appStore/store/deposit/details
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取服务中心押货保证金增减明细-成功路径: 默认查询当月检查")
    def test_appStore_store_deposit_details(self):
        
        data = deepcopy(self.data)                 
        with _appStore_store_deposit_details(data, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



