# coding:utf-8

from api.mall_center_sys._mgmt_sys_getComByCodeOrPri import params, _mgmt_sys_getComByCodeOrPri
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/getComByCodeOrPri")
class TestClass:
    """
    公司资料查询展示
    /mgmt/sys/getComByCodeOrPri
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("公司资料查询展示-成功路径: 支持模糊查询负责人检查")
    def test_01_mgmt_sys_getComByCodeOrPri(self):
        
        @allure.step("公司资料查询展示-成功路径: 查询存在的负责人检查")
        def step_01_mgmt_sys_getComByCodeOrPri():
            params = deepcopy(self.params)
            params["principal"] = "张勇"                       
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert d["principal"] == "张勇"
        
        @allure.step("公司资料查询展示-成功路径: 模糊查询负责人的一部分检查")
        def step_02_mgmt_sys_getComByCodeOrPri():
            params = deepcopy(self.params)
            params["principal"] = "勇"                       
            with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert "勇" in d["principal"]
        
        step_01_mgmt_sys_getComByCodeOrPri()
        step_02_mgmt_sys_getComByCodeOrPri()

    @allure.severity(P2)
    @allure.title("公司资料查询展示-成功路径: 查询公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(1, 37) if i != 35])
    def test_02_mgmt_sys_getComByCodeOrPri(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_sys_getComByCodeOrPri(params, self.access_token) as r:            
            for d in r.json()["data"]["list"]:
                assert d["code"] == companyCode

