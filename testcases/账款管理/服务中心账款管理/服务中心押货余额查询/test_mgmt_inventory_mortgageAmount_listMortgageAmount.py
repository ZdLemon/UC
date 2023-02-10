# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_listMortgageAmount import data ,_mgmt_inventory_mortgageAmount_listMortgageAmount

from setting import P1, P2, P3, username, mobile, username_vip, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/mortgageAmount/listMortgageAmount")
class TestClass:
    """
    服务中心账款管理 -- 押货余额列表
    /mgmt/inventory/mortgageAmount/listMortgageAmount
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("押货余额列表: 默认搜索条件检查")
    def test_00_mgmt_inventory_mortgageAmount_listMortgageAmount(self):
        
        data = deepcopy(self.data)                   
        with _mgmt_inventory_mortgageAmount_listMortgageAmount(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
   
    @allure.severity(P2)
    @allure.title("押货余额列表: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store, store[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_01_mgmt_inventory_mortgageAmount_listMortgageAmount(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode  
        data["searchIsAll"] = False                   
        with _mgmt_inventory_mortgageAmount_listMortgageAmount(data, self.access_token) as r:
            if r.json()["data"]["mortgageAmountSearch"]:
                assert r.json()["data"]["mortgageAmountSearch"]["list"][0]["storeCode"] == storeCode
            else:
                assert r.json()["data"]["mortgageAmountSearch"] == None

    @allure.severity(P2)
    @allure.title("押货余额列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_mortgageAmount_listMortgageAmount(self, companyCode):
        
        data = deepcopy(self.data)   
        data["companyCode"] = companyCode   
        data["searchIsAll"] = False         
        with _mgmt_inventory_mortgageAmount_listMortgageAmount(data, self.access_token) as r:
            if r.json()["data"]["mortgageAmountSearch"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["mortgageAmountSearch"]["list"]):
                    assert i == companyCode 
            else:
                assert r.json()["data"]["mortgageAmountSearch"] == None    

    @allure.severity(P2)
    @allure.title("押货余额列表-成功路径: 查询最大押货额检查")
    @pytest.mark.parametrize("startAmount,endAmount", [(100, 10000), (10000, 20000)])
    def test_03_mgmt_inventory_mortgageAmount_listMortgageAmount(self, startAmount, endAmount):
        
        data = deepcopy(self.data)   
        data["startAmount"] = str(startAmount)
        data["endAmount"] = str(endAmount)
        data["searchIsAll"] = False
        with _mgmt_inventory_mortgageAmount_listMortgageAmount(data, self.access_token) as r:
            if r.json()["data"]["mortgageAmountSearch"]:
                for d in r.json()["data"]["mortgageAmountSearch"]["list"]:
                    assert startAmount <= d["maxRemitAmount"] <= endAmount
            else:
                assert r.json()["data"]["mortgageAmountSearch"] == None

    @allure.severity(P2)
    @allure.title("押货余额列表-成功路径: 查询可用押货余额检查")
    @pytest.mark.parametrize("availableStartAmount,availableEndAmount", [(100, 200), (10000, 20000)])
    def test_04_mgmt_inventory_mortgageAmount_listMortgageAmount(self, availableStartAmount, availableEndAmount):
        
        data = deepcopy(self.data)   
        data["availableStartAmount"] = str(availableStartAmount)
        data["availableEndAmount"] = str(availableEndAmount)
        data["searchIsAll"] = False
        with _mgmt_inventory_mortgageAmount_listMortgageAmount(data, self.access_token) as r:
            if r.json()["data"]["mortgageAmountSearch"]:
                for d in r.json()["data"]["mortgageAmountSearch"]["list"]:
                    assert availableStartAmount <= d["availableAmount"] <= availableEndAmount
            else:
                assert r.json()["data"]["mortgageAmountSearch"] == None

