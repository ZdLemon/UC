# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_disBankRemit_pageList import data, _mgmt_inventory_disBankRemit_pageList
from api.mall_center_member._crm_member_serviceCompany_bankOfDeposit import _crm_member_serviceCompany_bankOfDeposit # 开户银行接口
from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode, USERNAME

from copy import deepcopy
import os
import allure
import pytest
import time
import uuid


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disBankRemit/pageList")
class TestClass:
    """
    85折银行流水分页搜索列表
    /mgmt/inventory/disBankRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_01_mgmt_inventory_disBankRemit_pageList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode                
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_disBankRemit_pageList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode                       
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表-成功路径: 查询付款银行检查")
    def test_03_mgmt_inventory_disBankRemit_pageList(self):
        
        payAccountBankNames = _crm_member_serviceCompany_bankOfDeposit(access_token=self.access_token).json()["data"]
        for i in payAccountBankNames:
            payAccountBankName = i["name"]
            data = deepcopy(self.data)
            data["payAccountBankName"] = payAccountBankName                    
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:            
                if r.json()["data"]["list"]:
                    for i in set(d["payAccountBankName"] for d in r.json()["data"]["list"]):
                        assert i == payAccountBankName
                else:
                    assert r.json()["data"]["list"] == []
         
    @allure.severity(P2)
    @allure.title("押货保证详情列表: 多选查询款项类型检查")
    @pytest.mark.parametrize("sourceType,ids", [([1], "汇押货款"), ([3], "其他"), ([7], "手工增加押货款"), ([8], "手工退押货款"), ([9], "押货保证金转移"), ([14], "无法识别款退款"), ([15], "无法识别款不处理")])
    def test_04_mgmt_inventory_disBankRemit_pageList(self, sourceType, ids):
        
        data = deepcopy(self.data)
        data["sourceType"].extend(sourceType)            
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["sourceType"] for d in r.json()["data"]["list"]):
                    assert i in sourceType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("押货保证详情列表: 多选查询交易类型检查")
    @pytest.mark.parametrize("dealType,ids", [([1], "汇押货款"), ([2], "退押货款"), ([3], "其他"), ([4], "不影响押货保证金"), ([5], "押货保证金转移")])
    def test_05_mgmt_inventory_disBankRemit_pageList(self, dealType, ids):
        
        data = deepcopy(self.data)
        data["dealType"].extend(dealType)            
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["dealType"] for d in r.json()["data"]["list"]):
                    assert i in dealType
            else:
                assert r.json()["data"]["list"] == []
              
    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表: 下拉单选查询自动&手工检查")
    @pytest.mark.parametrize("handleType,ids", [(1, "自动处理"), (2, "手工处理")])
    def test_06_mgmt_inventory_disBankRemit_pageList(self, handleType, ids):
        
        data = deepcopy(self.data)
        data["handleType"] = handleType                      
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["handleType"] for d in r.json()["data"]["list"]):
                    assert i == handleType
            else:
                assert r.json()["data"]["list"] == []
        
    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表: 查询系统到账时间检查")
    def test_07_mgmt_inventory_disBankRemit_pageList(self):
        
        data = deepcopy(self.data) 
        data["sourceType"] = [1]                      
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            for i in r.json()["data"]["list"]:
                if i["systemPaymentTime"]:
                    systemPaymentTime = r.json()["data"]["list"][0]["systemPaymentTime"] # 获取系统到账时间
        
        data["sysStartTime"] = time.strftime("%Y-%m-%d", time.localtime(int(systemPaymentTime)/1000))
        data["sysEndTime"] = time.strftime("%Y-%m-%d", time.localtime(int(systemPaymentTime)/1000))                
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert time.strftime("%Y-%m-%d", time.localtime(int(d["systemPaymentTime"])/1000)) == data["sysStartTime"]

    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表: 查询审核时间检查")
    def test_08_mgmt_inventory_disBankRemit_pageList(self):
        
        data = deepcopy(self.data)
        data["handleType"] = 2 # 手工处理                   
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            dealTime = r.json()["data"]["list"][0]["dealTime"] # 获取审核时间
        
        data["verifyStartTime"] = time.strftime("%Y-%m-%d", time.localtime(int(dealTime)/1000))
        data["verifyEndTime"] = time.strftime("%Y-%m-%d", time.localtime(int(dealTime)/1000))                
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert time.strftime("%Y-%m-%d", time.localtime(int(d["dealTime"])/1000)) == data["verifyStartTime"]

    @allure.severity(P2)
    @allure.title("85折银行流水分页搜索列表: 查询录入时间检查")
    def test_09_mgmt_inventory_disBankRemit_pageList(self):
        
        data = deepcopy(self.data)                
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            createTime = r.json()["data"]["list"][0]["createTime"] # 获取录入时间
        
        data["inputStartTime"] = time.strftime("%Y-%m-%d", time.localtime(int(createTime)/1000))
        data["inputEndTime"] = time.strftime("%Y-%m-%d", time.localtime(int(createTime)/1000))                
        with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert time.strftime("%Y-%m-%d", time.localtime(int(d["createTime"])/1000)) == data["inputStartTime"]


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disBankRemit/pageList")
class TestClass02:
    """
    85折银行流水分页搜索列表:店铺系统充值流水检查
    /mgmt/inventory/disBankRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 工行充值流水检查")
    def test_01_mgmt_inventory_disBankRemit_pageList(self, appStore_invest_2):
        
        payAmount, payOrderNo, getSignBankAccountList = appStore_invest_2 # 充值金额，充值流水号，银行列表
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList["accountBank"] # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList["account"] # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputRemark"] == "前端充值" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
    
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 建行充值流水检查")
    def test_02_mgmt_inventory_disBankRemit_pageList(self, appStore_invest_3):
        
        payAmount, payOrderNo, getSignBankAccountList = appStore_invest_3 # 充值金额，充值流水号，银行列表
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                # assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList["accountBank"] # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList["account"] # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputRemark"] == "前端充值" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
    

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disBankRemit/pageList")
class TestClass03:
    """
    85折银行流水分页搜索列表:押货单流水检查
    /mgmt/inventory/disBankRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 店铺系统-工行支付-押货流水检查")
    def test_01_mgmt_inventory_disBankRemit_pageList(self, mortgageOrder_85_2):
        
        _, payAmount, getSignBankAccountList = mortgageOrder_85_2 # 押货退货单号, 押货单金额,支付银行账号
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
    
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 店铺系统-建行支付-押货流水检查")
    def test_02_mgmt_inventory_disBankRemit_pageList(self, mortgageOrder_85_3):
        
        _, payAmount, getSignBankAccountList = mortgageOrder_85_3 # 押货退货单号, 押货单金额,支付银行账号
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[1]["accountBank"] # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[1]["account"] # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()

    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 店铺系统-工行+保证金支付-押货流水检查")
    def test_03_mgmt_inventory_disBankRemit_pageList(self, mortgageOrder_85_4):
        
        _, balance, payAmount, getSignBankAccountList = mortgageOrder_85_4 # 押货退货单号, 保证金余额，押货单金额，支付银行账号
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount - balance # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()

    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 店铺系统-建行+保证金支付-押货流水检查")
    def test_04_mgmt_inventory_disBankRemit_pageList(self, mortgageOrder_85_5):
        
        _, balance, payAmount, getSignBankAccountList = mortgageOrder_85_5 # 押货退货单号, 保证金余额，押货单金额，支付银行账号
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount - balance # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[1]["accountBank"] # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[1]["account"] # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disBankRemit/pageList")
class TestClass04:
    """
    85折银行流水分页搜索列表:手工录入流水检查
    /mgmt/inventory/disBankRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 手工录入其他款检查")
    def test_01_mgmt_inventory_disBankRemit_pageList(self, disManualInputRemit_add_3):
        
        remitMoneys = disManualInputRemit_add_3 # 录入金额
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoneys[1] # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 3 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "其他"
                assert r.json()["data"]["list"][0]["dealType"] == 3 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "其他"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][0]["inputMan"] == USERNAME # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == f"录入其他款 {remitMoneys[1]}元" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == f"同意录入其它款 {remitMoneys[1]}元" # 审核备注
                
                assert r.json()["data"]["list"][1]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][1]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][1]["remitMoney"] ==  remitMoneys[0] # 款项金额
                assert r.json()["data"]["list"][1]["sourceType"] == 3 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][1]["sourceTypeName"] == "其他"
                assert r.json()["data"]["list"][1]["dealType"] == 3 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][1]["dealTypeName"] == "其他"
                assert r.json()["data"]["list"][1]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][1]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][1]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][1]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][1]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][1]["inputMan"] == USERNAME # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][1]["inputRemark"] == f"录入其他款 {remitMoneys[0]}元" # 录入备注
                assert r.json()["data"]["list"][1]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][1]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][1]["verifyRemark"] == f"同意录入其它款 {remitMoneys[0]}元" # 审核备注
    
        step_mgmt_inventory_disBankRemit_pageList()
    
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 手工增加押货款检查")
    def test_02_mgmt_inventory_disBankRemit_pageList(self, disManualInputRemit_add_7):
        
        remitMoney = disManualInputRemit_add_7 # 录入金额
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoney # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 7 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "手工增加押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][0]["inputMan"] == USERNAME # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == f"录入手动增加押货款 {remitMoney}元" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == f"同意录入手动增加押货款 {remitMoney}元" # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
            
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 手工退押货款检查")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_03_mgmt_inventory_disBankRemit_pageList(self, disManualInputRemit_add_8):
        
        remitMoney = disManualInputRemit_add_8 # 录入金额
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoney # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 8 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "手工退押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 2 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "退押货款"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][0]["inputMan"] == USERNAME # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == f"录入手动退押货款 {remitMoney}元" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == f"同意录入手动退押货款 {remitMoney}元" # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
                
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 押货保证金转移检查")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_04_mgmt_inventory_disBankRemit_pageList(self, disManualInputRemit_add_9):
        
        remitMoney = disManualInputRemit_add_9 # 录入金额
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoney # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 9 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "押货保证金转移"
                assert r.json()["data"]["list"][0]["dealType"] == 5 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货保证金转移"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][0]["inputMan"] == USERNAME # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == f"录入保证金转移 {remitMoney}元" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == f"同意录入保证金转移 {remitMoney}元" # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
            
          
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disBankRemit/pageList")
class TestClass05:
    """
    85折银行流水分页搜索列表:线下汇款流水检查
    /mgmt/inventory/disBankRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 线下汇款自动识别流水检查")
    def test_01_mgmt_inventory_disBankRemit_pageList(self, pay_notify_mockBankflow):
        
        remitMoney = pay_notify_mockBankflow  
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns(counts=5)
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoney # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["bankPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                # assert r.json()["data"]["list"][0]["payAccountBankName"] == "中国工商银行深圳华南城支行" # 付款银行
                # assert r.json()["data"]["list"][0]["payAccount"] == "4000050909100468735" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == None # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
            
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 线下汇款无法识别款确认押货款流水检查")
    def test_02_mgmt_inventory_disBankRemit_pageList(self, unknownRemit_deal_5):
        
        remitMoney = unknownRemit_deal_5
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoney # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
                assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["bankPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                # assert r.json()["data"]["list"][0]["payAccountBankName"] == "中国工商银行深圳华南城支行" # 付款银行
                # assert r.json()["data"]["list"][0]["payAccount"] == "622123456789951753" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == None # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == "我是处理备注信息" # 审核备注
                
        step_mgmt_inventory_disBankRemit_pageList()

    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 线下汇款无法识别款退款流水检查")
    def test_03_mgmt_inventory_disBankRemit_pageList(self, unknownRemit_deal_6):
        
        remitMoney = unknownRemit_deal_6
        
        @allure.step("85折银行流水分页搜索列表")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList():
        
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  remitMoney # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 14 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "无法识别款退款"
                assert r.json()["data"]["list"][0]["dealType"] == 4 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "不影响押货保证金"
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["bankPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 银行到账时间
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
                # assert r.json()["data"]["list"][0]["payAccountBankName"] == "中国工商银行深圳华南城支行" # 付款银行
                # assert r.json()["data"]["list"][0]["payAccount"] == "622123456789951753" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 2 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "人为处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == None # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == USERNAME # 审核人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["dealTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == "我是处理备注信息" # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disBankRemit/pageList")
class TestClass06:
    """
    85折银行流水分页搜索列表:13押货转移流水检查
    /mgmt/inventory/disBankRemit/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 完美运营后台-13押货转移流水检查")
    def test_01_mgmt_inventory_disBankRemit_pageList(self, addTransfer):
        
        addTransferList, recordList = addTransfer # 库存列表:大于0的库存
        
        @allure.step("85折银行流水")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList(): 
                   
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  addTransferList["securityPrice"] # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 9 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "押货保证金转移"
                assert r.json()["data"]["list"][0]["dealType"] == 5 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货保证金转移"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == "押货保证金转移" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
                
    @allure.severity(P1)
    @allure.title("85折银行流水分页搜索列表: 完美运营后台-13押货转移流水检查")
    def test_02_mgmt_inventory_disBankRemit_pageList(self, disInventoryTransfer_addTransfer):
        
        addTransferList, recordList = disInventoryTransfer_addTransfer # 库存列表:大于0的库存
        
        @allure.step("85折银行流水")
        @stepreruns()
        def step_mgmt_inventory_disBankRemit_pageList(): 
                   
            data = deepcopy(self.data)
            data["storeCode"] = store_85              
            with _mgmt_inventory_disBankRemit_pageList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心编号
                assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
                assert r.json()["data"]["list"][0]["remitMoney"] ==  addTransferList["securityPrice"] # 款项金额
                assert r.json()["data"]["list"][0]["sourceType"] == 9 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
                assert r.json()["data"]["list"][0]["sourceTypeName"] == "押货保证金转移"
                assert r.json()["data"]["list"][0]["dealType"] == 5 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货保证金转移"
                assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
                assert r.json()["data"]["list"][0]["systemPaymentTime"] == None # 系统到账时间
                assert r.json()["data"]["list"][0]["payAccountBankName"] == "无" # 付款银行
                assert r.json()["data"]["list"][0]["payAccount"] == "无" # 付款账号
                assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
                assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
                assert r.json()["data"]["list"][0]["inputMan"] == None # 录入人
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 录入时间
                assert r.json()["data"]["list"][0]["inputRemark"] == "押货保证金转移" # 录入备注
                assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
                assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
                assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注
        
        step_mgmt_inventory_disBankRemit_pageList()
                
  







