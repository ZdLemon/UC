# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans import data ,_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans
from setting import P1, P2, P3, username, mobile

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/bill/queryFinWalletCompanyAccountTrans")
class TestClass:
    """
    查询分公司银行流水(商城后台)
    /mgmt/fin/wallet/bill/queryFinWalletCompanyAccountTrans
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("查询分公司银行流水列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username, username[:9]], ids=["正确的会员卡号", "会员卡号的一部分"])
    def test_01_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo               
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, self.access_token) as r:
            if r.json()["data"]["billTransDtlPage"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["billTransDtlPage"]["list"]):
                    assert i == data["cardNo"]               
            else:
                assert r.json()["data"]["billTransDtlPage"]["list"] == []

    @allure.severity(P2)
    @allure.title("查询分公司银行流水列表: 仅支持精确查询普客手机号码检查")
    @pytest.mark.parametrize("mobile", [mobile, mobile[:11]], ids=["正确的普客手机号", "普客手机号的一部分"])
    def test_02_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(self, mobile):
        
        data = deepcopy(self.data)   
        data["mobile"] = mobile                   
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, self.access_token) as r:
            if r.json()["data"]["billTransDtlPage"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["billTransDtlPage"]["list"]):
                    assert i == data["mobile"]                
            else:
                assert r.json()["data"]["billTransDtlPage"]["list"] == []

    @allure.severity(P2)
    @allure.title("查询分公司银行流水列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(self, companyCode):
        
        data = deepcopy(self.data)   
        data["companyCode"] = companyCode            
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, self.access_token) as r:
            if r.json()["data"]["billTransDtlPage"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["billTransDtlPage"]["list"]):
                    assert i == data["companyCode"]                
            else:
                assert r.json()["data"]["billTransDtlPage"]["list"] == []     

    @allure.severity(P2)
    @allure.title("查询分公司银行流水列表-成功路径: 支持多选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [[1], [2], [3], [4], [1, 2], [1, 2, 3], [1, 2, 3, 4]])
    def test_04_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(self, memberType):
        
        data = deepcopy(self.data)   
        data["memberTypeList"].extend(memberType)             
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, self.access_token) as r:
            if r.json()["data"]["billTransDtlPage"]["list"]:
                for i in set(d["memberType"] for d in r.json()["data"]["billTransDtlPage"]["list"]):
                    assert i in data["memberTypeList"]
            else:
                assert r.json()["data"]["billTransDtlPage"]["list"] == []

    @allure.severity(P2)
    @allure.title("查询分公司银行流水列表-成功路径: 查询账款类型检查")
    @pytest.mark.parametrize("transType", [1, 2, 6, 7, 9, 10, 11, 12, 13, 16], ids=["充值", "购货转入", "提现", "原路退款", "还欠款", "补银行流水", "手工退款", "押货款与钱包互转", "其他", "定金转入"])
    def test_05_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(self, transType):
        
        data = deepcopy(self.data)   
        data["transType"] = transType                 
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, self.access_token) as r:
            if r.json()["data"]["billTransDtlPage"]["list"]:
                for i in set(d["transType"] for d in r.json()["data"]["billTransDtlPage"]["list"]):
                    assert i == data["transType"]
            else:
                assert r.json()["data"]["billTransDtlPage"]["list"] == []

    @allure.severity(P2)
    @allure.title("查询分公司银行流水列表-成功路径: 查询自动手工检查")
    @pytest.mark.parametrize("autoType", [1, 2], ids=["自动", "手工"])
    def test_06_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(self, autoType):
        
        data = deepcopy(self.data)   
        data["autoType"] = autoType               
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, self.access_token) as r:
            if r.json()["data"]["billTransDtlPage"]["list"]:
                for i in set(d["transType"] for d in r.json()["data"]["billTransDtlPage"]["list"]):
                    if autoType == 1:
                        assert i in [1, 2, 6, 7, 16]
                    elif autoType == 2:
                        assert i in [9, 10, 11, 12, 13]
            else:
                assert r.json()["data"]["billTransDtlPage"]["list"] == []
