# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgage_common_fetchProductShowList import _appStore_store_dis_mortgage_common_fetchProductShowList
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story(" /appStore/store/dis/mortgage/common/fetchProductShowList")
class TestClass:
    """
    获取商品前端分类列表
    /appStore/store/dis/mortgage/common/fetchProductShowList
    """
    def setup_class(self):
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取商品前端分类列表-成功路径:押货时获取商品前端分类列表检查")
    def test_appStore_store_dis_mortgage_common_fetchProductShowList(self):
        
        with _appStore_store_dis_mortgage_common_fetchProductShowList(self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



