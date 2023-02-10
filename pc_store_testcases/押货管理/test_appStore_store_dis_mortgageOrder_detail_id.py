# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params, _appStore_store_dis_mortgageOrder_searchProductPage
from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data, _appStore_store_dis_mortgageOrder_pushProductsToCart
from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data02, _appStore_store_dis_mortgageOrder_mortgage
from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params02, _appStore_store_dis_mortgageOrder_detail_id
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import uuid


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgageOrder/detail/id")
class TestClass:
    """
    押货单详情
    /appStore/store/dis/mortgageOrder/detail/{id}
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P1)
    @allure.title("押货单详情-成功路径:85折押货单详情检查")
    def test_appStore_store_dis_mortgageOrder_detail_id(self):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        
        
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
        
        @allure.step("押货下单")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data02)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                
        @allure.step("押货单详情")
        def step_appStore_store_dis_mortgageOrder_detail_id():
            
            params = deepcopy(self.params02)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_appStore_store_dis_mortgageOrder_detail_id()

