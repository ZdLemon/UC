# coding:utf-8

from api.mall_center_sys._mgmt_sys_getComByCodeOrPri import params, _mgmt_sys_getComByCodeOrPri
from api.mall_center_sys._mgmt_sys_getComInfo import params as params02, _mgmt_sys_getComInfo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getComInfo")
class TestClass:
    """
    显示company的详情
    /mgmt/sys/getComInfo
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("显示company的详情-成功路径: 公司账号信息是否重复检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(1, 37) if i != 35])
    def test_mgmt_sys_getComInfo(self, companyCode):
        
        id = None
        
        @allure.step("公司资料查询展示: 获取分公司Id")
        def step_mgmt_sys_getComByCodeOrPri():
            
            nonlocal id
            params = deepcopy(self.params)
            params["companyCode"] = companyCode                     
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("显示company的详情:检查账号是否重复")
        def step_mgmt_sys_getComInfo():
            
            params = deepcopy(self.params02)
            params["id"] = id                     
            with _mgmt_sys_getComInfo(params, self.access_token) as r:
                assert len(r.json()["data"]["comAccounts"]) == len(set(d["account"] for d in r.json()["data"]["comAccounts"]))
        
        step_mgmt_sys_getComByCodeOrPri()
        step_mgmt_sys_getComInfo()
                    
                    
            






