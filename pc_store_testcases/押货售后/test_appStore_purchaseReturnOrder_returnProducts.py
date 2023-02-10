# coding:utf-8

from api.mall_store_application._appStore_purchaseReturnOrder_list import params, _appStore_purchaseReturnOrder_list # 押货退货单列表
from api.basic_services._auth_getUserInfo import _auth_getUserInfo # 获取当前用户登录缓存信息
from api.mall_store_application._appStore_common_getReason import _appStore_common_getReason # 获取各种退换货原因
from api.mall_store_application._appStore_purchaseReturnOrder_returnProducts import _appStore_purchaseReturnOrder_returnProducts # 提交退货单页面的押货退货商品搜索

from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchaseReturnOrder/returnProducts")
class TestClass:
    """
    提交退货单页面的押货退货商品搜索
    /appStore/purchaseReturnOrder/returnProducts
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("提交退货单页面的押货退货商品搜索-成功路径: 搜索产品检查")
    def test_appStore_purchaseReturnOrder_returnProducts(self):
        
        purchaseReturnOrder = None # 押货退货单列表信息
        getUserInfo = None # 获取当前用户登录缓存信息
        getReason = None # 获取各种退换货原因
        returnProducts = None # 提交退货单页面的押货退货商品搜索
        
        @allure.step("押货退货单列表")
        def step_appStore_purchaseReturnOrder_list():
            
            nonlocal purchaseReturnOrder
            params = deepcopy(self.params)
            with _appStore_purchaseReturnOrder_list(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                purchaseReturnOrder = r.json()["data"]["list"]
        
        @allure.step("获取当前用户登录缓存信息")
        def step_auth_getUserInfo():
            
            nonlocal getUserInfo
            with _auth_getUserInfo(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getUserInfo = r.json()["data"] 

        @allure.title("获取各种退换货原因")
        def step_appStore_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 3, # 类型: 3退货 4换货
            }
            with _appStore_common_getReason(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.title("提交退货单页面的押货退货商品搜索")
        def step_appStore_purchaseReturnOrder_returnProducts():
            
            nonlocal returnProducts
            params = {
                "product": productCode, # 产品名称/产品编号
                "pageNum": 1,
                "pageSize": 20
            }
            with _appStore_purchaseReturnOrder_returnProducts(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["productCode"] == productCode:
                        returnProducts = d
               
        step_appStore_purchaseReturnOrder_list()
        step_auth_getUserInfo()
        step_appStore_common_getReason()
        step_appStore_purchaseReturnOrder_returnProducts()



