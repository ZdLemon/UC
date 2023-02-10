# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getOrderSettlement import params, _mgmt_order_getOrderSettlement

from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSettlement")
class TestClass:
    """
    交付结算列表:搜索检查
    /mgmt/order/getOrderSettlement
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title(" 交付结算列表-成功路径: 查询业绩月份默认本月检查")
    def test_01_mgmt_order_getOrderSettlement(self):
        
        params = deepcopy(self.params)           
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["orderMonth"] for d in r.json()["data"]["list"]):
                    assert i == params["orderMonth"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title(" 交付结算列表: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_02_mgmt_order_getOrderSettlement(self, storeCode):
        
        params = deepcopy(self.params)
        params["storeCode"] = storeCode                
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []
               
    @allure.severity(P2)
    @allure.title(" 交付结算列表: 仅支持精确查询负责人卡号检查")
    @pytest.mark.parametrize("cardNo", [username_85, username_85[:-1]], ids=["正确的负责人卡号", "负责人卡号的一部分"])
    def test_03_mgmt_order_getOrderSettlement(self, cardNo):
        
        params = deepcopy(self.params)
        params["cardNo"] =  cardNo                      
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == cardNo
            else:
                assert r.json()["data"]["list"] == []
        
    @allure.severity(P2)
    @allure.title(" 交付结算列表 -成功路径: 支持模糊查询负责人检查")
    @pytest.mark.parametrize("realName", [name_85, name_85[:-1]], ids=["正确的负责人", "负责人的一部分"])
    def test_04_mgmt_order_getOrderSettlement(self, realName):
        
        params = deepcopy(self.params)
        params["realName"] = realName                      
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r: 
            if r.json()["data"]["list"]:          
                for i in set(d["realName"] for d in r.json()["data"]["list"]):
                    assert realName in i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title(" 交付结算列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_05_mgmt_order_getOrderSettlement(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert params["companyCode"] == i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title(" 交付结算列表: 下拉选项查询本期交付差额是否为负检查")
    @pytest.mark.parametrize("isDifference,ids", [(0, "否"), (1, "是")])
    def test_06_mgmt_order_getOrderSettlement(self, isDifference, ids):
        
        params = deepcopy(self.params)
        params["isDifference"] = isDifference                     
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:
            if isDifference == 1:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["difAmount"] < 0
                else:
                    assert r.json()["data"]["list"] == []
            
            elif isDifference == 0:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["difAmount"] >= 0
                else:
                    assert r.json()["data"]["list"] == []
       
    @allure.severity(P2)
    @allure.title(" 交付结算列表: 下拉选项查询差额校验是否为零检查")
    @pytest.mark.parametrize("isDifCheck,ids", [(0, "否"), (1, "是")])
    def test_06_mgmt_order_getOrderSettlement(self, isDifCheck, ids):
        
        params = deepcopy(self.params)
        params["isDifCheck"] = isDifCheck                     
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:
            if isDifCheck == 0:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["difCheck"] != 0
                else:
                    assert r.json()["data"]["list"] == []
            
            elif isDifCheck == 1:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["difCheck"] == 0
                else:
                    assert r.json()["data"]["list"] == []
 

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSettlement")
class TestClass02:
    """
    交付结算列表:各字段逻辑关系检查
    /mgmt/order/getOrderSettlement
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title(" 交付结算列表-成功路径: 各字段逻辑关系检查")
    def test_01_mgmt_order_getOrderSettlement(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = store_85           
        with _mgmt_order_getOrderSettlement(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["retailPrice"] - d["securityAmount"] == d["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
                    assert d["orderAmount"] - d["totalAmount"] == d["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
                    assert d["receiveAmount"] - d["payDifference"] == d["difAmount"] # 店应收回款 - 店应补差额 = 本期交付差额
                    assert d["securityTotal"] - d["securityAmount"] == d["difCheck"] # 交付总量对应的押货价合计 - 押货价金额 = 差额校验
            else:
                assert r.json()["data"]["list"] == []


