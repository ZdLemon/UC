# coding:utf-8

from api.basic_services._login_oauth_token import _login_oauth_token
from setting import P1, P2, P3, username

import allure
import pytest


@allure.feature("basic_services")
@pytest.mark.skip()
class TestLogin:
    
    @allure.story("/login/oauth/token")
    @allure.severity(P1)
    @allure.title("登录-成功路径: 登录PC商城")
    def test_login_oauth_token(self):
        with _login_oauth_token(username, "888888") as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            assert r.json()["data"]["cardNo"] == username

