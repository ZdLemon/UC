# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data, _mgmt_inventory_disManualInputRemit_pageList
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time


time_now = time.strftime('%Y%m',time.localtime(time.time()))

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disManualInputRemit/pageList")
class TestClass:
    """
    85折手工录入流水分页搜索列表
    /mgmt/inventory/disManualInputRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表-成功路径: 待审核列表查询月份检查")
    def test_01_mgmt_inventory_disManualInputRemit_pageList(self):
        
        data = deepcopy(self.data)
        data["startMonth"] = time.strftime('%Y%m',time.localtime(time.time()))
        data["endMonth"] = time.strftime('%Y%m',time.localtime(time.time()))
        data["verifyStatus"] = 0             
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(time.strftime('%Y%m',time.localtime(d["verifyTime"])) for d in r.json()["data"]["list"]):
                    assert i == time.strftime('%Y%m',time.localtime(time.time()))
            else:
                assert r.json()["data"]["list"] == []
 
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 待审核列表仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:5]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_02_mgmt_inventory_disManualInputRemit_pageList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode
        data["verifyStatus"] = 0              
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []
               
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表-成功路径: 待审核列表查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_inventory_disManualInputRemit_pageList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode  
        data["verifyStatus"] = 0                       
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert data["companyCode"] == i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 待审核列表下拉选项查询款项类型检查")
    @pytest.mark.parametrize("sourceType", [3, 7, 8, 9], ids=["其他", "手工增加押货款", "手工退押货款", "押货保证金转移"])
    def test_04_mgmt_inventory_disManualInputRemit_pageList(self, sourceType):
        
        data = deepcopy(self.data)
        data["sourceType"] = sourceType
        data["verifyStatus"] = 0               
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["sourceType"] for d in r.json()["data"]["list"]):
                    assert i == sourceType
            else:
                assert r.json()["data"]["list"] == []
        
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表 -成功路径: 待审核列表下拉选项查询审核结果检查")
    @pytest.mark.parametrize("verifyResult", [1, 2], ids=["通过", "拒绝"])
    def test_05_mgmt_inventory_disManualInputRemit_pageList(self, verifyResult):
        
        data = deepcopy(self.data)
        data["verifyResult"] = verifyResult
        data["verifyStatus"] = 0                   
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:           
            if r.json()["data"]["list"]:
                for i in set(d["verifyResult"] for d in r.json()["data"]["list"]):
                    assert i == verifyResult
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disManualInputRemit/pageList")
class TestClass02:
    """
    85折手工录入流水分页搜索列表
    /mgmt/inventory/disManualInputRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表-成功路径: 已审核列表查询月份检查")
    def test_01_mgmt_inventory_disManualInputRemit_pageList(self):
        
        data = deepcopy(self.data)
        data["startMonth"] = time.strftime('%Y%m',time.localtime(time.time()))
        data["endMonth"] = time.strftime('%Y%m',time.localtime(time.time()))
        data["verifyStatus"] = 1            
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(time.strftime('%Y%m',time.localtime(d["verifyTime"]/1000)) for d in r.json()["data"]["list"]):
                    assert i == time.strftime('%Y%m',time.localtime(time.time()))
            else:
                assert r.json()["data"]["list"] == []
 
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 已审核列表仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:5]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_02_mgmt_inventory_disManualInputRemit_pageList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode
        data["verifyStatus"] = 1             
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []
               
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表-成功路径: 已审核列表查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_inventory_disManualInputRemit_pageList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode  
        data["verifyStatus"] = 1                       
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert data["companyCode"] == i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 已审核列表下拉选项查询款项类型检查")
    @pytest.mark.parametrize("sourceType", [3, 7, 8, 9], ids=["其他", "手工增加押货款", "手工退押货款", "押货保证金转移"])
    def test_04_mgmt_inventory_disManualInputRemit_pageList(self, sourceType):
        
        data = deepcopy(self.data)
        data["sourceType"] = sourceType
        data["verifyStatus"] = 1               
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["sourceType"] for d in r.json()["data"]["list"]):
                    assert i == sourceType
            else:
                assert r.json()["data"]["list"] == []
        
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表 -成功路径: 已审核列表下拉选项查询审核结果检查")
    @pytest.mark.parametrize("verifyResult", [1, 2], ids=["通过", "拒绝"])
    def test_05_mgmt_inventory_disManualInputRemit_pageList(self, verifyResult):
        
        data = deepcopy(self.data)
        data["verifyResult"] = verifyResult
        data["verifyStatus"] = 1                 
        with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:           
            if r.json()["data"]["list"]:
                for i in set(d["verifyResult"] for d in r.json()["data"]["list"]):
                    assert i == verifyResult
            else:
                assert r.json()["data"]["list"] == []







