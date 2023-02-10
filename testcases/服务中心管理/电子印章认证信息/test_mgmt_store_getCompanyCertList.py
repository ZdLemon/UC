# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getCompanyCertList import params, _mgmt_store_getCompanyCertList
from setting import P1, P2, P3, store_8502

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/getCompanyCertList")
class TestClass:
    """
    获取电子印章认证列表:服务中心tab列表
    /mgmt/store/getCompanyCertList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 仅精确查询服务中心编号检查")
    def test_01_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取服务中心编号")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["storeCode"] = getStoreContractInvtBillList["storeCode"]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == getStoreContractInvtBillList["storeCode"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 模糊查询企业认证名称检查")
    def test_02_mgmt_store_getCompanyCertList(self):
        
        getCompanyCertList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表:获取企业认证名称")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getCompanyCertList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyName"]:
                            getCompanyCertList = i
                        
        @allure.step("获取电子印章认证列表:精确查询企业认证名称")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["companyName"] = getCompanyCertList["companyName"]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert getCompanyCertList["companyName"] in i["companyName"]

        @allure.step("获取电子印章认证列表:模糊查询企业认证名称")
        def step_03_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["companyName"] = getCompanyCertList["companyName"][:-2]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert getCompanyCertList["companyName"][:-2] in i["companyName"]
                           
        step_01_mgmt_store_getCompanyCertList()
        if getCompanyCertList:
            step_02_mgmt_store_getCompanyCertList()
            step_03_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 仅精确查询企业管理员名称检查")
    def test_03_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取企业管理员名称")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["adminName"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["adminName"] = getStoreContractInvtBillList["adminName"]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["adminName"] == getStoreContractInvtBillList["adminName"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 仅精确查询企业管理员手机号检查")
    def test_04_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取企业管理员手机号")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["adminMobile"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["adminMobile"] = getStoreContractInvtBillList["adminMobile"]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["adminMobile"] == getStoreContractInvtBillList["adminMobile"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 查询通过认证时间检查")
    def test_05_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取通过认证时间")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["certificationTime"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["certStartTime"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["certificationTime"])/1000))
            params["certEndTime"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["certificationTime"])/1000))
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["certificationTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["certificationTime"])/1000))
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 仅精确查询认证中信用代码检查")
    def test_06_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取认证中信用代码")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["creditNo"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["creditNo"] = getStoreContractInvtBillList["creditNo"]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["creditNo"] == getStoreContractInvtBillList["creditNo"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-成功路径: 仅精确查询法大大信用代码检查")
    def test_07_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取法大大信用代码")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["fddCreditNo"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["fddCreditNo"] = getStoreContractInvtBillList["fddCreditNo"]
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["fddCreditNo"] == getStoreContractInvtBillList["fddCreditNo"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/getCompanyCertList")
class TestClass02:
    """
    获取电子印章认证列表:服务公司tab列表
    /mgmt/store/getCompanyCertList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 仅精确查询服务中心编号检查")
    def test_01_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取服务中心编号")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["storeCode"] = getStoreContractInvtBillList["storeCode"]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == getStoreContractInvtBillList["storeCode"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 模糊查询企业认证名称检查")
    def test_02_mgmt_store_getCompanyCertList(self):
        
        getCompanyCertList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表:获取企业认证名称")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getCompanyCertList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyName"]:
                            getCompanyCertList = i
                        
        @allure.step("获取电子印章认证列表:精确查询企业认证名称")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["companyName"] = getCompanyCertList["companyName"]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert getCompanyCertList["companyName"] in i["companyName"]

        @allure.step("获取电子印章认证列表:模糊查询企业认证名称")
        def step_03_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["companyName"] = getCompanyCertList["companyName"][:-2]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert getCompanyCertList["companyName"][:-2] in i["companyName"]
                           
        step_01_mgmt_store_getCompanyCertList()
        if getCompanyCertList:
            step_02_mgmt_store_getCompanyCertList()
            step_03_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 仅精确查询企业管理员名称检查")
    def test_03_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取企业管理员名称")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["adminName"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["adminName"] = getStoreContractInvtBillList["adminName"]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["adminName"] == getStoreContractInvtBillList["adminName"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 仅精确查询企业管理员手机号检查")
    def test_04_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取企业管理员手机号")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["adminMobile"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["adminMobile"] = getStoreContractInvtBillList["adminMobile"]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["adminMobile"] == getStoreContractInvtBillList["adminMobile"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 查询通过认证时间检查")
    def test_05_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取通过认证时间")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["certificationTime"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["certStartTime"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["certificationTime"])/1000))
            params["certEndTime"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["certificationTime"])/1000))
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["certificationTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["certificationTime"])/1000))
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 仅精确查询认证中信用代码检查")
    def test_06_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取认证中信用代码")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["creditNo"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["creditNo"] = getStoreContractInvtBillList["creditNo"]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["creditNo"] == getStoreContractInvtBillList["creditNo"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()

    @allure.severity(P2)
    @allure.title("获取电子印章认证列表-服务公司tab列表-成功路径: 仅精确查询法大大信用代码检查")
    def test_07_mgmt_store_getCompanyCertList(self):
        
        getStoreContractInvtBillList = None # 获取电子印章认证列表
        
        @allure.step("获取电子印章认证列表: 获取法大大信用代码")
        def step_01_mgmt_store_getCompanyCertList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["pageSize"] = 100
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["fddCreditNo"]:
                            getStoreContractInvtBillList = i
        
        @allure.step("获取电子印章认证列表")
        def step_02_mgmt_store_getCompanyCertList():
            
            params = deepcopy(self.params)
            params["fddCreditNo"] = getStoreContractInvtBillList["fddCreditNo"]
            params["customerType"] = 2 # 客户类型，1/服务中心，2/服务公司
            with _mgmt_store_getCompanyCertList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["fddCreditNo"] == getStoreContractInvtBillList["fddCreditNo"]
       
        step_01_mgmt_store_getCompanyCertList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_getCompanyCertList()
