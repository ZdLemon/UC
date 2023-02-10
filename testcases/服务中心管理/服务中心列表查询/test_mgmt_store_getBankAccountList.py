# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getBankAccountList import params, _mgmt_store_getBankAccountList
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/getBankAccountList")
class TestClass:
    """
    通过storeCode获取银行账户资料信息
    /mgmt/store/getBankAccountList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("通过storeCode获取银行账户资料信息-成功路径: 85折服务中心银行信息检查")
    def test_mgmt_store_getBankAccountList(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = store_85               
        with _mgmt_store_getBankAccountList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
        


