# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgageOrder_searchCartProducts import _appStore_store_dis_mortgageOrder_searchCartProducts
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgageOrder/searchCartProducts")
class TestClass:
    """
    获取购物车数据
    /appStore/store/dis/mortgageOrder/searchCartProducts
    """
    def setup_class(self):
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取购物车数据-成功路径:押货时获取购物车数据检查")
    def test_appStore_store_dis_mortgageOrder_searchCartProducts(self):
        
        with _appStore_store_dis_mortgageOrder_searchCartProducts(self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



