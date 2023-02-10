# coding:utf-8

from api.mall_mgmt_application._mgmt_store_queryContractTemplateListPage import params, _mgmt_store_queryContractTemplateListPage
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    分页查询合同模板列表
    /mgmt/store/queryContractTemplateListPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/store/queryContractTemplateListPage")
    @allure.severity(P3)
    @allure.title("分页查询合同模板列表-成功路径: 查询合同类型检查")
    @pytest.mark.parametrize("contractType", list(range(1, 3)), ids=["经营合同", "协议"])
    def test_01_mgmt_store_queryContractTemplateListPage(self, contractType):
        
        params = deepcopy(self.params)
        params["contractType"] = contractType
        with _mgmt_store_queryContractTemplateListPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["contractType"] for d in r.json()["data"]["list"]):
                assert params["contractType"] == i

    @allure.story("/mgmt/store/queryContractTemplateListPage")
    @allure.severity(P3)
    @allure.title("分页查询合同模板列表-成功路径: 查询客户类型检查")
    @pytest.mark.parametrize("customerType", list(range(1, 3)), ids=["服务中心", "服务公司"])
    def test_02_mgmt_store_queryContractTemplateListPage(self, customerType):
        
        params = deepcopy(self.params)
        params["customerType"] = customerType
        with _mgmt_store_queryContractTemplateListPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.story("/mgmt/store/queryContractTemplateListPage")
    @allure.severity(P3)
    @allure.title("分页查询合同模板列表-成功路径: 查询是否线上模板检查")
    @pytest.mark.parametrize("isOnline", list(range(1, 3)), ids=["线上", "线下"])
    def test_03_mgmt_store_queryContractTemplateListPage(self, isOnline):
        
        params = deepcopy(self.params)
        params["isOnline"] = isOnline
        with _mgmt_store_queryContractTemplateListPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["isOnline"] for d in r.json()["data"]["list"]):
                assert params["isOnline"] == i

    @allure.story("/mgmt/store/queryContractTemplateListPage")
    @allure.severity(P3)
    @allure.title("分页查询合同模板列表-成功路径: 查询模板状态检查")
    @pytest.mark.parametrize("templateStatus", list(range(1, 3)), ids=["停用", "启用"])
    def test_04_mgmt_store_queryContractTemplateListPage(self, templateStatus):
        
        params = deepcopy(self.params)
        params["templateStatuse"] = templateStatus
        with _mgmt_store_queryContractTemplateListPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["templateStatus"] for d in r.json()["data"]["list"]):
                assert params["templateStatus"] == i
