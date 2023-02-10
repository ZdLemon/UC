# coding:utf-8

from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchaseOrder/negateProducts")
class TestClass:
    """
    提交押货单页面的负库存押货商品列表
    /appStore/purchaseOrder/negateProducts
    """
    def setup_class(self):
        self.store_token = os.environ["store_token"]
               
    @allure.severity(P2)
    @allure.title("提交押货单页面的负库存押货商品列表-成功路径: 没有负库存时检查")
    def test_appStore_purchaseOrder_negateProducts(self):
        
        with _appStore_purchaseOrder_negateProducts(self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



