# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_listPage import params, _appStore_store_dis_mortgage_returnOrder_listPage
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgage/returnOrder/listPage")
class TestClass:
    """
    押货退货分页列表
    /appStore/store/dis/mortgage/returnOrder/listPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token_85 = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("押货退货分页列表-成功路径:默认搜索检查")
    def test_appStore_store_dis_mortgage_returnOrder_listPage(self):
        
        params = deepcopy(self.params)
        with _appStore_store_dis_mortgage_returnOrder_listPage(params, self.store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



