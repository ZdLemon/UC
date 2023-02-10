# coding:utf-8

from api.mall_store_application._appStore_inventory_combine_page import params, _appStore_inventory_combine_page # 套装组合列表
from api.mall_store_application._appStore_inventory_combine_preview import _appStore_inventory_combine_preview # 套装组合预览
from api.mall_store_application._appStore_inventory_combine_confirm import _appStore_inventory_combine_confirm # 确认套装组合
from api.mall_store_application._appStore_inventory_combine_history_page import _appStore_inventory_combine_history_page # 套装组合记录列表
from api.mall_store_application._appStore_inventory_combine_detail import _appStore_inventory_combine_detail # 套装组合明细

from setting import P1, P2, P3, productCode_zh, store

from copy import deepcopy
import os
import allure
import time


@allure.feature("mall_store_application")
@allure.story("/appStore/inventory/combine/confirm")
class TestClass:
    """
    确认套装组合
    /appStore/inventory/combine/confirm
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("确认套装组合-成功路径:确认套装组合检查")
    def test_appStore_inventory_combine_confirm(self, onSaleVersion, returnOrder_auditOrder_zh):
        
        combine_page = None # 套装组合
        combine_detail = None # 套装组合明细
        
        @allure.step("套装组合列表:获取套装组合")
        def test_appStore_inventory_combine_page():
            
            nonlocal combine_page
            params = deepcopy(self.params)
            with _appStore_inventory_combine_page(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                combine_page = r.json()["data"]["list"][0]
        
        @allure.step("套装组合预览")
        def test_appStore_inventory_combine_preview():
            
            params = {
                "id": combine_page["id"], # 套装组合id
                "combineNum": combine_page["maxCombine"], # 套装组合数量
                "productCode": combine_page["productCode"]
            }
            with _appStore_inventory_combine_preview(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("确认套装组合")
        def test_appStore_inventory_combine_confirm():
            
            data = {
                "combineId": combine_page["id"], # 套装组合id
                "combineNum": 1, #combine_page["maxCombine"], # 套装组合数量
                "productCode": combine_page["productCode"]
            }
            with _appStore_inventory_combine_confirm(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("套装组合记录列表")
        def test_appStore_inventory_combine_history_page():
            
            params = {
                "pageNum": 1,
                "pageSize": 20,
                "beginTime": "", # 开始时间
                "endTime": "" # 结束时间
            }
            with _appStore_inventory_combine_history_page(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("套装组合明细")
        def test_appStore_inventory_combine_detail():
            
            nonlocal combine_detail
            params = {
                "id": combine_page["id"], # 套装组合id
            }
            with _appStore_inventory_combine_detail(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                combine_detail = r.json()["data"]

        test_appStore_inventory_combine_page()
        test_appStore_inventory_combine_preview()
        test_appStore_inventory_combine_confirm()
        test_appStore_inventory_combine_history_page()
        test_appStore_inventory_combine_detail()




