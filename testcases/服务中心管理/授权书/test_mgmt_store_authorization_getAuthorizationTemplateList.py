# coding:utf-8

from api.mall_mgmt_application._mgmt_store_authorization_getAuthorizationTemplateList import params, _mgmt_store_authorization_getAuthorizationTemplateList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/authorization/getAuthorizationTemplateList")
class TestClass:
    """
    获取授权书模板列表
    /mgmt/store/authorization/getAuthorizationTemplateList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("获取授权书模板列表-成功路径: 仅支持精确查询模板编号检查")
    def test_01_mgmt_store_authorization_getAuthorizationTemplateList(self):
        
        getAuthorizationTemplateList = None
        
        @allure.step("获取授权书模板列表")
        def step_01_mgmt_store_authorization_getAuthorizationTemplateList():
            
            nonlocal getAuthorizationTemplateList
            params = deepcopy(self.params)               
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getAuthorizationTemplateList = r.json()["data"]["list"][0]
        
        @allure.step("获取授权书模板列表")
        def step_02_mgmt_store_authorization_getAuthorizationTemplateList():
            
            params = deepcopy(self.params)
            params["templateNo"] = getAuthorizationTemplateList["templateNo"]              
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["templateNo"] for d in r.json()["data"]["list"]):    
                    assert i == getAuthorizationTemplateList["templateNo"]
        
        step_01_mgmt_store_authorization_getAuthorizationTemplateList()
        if getAuthorizationTemplateList:
            step_02_mgmt_store_authorization_getAuthorizationTemplateList()
    
    @allure.severity(P2)
    @allure.title("获取授权书模板列表-成功路径: 仅支持精确查询模板名称检查")
    def test_02_mgmt_store_authorization_getAuthorizationTemplateList(self):
        
        getAuthorizationTemplateList = None
        
        @allure.step("获取授权书模板列表")
        def step_01_mgmt_store_authorization_getAuthorizationTemplateList():
            
            nonlocal getAuthorizationTemplateList
            params = deepcopy(self.params)               
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getAuthorizationTemplateList = r.json()["data"]["list"][0]
        
        @allure.step("获取授权书模板列表")
        def step_02_mgmt_store_authorization_getAuthorizationTemplateList():
            
            params = deepcopy(self.params)
            params["templateName"] = getAuthorizationTemplateList["templateName"]              
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["templateName"] for d in r.json()["data"]["list"]):    
                    assert i == getAuthorizationTemplateList["templateName"]
        
        step_01_mgmt_store_authorization_getAuthorizationTemplateList()
        if getAuthorizationTemplateList:
            step_02_mgmt_store_authorization_getAuthorizationTemplateList()
             
    @allure.severity(P2)
    @allure.title("获取授权书模板列表-成功路径: 查询状态检查")
    @pytest.mark.parametrize("status", [1, 0])
    def test_03_mgmt_store_authorization_getAuthorizationTemplateList(self, status):
        
        @allure.step("获取授权书模板列表")
        def step_01_mgmt_store_authorization_getAuthorizationTemplateList():
            
            params = deepcopy(self.params)
            params["status"] = status # 状态，0：已失效，1：生效中                      
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["status"] for d in r.json()["data"]["list"]):    
                        assert i == status

        step_01_mgmt_store_authorization_getAuthorizationTemplateList()

    @allure.severity(P2)
    @allure.title("获取授权书模板列表-成功路径: 查询添加日期检查")
    def test_04_mgmt_store_authorization_getAuthorizationTemplateList(self):
        
        getAuthorizationTemplateList = None
        
        @allure.step("获取授权书模板列表")
        def step_01_mgmt_store_authorization_getAuthorizationTemplateList():
            
            nonlocal getAuthorizationTemplateList
            params = deepcopy(self.params)               
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getAuthorizationTemplateList = r.json()["data"]["list"][0]
        
        @allure.step("获取授权书模板列表")
        def step_02_mgmt_store_authorization_getAuthorizationTemplateList():
            
            params = deepcopy(self.params)
            params["addStartTime"] = f'{time.strftime("%Y-%m-%d", time.localtime(int(getAuthorizationTemplateList["addTime"])/1000))} 00:00:00'
            params["addEndTime"] = f'{time.strftime("%Y-%m-%d", time.localtime(int(getAuthorizationTemplateList["addTime"])/1000))} 23:59:59'              
            with _mgmt_store_authorization_getAuthorizationTemplateList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(time.strftime("%Y-%m-%d", time.localtime(int(d["addTime"])/1000)) for d in r.json()["data"]["list"]):    
                    assert i == time.strftime("%Y-%m-%d", time.localtime(int(getAuthorizationTemplateList["addTime"])/1000))
        
        step_01_mgmt_store_authorization_getAuthorizationTemplateList()
        if getAuthorizationTemplateList:
            step_02_mgmt_store_authorization_getAuthorizationTemplateList()
      