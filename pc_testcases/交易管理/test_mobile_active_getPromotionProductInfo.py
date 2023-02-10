# coding:utf-8

from api.mall_mobile_application._mobile_active_getPromotionProductInfo import params, _mobile_active_getPromotionProductInfo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获活动商品详情以及已购买数量
    /mobile/active/getPromotionProductInfo
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)

    @allure.story("/mobile/active/getPromotionProductInfo")
    @allure.severity(P1)
    @allure.title("获活动商品详情以及已购买数量-成功路径: 获活动商品详情以及已购买数量检查")
    def test_mobile_active_getPromotionProductInfo(self):

        params = deepcopy(self.params)
        with _mobile_active_getPromotionProductInfo(params, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


