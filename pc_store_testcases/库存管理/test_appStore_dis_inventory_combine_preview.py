# coding:utf-8

from api.mall_store_application._appStore_dis_inventory_combine_page import _appStore_dis_inventory_combine_page
from api.mall_store_application._appStore_dis_inventory_combine_preview import params, _appStore_dis_inventory_combine_preview
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/dis-inventory/combine/preview")
class TestClass:
    """
    套装组合预览
    /appStore/dis-inventory/combine/preview
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("套装组合列表-成功路径:套装组合列表检查")
    def test_appStore_dis_inventory_combine_preview(self):
        
        page = None # 组合产品列表
        
        @allure.step("套装组合列表")
        def step_appStore_dis_inventory_combine_page(self):
            
            nonlocal page
            with _appStore_dis_inventory_combine_page(access_token=self.store_token) as r:
                page = r.json()["data"]["list"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("套装组合预览")
        def step_appStore_dis_inventory_combine_preview(self):
            
            params = deepcopy(self.params)
            params["combineNum"] = page[0]["maxCombine"]
            params["productCode"] = page[0]["productCode"]
            with _appStore_dis_inventory_combine_preview(access_token=self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200



