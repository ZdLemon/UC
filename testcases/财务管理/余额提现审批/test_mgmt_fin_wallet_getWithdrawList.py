# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getWithdrawList import data ,_mgmt_fin_wallet_getWithdrawList
from setting import P1, P2, P3, username_vip

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/getWithdrawList")
class TestClass:
    """
    余额提现审批-列表
    /mgmt/fin/wallet/getWithdrawList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
   
    
    @allure.severity(P2)
    @allure.title("余额提现审批列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username_vip, username_vip[:-2]], ids=["正确会员卡号", "会员卡号的一部分"])
    def test_01_mgmt_fin_wallet_getWithdrawList(self, cardNo):
        
        data = deepcopy(self.data)   
        data["cardNo"] = cardNo                  
        with _mgmt_fin_wallet_getWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["cardNo"] == data["cardNo"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("余额提现审批列表: 仅支持精确查询手机号码检查")
    @pytest.mark.parametrize("mobile", ["18812300040", "1881230004"], ids=["正确手机号码", "手机号码的一部分"])
    def test_02_mgmt_fin_wallet_getWithdrawList(self, mobile):
        
        data = deepcopy(self.data)   
        data["mobile"] = mobile                 
        with _mgmt_fin_wallet_getWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["mobile"] == "18812300040"
            else:
                assert r.json()["data"]["list"] == None

    @allure.severity(P2)
    @allure.title("余额提现审批列表: 查询顾客姓名检查")
    @pytest.mark.parametrize("realname", ["魏老师", "魏老"], ids=["精确姓名", "姓名的一部分"])
    def test_03_mgmt_fin_wallet_getWithdrawList(self, realname):
        
        data = deepcopy(self.data)   
        data["realname"] = realname                
        with _mgmt_fin_wallet_getWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                        assert "魏老" in d["realname"]
            else:
                r.json()["data"]["list"] is None

    @allure.severity(P2)
    @allure.title("余额提现审批列表: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_04_mgmt_fin_wallet_getWithdrawList(self, companyCode):
        
        data = deepcopy(self.data)   
        data["companyCode"] = companyCode              
        with _mgmt_fin_wallet_getWithdrawList(data, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert d["companyNo"] == data["companyCode"]
 
    @allure.severity(P2)
    @allure.title("余额提现审批列表: 查询申请提现时间检查")
    def test_05_mgmt_fin_wallet_getWithdrawList(self):
        
        data = deepcopy(self.data)   
        data["applyEndTime"] = "2022-03-24 23:59:59"  
        data["applyStartTime"] = "2022-03-24 00:00:00"             
        with _mgmt_fin_wallet_getWithdrawList(data, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert d["applyTimeDesc"][:10] == "2022-03-24"
 
 