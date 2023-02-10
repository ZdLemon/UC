# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data, _mgmt_inventory_remit_pageSearchList
from api.mall_center_member._crm_member_serviceCompany_bankOfDeposit import params, _crm_member_serviceCompany_bankOfDeposit # 注销原因、审核不通过原因、开户银行接口
from setting import P1, P2, P3, username, mobile, username_vip, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/remit/pageSearchList")
class TestClass:
    """
    手工录入流水分页搜索列表: 待审核列表查询
    /mgmt/inventory/remit/pageSearchList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 默认查询检查")
    def test_00_mgmt_inventory_remit_pageSearchList(self):
        
        data = deepcopy(self.data)                   
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 仅支持精确查询服务中心编号检查")
    def test_01_mgmt_inventory_remit_pageSearchList(self):
        
        storeCode = ""
        data = deepcopy(self.data)
        
        @allure.step("获取服务中心编号")
        def step_01_mgmt_inventory_remit_pageSearchList():
            
            nonlocal storeCode                   
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeCode = r.json()["data"]["list"][0]["storeCode"]
        
        @allure.step("精确查询服务中心编号")
        def step_02_mgmt_inventory_remit_pageSearchList():
            
            data["storeCode"] = storeCode 
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    assert d["storeCode"] == storeCode
        
        @allure.step("模糊查询服务中心编号")
        def step_03_mgmt_inventory_remit_pageSearchList():
            
            data["storeCode"] = storeCode[:-1]
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_remit_pageSearchList()
        step_02_mgmt_inventory_remit_pageSearchList()
        step_03_mgmt_inventory_remit_pageSearchList()
        
    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_remit_pageSearchList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode                     
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []
    
    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 查询款项类型检查")
    @pytest.mark.parametrize("sourceType,ids", [(7, "手工退押货款"), (8, "手工增押货款"), (9, "转销售"), (14, "钱包款与押货款互转"), (12, "其他")])
    def test_03_mgmt_inventory_remit_pageSearchList(self, sourceType, ids):
        
        data = deepcopy(self.data)
        data["sourceType"] = sourceType                     
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["sourceType"] == sourceType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 查询付款银行检查")
    def test_04_mgmt_inventory_remit_pageSearchList(self):
        
        bankName = ""
        data = deepcopy(self.data)
        
        @allure.step("注销原因、审核不通过原因、开户银行接口")
        def step_crm_member_serviceCompany_bankOfDeposit():
            
            nonlocal bankName
            params = deepcopy(self.params)
            with _crm_member_serviceCompany_bankOfDeposit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                bankName = r.json()["data"]
        
        @allure.step("查询付款银行")
        def step_mgmt_inventory_remit_pageSearchList():
            
            for i in bankName:
                data["bankName"] = i["name"]
                with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                    if r.json()["data"]["list"]:
                        for d in r.json()["data"]["list"]:
                            assert i["name"] in d["bankName"]
                    else:
                        assert r.json()["data"]["list"] == []
        
        step_crm_member_serviceCompany_bankOfDeposit()
        step_mgmt_inventory_remit_pageSearchList()

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 查询审核结果检查")
    @pytest.mark.parametrize("verifyResult,ids", [(0, "未审核"), (1, "通过"), (2, "拒绝")])
    def test_05_mgmt_inventory_remit_pageSearchList(self, verifyResult, ids):
        
        data["verifyResult"] = verifyResult
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["verifyResult"] == verifyResult
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/remit/pageSearchList")
class TestClass02:
    """
    手工录入流水分页搜索列表: 已审核列表查询
    /mgmt/inventory/remit/pageSearchList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 已审核tab默认查询检查")
    def test_00_mgmt_inventory_remit_pageSearchList(self):
        
        data = deepcopy(self.data) 
        data["verifyStatus"] = 1 # 审核状态 0 待审核 1 已审核     
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 已审核tab仅支持精确查询服务中心编号检查")
    def test_01_mgmt_inventory_remit_pageSearchList(self):
        
        storeCode = ""
        data = deepcopy(self.data)
        data["verifyStatus"] = 1 # 审核状态 0 待审核 1 已审核
        
        @allure.step("获取服务中心编号")
        def step_01_mgmt_inventory_remit_pageSearchList():
            
            nonlocal storeCode                   
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeCode = r.json()["data"]["list"][0]["storeCode"]
        
        @allure.step("精确查询服务中心编号")
        def step_02_mgmt_inventory_remit_pageSearchList():
            
            data["storeCode"] = storeCode 
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    assert d["storeCode"] == storeCode
        
        @allure.step("模糊查询服务中心编号")
        def step_03_mgmt_inventory_remit_pageSearchList():
            
            data["storeCode"] = storeCode[:-1]
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_remit_pageSearchList()
        step_02_mgmt_inventory_remit_pageSearchList()
        step_03_mgmt_inventory_remit_pageSearchList()
        
    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 已审核tab查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_remit_pageSearchList(self, companyCode):
        
        data = deepcopy(self.data)
        data["verifyStatus"] = 1 # 审核状态 0 待审核 1 已审核
        data["companyCode"] = companyCode                     
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []
    
    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 已审核tab查询款项类型检查")
    @pytest.mark.parametrize("sourceType,ids", [(7, "手工退押货款"), (8, "手工增押货款"), (9, "转销售"), (14, "钱包款与押货款互转"), (12, "其他")])
    def test_03_mgmt_inventory_remit_pageSearchList(self, sourceType, ids):
        
        data = deepcopy(self.data)
        data["verifyStatus"] = 1 # 审核状态 0 待审核 1 已审核
        data["sourceType"] = sourceType                     
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["sourceType"] == sourceType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 已审核tab查询付款银行检查")
    def test_04_mgmt_inventory_remit_pageSearchList(self):
        
        bankName = ""
        data = deepcopy(self.data)
        data["verifyStatus"] = 1 # 审核状态 0 待审核 1 已审核
        
        @allure.step("注销原因、审核不通过原因、开户银行接口")
        def step_crm_member_serviceCompany_bankOfDeposit():
            
            nonlocal bankName
            params = deepcopy(self.params)
            with _crm_member_serviceCompany_bankOfDeposit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                bankName = r.json()["data"]
        
        @allure.step("查询付款银行")
        def step_mgmt_inventory_remit_pageSearchList():
            
            for i in bankName:
                data["bankName"] = i["name"]
                with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                    if r.json()["data"]["list"]:
                        for d in r.json()["data"]["list"]:
                            assert i["name"] in d["bankName"]
                    else:
                        assert r.json()["data"]["list"] == []
        
        step_crm_member_serviceCompany_bankOfDeposit()
        step_mgmt_inventory_remit_pageSearchList()

    @allure.severity(P2)
    @allure.title("手工录入流水分页搜索列表: 已审核tab查询审核结果检查")
    @pytest.mark.parametrize("verifyResult,ids", [(0, "未审核"), (1, "通过"), (2, "拒绝")])
    def test_05_mgmt_inventory_remit_pageSearchList(self, verifyResult, ids):
        
        data = deepcopy(self.data)
        data["verifyStatus"] = 1 # 审核状态 0 待审核 1 已审核
        data["verifyResult"] = verifyResult
        with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["verifyResult"] == verifyResult
            else:
                assert r.json()["data"]["list"] == []

