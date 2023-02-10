# coding:utf-8

from api.mall_store_application._appStore_purchaseOrder_getNegateCusProductsForWebAddPage import _appStore_purchaseOrder_getNegateCusProductsForWebAddPage # 提交定制押货单页面的负库存押货商品列表
from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
from api.mall_store_application._appStore_purchaseOrder_getCusProductsForWebAddPage import _appStore_purchaseOrder_getCusProductsForWebAddPage # 提交定制品押货单页面的押货商品搜索列表
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchaseOrder/getCusProductsForWebAddPage")
class TestClass:
    """
    提交定制品押货单页面的押货商品搜索列表
    /appStore/purchaseOrder/getCusProductsForWebAddPage
    """
    def setup_class(self):
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("提交定制品押货单页面的押货商品搜索列表-成功路径: 搜索定制产品检查")
    def test_appStore_purchaseOrder_getCusProductsForWebAddPage(self):
        
        getNegateCusProductsForWebAddPage = None # 负库存产品
        availableAmount = None # 可用余额
        getCusProductsForWebAddPage = None # 产品信息
        
        @allure.step("提交定制押货单页面的负库存押货商品列表")
        def step_appStore_purchaseOrder_getNegateCusProductsForWebAddPage():
            
            nonlocal getNegateCusProductsForWebAddPage
            with _appStore_purchaseOrder_getNegateCusProductsForWebAddPage(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getNegateCusProductsForWebAddPage = r.json()["data"]
        
        @allure.step("押货金额")
        def step_appStore_purchase_balanceAmount():
            
            nonlocal availableAmount
            with _appStore_purchase_balanceAmount(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]["availableAmount"]
        
        @allure.step("提交定制品押货单页面的押货商品搜索列表")
        def step_appStore_purchaseOrder_getCusProductsForWebAddPage():
            
            nonlocal getCusProductsForWebAddPage
            params = {
                "keyword": "" # 一或二级商品关键字
            }
            with _appStore_purchaseOrder_getCusProductsForWebAddPage(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getCusProductsForWebAddPage = r.json()["data"][0]
        
        step_appStore_purchaseOrder_getNegateCusProductsForWebAddPage()
        step_appStore_purchase_balanceAmount()
        step_appStore_purchaseOrder_getCusProductsForWebAddPage()




