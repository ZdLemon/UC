# coding:utf-8

from api.mall_store_application._appStore_dis_inventory_combine_confirm import data, _appStore_dis_inventory_combine_confirm
from api.mall_store_application._appStore_dis_inventory_combine_record_page import params, _appStore_dis_inventory_combine_record_page
from api.mall_store_application._appStore_dis_inventory_combine_detail import params as params02, _appStore_dis_inventory_combine_detail

from setting import P1, P2, P3, username_85, store_85, name_85, productCode, productCode_zh

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/dis-inventory/combine/confirm")
class TestClass:
    """
    确认套装组合
    /appStore/dis-inventory/combine/confirm
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P1)
    @allure.title("确认套装组合-成功路径:确认套装组合检查")
    def test_appStore_dis_inventory_combine_confirm(self):
        
        id = None
        combine_detail = None # 组合明细
        
        @allure.step("套装组合")
        def step_appStore_dis_inventory_combine_confirm():
            
            data = deepcopy(self.data)
            data["combineNum"] = 2
            data["productCode"] = productCode_zh
            with _appStore_dis_inventory_combine_confirm(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                
        @allure.step("套装组合记录列表:获取Id")
        def step_appStore_dis_inventory_combine_record_page():
            
            nonlocal id
            params = deepcopy(self.params)
            with _appStore_dis_inventory_combine_record_page(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("套装组合明细")
        def step_appStore_dis_inventory_combine_detail():
            
            nonlocal combine_detail
            params = deepcopy(self.params02)
            params["id"] = id
            with _appStore_dis_inventory_combine_detail(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                combine_detail = r.json()["data"]
        
        step_appStore_dis_inventory_combine_confirm()
        step_appStore_dis_inventory_combine_record_page()
        step_appStore_dis_inventory_combine_detail()


