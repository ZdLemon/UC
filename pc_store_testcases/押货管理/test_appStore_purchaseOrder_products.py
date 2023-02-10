# coding:utf-8

from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchaseOrder/products")
class TestClass:
    """
    提交押货单页面的押货商品搜索
    /appStore/purchaseOrder/products
    """
    def setup_class(self):
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("提交押货单页面的押货商品搜索-成功路径: 搜索普通产品检查")
    def test_appStore_purchaseOrder_products(self):
        
        negateProducts = None # 负库存产品
        availableAmount = None # 可用余额
        purchaseAmount = None # 当前押货价
        products = None # 产品信息
        

        @allure.step("提交押货单页面的负库存押货商品列表")
        def step_appStore_purchaseOrder_negateProducts():
            
            nonlocal negateProducts
            with _appStore_purchaseOrder_negateProducts(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                negateProducts = r.json()["data"]
        
        @allure.step("押货金额")
        def step_appStore_purchase_balanceAmount():
            
            nonlocal availableAmount, purchaseAmount
            with _appStore_purchase_balanceAmount(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]["availableAmount"]
                purchaseAmount = r.json()["data"]["purchaseAmount"]
        
        @allure.step("提交押货单页面的押货商品搜索")
        def step_appStore_purchaseOrder_products():
            
            nonlocal products
            params = {
                "pageNum": 1,
                "pageSize": 40,
                "product": productCode
            }
            with _appStore_purchaseOrder_products(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        products = d
        
        step_appStore_purchaseOrder_negateProducts()
        step_appStore_purchase_balanceAmount()
        step_appStore_purchaseOrder_products()




