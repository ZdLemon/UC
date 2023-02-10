# coding:utf-8

from api.basic_services._login import _login
from setting import P1, P2, P3, store, store_85

import allure
import pytest


@allure.feature("basic_services")
@allure.story("/login")
@pytest.mark.skip()
class TestLogin:
    
    @allure.severity(P1)
    @allure.title("登录-成功路径: 登录店铺系统")
    def test_01_login(self):
        with _login(username=store, password="277833", channel="store") as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.severity(P1)
    @allure.title("登录-成功路径: 85折店铺登录登录店铺系统")
    def test_02_login(self):
        with _login(username=store_85, password="133266", channel="store") as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
