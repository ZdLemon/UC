# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_deposit_storeDepositDetail import data, _mgmt_inventory_deposit_storeDepositDetail # 服务中心押货保证详情
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params, _mgmt_inventory_dis_mortgage_returnOrder_listPage # 押货退货分页列表
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_listPage import params as params02, _mgmt_inventory_dis_mortgage_order_listPage # 85折押货单列表查询
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detail_id import _mgmt_inventory_dis_mortgage_order_detail_id # 押货单详情

from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/storeDepositDetail")
class TestClass:
    """
    85折账款管理 -- 服务中心押货保证详情:搜索检查
    /mgmt/inventory/deposit/storeDepositDetail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("押货保证详情列表: 查询交易日期检查")
    def test_01_mgmt_inventory_deposit_storeDepositDetail(self):
        
        data = deepcopy(self.data)
        data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
        data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
            if r.json()["data"]["list"]:
                for i in set(d["dealTimeExcel"][:7] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m",time.localtime(time.time()))
            else:
                assert r.json()["data"]["list"] == []
               
    @allure.severity(P2)
    @allure.title("押货保证详情列表: 多选查询报表字段检查")
    @pytest.mark.parametrize("reportType", [[1], [2], [3], [1, 2]])
    def test_02_mgmt_inventory_deposit_storeDepositDetail(self, reportType):
        
        data = deepcopy(self.data)
        data["reportType"].extend(reportType) # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入              
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["recordType"] for d in r.json()["data"]["list"]):
                    if reportType == [1]:
                        assert i in [1, 3, 7, 8, 9]
                    elif reportType == [2]:
                        assert i in [4, 5]
                    elif reportType == [3]:
                        assert i in [6]
                    elif reportType == [1, 2]:
                        assert i in [1, 3, 4, 5, 7, 8, 9]
            else:
                assert r.json()["data"]["list"] == []
        
    @allure.severity(P2)
    @allure.title("押货保证详情列表: 多选查询款项类型检查")
    @pytest.mark.parametrize("moneyType", [[1], [3], [7], [8], [9], [1, 3], [1, 3, 7], [7,8]])
    def test_03_mgmt_inventory_deposit_storeDepositDetail(self, moneyType):
        
        data = deepcopy(self.data)
        data["moneyType"].extend(moneyType) # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移               
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["recordType"] for d in r.json()["data"]["list"]):
                    assert i in moneyType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("押货保证详情列表: 多选查询交易类型检查")
    @pytest.mark.parametrize("dealType,dealTypeName", [([1], ["汇押货款"]), ([2], ["退押货款"]), ([3], ["其他"]), ([4], ["押货使用"]), ([5], ["押货退货"]), ([6], ["交付差额转入"]), ([9], ["押货保证金转移"]),( [1, 2], ["汇押货款", "退押货款"]), ([4, 5], ["押货使用", "押货退货"])])
    def test_04_mgmt_inventory_deposit_storeDepositDetail(self, dealType, dealTypeName):
        
        data = deepcopy(self.data)
        data["dealType"].extend(dealType) # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移                 
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["dealTypeName"] for d in r.json()["data"]["list"]):
                    assert i in dealTypeName
            else:
                assert r.json()["data"]["list"] == []
                

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/storeDepositDetail")
class TestClass05:
    """
    85折账款管理 -- 服务中心押货保证详情:手工录入流水检查
    /mgmt/inventory/deposit/storeDepositDetail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("手工录入其他款: 押货保证金流水检查")
    def test_01_mgmt_inventory_deposit_storeDepositDetail(self, disManualInputRemit_add_3):
    
        remitMoneys = disManualInputRemit_add_3   
        data = deepcopy(self.data)
        data["storeCode"] = store_85
        data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
        data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
            assert r.json()["data"]["list"][0]["dealTypeName"] == "其他" # 交易类型
            assert r.json()["data"]["list"][0]["recordType"] == 3 # 款项类型
            assert r.json()["data"]["list"][0]["recordTypeName"] == "其他" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == remitMoneys[1] # 交易金额
            assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
            assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
            assert r.json()["data"]["list"][0]["remark"] == f"同意录入其它款 {remitMoneys[1]}元" # 备注
            assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
            
            assert r.json()["data"]["list"][1]["dealTypeName"] == "其他" # 交易类型
            assert r.json()["data"]["list"][1]["recordType"] == 3 # 款项类型
            assert r.json()["data"]["list"][1]["recordTypeName"] == "其他" # 款项类型
            assert r.json()["data"]["list"][1]["diffMoney"] == remitMoneys[0] # 交易金额
            assert r.json()["data"]["list"][1]["bankAccount"] == None # 银行账号
            assert r.json()["data"]["list"][1]["payTypeName"] == None # 支付方式
            assert r.json()["data"]["list"][1]["remark"] == f"同意录入其它款 {remitMoneys[0]}元" # 备注
            assert r.json()["data"]["list"][1]["mortgageOrderNo"] == None # 关联单号
                
    @allure.severity(P1)
    @allure.title("手工录入增加押货款: 押货保证金流水检查")
    def test_02_mgmt_inventory_deposit_storeDepositDetail(self, disManualInputRemit_add_7):
    
        remitMoney = disManualInputRemit_add_7
        data = deepcopy(self.data)
        data["storeCode"] = store_85
        data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
        data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款" # 交易类型
            assert r.json()["data"]["list"][0]["recordType"] == 7 # 款项类型
            assert r.json()["data"]["list"][0]["recordTypeName"] == "手工增加押货款" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
            assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
            assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
            assert r.json()["data"]["list"][0]["remark"] == f"同意录入手动增加押货款 {remitMoney}元" # 备注
            assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
            
    @allure.severity(P1)
    @allure.title("手工录入退押货款: 押货保证金流水检查")
    def test_03_mgmt_inventory_deposit_storeDepositDetail(self, disManualInputRemit_add_8):
    
        remitMoney = disManualInputRemit_add_8
        data = deepcopy(self.data)
        data["storeCode"] = store_85
        data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
        data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
            assert r.json()["data"]["list"][0]["dealTypeName"] == "退押货款" # 交易类型
            assert r.json()["data"]["list"][0]["recordType"] == 8 # 款项类型
            assert r.json()["data"]["list"][0]["recordTypeName"] == "手工退押货款" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
            assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
            assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
            assert r.json()["data"]["list"][0]["remark"] == f"同意录入手动退押货款 {remitMoney}元" # 备注
            assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号     

    @allure.severity(P1)
    @allure.title("手工录入押货保证金转移: 押货保证金流水检查")
    def test_04_mgmt_inventory_deposit_storeDepositDetail(self, disManualInputRemit_add_9):
    
        remitMoney = disManualInputRemit_add_9
        data = deepcopy(self.data)
        data["storeCode"] = store_85
        data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
        data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
        with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
            assert r.json()["data"]["list"][0]["dealTypeName"] == "押货保证金转移" # 交易类型
            assert r.json()["data"]["list"][0]["recordType"] == 9 # 款项类型
            assert r.json()["data"]["list"][0]["recordTypeName"] == "押货保证金转移" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == remitMoney # 交易金额
            assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
            assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
            assert r.json()["data"]["list"][0]["remark"] == f"同意录入保证金转移 {remitMoney}元" # 备注
            assert r.json()["data"]["list"][0]["mortgageOrderNo"] =="无" # 关联单号 


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/storeDepositDetail")
class TestClass06:
    """
    85折账款管理 -- 服务中心押货保证详情:线下汇款流水检查
    /mgmt/inventory/deposit/storeDepositDetail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("线下汇款自动识别: 押货保证金流水检查")
    def test_01_mgmt_inventory_deposit_pageList(self, pay_notify_mockBankflow):
        

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 1 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "汇押货款" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == 11 # 交易金额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
                
        step_mgmt_inventory_deposit_storeDepositDetail()
    
    @allure.severity(P1)
    @allure.title("线下汇款无法识别款确认押货款: 押货保证金流水检查")
    def test_02_mgmt_inventory_deposit_pageList(self):
        
        from api.mall_center_pay._pay_notify_mockBankflow import data as data02, _pay_notify_mockBankflow
        from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_pageList import data as data01, _mgmt_inventory_remit_unknownRemit_pageList
        from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params01, _mgmt_store_getStoreByCode
        from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_deal import _mgmt_inventory_remit_unknownRemit_deal 
        pageList = None # 待处理的未识别流水
        getStoreByCode = None # 服务中心信息  
                           
        @allure.step("生成无法识别流水，方便测试")    
        def step_pay_notify_mockBankflow():
            
            data = deepcopy(data02)
            data[0]["accountName"] = "我是无法识别的银行账户"
            data[0]["accountNo"] = "622123456789951753"
            data[0]["bankName"] = "中国工商银行深圳华南城支行"
            data[0]["tradeAmount"] = 10
            with _pay_notify_mockBankflow(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.text == "SUCCESS"
        
        @allure.step("未知款项流水分页搜索列表")
        def step_mgmt_inventory_remit_unknownRemit_pageList():
            
            nonlocal pageList
            data = deepcopy(data01)
            data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
            with _mgmt_inventory_remit_unknownRemit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]

        @allure.step("根据服务中心编号获取服务中心")    
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(params01)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreByCode = r.json()["data"]
        
        @allure.step("无法识别款确认押货款")    
        def step_mgmt_inventory_remit_unknownRemit_deal():
            
            data = pageList
            data["businessMode"] = 2
            data["changeReason"] = "汇押货款"
            data["dealRemark"] = "我是处理备注信息"
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["show"] = True 
            data["sourceType"] = 5 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
            data["storeCode"] = getStoreByCode["store"]["code"]  
            data["storeCodeSearch"] = True  
            data["storeName"] = getStoreByCode["store"]["name"]
            data["type"] = 2  
            data["sourceTypeList"] = [
                {
                    "id": 5,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 5,
                    "name": "无法识别款确认押货款",
                    "changeReason": "汇押货款",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "id": 6,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 6,
                    "name": "无法识别款退款",
                    "changeReason": "无",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "type": 15,
                    "name": "无法识别款不处理（需有批示或批文时可选择）",
                    "changeReason": "无"
                }
            ]
            with _mgmt_inventory_remit_unknownRemit_deal(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
                assert r.json()["message"] == "操作成功"

        @allure.step("押货保证详情列表: 新增流水明细检查")
        def step_mgmt_inventory_deposit_storeDepositDetail():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r: 
                assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 1 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "汇押货款" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == 10 # 交易金额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == None # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == None # 关联单号
                
        step_pay_notify_mockBankflow()
        step_mgmt_inventory_remit_unknownRemit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_inventory_remit_unknownRemit_deal()
        step_mgmt_inventory_deposit_storeDepositDetail()
    

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/storeDepositDetail")
class TestClass08:
    """
    85折账款管理 -- 服务中心押货保证详情:13押货转移检查
    /mgmt/inventory/deposit/storeDepositDetail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("完美运营后台-13押货转移: 押货保证金流水检查")
    def test_01_mgmt_inventory_deposit_pageList(self, addTransfer):
        
        addTransferList, recordList = addTransfer # 库存列表:大于0的库存
        
        @allure.step("押货保证金流水")
        @stepreruns()
        def step_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -addTransferList["orderPrice"] # 交易金额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == recordList["orderSn"] # 关联单号
                
                assert r.json()["data"]["list"][1]["dealTypeName"] == "押货保证金转移" # 交易类型
                assert r.json()["data"]["list"][1]["recordType"] == 9 # 款项类型
                assert r.json()["data"]["list"][1]["recordTypeName"] == "押货保证金转移" # 款项类型
                assert r.json()["data"]["list"][1]["diffMoney"] == addTransferList["securityPrice"] # 交易金额
                assert r.json()["data"]["list"][1]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][1]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][1]["remark"] == None # 备注
                assert r.json()["data"]["list"][1]["mortgageOrderNo"] == "无" # 关联单号
        
        step_mgmt_inventory_deposit_pageList()

    @allure.severity(P1)
    @allure.title("店铺系统-13押或转移: 押货保证金流水检查")
    def test_02_mgmt_inventory_deposit_pageList(self, disInventoryTransfer_addTransfer):
        
        addTransferList, recordList = disInventoryTransfer_addTransfer # 库存列表:大于0的库存
        
        @allure.step("押货保证金流水")
        @stepreruns()
        def step_mgmt_inventory_deposit_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85
            data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
            data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["dealTypeName"] == "押货使用" # 交易类型
                assert r.json()["data"]["list"][0]["recordType"] == 4 # 款项类型
                assert r.json()["data"]["list"][0]["recordTypeName"] == "无" # 款项类型
                assert r.json()["data"]["list"][0]["diffMoney"] == -addTransferList["orderPrice"] # 交易金额
                assert r.json()["data"]["list"][0]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][0]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][0]["remark"] == None # 备注
                assert r.json()["data"]["list"][0]["mortgageOrderNo"] == recordList["orderSn"] # 关联单号
                
                assert r.json()["data"]["list"][1]["dealTypeName"] == "押货保证金转移" # 交易类型
                assert r.json()["data"]["list"][1]["recordType"] == 9 # 款项类型
                assert r.json()["data"]["list"][1]["recordTypeName"] == "押货保证金转移" # 款项类型
                assert r.json()["data"]["list"][1]["diffMoney"] == addTransferList["securityPrice"] # 交易金额
                assert r.json()["data"]["list"][1]["bankAccount"] == None # 银行账号
                assert r.json()["data"]["list"][1]["payTypeName"] == "保证金" # 支付方式
                assert r.json()["data"]["list"][1]["remark"] == None # 备注
                assert r.json()["data"]["list"][1]["mortgageOrderNo"] == "无" # 关联单号
        
        step_mgmt_inventory_deposit_pageList()
