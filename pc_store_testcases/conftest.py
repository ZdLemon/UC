# coding:utf-8

import pytest
from api.basic_services._login import _login
from api.basic_services._login_oauth_token import _login_oauth_token
from setting import username_vip, username ,username_85, store, store_85
import os


@pytest.fixture(scope="package", autouse=True)
def login():
    "hewei01 登录完美运营后台"
    r = _login().json()
    os.environ["access_token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="package", autouse=True)
def login_oauth_token():
    "云商 12597198 登录商城"
    r = _login_oauth_token().json()
    os.environ["token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="package", autouse=True)
def login_oauth_token_02():
    "云商 14498218 登录商城"
    r = _login_oauth_token(username=username_85).json()
    os.environ["token_85"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="package", autouse=True)
def vip_login():
    "vip顾客 26712599 登录商城"
    r = _login_oauth_token(username=username_vip).json()
    os.environ["vip_token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def login_store():
    "云商 45722864 登录店铺系统902804"
    r = _login(username=store, password="206822", channel="store").json()
    os.environ["store_token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def login_store_85():
    "云商 14498218 登录店铺系统902208"
    r = _login(username=store_85, password="133266", channel="store").json()
    os.environ["store_token_85"] = r["data"]["access_token"]
    return r
