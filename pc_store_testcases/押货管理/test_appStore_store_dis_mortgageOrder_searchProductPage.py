# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params, _appStore_store_dis_mortgageOrder_searchProductPage
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgageOrder/searchProductPage")
class TestClass:
    """
    关键字搜索可押货商品分页
    /appStore/store/dis/mortgageOrder/searchProductPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("关键字搜索可押货商品分页-成功路径:押货时搜索商品检查")
    def test_appStore_store_dis_mortgageOrder_searchProductPage(self):
        
        params = deepcopy(self.params) 
        params["keyword"] = productCode
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



