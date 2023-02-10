# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params, _appStore_store_dis_mortgageOrder_searchProductPage
from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data, _appStore_store_dis_mortgageOrder_pushProductsToCart
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgageOrder/pushProductsToCart")
class TestClass:
    """
    推送购物车数据
    /appStore/store/dis/mortgageOrder/pushProductsToCart
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.data = deepcopy(data)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P1)
    @allure.title("推送购物车数据-成功路径:押货时推送购物车数据检查")
    def test_appStore_store_dis_mortgageOrder_pushProductsToCart(self):
        
        searchProductPage = None # 商品信息
        
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()

