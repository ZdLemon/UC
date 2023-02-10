# coding:utf-8

from api.mall_center_sys._mgmt_sys_getAccountList import params, _mgmt_sys_getAccountList
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time


time_now = time.strftime('%Y%m',time.localtime(time.time()))

@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getAccountList")
class TestClass:
    """
    查询分公司银行账号
    /mgmt/sys/getAccountList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("查询分公司银行账号-成功路径: 手工录入流水时查询分公司银行账号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_mgmt_sys_getAccountList(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                     
        with _mgmt_sys_getAccountList(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



