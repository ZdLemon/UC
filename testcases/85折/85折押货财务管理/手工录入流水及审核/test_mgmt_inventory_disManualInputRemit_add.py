# coding:utf-8

from api.mall_center_sys._mgmt_sys_getAccountList import params, _mgmt_sys_getAccountList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data, _mgmt_inventory_disManualInputRemit_add
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disManualInputRemit/add")
class TestClass:
    """
    85折手工录入流水
    /mgmt/inventory/disManualInputRemit/add
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.params05 = deepcopy(params05)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("85折手工录入流水-成功路径: 其他款检查")
    @pytest.mark.parametrize("remitMoney", [2, -1], ids=["2元", "-1元"])
    def test_01_mgmt_inventory_disManualInputRemit_add(self, remitMoney):
        
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        
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
                 
            data = deepcopy(self.data)
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
            elif remitMoney < 0: # 公司付款
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
            params["verifyRemark"] = f"同意录入其它款 {remitMoney}元", # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add()
        step_mgmt_inventory_disManualInputRemit_pageList()  
        step_mgmt_inventory_disManualInputRemit_verify()

    @allure.severity(P1)
    @allure.title("85折手工录入流水-成功路径: 手动增加押货款检查")
    def test_02_mgmt_inventory_disManualInputRemit_add(self):
        
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        remitMoney = 4 # 金额
        
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
                 
            data = deepcopy(self.data)
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
            params["verifyRemark"] = f"同意录入手动增加押货款 {remitMoney}元", # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()

    @allure.severity(P1)
    @allure.title("85折手工录入流水-成功路径: 手动退押货款检查")
    def test_03_mgmt_inventory_disManualInputRemit_add(self):
        
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        remitMoney = -2 # 金额
        
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
                 
            data = deepcopy(self.data)
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
            params["verifyRemark"] = f"同意录入手动退押货款 {remitMoney}元", # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()

    @allure.severity(P1)
    @allure.title("85折手工录入流水-成功路径: 押货保证金转移检查")
    def test_04_mgmt_inventory_disManualInputRemit_add(self):
        
        getStoreWalletMsg = None # 现有押货余额及保证金信息
        getAccountList = None # 分公司银行账号信息
        getStoreByCode = None # 服务中心信息
        getBankAccountList = None # 服务中心银行账号信息
        id = None
        remitMoney = 1 # 金额
        
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
                 
            data = deepcopy(self.data)
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
            params["verifyRemark"] = f"同意录入保证金转移 {remitMoney}元", # 审核备注
            params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
            with _mgmt_inventory_disManualInputRemit_verify(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        step_mgmt_store_getStoreByCode()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()

