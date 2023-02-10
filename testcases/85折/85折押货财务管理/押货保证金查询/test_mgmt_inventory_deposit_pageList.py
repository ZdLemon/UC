# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_deposit_pageList import data, _mgmt_inventory_deposit_pageList

from api.mall_center_sys._mgmt_sys_getAccountList import params, _mgmt_sys_getAccountList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data as data03, _mgmt_inventory_disManualInputRemit_add
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify
from api.mall_mgmt_application._mgmt_inventory_deposit_storeDepositDetail import data as data04, _mgmt_inventory_deposit_storeDepositDetail

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_audit import data as data05, _mgmt_inventory_dis_mortgage_order_audit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import params as params06, _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import _mgmt_inventory_dis_mortgage_order_mortgage
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import params as params07, _mgmt_inventory_dis_mortgage_order_searchProductPage

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detailForModify_id import _mgmt_inventory_dis_mortgage_order_detailForModify_id
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_modify import data as data06, _mgmt_inventory_dis_mortgage_order_modify

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_stopDeliver import params as params08, _mgmt_inventory_dis_mortgage_order_stopDeliver
from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo

from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params as params09, _appStore_store_dis_mortgageOrder_searchProductPage
from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data as data07, _appStore_store_dis_mortgageOrder_pushProductsToCart
from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data08, _appStore_store_dis_mortgageOrder_mortgage
from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data09, _appStore_store_dis_mortgageOrder_prePayCheck
from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params10, _appStore_store_dis_mortgageOrder_detail_id
from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
from api.mall_store_application._appStore_store_deposit_msg import params as params11, _appStore_store_deposit_msg

