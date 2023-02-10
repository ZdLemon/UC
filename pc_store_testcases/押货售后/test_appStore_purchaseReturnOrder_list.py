# coding:utf-8

from api.mall_store_application._appStore_purchaseReturnOrder_list import params, _appStore_purchaseReturnOrder_list # 押货退货单列表
from api.basic_services._auth_getUserInfo import _auth_getUserInfo # 获取当前用户登录缓存信息
from api.mall_store_application._appStore_common_getReason import _appStore_common_getReason # 获取各种退换货原因

from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchaseReturnOrder/list")
class TestClass:
    """
    押货退货单列表（分页）
    /appStore/purchaseReturnOrder/list
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("押货退货单列表（分页）-成功路径: 押货退货单列表检查")
    def test_appStore_purchaseReturnOrder_list(self):
        
        purchaseReturnOrder = None # 押货退货单列表信息
        getUserInfo = None # 获取当前用户登录缓存信息
        getReason = None # 获取各种退换货原因
        
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
                
        step_appStore_purchaseReturnOrder_list()
        step_auth_getUserInfo()
        step_appStore_common_getReason()



