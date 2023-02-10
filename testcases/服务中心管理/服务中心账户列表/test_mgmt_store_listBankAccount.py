# coding:utf-8

from ctypes.wintypes import PWIN32_FIND_DATAW
from api.mall_mgmt_application._mgmt_store_listBankAccount import params, _mgmt_store_listBankAccount
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/listBankAccount")
class TestClass:
    """
    银行账号列表
    /mgmt/store/listBankAccount
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("银行账号列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_01_mgmt_store_listBankAccount(self):
        
        listBankAccount = None 
        
        @allure.step("银行账号列表: 获取服务中心编号")
        def step_01_mgmt_store_listBankAccount():
            
            nonlocal listBankAccount
            params = deepcopy(self.params)       
            with _mgmt_store_listBankAccount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    listBankAccount = r.json()["data"]["list"][0]
        
        @allure.step("银行账号列表-成功路径: 持精确查询服务中心编号检查")
        def step_02_mgmt_store_listBankAccount():
            
            params = deepcopy(self.params)
            params["storeCode"] = listBankAccount["storeCode"]              
            with _mgmt_store_listBankAccount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == listBankAccount["storeCode"]
        
        step_01_mgmt_store_listBankAccount()
        if listBankAccount:
            step_02_mgmt_store_listBankAccount()
        
    @allure.severity(P2)
    @allure.title("银行账号列表-成功路径: 仅支持精确查询负责人卡号检查")
    def test_02_mgmt_store_listBankAccount(self):
        
        listBankAccount = None 
        
        @allure.step("银行账号列表: 获取负责人卡号")
        def step_01_mgmt_store_listBankAccount():
            
            nonlocal listBankAccount
            params = deepcopy(self.params)       
            with _mgmt_store_listBankAccount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    listBankAccount = r.json()["data"]["list"][0]
        
        @allure.step("银行账号列表-成功路径: 持精确查询负责人卡号检查")
        def step_02_mgmt_store_listBankAccount():
            
            params = deepcopy(self.params)
            params["leaderCardNo"] = listBankAccount["leaderNo"]              
            with _mgmt_store_listBankAccount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["leaderNo"] == listBankAccount["leaderNo"]
        
        step_01_mgmt_store_listBankAccount()
        if listBankAccount:
            step_02_mgmt_store_listBankAccount()
     
    @allure.severity(P2)
    @allure.title("银行账号列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_store_listBankAccount_08(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_store_listBankAccount(params, self.access_token) as r:
            if r.json()["data"]["list"]:            
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert params["companyCode"] == i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("银行账号列表-成功路径: 查询账号状态检查")
    @pytest.mark.parametrize("isUsed", [1, 2], ids=["生效", "作废"])
    def test_04_mgmt_store_listBankAccount_09(self, isUsed):
        
        params = deepcopy(self.params)
        params["isUsed"] = isUsed                      
        with _mgmt_store_listBankAccount(params, self.access_token) as r:
            if r.json()["data"]["list"]:      
                for i in set(d["isUsed"] for d in r.json()["data"]["list"]):
                    assert i == isUsed
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("银行账号列表-成功路径: 查询是否已签约检查")
    @pytest.mark.parametrize("isSigned", [1, 2], ids=["是", "否"])
    def test_05_mgmt_store_listBankAccount_09(self, isSigned):
        
        params = deepcopy(self.params)
        params["isSigned"] = isSigned                      
        with _mgmt_store_listBankAccount(params, self.access_token) as r:
            if r.json()["data"]["list"]:      
                for i in set(d["isSigned"] for d in r.json()["data"]["list"]):
                    assert i == isSigned
            else:
                assert r.json()["data"]["list"] == []


       