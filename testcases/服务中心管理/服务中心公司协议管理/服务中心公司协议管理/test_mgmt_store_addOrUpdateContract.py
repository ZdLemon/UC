# coding:utf-8

from api.mall_mgmt_application._mgmt_store_addOrUpdateContract import data, _mgmt_store_addOrUpdateContract
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@pytest.mark.skip()
class TestClass:
    """
    添加合同/修改合同
    /mgmt/store/addOrUpdateContract
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.story("/mgmt/store/addOrUpdateContract")
    @allure.severity(P1)
    @allure.title("添加合同/修改合同-成功路径: 服务中心新建协议检查")
    def test_01_mgmt_store_addOrUpdateContract(self):
        
        data = deepcopy(self.data)   
        with _mgmt_store_addOrUpdateContract(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"











