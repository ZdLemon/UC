# coding:utf-8

from api.mall_mobile_application._mobile_myShareAndFavorite_whetherAddFavPro import params, _mobile_myShareAndFavorite_whetherAddFavPro
from api.mall_mobile_application._mobile_product_getProductDetail import params as params01, _mobile_product_getProductDetail
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    判断该商品是否被此会员收藏
    /mobile/myShareAndFavorite/whetherAddFavPro
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)
        self.params01 = deepcopy(params01)
        self.productId = None

    @allure.story("/mobile/myShareAndFavorite/whetherAddFavPro")
    @allure.severity(P1)
    @allure.title("判断该商品是否被此会员收藏-成功路径: 判断该商品是否被此会员收藏检查")
    def test_mobile_myShareAndFavorite_whetherAddFavPro(self):

        @allure.step("商品详情: 获取商品Id")
        def step_mobile_product_getProductDetail():
            
            params = deepcopy(self.params01)
            with _mobile_product_getProductDetail(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.productId = r.json()["data"]["productId"]

        @allure.step("判断该商品是否被此会员收藏")
        def step_mobile_myShareAndFavorite_whetherAddFavPro():
            
            params = deepcopy(self.params)
            params["productId"] = self.productId
            with _mobile_myShareAndFavorite_whetherAddFavPro(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                    


