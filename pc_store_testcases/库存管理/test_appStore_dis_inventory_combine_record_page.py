# coding:utf-8

from api.mall_store_application._appStore_dis_inventory_combine_record_page import params, _appStore_dis_inventory_combine_record_page
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/dis-inventory/combine/record/page")
class TestClass:
    """
    套装组合记录列表
    /appStore/dis-inventory/combine/record/page
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("套装组合记录列表-成功路径:默认查询检查")
    def test_appStore_dis_inventory_combine_record_page(self):
        
        params = deepcopy(self.params)
        with _appStore_dis_inventory_combine_record_page(params, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



