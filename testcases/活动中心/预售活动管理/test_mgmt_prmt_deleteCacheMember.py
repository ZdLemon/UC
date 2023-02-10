# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_deleteCacheMember import _mgmt_prmt_deleteCacheMember
from setting import P1, P2, P3, couponName, promotionName, promotionCode, productCode_ys

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/deleteCacheMember")
class TestClass:
    """
    删除缓存的活动用户
    /mgmt/prmt/deleteCacheMember
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P3)
    @allure.title("删除缓存的活动用户-成功路径: 新建预售活动时删除缓存的活动用户检查")
    def test_mgmt_prmt_deleteCacheMember(self):
        
        data = {
            "id": None
        }                  
        with _mgmt_prmt_deleteCacheMember(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200




            
