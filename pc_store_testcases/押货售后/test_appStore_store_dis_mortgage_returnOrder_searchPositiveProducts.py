# coding:utf-8

from api.mall_store_application._appStore_common_getReason import params, _appStore_common_getReason
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_searchPositiveProducts import params as params02, _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgage/returnOrder/searchPositiveProducts")
class TestClass:
    """
    获取服务中心正库存的商品信息
    /appStore/store/dis/mortgage/returnOrder/searchPositiveProducts
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.store_token_85 = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取服务中心正库存的商品信息-成功路径:押货退货时正库存的商品信息检查")
    def test_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts(self):
        
        getReason = None # 获取各种退换货原因
        searchPositiveProducts = None # 正库存商品信息
        
        @allure.step("获取各种退换货原因")
        def step_appStore_common_getReason():
            
            nonlocal getReason
            params = deepcopy(self.params)
            with _appStore_common_getReason(params, self.store_token_85) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]
            
        @allure.step("获取服务中心正库存的商品信息")
        def step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts():
            
            nonlocal searchPositiveProducts
            params = deepcopy(self.params02)
            with _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts(params, self.store_token_85) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["productCode"] == productCode:
                        searchPositiveProducts = d["productCode"]
        
        step_appStore_common_getReason()
        step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts()
                    



