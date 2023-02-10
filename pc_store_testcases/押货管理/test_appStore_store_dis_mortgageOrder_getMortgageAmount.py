# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgageOrder_getMortgageAmount import _appStore_store_dis_mortgageOrder_getMortgageAmount
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgageOrder/getMortgageAmount")
class TestClass:
    """
    查询店铺押货余额与限额
    /appStore/store/dis/mortgageOrder/getMortgageAmount
    """
    def setup_class(self):
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("查询店铺押货余额与限额-成功路径:押货时查询店铺押货余额与限额检查")
    def test_appStore_store_dis_mortgageOrder_getMortgageAmount(self):
        
        with _appStore_store_dis_mortgageOrder_getMortgageAmount(self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



