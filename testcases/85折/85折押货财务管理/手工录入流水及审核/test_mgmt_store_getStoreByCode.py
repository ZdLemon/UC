# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getStoreByCode import params, _mgmt_store_getStoreByCode
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time


time_now = time.strftime('%Y%m',time.localtime(time.time()))

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/getStoreByCode")
class TestClass:
    """
    根据服务中心编号获取服务中心
    /mgmt/store/getStoreByCode
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("根据服务中心编号获取服务中心-成功路径: 手工录入流水时获取服务中心信息检查")
    def test_mgmt_store_getStoreByCode(self):
        
        params = deepcopy(self.params)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



