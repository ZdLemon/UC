# coding:utf-8

from api.settle_job._months_deposit_billCheck_page import data, _months_deposit_billCheck_page
from setting import P1, P2, P3, store_8502

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("settle_job")
@allure.story("/months/deposit/billCheck/page")
class TestClass:
    """
    押货保证金月结列表
    /months/deposit/billCheck/page
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询已月结服务中心-成功路径: 查询服务中心编号检查")
    def test_01_months_deposit_billCheck_page(self):
        
        getStoreContractInvtBillList = None # 查询已月结服务中心
        
        @allure.step("查询已月结服务中心: 获取服务中心编号")
        def step_01_months_deposit_billCheck_page():
            
            nonlocal getStoreContractInvtBillList
            data = deepcopy(self.data)
            with _months_deposit_billCheck_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("查询已月结服务中心")
        def step_02_months_deposit_billCheck_page():
            
            data = deepcopy(self.data)
            data["storeCode"] = getStoreContractInvtBillList["storeCode"]
            with _months_deposit_billCheck_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == getStoreContractInvtBillList["storeCode"]
       
        step_01_months_deposit_billCheck_page()
        if getStoreContractInvtBillList:
            step_02_months_deposit_billCheck_page()

    @allure.severity(P2)
    @allure.title("查询已月结服务中心-成功路径: 查询月份检查")
    def test_02_months_deposit_billCheck_page(self):
        
        @allure.step("查询已月结服务中心:查询上个月")
        def step_01_months_deposit_billCheck_page():
            
            data = deepcopy(self.data)
            with _months_deposit_billCheck_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        assert i["month"] == f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1)
        
        @allure.step("查询已月结服务中心:查询202201-上个月")
        def step_02_months_deposit_billCheck_page():
            
            data = deepcopy(self.data)
            data["minMonth"] = "202201"
            with _months_deposit_billCheck_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
       
        step_01_months_deposit_billCheck_page()
        step_02_months_deposit_billCheck_page()

    @allure.severity(P2)
    @allure.title("查询已月结服务中心-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_months_deposit_billCheck_page(self, companyCode):       
            
        data = deepcopy(self.data)
        data["companyCode"] = companyCode
        with _months_deposit_billCheck_page(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["companyCode"] == companyCode
            else:
                assert r.json()["data"]["list"] == []