from api.mall_store_application._appStore_store_getSignBankAccountList import params as params12, _appStore_store_getSignBankAccountList
from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
import uuid


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/pageList")
class TestClass:
    """
    85折账款管理-押货保证金分页查询列表
    /mgmt/inventory/deposit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_01_mgmt_inventory_deposit_pageList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode                
        with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []
               
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 仅支持精确查询负责人卡号检查")
    @pytest.mark.parametrize("leaderNo", [username_85, username_85[:-1]], ids=["正确的负责人卡号", "负责人卡号的一部分"])
    def test_02_mgmt_inventory_deposit_pageList(self, leaderNo):
        
        data = deepcopy(self.data)
        data["leaderNo"] = leaderNo                      
        with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["leaderNo"] for d in r.json()["data"]["list"]):
                    assert i == leaderNo
            else:
                assert r.json()["data"]["list"] == []
        
    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 支持模糊查询负责人检查")
    @pytest.mark.parametrize("leaderName", [name_85, name_85[:-1]], ids=["正确的负责人", "负责人的一部分"])
    def test_03_mgmt_inventory_deposit_pageList(self, leaderName):
        
        data = deepcopy(self.data)
        data["leaderName"] = leaderName                      
        with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:           
            for i in set(d["leaderName"] for d in r.json()["data"]["list"]):
                assert leaderName in i

    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_04_mgmt_inventory_deposit_pageList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode                       
        with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert data["companyCode"] == i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折押货保证金分页查询列表: 下拉选项查询可用结余为负检查")
    @pytest.mark.parametrize("moneyType", [0, 1], ids=["是", "否"])
    def test_05_mgmt_inventory_deposit_pageList(self, moneyType):
        
        data = deepcopy(self.data)
        data["moneyType"] = moneyType                     
        with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
            if moneyType == 0:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["balance"] < 0
                else:
                    assert r.json()["data"]["list"] == []
            
            elif moneyType == 1:
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["balance"] >= 0
                else:
                    assert r.json()["data"]["list"] == []
       

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/pageList")
@pytest.mark.skip()
class TestClass02:
    """
    完美运营后台：手工录入款
    85折账款管理-押货保证金分页查询列表
    /mgmt/inventory/deposit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.params05 = deepcopy(params05)
        self.data03 = deepcopy(data03)
        self.data02 = deepcopy(data02)
        self.data04 = deepcopy(data04)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("手工录入其他款: 押货保证金流水检查")
    @pytest.mark.parametrize("remitMoney", [2, -1], ids=["2元", "-1元"])
    def test_01_mgmt_inventory_deposit_pageList(self, remitMoney):
        
        pageList = None # 押货保证金信息
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        
        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                   
        @allure.step("根据服务中心编号获取服务中心信息")
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                getStoreByCode = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询分公司银行账号")
        def step_mgmt_sys_getAccountList():
            
            nonlocal getAccountList
            params = deepcopy(self.params)
            params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
            with _mgmt_sys_getAccountList(params, self.access_token) as r:
                getAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("通过storeCode获取银行账户资料信息")
        def step_mgmt_store_getBankAccountList():
            
            nonlocal getBankAccountList
            params = deepcopy(self.params04)
            params["storeCode"] = getStoreByCode["store"]["code"]               
            with _mgmt_store_getBankAccountList(params, self.access_token) as r:
                getBankAccountList = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("1:3押货余额及85折保证金余额查询")
        def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
            
            nonlocal getStoreWalletMsg
            params = deepcopy(self.params02)
            params["storeCode"] = getStoreByCode["store"]["code"]                  
            with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, self.access_token) as r:
                getStoreWalletMsg = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("85折手工录入流水")
        def step_mgmt_inventory_disManualInputRemit_add(): 
                 
            data = deepcopy(self.data03)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["storeName"] = getStoreByCode["store"]["name"]
            data["companyCode"] = getStoreByCode["store"]["companyCode"]
            data["companyName"] = getAccountList[0]["accountName"]
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["changeReason"] = "其他"
            if remitMoney > 0: # 服务中心付款
                data["payAccount"] = getBankAccountList[0]["account"]
                data["payAccountBankName"] = getBankAccountList[0]["branch"]
                data["receiptAccount"] = getAccountList[0]["account"]
                data["receiptBankName"] = getAccountList[0]["bankType"]
            elif remitMoney < 0: # 分公司付款
                data["payAccount"] = getAccountList[0]["account"]
                data["payAccountBankName"] = getAccountList[0]["bankType"]
                data["receiptAccount"] = getBankAccountList[0]["account"]
                data["receiptBankName"] = getBankAccountList[0]["branch"]
            data["remitMoney"] = remitMoney
            data["sourceType"] = 3 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
            data["inputRemark"] = f"录入其他款 {remitMoney}元"              
            with _mgmt_inventory_disManualInputRemit_add(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("85折手工录入流水分页搜索列表,获取id")
        def step_mgmt_inventory_disManualInputRemit_pageList():
            
            nonlocal id
            data = deepcopy(self.data02)
            data["storeCode"] = getStoreByCode["store"]["code"] 
            data["verifyStatus"] = 0 # 待审核列表             
            with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
                id = r.json()["data"]["list"][0]["id"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("85折手工录入流水单个审核")
        def step_mgmt_inventory_disManualInputRemit_verify():
            
            params = deepcopy(self.params05)
            params["id"] = id
            params["verifyRemark"] = f"同意录入其它款 {remitMoney}元" # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("手工录入其他款后: 押货保证金明细检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = getStoreByCode["store"]["code"]            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + remitMoney
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"]
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] + remitMoney

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "其他" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 3 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "其他" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == f"同意录入其它款 {remitMoney}元" # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
                
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()
    
    @allure.severity(P1)
    @allure.title("手工录入增加押货款: 押货保证金流水检查")
    def test_02_mgmt_inventory_deposit_pageList(self):
        
        pageList = None # 押货保证金信息
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        remitMoney = 4 # 金额
        
        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                   
        @allure.step("根据服务中心编号获取服务中心信息")
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                getStoreByCode = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询分公司银行账号")
        def step_mgmt_sys_getAccountList():
            
            nonlocal getAccountList
            params = deepcopy(self.params)
            params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
            with _mgmt_sys_getAccountList(params, self.access_token) as r:
                getAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("通过storeCode获取银行账户资料信息")
        def step_mgmt_store_getBankAccountList():
            
            nonlocal getBankAccountList
            params = deepcopy(self.params04)
            params["storeCode"] = getStoreByCode["store"]["code"]               
            with _mgmt_store_getBankAccountList(params, self.access_token) as r:
                getBankAccountList = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("1:3押货余额及85折保证金余额查询")
        def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
            
            nonlocal getStoreWalletMsg
            params = deepcopy(self.params02)
            params["storeCode"] = getStoreByCode["store"]["code"]                  
            with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, self.access_token) as r:
                getStoreWalletMsg = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("85折手工录入流水")
        def step_mgmt_inventory_disManualInputRemit_add(): 
                 
            data = deepcopy(self.data03)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["storeName"] = getStoreByCode["store"]["name"]
            data["companyCode"] = getStoreByCode["store"]["companyCode"]
            data["companyName"] = getAccountList[0]["accountName"]
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["changeReason"] = "汇押货款"
            data["payAccount"] = getBankAccountList[0]["account"] # 服务中心付款
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"] # 分公司收款
            data["receiptBankName"] = getAccountList[0]["bankType"]
            data["remitMoney"] = remitMoney
            data["sourceType"] = 7 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
            data["inputRemark"] = f"录入手动增加押货款 {remitMoney}元"              
            with _mgmt_inventory_disManualInputRemit_add(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("85折手工录入流水分页搜索列表,获取id")
        def step_mgmt_inventory_disManualInputRemit_pageList():
            
            nonlocal id
            data = deepcopy(self.data02)
            data["storeCode"] = getStoreByCode["store"]["code"] 
            data["verifyStatus"] = 0 # 待审核列表             
            with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
                id = r.json()["data"]["list"][0]["id"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("85折手工录入流水单个审核")
        def step_mgmt_inventory_disManualInputRemit_verify():
            
            params = deepcopy(self.params05)
            params["id"] = id
            params["verifyRemark"] = f"同意录入手动增加押货款 {remitMoney}元" # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("手工录入其他款后: 押货保证金明细检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = getStoreByCode["store"]["code"]            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + remitMoney
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"]
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] + remitMoney

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 7 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "手工增加押货款" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == f"同意录入手动增加押货款 {remitMoney}元" # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
                
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()
     
    @allure.severity(P1)
    @allure.title("手工录入退押货款: 押货保证金流水检查")
    def test_03_mgmt_inventory_deposit_pageList(self):
        
        pageList = None # 押货保证金信息
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        remitMoney = -2 # 金额
        
        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                   
        @allure.step("根据服务中心编号获取服务中心信息")
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                getStoreByCode = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询分公司银行账号")
        def step_mgmt_sys_getAccountList():
            
            nonlocal getAccountList
            params = deepcopy(self.params)
            params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
            with _mgmt_sys_getAccountList(params, self.access_token) as r:
                getAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("通过storeCode获取银行账户资料信息")
        def step_mgmt_store_getBankAccountList():
            
            nonlocal getBankAccountList
            params = deepcopy(self.params04)
            params["storeCode"] = getStoreByCode["store"]["code"]               
            with _mgmt_store_getBankAccountList(params, self.access_token) as r:
                getBankAccountList = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("1:3押货余额及85折保证金余额查询")
        def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
            
            nonlocal getStoreWalletMsg
            params = deepcopy(self.params02)
            params["storeCode"] = getStoreByCode["store"]["code"]                  
            with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, self.access_token) as r:
                getStoreWalletMsg = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("85折手工录入流水")
        def step_mgmt_inventory_disManualInputRemit_add(): 
                 
            data = deepcopy(self.data03)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["storeName"] = getStoreByCode["store"]["name"]
            data["companyCode"] = getStoreByCode["store"]["companyCode"]
            data["companyName"] = getAccountList[0]["accountName"]
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["changeReason"] = "退押货款"
            data["payAccount"] = getAccountList[0]["account"] # 分公司付款
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"] # 服务中心收款
            data["receiptBankName"] = getBankAccountList[0]["branch"]
            data["remitMoney"] = remitMoney
            data["sourceType"] = 8 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
            data["inputRemark"] = f"录入手动退押货款 {remitMoney}元"                
            with _mgmt_inventory_disManualInputRemit_add(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("85折手工录入流水分页搜索列表,获取id")
        def step_mgmt_inventory_disManualInputRemit_pageList():
            
            nonlocal id
            data = deepcopy(self.data02)
            data["storeCode"] = getStoreByCode["store"]["code"] 
            data["verifyStatus"] = 0 # 待审核列表             
            with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
                id = r.json()["data"]["list"][0]["id"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("85折手工录入流水单个审核")
        def step_mgmt_inventory_disManualInputRemit_verify():
            
            params = deepcopy(self.params05)
            params["id"] = id
            params["verifyRemark"] = f"同意录入手动退押货款 {remitMoney}元" # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("手工录入其他款后: 押货保证金明细检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = getStoreByCode["store"]["code"]            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + remitMoney
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"]
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] + remitMoney

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "退押货款" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 8 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "手工退押货款" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == f"同意录入手动退押货款 {remitMoney}元" # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
                
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()
    
    @allure.severity(P1)
    @allure.title("手工录入押货保证金转移: 押货保证金流水检查")
    def test_04_mgmt_inventory_deposit_pageList(self):
        
        pageList = None # 押货保证金信息
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        remitMoney = 1 # 金额
        
        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                   
        @allure.step("根据服务中心编号获取服务中心信息")
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                getStoreByCode = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询分公司银行账号")
        def step_mgmt_sys_getAccountList():
            
            nonlocal getAccountList
            params = deepcopy(self.params)
            params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
            with _mgmt_sys_getAccountList(params, self.access_token) as r:
                getAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("通过storeCode获取银行账户资料信息")
        def step_mgmt_store_getBankAccountList():
            
            nonlocal getBankAccountList
            params = deepcopy(self.params04)
            params["storeCode"] = getStoreByCode["store"]["code"]               
            with _mgmt_store_getBankAccountList(params, self.access_token) as r:
                getBankAccountList = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("1:3押货余额及85折保证金余额查询")
        def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
            
            nonlocal getStoreWalletMsg
            params = deepcopy(self.params02)
            params["storeCode"] = getStoreByCode["store"]["code"]                  
            with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, self.access_token) as r:
                getStoreWalletMsg = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("85折手工录入流水")
        def step_mgmt_inventory_disManualInputRemit_add(): 
                 
            data = deepcopy(self.data03)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["storeName"] = getStoreByCode["store"]["name"]
            data["companyCode"] = getStoreByCode["store"]["companyCode"]
            data["companyName"] = getAccountList[0]["accountName"]
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["changeReason"] = "汇押货款"
            data["payAccount"] = getBankAccountList[0]["account"] # 服务中心付款
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"] # 分公司收款
            data["receiptBankName"] = getAccountList[0]["bankType"]
            data["remitMoney"] = remitMoney
            data["sourceType"] = 9 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
            data["inputRemark"] = f"录入保证金转移 {remitMoney}元"         
            with _mgmt_inventory_disManualInputRemit_add(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("85折手工录入流水分页搜索列表,获取id")
        def step_mgmt_inventory_disManualInputRemit_pageList():
            
            nonlocal id
            data = deepcopy(self.data02)
            data["storeCode"] = getStoreByCode["store"]["code"] 
            data["verifyStatus"] = 0 # 待审核列表             
            with _mgmt_inventory_disManualInputRemit_pageList(data, self.access_token) as r:
                id = r.json()["data"]["list"][0]["id"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("85折手工录入流水单个审核")
        def step_mgmt_inventory_disManualInputRemit_verify():
            
            params = deepcopy(self.params05)
            params["id"] = id
            params["verifyRemark"] = f"同意录入保证金转移 {remitMoney}元" # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("手工录入其他款后: 押货保证金明细检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = getStoreByCode["store"]["code"]            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + remitMoney
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"]
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] + remitMoney

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = getStoreByCode["store"]["code"]
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货保证金转移" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 9 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "押货保证金转移" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == f"同意录入保证金转移 {remitMoney}元" # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] =="无" # 关联单号
                
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()
    
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/pageList")
@pytest.mark.skip()
class TestClass03:
    """
    完美运营后台：新建押货单，修改押货单，欠货不发
    85折账款管理-押货保证金分页查询列表
    /mgmt/inventory/deposit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params06 = deepcopy(params06)
        self.params07 = deepcopy(params07)
        self.params08 = deepcopy(params08)
        self.data04 = deepcopy(data04)
        self.data05 = deepcopy(data05)
        self.data06 = deepcopy(data06)

        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("完美运营后台下押货单: 押货保证金流水检查")
    def test_01_mgmt_inventory_deposit_pageList(self):
        
        pageList = None # 押货保证金信息
        orderId = None # 押货单id
        searchProductPage = None, # 商品信息
        checkIsAuditAmountOverLimit = True # 是否超出库存限额
        orderSn = None # 押货单号
        
        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
        
        @allure.title("关键字搜索可押货商品")
        def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params07)
            params["storeCode"] = store_85
            params["keyword"] = productCode              
            with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break                
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                   
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = {
                "storeCode": store_85, 
                "isDelivery": 1, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": 2 # 押货商品数量
                }],
                "transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
            }
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                orderId = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询押货单是否超出库存限额")
        def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
            
            nonlocal checkIsAuditAmountOverLimit
            params = deepcopy(self.params06)
            params["orderId"] = orderId               
            with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, self.access_token) as r:
                checkIsAuditAmountOverLimit = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("审核通过押货单")
        def step_mgmt_inventory_dis_mortgage_order_audit():
            data = deepcopy(self.data05)
            data["orderId"] = orderId 
            data["auditRemarks"] = "同意押货单申请"
            data["auditResult"] = 1 # 审批结果 0不通过 1通过
            with _mgmt_inventory_dis_mortgage_order_audit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情，获取押货单编号")
        def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
            
            nonlocal orderSn
            params = {"id": orderId}           
            with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, self.access_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 2, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"
               
        @allure.step("押货单审核通过后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"]
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] - searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] - searchProductPage["mortgagePrice"] * 2

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
                
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_dis_mortgage_order_searchProductPage()
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
        step_mgmt_inventory_dis_mortgage_order_audit()
        step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()

    @allure.severity(P1)
    @allure.title("完美运营后台修改押货单: 押货保证金流水检查")
    def test_02_mgmt_inventory_deposit_pageList(self):
        
        pageList = None # 押货保证金信息
        orderId = None # 押货单id
        searchProductPage = None, # 商品信息
        checkIsAuditAmountOverLimit = True # 是否超出库存限额
        orderSn = None # 押货单号
       
        @allure.title("关键字搜索可押货商品")
        def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params07)
            params["storeCode"] = store_85
            params["keyword"] = productCode              
            with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break 
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                   
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = {
                "storeCode": store_85, 
                "isDelivery": 1, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": 2 # 押货商品数量
                }],
                "transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
            }
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                orderId = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询押货单是否超出库存限额")
        def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
            
            nonlocal checkIsAuditAmountOverLimit
            params = deepcopy(self.params06)
            params["orderId"] = orderId               
            with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, self.access_token) as r:
                checkIsAuditAmountOverLimit = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("审核通过押货单")
        def step_mgmt_inventory_dis_mortgage_order_audit():
            data = deepcopy(self.data05)
            data["orderId"] = orderId 
            data["auditRemarks"] = "同意押货单申请"
            data["auditResult"] = 1 # 审批结果 0不通过 1通过
            with _mgmt_inventory_dis_mortgage_order_audit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
 
        @allure.step("押货单详情，获取压货单编号")
        def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
            
            nonlocal orderSn
            params = {"id": orderId}           
            with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, self.access_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("押货单修改")
        def step_mgmt_inventory_dis_mortgage_order_modify():
            
            data = deepcopy(data06)
            data["orderSn"] = orderSn # 押货单号
            data["productList"][0]["mortgageNum"] = 1 # 商品数量(减一半)
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"] # 商品押货价
            data["productList"][0]["productCode"] = searchProductPage["productCode"] # 商品编码
            with _mgmt_inventory_dis_mortgage_order_modify(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 1, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"
        
        @allure.step("押货单修改后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"]
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] + searchProductPage["mortgagePrice"]
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] + searchProductPage["mortgagePrice"]

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == searchProductPage["mortgagePrice"] # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == "押货调整" # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
                
        step_mgmt_inventory_dis_mortgage_order_searchProductPage()
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
        step_mgmt_inventory_dis_mortgage_order_audit()
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
        step_mgmt_inventory_dis_mortgage_order_modify()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()

    @allure.severity(P1)
    @allure.title("完美运营后台欠货不发: 押货保证金流水检查")
    def test_03_mgmt_inventory_deposit_pageList(self):
        
        pageList = None # 押货保证金信息
        orderId = None # 押货单id
        searchProductPage = None, # 商品信息
        checkIsAuditAmountOverLimit = True # 是否超出库存限额
        orderSn = None # 押货单号
        returnOrderSn = None # 退押货单号
       
        @allure.title("关键字搜索可押货商品")
        def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params07)
            params["storeCode"] = store_85
            params["keyword"] = productCode              
            with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break 
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                   
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = {
                "storeCode": store_85, 
                "isDelivery": 1, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": 2 # 押货商品数量
                }],
                "transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
            }
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                orderId = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询押货单是否超出库存限额")
        def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
            
            nonlocal checkIsAuditAmountOverLimit
            params = deepcopy(self.params06)
            params["orderId"] = orderId               
            with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, self.access_token) as r:
                checkIsAuditAmountOverLimit = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("审核通过押货单")
        def step_mgmt_inventory_dis_mortgage_order_audit():
            data = deepcopy(self.data05)
            data["orderId"] = orderId 
            data["auditRemarks"] = "同意押货单申请"
            data["auditResult"] = 1 # 审批结果 0不通过 1通过
            with _mgmt_inventory_dis_mortgage_order_audit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
 
        @allure.step("押货单详情，获取压货单编号")
        def step_01_mgmt_inventory_dis_mortgage_order_detailForModify_id():
            
            nonlocal orderSn
            params = {"id": orderId}           
            with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, self.access_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("押货单修改")
        def step_mgmt_inventory_dis_mortgage_order_modify():
            
            data = deepcopy(data06)
            data["orderSn"] = orderSn # 押货单号
            data["productList"][0]["mortgageNum"] = 1 # 商品数量(减一半)
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"] # 商品押货价
            data["productList"][0]["productCode"] = searchProductPage["productCode"] # 商品编码
            with _mgmt_inventory_dis_mortgage_order_modify(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

        @allure.step("押货单欠货不发")
        def step_mgmt_inventory_dis_mortgage_order_stopDeliver():
            
            params = deepcopy(params08)
            params["orderSn"] = orderSn # 押货单号
            with _mgmt_inventory_dis_mortgage_order_stopDeliver(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情，获取退押货单号")
        def step_02_mgmt_inventory_dis_mortgage_order_detailForModify_id():
            
            nonlocal returnOrderSn
            params = {"id": orderId}           
            with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, self.access_token) as r:
                returnOrderSn = r.json()["data"]["returnOrderSn"]
                assert r.status_code == 200
                assert r.json()["code"] == 200
       
        @allure.step("押货单欠货不发后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"]
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] + searchProductPage["mortgagePrice"]
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] + searchProductPage["mortgagePrice"]

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货退货" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 5 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == searchProductPage["mortgagePrice"] # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == returnOrderSn # 关联单号
                
        step_mgmt_inventory_dis_mortgage_order_searchProductPage()
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
        step_mgmt_inventory_dis_mortgage_order_audit()
        step_01_mgmt_inventory_dis_mortgage_order_detailForModify_id()
        step_mgmt_inventory_dis_mortgage_order_modify()
        step_01_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_dis_mortgage_order_stopDeliver()
        step_02_mgmt_inventory_dis_mortgage_order_detailForModify_id()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/pageList")
@pytest.mark.skip()
class TestClass04:
    """
    店铺运营后台：新建押货单
    85折账款管理-押货保证金分页查询列表
    /mgmt/inventory/deposit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data04 = deepcopy(data04)
        self.params09 = deepcopy(params09)
        self.params10 = deepcopy(params10)
        self.params11 = deepcopy(params11)
        self.params12 = deepcopy(params12)
        self.data07 = deepcopy(data07)
        self.data08 = deepcopy(data08)
        self.data09 = deepcopy(data09)

        self.store_token = os.environ["store_token_85"]
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("店铺运营后台下押货单: 保证金支付流水检查")
    def test_01_mgmt_inventory_deposit_pageList(self, login_store, inventory_add_1000):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        payAmount = None # 押货单金额
        balance = None # 保证金余额
        orderSn = None # 押货单号
        pageList = None # 押货保证金信息
                
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params09) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data07) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货下单, 获取押货单Id")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data08)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情, 获取押货单金额")
        def step_01_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal payAmount
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                payAmount = r.json()["data"]["payAmount"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取服务中心可用押货保证金余额")
        def step_appStore_store_deposit_msg():
            
            nonlocal balance
            params = deepcopy(self.params11)
            params["storeCode"] = store_85
            with _appStore_store_deposit_msg(params, self.store_token) as r:
                balance = r.json()["data"]["balance"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                  
        @allure.step("押货单支付前的金额校验")
        def step_appStore_store_dis_mortgageOrder_prePayCheck():
            
            data = deepcopy(self.data09)
            data["orderId"] = id
            data["oweDepositAmount"] = 0
            data["payAmount"] = payAmount
            with _appStore_store_dis_mortgageOrder_prePayCheck(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
        @allure.step("押货单支付")
        def step_appStore_api_wallet_pay():
            
            data = {
                "accountName": "", # 户名(仅钱包支付不用传)
                "bankAccount": "", # 代扣账户(仅钱包支付不用传)
                "bankName": "", # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str({"balance":balance,"payAmount":payAmount,"payWays":[{"name":"押货保证金支付","payAmount":payAmount,"data":None}]}), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 1, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store["data"]["userId"] # 用户ID
            }
            with _appStore_api_wallet_pay(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"]["payStatus"] == 2

        @allure.step("押货单详情, 获取押货单号")
        def step_02_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal orderSn
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 2, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"

        @allure.step("押货单支付后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"]
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] - searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] - searchProductPage["mortgagePrice"] * 2

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == "" # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
       
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_01_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_prePayCheck()
        step_01_mgmt_inventory_deposit_pageList()
        step_appStore_api_wallet_pay()
        step_02_appStore_store_dis_mortgageOrder_detail_id()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()

    @allure.severity(P1)
    @allure.title("店铺运营后台下押货单: 签约工行代扣流水检查")
    def test_02_mgmt_inventory_deposit_pageList(self, login_store):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        payAmount = None # 押货单金额
        balance = None # 保证金余额
        orderSn = None # 押货单号
        pageList = None # 押货保证金信息
        getSignBankAccountList = None # 签约银行信息
               
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params09) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data07) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货下单, 获取押货单Id")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data08)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情, 获取押货单金额")
        def step_01_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal payAmount
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                payAmount = r.json()["data"]["payAmount"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取服务中心可用押货保证金余额")
        def step_appStore_store_deposit_msg():
            
            nonlocal balance
            params = deepcopy(self.params11)
            params["storeCode"] = store_85
            with _appStore_store_deposit_msg(params, self.store_token) as r:
                balance = r.json()["data"]["balance"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                 
        @allure.step("押货单支付前的金额校验")
        def step_appStore_store_dis_mortgageOrder_prePayCheck():
            
            data = deepcopy(self.data09)
            data["orderId"] = id
            data["oweDepositAmount"] = 0
            data["payAmount"] = payAmount
            with _appStore_store_dis_mortgageOrder_prePayCheck(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取签约银行列表")
        def step_appStore_store_getSignBankAccountList():
            
            nonlocal getSignBankAccountList
            params = deepcopy(self.params12)   
            params["isSigned"] = 1 # 是否已签约，1/是，2/否             
            with _appStore_store_getSignBankAccountList(params, self.store_token) as r:
                getSignBankAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
        @allure.step("押货单支付")
        def step_appStore_api_wallet_pay():
            
            data = {
                "accountName": getSignBankAccountList[0]["accountName"], # 户名(仅钱包支付不用传)
                "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户(仅钱包支付不用传)
                "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str(
                    {
                        "balance":balance,
                        "payAmount":payAmount,
                        "payWays":[
                            {
                                "name":getSignBankAccountList[0]["accountBank"],
                                "payAmount":payAmount,
                                "data":{
                                    "accountName":getSignBankAccountList[0]["accountName"],
                                    "account":getSignBankAccountList[0]["account"],
                                    "accountBank":getSignBankAccountList[0]["accountBank"],
                                    "accountType":getSignBankAccountList[0]["accountType"],
                                    "isSigned":getSignBankAccountList[0]["isSigned"]
                                }
                            }
                        ]
                    }
                ), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 2, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store["data"]["userId"] # 用户ID
            }
            with _appStore_api_wallet_pay(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"]["payStatus"] == 2

        @allure.step("押货单详情, 获取押货单号")
        def step_02_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal orderSn
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 2, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"

        @allure.step("押货单支付后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] - searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"]

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号,但前端不应该取值
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
                
                assert r.json()["data"]["list"][1]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][1]["recordType"] == 1 # 款项类型
                assert r.json()["data"]["list"][1]["recordTypeName"] == "汇押货款" # 款项类型
                assert r.json()["data"]["list"][1]["diffMoney"] == float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][1]["balance"] == r.json()["data"]["list"][2]["balance"] + r.json()["data"]["list"][1]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][1]["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                assert r.json()["data"]["list"][1]["payTypeName"] == "工行代扣" # 支付方式
                assert r.json()["data"]["list"][1]["remark"] == None # 备注
                assert r.json()["data"]["list"][1]["mortgageOrderNo"] == orderSn # 关联单号
       
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_01_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_store_getSignBankAccountList()
        step_01_mgmt_inventory_deposit_pageList()
        step_appStore_api_wallet_pay()
        step_02_appStore_store_dis_mortgageOrder_detail_id()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()

    @allure.severity(P1)
    @allure.title("店铺运营后台下押货单: 签约建行代扣流水检查")
    def test_03_mgmt_inventory_deposit_pageList(self, login_store):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        payAmount = None # 押货单金额
        balance = None # 保证金余额
        orderSn = None # 押货单号
        pageList = None # 押货保证金信息
        getSignBankAccountList = None # 签约银行信息
               
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params09) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data07) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货下单, 获取押货单Id")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data08)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情, 获取押货单金额")
        def step_01_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal payAmount
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                payAmount = r.json()["data"]["payAmount"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取服务中心可用押货保证金余额")
        def step_appStore_store_deposit_msg():
            
            nonlocal balance
            params = deepcopy(self.params11)
            params["storeCode"] = store_85
            with _appStore_store_deposit_msg(params, self.store_token) as r:
                balance = r.json()["data"]["balance"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                 
        @allure.step("押货单支付前的金额校验")
        def step_appStore_store_dis_mortgageOrder_prePayCheck():
            
            data = deepcopy(self.data09)
            data["orderId"] = id
            data["oweDepositAmount"] = 0
            data["payAmount"] = payAmount
            with _appStore_store_dis_mortgageOrder_prePayCheck(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取签约银行列表")
        def step_appStore_store_getSignBankAccountList():
            
            nonlocal getSignBankAccountList
            params = deepcopy(self.params12)   
            params["isSigned"] = 1 # 是否已签约，1/是，2/否             
            with _appStore_store_getSignBankAccountList(params, self.store_token) as r:
                getSignBankAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
        @allure.step("押货单支付")
        def step_appStore_api_wallet_pay():
            
            data = {
                "accountName": getSignBankAccountList[1]["accountName"], # 户名(仅钱包支付不用传)
                "bankAccount": getSignBankAccountList[1]["account"], # 代扣账户(仅钱包支付不用传)
                "bankName": getSignBankAccountList[1]["accountBank"], # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str(
                    {
                        "balance":balance,
                        "payAmount":payAmount,
                        "payWays":[
                            {
                                "name":getSignBankAccountList[1]["accountBank"],
                                "payAmount":payAmount,
                                "data":{
                                    "accountName":getSignBankAccountList[1]["accountName"],
                                    "account":getSignBankAccountList[1]["account"],
                                    "accountBank":getSignBankAccountList[1]["accountBank"],
                                    "accountType":getSignBankAccountList[1]["accountType"],
                                    "isSigned":getSignBankAccountList[1]["isSigned"]
                                }
                            }
                        ]
                    }
                ), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 3, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store["data"]["userId"] # 用户ID
            }
            with _appStore_api_wallet_pay(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"]["payStatus"] == 2

        @allure.step("押货单详情, 获取押货单号")
        def step_02_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal orderSn
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 2, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"

        @allure.step("押货单支付后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] - searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"]

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号,但前端不应该取值
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
                
                assert r.json()["data"]["list"][1]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][1]["recordType"] == 1 # 款项类型
                assert r.json()["data"]["list"][1]["recordTypeName"] == "汇押货款" # 款项类型
                assert r.json()["data"]["list"][1]["diffMoney"] == float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][1]["balance"] == r.json()["data"]["list"][2]["balance"] + r.json()["data"]["list"][1]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][1]["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                assert r.json()["data"]["list"][1]["payTypeName"] == "建行代扣" # 支付方式
                assert r.json()["data"]["list"][1]["remark"] == None # 备注
                assert r.json()["data"]["list"][1]["mortgageOrderNo"] == orderSn # 关联单号
       
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_01_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_store_getSignBankAccountList()
        step_01_mgmt_inventory_deposit_pageList()
        step_appStore_api_wallet_pay()
        step_02_appStore_store_dis_mortgageOrder_detail_id()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()

    @allure.severity(P1)
    @allure.title("店铺运营后台下押货单: 签约工行+保证金组合支付流水检查")
    def test_04_mgmt_inventory_deposit_pageList(self, login_store, inventory_add):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        payAmount = None # 押货单金额
        balance = None # 保证金余额
        orderSn = None # 押货单号
        pageList = None # 押货保证金信息
        getSignBankAccountList = None # 签约银行信息
               
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params09) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data07) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货下单, 获取押货单Id")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data08)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情, 获取押货单金额")
        def step_01_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal payAmount
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                payAmount = r.json()["data"]["payAmount"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取服务中心可用押货保证金余额")
        def step_appStore_store_deposit_msg():
            
            nonlocal balance
            params = deepcopy(self.params11)
            params["storeCode"] = store_85
            with _appStore_store_deposit_msg(params, self.store_token) as r:
                balance = r.json()["data"]["balance"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                 
        @allure.step("押货单支付前的金额校验")
        def step_appStore_store_dis_mortgageOrder_prePayCheck():
            
            data = deepcopy(self.data09)
            data["orderId"] = id
            data["oweDepositAmount"] = 0
            data["payAmount"] = payAmount
            with _appStore_store_dis_mortgageOrder_prePayCheck(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取签约银行列表")
        def step_appStore_store_getSignBankAccountList():
            
            nonlocal getSignBankAccountList
            params = deepcopy(self.params12)   
            params["isSigned"] = 1 # 是否已签约，1/是，2/否             
            with _appStore_store_getSignBankAccountList(params, self.store_token) as r:
                getSignBankAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
        @allure.step("押货单支付")
        def step_appStore_api_wallet_pay():
            
            data = {
                "accountName": getSignBankAccountList[0]["accountName"], # 户名(仅钱包支付不用传)
                "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户(仅钱包支付不用传)
                "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str(
                    {
                        "balance":balance,
                        "payAmount":payAmount,
                        "payWays":[
                            {
                                "name":"押货保证金支付",
                                "payAmount":balance,
                                "data":None
                            },
                            {
                                "name":getSignBankAccountList[0]["accountBank"],
                                "payAmount":payAmount-balance,
                                "data":{
                                    "accountName":getSignBankAccountList[0]["accountName"],
                                    "account":getSignBankAccountList[0]["account"],
                                    "accountBank":getSignBankAccountList[0]["accountBank"],
                                    "accountType":getSignBankAccountList[0]["accountType"],
                                    "isSigned":getSignBankAccountList[0]["isSigned"]
                                }
                            }
                        ]
                    }
                ), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 4, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store["data"]["userId"] # 用户ID
            }
            with _appStore_api_wallet_pay(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"]["payStatus"] == 2

        @allure.step("押货单详情, 获取押货单号")
        def step_02_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal orderSn
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 2, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"

        @allure.step("押货单支付后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + searchProductPage["mortgagePrice"] * 2 - balance
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] - searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] - balance

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号,但前端不应该取值
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
                
                assert r.json()["data"]["list"][1]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][1]["recordType"] == 1 # 款项类型
                assert r.json()["data"]["list"][1]["recordTypeName"] == "汇押货款" # 款项类型
                assert r.json()["data"]["list"][1]["diffMoney"] == float(searchProductPage["mortgagePrice"]) * 2 - balance # 工行汇款
                assert r.json()["data"]["list"][1]["balance"] == r.json()["data"]["list"][2]["balance"] + r.json()["data"]["list"][1]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][1]["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                assert r.json()["data"]["list"][1]["payTypeName"] == "工行代扣" # 支付方式
                assert r.json()["data"]["list"][1]["remark"] == None # 备注
                assert r.json()["data"]["list"][1]["mortgageOrderNo"] == orderSn # 关联单号
       
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_01_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_store_getSignBankAccountList()
        step_01_mgmt_inventory_deposit_pageList()
        step_appStore_api_wallet_pay()
        step_02_appStore_store_dis_mortgageOrder_detail_id()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()

    @allure.severity(P1)
    @allure.title("店铺运营后台下押货单: 签约建行+保证金组合支付流水检查")
    def test_05_mgmt_inventory_deposit_pageList(self, login_store, inventory_add):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        payAmount = None # 押货单金额
        balance = None # 保证金余额
        orderSn = None # 押货单号
        pageList = None # 押货保证金信息
        getSignBankAccountList = None # 签约银行信息
               
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params09) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data07) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货下单, 获取押货单Id")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data08)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情, 获取押货单金额")
        def step_01_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal payAmount
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                payAmount = r.json()["data"]["payAmount"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取服务中心可用押货保证金余额")
        def step_appStore_store_deposit_msg():
            
            nonlocal balance
            params = deepcopy(self.params11)
            params["storeCode"] = store_85
            with _appStore_store_deposit_msg(params, self.store_token) as r:
                balance = r.json()["data"]["balance"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                 
        @allure.step("押货单支付前的金额校验")
        def step_appStore_store_dis_mortgageOrder_prePayCheck():
            
            data = deepcopy(self.data09)
            data["orderId"] = id
            data["oweDepositAmount"] = 0
            data["payAmount"] = payAmount
            with _appStore_store_dis_mortgageOrder_prePayCheck(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取签约银行列表")
        def step_appStore_store_getSignBankAccountList():
            
            nonlocal getSignBankAccountList
            params = deepcopy(self.params12)   
            params["isSigned"] = 1 # 是否已签约，1/是，2/否             
            with _appStore_store_getSignBankAccountList(params, self.store_token) as r:
                getSignBankAccountList = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货保证金分页查询列表: 获取押货保证金初始值")
        def step_01_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                    pageList = r.json()["data"]["list"][0]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
        @allure.step("押货单支付")
        def step_appStore_api_wallet_pay():
            
            data = {
                "accountName": getSignBankAccountList[1]["accountName"], # 户名(仅钱包支付不用传)
                "bankAccount": getSignBankAccountList[1]["account"], # 代扣账户(仅钱包支付不用传)
                "bankName": getSignBankAccountList[1]["accountBank"], # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str(
                    {
                        "balance":balance,
                        "payAmount":payAmount,
                        "payWays":[
                            {
                                "name":"押货保证金支付",
                                "payAmount":balance,
                                "data":None
                            },
                            {
                                "name":getSignBankAccountList[1]["accountBank"],
                                "payAmount":payAmount-balance,
                                "data":{
                                    "accountName":getSignBankAccountList[1]["accountName"],
                                    "account":getSignBankAccountList[1]["account"],
                                    "accountBank":getSignBankAccountList[1]["accountBank"],
                                    "accountType":getSignBankAccountList[1]["accountType"],
                                    "isSigned":getSignBankAccountList[1]["isSigned"]
                                }
                            }
                        ]
                    }
                ), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 5, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store["data"]["userId"] # 用户ID
            }
            with _appStore_api_wallet_pay(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"]["payStatus"] == 2

        @allure.step("押货单详情, 获取押货单号")
        def step_02_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal orderSn
            params = deepcopy(self.params10)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                orderSn = r.json()["data"]["orderSn"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单发货")
        def step_esb_third_mortgage_syncDeliveryInfo():
            data = {
                "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
                "mortgageItemReqDtoList": [
                    {
                        "itemCode": productCode, # 商品编号
                        "num": 2, # 数量
                        "skuCode": ""
                    }
                ],
                "mortgageOrderNo": orderSn, # 押货单号
                "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
                "status": 2,
                "type": 5 # 1:3是2,85折是5
            }
            with _esb_third_mortgage_syncDeliveryInfo(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["resultMsg"] == "success"

        @allure.step("押货单支付后: 押货保证金列表各字段信息检查")
        def step_02_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["lastMonthBalance"] == pageList["lastMonthBalance"]
                assert r.json()["data"]["list"][0]["currentMonthRemitAndRefund"] == pageList["currentMonthRemitAndRefund"] + searchProductPage["mortgagePrice"] * 2 - balance
                assert r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"] == pageList["currentMonthMortgageAndReturn"] - searchProductPage["mortgagePrice"] * 2
                assert r.json()["data"]["list"][0]["currentTransferOrderIn"] == pageList["currentTransferOrderIn"]
                assert r.json()["data"]["list"][0]["balance"] == pageList["balance"] - balance

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data04)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -float(searchProductPage["mortgagePrice"]) * 2 # 交易金额
                assert r.json()["data"]["list"][0]["balance"] == r.json()["data"]["list"][1]["balance"] + r.json()["data"]["list"][0]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][0]["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号,但前端不应该取值
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == orderSn # 关联单号
                
                assert r.json()["data"]["list"][1]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][1]["recordType"] == 1 # 款项类型
                assert r.json()["data"]["list"][1]["recordTypeName"] == "汇押货款" # 款项类型
                assert r.json()["data"]["list"][1]["diffMoney"] == float(searchProductPage["mortgagePrice"]) * 2 - balance # 工行汇款
                assert r.json()["data"]["list"][1]["balance"] == r.json()["data"]["list"][2]["balance"] + r.json()["data"]["list"][1]["diffMoney"] # 保证金余额
                assert r.json()["data"]["list"][1]["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                assert r.json()["data"]["list"][1]["payTypeName"] == "建行代扣" # 支付方式
                assert r.json()["data"]["list"][1]["remark"] == None # 备注
                assert r.json()["data"]["list"][1]["mortgageOrderNo"] == orderSn # 关联单号
       
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_01_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_store_getSignBankAccountList()
        step_01_mgmt_inventory_deposit_pageList()
        step_appStore_api_wallet_pay()
        step_02_appStore_store_dis_mortgageOrder_detail_id()
        step_esb_third_mortgage_syncDeliveryInfo()
        step_02_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_storeDepositDetail()


