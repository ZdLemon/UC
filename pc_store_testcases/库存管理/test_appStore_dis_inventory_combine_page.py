# coding:utf-8

from api.mall_store_application._appStore_dis_inventory_combine_page import _appStore_dis_inventory_combine_page
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/dis-inventory/combine/page")
class TestClass:
    """
    套装组合列表85
    /appStore/dis-inventory/combine/page
    """
    def setup_class(self):
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("套装组合列表-成功路径:套装组合列表检查")
    def test_appStore_dis_inventory_combine_page(self):
        
        with _appStore_dis_inventory_combine_page(access_token=self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



