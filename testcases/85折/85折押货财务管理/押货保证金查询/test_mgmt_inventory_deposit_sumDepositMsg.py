# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_deposit_pageList import data, _mgmt_inventory_deposit_pageList
from api.mall_mgmt_application._mgmt_inventory_deposit_sumDepositMsg import data as data02, _mgmt_inventory_deposit_sumDepositMsg

from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode, BASE_URL

from copy import deepcopy
import os
import allure
import pytest
import time
import uuid


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/deposit/sumDepositMsg")
class TestClass:
    """
    85折账款管理 -- 押货保证列表统计信息
    /mgmt/inventory/deposit/sumDepositMsg
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)

        self.store_token = os.environ["store_token_85"]
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("押货保证列表统计信息-成功路径: 各字段必须和列表各字段数据一致检查")
    @pytest.mark.skipif("test" in BASE_URL, reason="test环境没有月结，只能在uat环境测试")
    def test_mgmt_inventory_deposit_sumDepositMsg(self):
        
        lastMonthBalance = None # 上期可用结余
        currentMonthRemitAndRefund = None # 本期汇退款
        currentMonthMortgageAndReturn = None # 本期押货退押
        currentTransferOrderIn = None # 交付差额转入
        balance = None # 本期可用余额
                
        @allure.step("押货保证金列表各字段信息")
        @stepreruns()
        def step_mgmt_inventory_deposit_pageList():
            
            nonlocal lastMonthBalance, currentMonthRemitAndRefund, currentMonthMortgageAndReturn, currentTransferOrderIn, balance
            data = deepcopy(self.data)
            data["storeCode"] = store_85         
            with _mgmt_inventory_deposit_pageList(data, self.access_token) as r:
                lastMonthBalance = r.json()["data"]["list"][0]["lastMonthBalance"]
                currentMonthRemitAndRefund = r.json()["data"]["list"][0]["currentMonthRemitAndRefund"]
                currentMonthMortgageAndReturn = r.json()["data"]["list"][0]["currentMonthMortgageAndReturn"]
                currentTransferOrderIn = r.json()["data"]["list"][0]["currentTransferOrderIn"]
                balance = r.json()["data"]["list"][0]["balance"]
                assert balance == lastMonthBalance + currentMonthRemitAndRefund + currentMonthMortgageAndReturn + currentTransferOrderIn
                
        @allure.step("本期汇退款一致检查")
        @stepreruns()
        def step_mgmt_inventory_deposit_sumDepositMsg():
            
            data = deepcopy(self.data02)
            data["storeCode"] = store_85          
            with _mgmt_inventory_deposit_sumDepositMsg(data, self.access_token) as r: 
                assert r.json()["data"]["sumLastMonthBalance"] == lastMonthBalance or r.json()["data"]["sumLastMonthBalance"] is None
                assert r.json()["data"]["sumCurrentMonthRemitAndRefund"] == currentMonthRemitAndRefund or r.json()["data"]["sumCurrentMonthRemitAndRefund"] is None
                assert r.json()["data"]["sumCurrentMonthMortgageAndReturn"] == currentMonthMortgageAndReturn or r.json()["data"]["sumCurrentMonthMortgageAndReturn"] is None
                assert r.json()["data"]["sumCurrentTransferOrderIn"] == currentTransferOrderIn or r.json()["data"]["sumCurrentTransferOrderIn"] is None
                assert r.json()["data"]["sumBalance"] == balance or r.json()["data"]["sumBalance"] is None
       
        step_mgmt_inventory_deposit_pageList()
        step_mgmt_inventory_deposit_sumDepositMsg()
