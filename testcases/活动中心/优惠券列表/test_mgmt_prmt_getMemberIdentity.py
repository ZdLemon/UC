# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity
from setting import P1, P2, P3, couponName, couponNumber

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/getMemberIdentity")
class TestClass:
    """
    获取所有顾客身份类型
    /mgmt/prmt/getMemberIdentity
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("获取所有顾客身份类型-成功路径: 派发优惠券时获取所有顾客身份类型检查")
    def test_mgmt_prmt_getMemberIdentity(self):
                           
        with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == [
                {
                    "code": 1,
                    "typeName": "会员"
                }, 
                {
                    "code": 2,
                    "typeName": "VIP会员"
                }, 
                {
                    "code": 3,
                    "typeName": "云商"
                }, 
                {
                    "code": 4,
                    "typeName": "微店"
                }
            ]
            
