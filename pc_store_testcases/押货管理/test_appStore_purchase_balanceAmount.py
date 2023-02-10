# coding:utf-8

from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchase/balanceAmount")
class TestClass:
    """
    押货金额
    /appStore/purchase/balanceAmount
    """
    def setup_class(self):
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("押货金额-成功路径: 提交押货单时押货余额检查")
    def test_appStore_purchase_balanceAmount(self):
        
        negateProducts = None # 负库存产品
        availableAmount = None # 可用余额
        purchaseAmount = None # 当前押货价
        

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
        
        step_appStore_purchaseOrder_negateProducts()
        step_appStore_purchase_balanceAmount()




