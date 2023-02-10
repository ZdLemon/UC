# coding:utf-8

from api.mall_mobile_application._mobile_personalInfo_getMemberAddressList import _mobile_personalInfo_getMemberAddressList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    获取当前登录用户的配送地址列表接口
    /mobile/personalInfo/getMemberAddressList
    """
    def setup_class(self):
        self.token = os.environ["token"]

    @allure.story("/mobile/personalInfo/getMemberAddressList")
    @allure.severity(P1)
    @allure.title("获取当前登录用户的配送地址列表接口-成功路径: 获取当前登录用户的配送地址列表接口检查")
    def test_mobile_personalInfo_getMemberAddressList(self):
                  
        with _mobile_personalInfo_getMemberAddressList(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

