# coding:utf-8

from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo
from setting import P1, P2, P3, username

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    个人用户信息接口
    /mobile/personalInfo/getCurrentUserInfo
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.story("/mobile/personalInfo/getCurrentUserInfo")
    @allure.severity(P2)
    @allure.title("个人用户信息接口-成功路径: 获取开单人信息检查")
    def test_mobile_personalInfo_getCurrentUserInfo(self):

        with _mobile_personalInfo_getCurrentUserInfo(self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["cardNo"] == username
                


