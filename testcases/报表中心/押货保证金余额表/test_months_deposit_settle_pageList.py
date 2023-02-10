# coding:utf-8

from api.settle_job._months_deposit_settle_pageList import data, _months_deposit_settle_pageList # 押货保证金余额表

from setting import P1, P2, P3, BASE_URL

from copy import deepcopy
import os
import allure
import pytest
import time
import datetime


@allure.feature("mall_center_months")
@allure.story("/months/deposit/settle/pageList")
class TestClass:
    """
    押货保证金余额表
    /months/deposit/settle/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
  
    
    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询默认条件检查")
    def test_01_months_deposit_settle_pageList(self):
        
        data = deepcopy(self.data) 
        data["startMonth"] = None 
        data["endMonth"] = None                    
        with _months_deposit_settle_pageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询月份检查")
    def test_02_months_deposit_settle_pageList(self):
        
        data = deepcopy(self.data) 
        data["startMonth"] = f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1) # 月份最小值,格式：yyyyMM, 上个月 
        data["endMonth"] = f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1) # 月份最小值,格式：yyyyMM, 上个月                    
        with _months_deposit_settle_pageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["month"] for d in r.json()["data"]["list"]):
                    assert i["month"] == f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1)

    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询服务中心编号检查")
    def test_03_months_deposit_settle_pageList(self):

        pageList = None
        
        @allure.step("押货保证金余额表: 获取服务中心编号")
        def test_01_months_deposit_settle_pageList():
                    
            nonlocal pageList
            data = deepcopy(self.data) 
            data["startMonth"] = None
            data["endMonth"] = None                    
            with _months_deposit_settle_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    pageList =  r.json()["data"]["list"][0]

        @allure.step("押货保证金余额表")
        def test_02_months_deposit_settle_pageList():
                    
            data = deepcopy(self.data)
            data["storeCode"] = pageList["storeCode"]
            data["startMonth"] = None
            data["endMonth"] = None                    
            with _months_deposit_settle_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == pageList["storeCode"]
        
        test_01_months_deposit_settle_pageList()
        if pageList:
            test_02_months_deposit_settle_pageList()

    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询负责人卡号检查")
    def test_04_months_deposit_settle_pageList(self):

        pageList = None
        
        @allure.step("押货保证金余额表: 获取负责人卡号")
        def test_01_months_deposit_settle_pageList():
                    
            nonlocal pageList
            data = deepcopy(self.data) 
            data["startMonth"] = None
            data["endMonth"] = None                    
            with _months_deposit_settle_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    pageList =  r.json()["data"]["list"][0]

        @allure.step("押货保证金余额表")
        def test_02_months_deposit_settle_pageList():
                    
            data = deepcopy(self.data)
            data["leaderNo"] = pageList["leaderNo"]
            data["startMonth"] = None
            data["endMonth"] = None                    
            with _months_deposit_settle_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["leaderNo"] == pageList["leaderNo"]
        
        test_01_months_deposit_settle_pageList()
        if pageList:
            test_02_months_deposit_settle_pageList()

    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询负责人检查")
    def test_05_months_deposit_settle_pageList(self):

        pageList = None
        
        @allure.step("押货保证金余额表: 获取负责人")
        def test_01_months_deposit_settle_pageList():
                    
            nonlocal pageList
            data = deepcopy(self.data) 
            data["startMonth"] = None
            data["endMonth"] = None                    
            with _months_deposit_settle_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    pageList =  r.json()["data"]["list"][0]

        @allure.step("押货保证金余额表")
        def test_02_months_deposit_settle_pageList():
                    
            data = deepcopy(self.data)
            data["leaderName"] = pageList["leaderName"]
            data["startMonth"] = None
            data["endMonth"] = None                    
            with _months_deposit_settle_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["leaderName"] == pageList["leaderName"]
        
        test_01_months_deposit_settle_pageList()
        if pageList:
            test_02_months_deposit_settle_pageList()

    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_06_months_deposit_settle_pageList(self, companyCode):
                    
        data = deepcopy(self.data)
        data["companyCode"] = companyCode
        data["startMonth"] = None
        data["endMonth"] = None                    
        with _months_deposit_settle_pageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(i["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
        
    @allure.severity(P2)
    @allure.title("押货保证金余额表-成功路径: 查询可用结余为负检查")
    @pytest.mark.parametrize("moneyType", [0, 1], ids=["是", "否"])
    def test_06_months_deposit_settle_pageList(self, moneyType):
        
        data = deepcopy(self.data) 
        data["moneyType"] = moneyType # 可用结余为负 0 是，1 否  
        data["startMonth"] = None
        data["endMonth"] = None                    
        with _months_deposit_settle_pageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if moneyType == 1:
                        assert i["closingDepositAmount"] >= 0
                    else:
                        assert i["closingDepositAmount"] < 0



