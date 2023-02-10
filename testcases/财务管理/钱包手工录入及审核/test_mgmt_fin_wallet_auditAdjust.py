# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import data, _mgmt_fin_wallet_applyAdjust
from api.mall_mgmt_application._mgmt_fin_wallet_getList import data as data02, _mgmt_fin_wallet_getList
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import data as data03, _mgmt_fin_wallet_getAdjustList
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import params, _mgmt_fin_wallet_getAdjustDetail
from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust
from setting import P1, P2, P3, username, mobile
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/auditAdjust")
class TestClass:
    """
    手工录入款项审核-审核
    /mgmt/fin/wallet/auditAdjust
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.params = deepcopy(params)
        
        self.access_token = os.environ["access_token_2"]
      
    @allure.severity(P1)
    @allure.title("手工录入款项审核-审核: 审核-还欠款申请检查")
    def test_01_mgmt_fin_wallet_auditAdjust(self,login_oauth_token):
        
        wallet = None
        walletAdjustId = None
        getAdjustDetail = None
        
        @allure.step("钱包手工录入列表: 查询会员卡号,获取钱包id")
        def step_mgmt_fin_wallet_getList():
            
            nonlocal wallet
            data = deepcopy(self.data02)
            data["cardNo"] = login_oauth_token["cardNo"]                  
            with _mgmt_fin_wallet_getList(data, self.access_token) as r:
                wallet = r.json()["data"]["list"][0]
                assert r.json()["data"]["list"][0]["cardNo"] == login_oauth_token["cardNo"]
                
        @allure.step("手工录入流水-还欠款")
        def step_mgmt_fin_wallet_applyAdjust():
            
            data = deepcopy(self.data)
            data["walletId"] = wallet["walletId"]   
            data["companyCode"] = wallet["companyNo"] 
            data["type"] = 1
            data["adjustAmount"] = 1   
            data["adjustReason"] = "还欠款1元"           
            with _mgmt_fin_wallet_applyAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("手工录入款项审核-列表")
        def step_mgmt_fin_wallet_getAdjustList():
            
            nonlocal walletAdjustId
            data = deepcopy(self.data03)
            data["cardNo"] = login_oauth_token["cardNo"]       
            with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
                walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["adjustStatus"] == 1

        @allure.step("手工录入款项审核-详情")
        def step_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = deepcopy(self.params)
            params["id"] = walletAdjustId        
            with _mgmt_fin_wallet_getAdjustDetail(params, self.access_token) as r:
                getAdjustDetail = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("手工录入款项审核-审核")
        def step_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = "同意还欠款申请"   
            data["walletAdjustId"] = walletAdjustId    
            with _mgmt_fin_wallet_auditAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_mgmt_fin_wallet_getList()
        step_mgmt_fin_wallet_applyAdjust()
        step_mgmt_fin_wallet_getAdjustList()
        step_mgmt_fin_wallet_getAdjustDetail()
        step_mgmt_fin_wallet_auditAdjust()
        
    @allure.severity(P1)
    @allure.title("手工录入款项审核-审核: 审核-补银行流水申请检查")
    @pytest.mark.parametrize("transMethod", [201, 203, 202, 103, 101, 102], ids=["工商银行（签约卡）", "邮政储蓄银行（签约卡）", "建设银行", "银联", "微信支付", "支付宝支付"])
    def test_02_mgmt_fin_wallet_auditAdjust(self, transMethod, login_oauth_token):
        
        wallet = None
        walletAdjustId = None
        getAdjustDetail = None
        
        @allure.step("钱包手工录入列表: 查询会员卡号,获取钱包id")
        def step_mgmt_fin_wallet_getList():
            
            nonlocal wallet
            data = deepcopy(self.data02)
            data["cardNo"] = login_oauth_token["cardNo"]                
            with _mgmt_fin_wallet_getList(data, self.access_token) as r:
                wallet = r.json()["data"]["list"][0]
                assert r.json()["data"]["list"][0]["cardNo"] == login_oauth_token["cardNo"]
                
        @allure.title("手工录入流水-补银行流水")
        def step_mgmt_fin_wallet_applyAdjust():
            
            data = deepcopy(self.data)
            data["walletId"] = wallet["walletId"]   
            data["companyCode"] = wallet["companyNo"] 
            data["type"] = 2
            data["adjustAmount"] = 2   
            data["adjustReason"] = "补银行流水2元"    
            data["transMethod"] = transMethod        
            with _mgmt_fin_wallet_applyAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.title("手工录入款项审核-列表")
        def step_mgmt_fin_wallet_getAdjustList():
            
            nonlocal walletAdjustId
            data = deepcopy(self.data03)
            data["cardNo"] = login_oauth_token["cardNo"]    
            with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
                walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["adjustStatus"] == 1

        @allure.title("手工录入款项审核-详情")
        def step_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = deepcopy(self.params)
            params["id"] = walletAdjustId        
            with _mgmt_fin_wallet_getAdjustDetail(params, self.access_token) as r:
                getAdjustDetail = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("手工录入款项审核-审核")
        def step_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = "同意补银行流水申请"   
            data["walletAdjustId"] = walletAdjustId    
            with _mgmt_fin_wallet_auditAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200


        step_mgmt_fin_wallet_getList()
        step_mgmt_fin_wallet_applyAdjust()
        step_mgmt_fin_wallet_getAdjustList()
        step_mgmt_fin_wallet_getAdjustDetail()
        step_mgmt_fin_wallet_auditAdjust()       

    @allure.severity(P1)
    @allure.title("手工录入款项审核-审核: 审核-手工退款申请检查")
    def test_03_mgmt_fin_wallet_auditAdjust(self, login_oauth_token):
        
        wallet = None
        walletAdjustId = None
        getAdjustDetail = None
        
        @allure.step("钱包手工录入列表: 查询会员卡号,获取钱包id")
        def step_mgmt_fin_wallet_getList():
            
            nonlocal wallet
            data = deepcopy(self.data02)
            data["cardNo"] = login_oauth_token["cardNo"]                 
            with _mgmt_fin_wallet_getList(data, self.access_token) as r:
                wallet = r.json()["data"]["list"][0]
                assert r.json()["data"]["list"][0]["cardNo"] == login_oauth_token["cardNo"]
                
        @allure.title("手工录入流水-手工退款")
        def step_mgmt_fin_wallet_applyAdjust():
            
            data = deepcopy(self.data)
            data["walletId"] = wallet["walletId"]   
            data["companyCode"] = wallet["companyNo"] 
            data["type"] = 3
            data["adjustAmount"] = -3
            data["adjustReason"] = "手工退款-3元"           
            with _mgmt_fin_wallet_applyAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.title("手工录入款项审核-列表")
        def step_mgmt_fin_wallet_getAdjustList():
            
            nonlocal walletAdjustId
            data = deepcopy(self.data03)
            data["cardNo"] = login_oauth_token["cardNo"]  
            with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
                walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["adjustStatus"] == 1

        @allure.title("手工录入款项审核-详情")
        def step_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = deepcopy(self.params)
            params["id"] = walletAdjustId        
            with _mgmt_fin_wallet_getAdjustDetail(params, self.access_token) as r:
                getAdjustDetail = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("手工录入款项审核-审核")
        def step_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = "同意手工退款申请"   
            data["walletAdjustId"] = walletAdjustId    
            with _mgmt_fin_wallet_auditAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_mgmt_fin_wallet_getList()
        step_mgmt_fin_wallet_applyAdjust()
        step_mgmt_fin_wallet_getAdjustList()
        step_mgmt_fin_wallet_getAdjustDetail()
        step_mgmt_fin_wallet_auditAdjust()
 
    @allure.severity(P1)
    @allure.title("手工录入款项审核-审核: 审核-押货款与钱包互转申请检查")
    @pytest.mark.parametrize("adjustAmount", [4, -4])
    def test_04_mgmt_fin_wallet_auditAdjust(self, adjustAmount, login_oauth_token):
        
        wallet = None
        walletAdjustId = None
        getAdjustDetail = None
        
        @allure.step("钱包手工录入列表: 查询会员卡号,获取钱包id")
        def step_mgmt_fin_wallet_getList():
            
            nonlocal wallet
            data = deepcopy(self.data02)
            data["cardNo"] = login_oauth_token["cardNo"]             
            with _mgmt_fin_wallet_getList(data, self.access_token) as r:
                wallet = r.json()["data"]["list"][0]
                assert r.json()["data"]["list"][0]["cardNo"] == login_oauth_token["cardNo"]
                
        @allure.title("手工录入流水-押货款与钱包互转")
        def step_mgmt_fin_wallet_applyAdjust():
            
            data = deepcopy(self.data)
            data["walletId"] = wallet["walletId"]   
            data["companyCode"] = wallet["companyNo"] 
            data["type"] = 4
            data["adjustAmount"] = adjustAmount
            data["adjustReason"] = f"押货款与钱包互转{adjustAmount}元"           
            with _mgmt_fin_wallet_applyAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.title("手工录入款项审核-列表")
        def step_mgmt_fin_wallet_getAdjustList():
            
            nonlocal walletAdjustId
            data = deepcopy(self.data03)
            data["cardNo"] = login_oauth_token["cardNo"]  
            with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
                walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["adjustStatus"] == 1

        @allure.title("手工录入款项审核-详情")
        def step_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = deepcopy(self.params)
            params["id"] = walletAdjustId        
            with _mgmt_fin_wallet_getAdjustDetail(params, self.access_token) as r:
                getAdjustDetail = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("手工录入款项审核-审核")
        def step_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = "同意押货款与钱包互转申请"   
            data["walletAdjustId"] = walletAdjustId    
            with _mgmt_fin_wallet_auditAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200


        step_mgmt_fin_wallet_getList()
        step_mgmt_fin_wallet_applyAdjust()
        step_mgmt_fin_wallet_getAdjustList()
        step_mgmt_fin_wallet_getAdjustDetail()
        step_mgmt_fin_wallet_auditAdjust()
 
    @allure.severity(P1)
    @allure.title("手工录入款项审核-审核: 审核-其他申请检查")
    @pytest.mark.parametrize("adjustAmount", [5, -5])
    def test_05_mgmt_fin_wallet_auditAdjust(self, adjustAmount, login_oauth_token):
        
        wallet = None
        walletAdjustId = None
        getAdjustDetail = None
        
        @allure.step("钱包手工录入列表: 查询会员卡号,获取钱包id")
        def step_mgmt_fin_wallet_getList():
            
            nonlocal wallet
            data = deepcopy(self.data02)
            data["cardNo"] = login_oauth_token["cardNo"]            
            with _mgmt_fin_wallet_getList(data, self.access_token) as r:
                wallet = r.json()["data"]["list"][0]
                assert r.json()["data"]["list"][0]["cardNo"] == login_oauth_token["cardNo"]
                
        @allure.title("手工录入流水-其他")
        @stepreruns()
        def step_mgmt_fin_wallet_applyAdjust():
            
            data = deepcopy(self.data)
            data["walletId"] = wallet["walletId"]   
            data["companyCode"] = wallet["companyNo"] 
            data["type"] = 4
            data["adjustAmount"] = adjustAmount
            data["adjustReason"] = f"其他款{adjustAmount}元"           
            with _mgmt_fin_wallet_applyAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.title("手工录入款项审核-列表")
        def step_mgmt_fin_wallet_getAdjustList():
            
            nonlocal walletAdjustId
            data = deepcopy(self.data03)
            data["cardNo"] = login_oauth_token["cardNo"]    
            with _mgmt_fin_wallet_getAdjustList(data, self.access_token) as r:
                walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["adjustStatus"] == 1

        @allure.title("手工录入款项审核-详情")
        def step_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = deepcopy(self.params)
            params["id"] = walletAdjustId        
            with _mgmt_fin_wallet_getAdjustDetail(params, self.access_token) as r:
                getAdjustDetail = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("手工录入款项审核-审核")
        def step_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = "同意其他款申请"   
            data["walletAdjustId"] = walletAdjustId    
            with _mgmt_fin_wallet_auditAdjust(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200


        step_mgmt_fin_wallet_getList()
        step_mgmt_fin_wallet_applyAdjust()
        step_mgmt_fin_wallet_getAdjustList()
        step_mgmt_fin_wallet_getAdjustDetail()
        step_mgmt_fin_wallet_auditAdjust()
 





