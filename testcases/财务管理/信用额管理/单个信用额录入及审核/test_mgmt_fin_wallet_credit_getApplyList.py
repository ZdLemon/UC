# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import data ,_mgmt_fin_wallet_credit_getApplyList
from setting import P1, P2, P3, username, mobile, store

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/credit/getApplyList")
class TestClass:
    """
    顾客信用额列表-列表
    /mgmt/fin/wallet/credit/getApplyList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("单个信用额列表: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store, store[:6]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_01_mgmt_fin_wallet_credit_getApplyList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode                 
        with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == data["storeCode"]
            else:
                assert r.json()["data"]["list"] == []


    @allure.severity(P2)
    @allure.title("单个信用额列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username, username[:9]], ids=["正确的会员卡号", "会员卡号的一部分"])
    def test_02_mgmt_fin_wallet_credit_getApplyList(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo                    
        with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == cardNo 
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("单个信用额列表: 查询审核状态检查")
    @pytest.mark.parametrize("auditStatus", [7, 1, 2, 9], ids=["待提交", "待审核", "已通过", "不通过"])
    def test_03_mgmt_fin_wallet_credit_getApplyList(self, auditStatus):
        
        data = deepcopy(self.data)   
        data["auditStatus"] = auditStatus                   
        with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["auditStatus"] for d in r.json()["data"]["list"]):
                    assert i == auditStatus
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("单个信用额列表-成功路径: 查询生效状态检查")
    @pytest.mark.parametrize("effectStatus", [1, 2], ids=["未生效", "已生效"])
    def test_04_mgmt_fin_wallet_credit_getApplyList(self, effectStatus):
        
        data = deepcopy(self.data)   
        data["effectStatus"] = effectStatus            
        with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["effectStatus"] for d in r.json()["data"]["list"]):
                    assert i == data["effectStatus"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title(" 单个信用额列表-成功路径: 查询生效时间范围检查")
    def test_05_mgmt_fin_wallet_credit_getApplyList(self):
        
        data = deepcopy(self.data)   
        data["ffectEndTime"] = "2022-03-31 00:00:00"  
        data["effectStartTime"] = "2022-04-01 00:00:00"           
        with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["auditTime"] for d in r.json()["data"]["list"]):
                    assert time.strftime("%m", time.localtime(i/1000)) == "03"
            else:
                assert r.json()["data"]["list"] == []



