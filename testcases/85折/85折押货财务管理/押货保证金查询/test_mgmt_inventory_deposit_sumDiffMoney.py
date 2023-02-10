# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_deposit_sumDiffMoney import data, _mgmt_inventory_deposit_sumDiffMoney
from api.mall_mgmt_application._mgmt_inventory_deposit_pageList import data as data02, _mgmt_inventory_deposit_pageList
from api.mall_mgmt_application._mgmt_inventory_deposit_storeDepositDetail import data as data03, _mgmt_inventory_deposit_storeDepositDetail
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time

#TODO
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/sumDiffMoney")
class TestClass:
    """
    85折账款管理 -- 交易金额合计--保证金详情金额合计:搜索合计检查
    /mgmt/inventory/deposit/sumDiffMoney
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data03 = deepcopy(data03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("押货保证详情列表-合计: 查询交易日期检查")
    def test_01_mgmt_inventory_deposit_sumDiffMoney(self):
        
        data = deepcopy(self.data)
        data["startDay"] = f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01" # 当月第一天
        data["endDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天            
        with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
               
    @allure.severity(P2)
    @allure.title("押货保证详情列表-合计: 多选查询报表字段检查")
    @pytest.mark.parametrize("reportType", [[1], [2], [3], [1, 2], [1, 2, 3]], ids=["本期汇退款", "本期押货退押", "交付差额转入", "本期汇退款+本期押货退押", "本期汇退款+本期押货退押+交付差额转入"])
    def test_02_mgmt_inventory_deposit_sumDiffMoney(self, reportType):
        
        data = deepcopy(self.data)
        data["reportType"].extend(reportType) # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入              
        with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.severity(P2)
    @allure.title("押货保证详情列表-合计: 多选查询款项类型检查")
    @pytest.mark.parametrize("moneyType", [[1], [3], [7], [8], [9], [1, 3], [1, 3, 7], [7,8], [1, 3, 7, 8, 9]])
    def test_03_mgmt_inventory_deposit_sumDiffMoney(self, moneyType):
        
        data = deepcopy(self.data)
        data["moneyType"].extend(moneyType) # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移               
        with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("押货保证详情列表-合计: 多选查询交易类型检查")
    @pytest.mark.parametrize("dealType,dealTypeName", [([1], ["汇押货款"]), ([2], ["退押货款"]), ([3], ["其他"]), ([4], ["押货使用"]), ([5], ["押货退货"]), ([6], ["交付差额转入"]), ([9], ["押货保证金转移"]),( [1, 2], ["汇押货款", "退押货款"]), ([4, 5], ["押货使用", "押货退货"])])
    def test_04_mgmt_inventory_deposit_sumDiffMoney(self, dealType, dealTypeName):
        
        data = deepcopy(self.data)
        data["dealType"].extend(dealType) # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移                 
        with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                
    @allure.severity(P2)
    @allure.title("押货保证详情列表-合计: 查询关联单号或流水号检查")
    def test_05_mgmt_inventory_deposit_sumDiffMoney(self):
        
        mortgageOrderNo = None # 关联单号
        businessNo = None # 流水号
        mortgageOrderNo_diffMoney = 0 # 关联单号金额
        businessNo_diffMoney = 0 # 流水号金额
        
        @allure.step("押货保证详情列表:获取关联单号+流水号")
        def step_01_mgmt_inventory_deposit_storeDepositDetail():
            
            nonlocal mortgageOrderNo, businessNo
            data = deepcopy(self.data03)
            data["dealType"].extend([4]) # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移                 
            with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["mortgageOrderNo"] and d["businessNo"]:
                        mortgageOrderNo = d["mortgageOrderNo"]
                        businessNo = d["businessNo"]
                        break
        
        @allure.step("押货保证详情列表:获取交易金额合计")
        def step_02_mgmt_inventory_deposit_storeDepositDetail():
            
            nonlocal mortgageOrderNo_diffMoney, businessNo_diffMoney
            data = deepcopy(self.data03)
            for i in [mortgageOrderNo, businessNo]:
                data["mortgageOrderNoOrBusinessNo"] = i               
                with _mgmt_inventory_deposit_storeDepositDetail(data, self.access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if i == mortgageOrderNo:
                            mortgageOrderNo_diffMoney += d["diffMoney"]
                        elif i == businessNo:
                            businessNo_diffMoney += d["diffMoney"]
                        
        @allure.title("押货保证详情列表-合计")
        def step_mgmt_inventory_deposit_sumDiffMoney():
            
            data = deepcopy(self.data)
            for i in [mortgageOrderNo, businessNo]:
                data["mortgageOrderNoOrBusinessNo"] = i 
                with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r: 
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if i == mortgageOrderNo:
                        r.json()["data"] == mortgageOrderNo_diffMoney
                    elif i == businessNo:
                        r.json()["data"] ==  businessNo_diffMoney
        
        step_01_mgmt_inventory_deposit_storeDepositDetail()
        step_02_mgmt_inventory_deposit_storeDepositDetail()
        step_mgmt_inventory_deposit_sumDiffMoney()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/sumDiffMoney")
class TestClass02:
    """
    85折账款管理 -- 交易金额合计--保证金详情金额合计：合计和保证金列表字段关系检查
    /mgmt/inventory/deposit/sumDiffMoney
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("押货保证详情列表-合计: 报表字段=保证金列表相应字段金额检查")
    @pytest.mark.parametrize("reportType", [[1], [2], [3]], ids=["本期汇退款", "本期押货退押", "交付差额转入"])
    def test_01_mgmt_inventory_deposit_sumDiffMoney(self, reportType):
        
        pageList = None # 保证金列表字段信息
        
        @allure.step("85折押货保证金分页查询列表")
        def step_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data02)
            data["storeCode"] = store_85               
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]
        
        @allure.step("详情金额合计")
        def step_mgmt_inventory_deposit_sumDiffMoney():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85
            data["reportType"].extend(reportType) # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入              
            with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if reportType == 1:
                    assert r.json()["data"] == pageList["currentMonthRemitAndRefund"] # 本期汇/退款
                if reportType == 2:
                    assert r.json()["data"] == pageList["currentMonthMortgageAndReturn"] # 本期押货/退押
                if reportType == 3:
                    assert r.json()["data"] == pageList["currentTransferOrderIn"] # 交付差额转入
        
        step_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_sumDiffMoney()
        
    @allure.severity(P1)
    @allure.title("押货保证详情列表-合计: 所有款项类型合计=押货保证金列表本期汇退款检查")
    def test_02_mgmt_inventory_deposit_sumDiffMoney(self):
        
        pageList = None # 保证金列表字段信息
        
        @allure.step("85折押货保证金分页查询列表")
        def step_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data02)
            data["storeCode"] = store_85               
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]
        
        @allure.step("详情金额合计")
        def step_mgmt_inventory_deposit_sumDiffMoney():
            
            data = deepcopy(self.data)
            data["moneyType"].extend([1, 3, 7, 8, 9]) # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移   
            data["storeCode"] = store_85            
            with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == pageList["currentMonthRemitAndRefund"] # 本期汇/退款
        
        step_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_sumDiffMoney()

    @allure.severity(P1)
    @allure.title("押货保证详情列表-合计: 多选交易类型=押货保证金列表相应字段金额检查")
    @pytest.mark.parametrize("dealType,dealTypeName", [([1, 2, 3, 9], ["汇押货款,退押货款,其他,押货保证金转移"]), ([4, 5], ["押货使用,押货退货"]), ([6], ["交付差额转入"])])
    def test_03_mgmt_inventory_deposit_sumDiffMoney(self, dealType, dealTypeName):
        
        pageList = None # 保证金列表字段信息
        
        @allure.step("85折押货保证金分页查询列表")
        def step_mgmt_inventory_deposit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data02)
            data["storeCode"] = store_85               
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]
        
        @allure.step("详情金额合计")
        def step_mgmt_inventory_deposit_sumDiffMoney():
            data = deepcopy(self.data)
            data["dealType"].extend(dealType) # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移 
            data["storeCode"] = store_85                
            with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if dealType == [1, 2, 3, 9]:
                    assert r.json()["data"] == pageList["currentMonthRemitAndRefund"] # 本期汇/退款
                if dealType == [4, 5]:
                    assert r.json()["data"] == pageList["currentMonthMortgageAndReturn"] # 本期押货/退押
                if dealType == [6]:
                    assert r.json()["data"] == pageList["currentTransferOrderIn"] # 交付差额转入
                
    @allure.severity(P2)
    @allure.title("押货保证详情列表-合计: 交易类型=款项类型相应字段金额检查")
    @pytest.mark.parametrize("moneyType,dealType", [([1, 7], [1]), ([9],[9]), ([8], [2]), ([3], [3])])
    def test_04_mgmt_inventory_deposit_sumDiffMoney(self, moneyType, dealType):

        sumDiffMoney = None # 款项类型合计金额
        
        @allure.step("详情金额合计:款项类型")
        def step_01_mgmt_inventory_deposit_sumDiffMoney():
            
            nonlocal sumDiffMoney
            data = deepcopy(self.data)
            data["moneyType"].extend(moneyType) # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移 
            data["storeCode"] = store_85                
            with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                sumDiffMoney = r.json()["data"]
        
        @allure.step("详情金额合计:交易类型")
        def step_02_mgmt_inventory_deposit_sumDiffMoney():
            data = deepcopy(self.data)
            data["dealType"].extend(dealType) # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移 
            data["storeCode"] = store_85                
            with _mgmt_inventory_deposit_sumDiffMoney(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == sumDiffMoney
        
        step_01_mgmt_inventory_deposit_sumDiffMoney()
        step_02_mgmt_inventory_deposit_sumDiffMoney()
                


