# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import data ,_mgmt_fin_wallet_getAdjustList
from setting import P1, P2, P3, username, mobile

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/getAdjustList")
class TestClass:
    """
    手工录入款项审核-列表
    /mgmt/fin/wallet/getAdjustList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("手工录入款项审核列表: 查询录入月份检查")
    def test_01_mgmt_fin_wallet_getAdjustList(self):
        
        data = deepcopy(self.data)
        data["adjustMonth"] = time.strftime('%Y-%m',time.localtime(time.time()))                   
        with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["entryTimeDesc"][:7] for d in r.json()["data"]["list"]):
                    assert i == data["adjustMonth"] 
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("手工录入款项审核列表: 仅支持精确查询普客手机号码检查")
    @pytest.mark.parametrize("mobile", [mobile, mobile[:11]], ids=["正确的普客手机号", "普客手机号的一部分"])
    def test_02_mgmt_fin_wallet_getAdjustList(self, mobile):
        
        data = deepcopy(self.data)   
        data["mobile"] = mobile                   
        with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                 assert r.json()["data"]["list"][0]["mobile"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("手工录入款项审核列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username, username[:9]], ids=["正确的会员卡号", "会员卡号的一部分"])
    def test_03_mgmt_fin_wallet_getAdjustList(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo                    
        with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                assert r.json()["data"]["list"][0]["cardNo"] == username
            else:
                assert r.json()["data"]["list"] == None


    @allure.severity(P2)
    @allure.title("手工录入款项审核列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_04_mgmt_fin_wallet_getAdjustList(self, companyCode):
        
        data = deepcopy(self.data)   
        data["companyCode"] = companyCode            
        with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyNo"] for d in r.json()["data"]["list"]):
                    assert i == data["companyCode"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("手工录入款项审核列表-成功路径: 查询审核状态检查")
    @pytest.mark.parametrize("adjustStatus", [1, 2, 3, 6], ids=["待审核", "已通过", "已驳回", "已撤回"])
    def test_05_mgmt_fin_wallet_getAdjustList(self, adjustStatus):
        
        data = deepcopy(self.data)   
        data["adjustStatus"] = adjustStatus # 审批状态：1：待审核；2：已通过；3：已驳回，6：已撤回           
        with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["adjustStatus"] for d in r.json()["data"]["list"]):
                    assert i == adjustStatus
            else:
                assert r.json()["data"]["list"] == []






