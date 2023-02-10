# coding:utf-8

from api.mall_mobile_application._mobile_home_getLogoConfig import _mobile_home_getLogoConfig
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取logo配置
    /mobile/home/getLogoConfig
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.story("/mobile/home/getLogoConfig")
    @allure.severity(P1)
    @allure.title("获取logo配置-成功路径: 获取logo配置检查")
    def test_mobile_home_getLogoConfig(self):
                  
        with _mobile_home_getLogoConfig(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

