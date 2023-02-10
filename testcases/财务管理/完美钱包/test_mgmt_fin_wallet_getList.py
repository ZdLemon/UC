# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getList import data ,_mgmt_fin_wallet_getList
from api.mall_mobile_application._mobile_wallet_recharge import data as data01, _mobile_wallet_recharge
from api.mall_mgmt_application._mgmt_fin_wallet_getTransDetail import data as data02, _mgmt_fin_wallet_getTransDetail
from api.mall_mobile_application._mobile_wallet_applyWalletWithdraw import data as data03, _mobile_wallet_applyWalletWithdraw
from api.mall_mgmt_application._mgmt_fin_wallet_getWithdrawList import data as data04,_mgmt_fin_wallet_getWithdrawList
from api.mall_mgmt_application._mgmt_fin_wallet_auditTransferWithdraw import data as data05, _mgmt_fin_wallet_auditTransferWithdraw
from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay
from api.mall_mobile_application._mobile_product_getProductDetail import params, _mobile_product_getProductDetail
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit
from api.mall_mobile_application._mobile_order_return_applyReturn import data as data06, _mobile_order_return_applyReturn
from api.mall_mobile_application._mobile_wallet_getBankCardInfo import _mobile_wallet_getBankCardInfo
from api.mall_mobile_application._mobile_payment_getPayMethod import data as data13, _mobile_payment_getPayMethod

from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import data as data07,_mgmt_fin_wallet_credit_getApplyList
from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import data as data08, _mgmt_fin_wallet_credit_addApply
from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import data as data09, _mgmt_fin_wallet_credit_auditApply

from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import data as data10, _mgmt_fin_wallet_applyAdjust
from api.mall_mgmt_application._mgmt_fin_wallet_getList import data as data11, _mgmt_fin_wallet_getList
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import data as data12, _mgmt_fin_wallet_getAdjustList
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import params as params02, _mgmt_fin_wallet_getAdjustDetail
from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust
from util.stepreruns import stepreruns
from setting import P1, P2, P3, username, mobile, username_vip

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/getList")
class TestClass:
    """
    完美钱包管理-列表:搜索检查
    /mgmt/fin/wallet/getList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("完美钱包管理列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username, username[:9]], ids=["正确的会员卡号", "会员卡号的一部分"])
    def test_01_mgmt_fin_wallet_getList(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo                    
        with _mgmt_fin_wallet_getList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                assert r.json()["data"]["list"][0]["cardNo"] == username
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("完美钱包管理列表: 仅支持精确查询普客手机号码检查")
    @pytest.mark.parametrize("mobile", [mobile, mobile[:11]], ids=["正确的普客手机号", "普客手机号的一部分"])
    def test_02_mgmt_fin_wallet_getList(self, mobile):
        
        data = deepcopy(self.data)   
        data["mobile"] = mobile                   
        with _mgmt_fin_wallet_getList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                 assert r.json()["data"]["list"][0]["mobile"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("完美钱包管理列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_fin_wallet_getList(self, companyCode):
        
        data = deepcopy(self.data)   
        data["companyCode"] = companyCode            
        with _mgmt_fin_wallet_getList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyNo"] for d in r.json()["data"]["list"]):
                    assert i == data["companyCode"]
            else:
                assert r.json()["data"]["list"] == []       

    @allure.severity(P2)
    @allure.title("完美钱包管理列表-成功路径: 支持多选查询顾客类型检查")
    @pytest.mark.parametrize("cardType", [[1], [2], [3], [4], [1, 2], [1, 2, 3], [1, 2, 3, 4]])
    def test_04_mgmt_fin_wallet_getList(self, cardType):
        
        data = deepcopy(self.data)   
        data["cardTypeList"].extend(cardType)             
        with _mgmt_fin_wallet_getList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["cardType"] for d in r.json()["data"]["list"]):
                    assert i in data["cardTypeList"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("完美钱包管理列表-成功路径: 查询是否有信用额检查")
    @pytest.mark.parametrize("creditEnable", [True, False], ids=["是", "否"])
    def test_05_mgmt_fin_wallet_getList(self, creditEnable):
        
        data = deepcopy(self.data)   
        data["creditEnable"] = creditEnable                 
        with _mgmt_fin_wallet_getList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["creditEnable"] for d in r.json()["data"]["list"]):
                    assert i == data["creditEnable"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("完美钱包管理列表-成功路径: 查询实际结余为负检查")
    @pytest.mark.parametrize("negativeEnable", [True, False], ids=["是", "否"])
    def test_06_mgmt_fin_wallet_getList(self, negativeEnable):
        
        data = deepcopy(self.data)   
        data["negativeEnable"] = negativeEnable                    
        with _mgmt_fin_wallet_getList(data, self.access_token) as r:
            if negativeEnable:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["thisBigWalletBalanceAmt"] < 0
                else:
                    assert r.json()["data"]["list"] == []
            else:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["thisBigWalletBalanceAmt"] >= 0
                else:
                    assert r.json()["data"]["list"] == []
