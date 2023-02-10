# coding:utf-8

from api.mall_mobile_application._mobile_product_search import data, _mobile_product_search
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    搜索商品
    /mobile/product/search
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.story("/mobile/product/search")
    @allure.severity(P2)
    @allure.title("搜索商品-成功路径: 搜索产品编号检查")
    def test_mobile_product_search(self):
        
        data = deepcopy(self.data)             
        with _mobile_product_search(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["data"]["list"][0]["serialNo"] == "M7035"

