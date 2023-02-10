# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
from api.mall_mgmt_application._mgmt_fin_wallet_credit_submitApply import _mgmt_fin_wallet_credit_submitApply # 顾客信用额列表-提交审核
from setting import P1, P2, P3, username, mobile, store
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
import datetime


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/credit/submitApply")
class TestClass:
    """
    顾客信用额列表-提交审核
    /mgmt/fin/wallet/credit/submitApply
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("提交审核-成功路径: 正数的待提交的申请提交审核后待审核状态检查")
    def test_01_mgmt_fin_wallet_credit_submitApply(self, credit_addApply_notCommit):
        
        getApplyList = credit_addApply_notCommit # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-提交审核")
        def step_mgmt_fin_wallet_credit_submitApply():
        
            data = {
                "auditStatus": 1, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_submitApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量提交审核成功，非待提交状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": getApplyList["cardNo"], # 会员卡号
                "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][0]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额

        step_mgmt_fin_wallet_credit_submitApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("提交审核-成功路径: 负数的待提交的申请提交审核后立即生效状态检查")
    def test_02_mgmt_fin_wallet_credit_submitApply(self, credit_addApply_notCommit_5):
        
        getApplyList = credit_addApply_notCommit_5 # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-提交审核")
        def step_mgmt_fin_wallet_credit_submitApply():
        
            data = {
                "auditStatus": 1, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_submitApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量提交审核成功，非待提交状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": getApplyList["cardNo"], # 会员卡号
                "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][0]["auditStatus"] == 2 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "已生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额

        step_mgmt_fin_wallet_credit_submitApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P3)
    @allure.title("提交审核-失败路径: 非待提交的申请不能提交审核检查")
    @pytest.mark.parametrize("auditStatus", [1, 2, 3])
    def test_03_mgmt_fin_wallet_credit_submitApply(self, credit_addApply_isCommit, auditStatus):
        
        getApplyList = None # 单个信用额列表查询
        
        @allure.step("单个信用额列表查询")
        def step_01_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": auditStatus, # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                 
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getApplyList = r.json()["data"]["list"][0]
       
        @allure.step("顾客信用额列表-提交审核")
        def step_mgmt_fin_wallet_credit_submitApply():
        
            data = {
                "auditStatus": 1, # 审核结果:1：待审核；2：已通过；3：审核不通过；7：待提交
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_submitApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量提交审核成功，非待提交状态记录已忽略"
 
        @allure.step("单个信用额列表查询:确认提交审核不成功")
        @stepreruns()
        def step_02_mgmt_fin_wallet_credit_getApplyList():
            
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": auditStatus, # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                 
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getApplyList["walletCreditApplyId"] in [i["walletCreditApplyId"] for i in r.json()["data"]["list"]]

        step_01_mgmt_fin_wallet_credit_getApplyList()
        step_mgmt_fin_wallet_credit_submitApply()
        step_02_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("批量提交审核-成功路径: 批量提交后状态检查")
    def test_04_mgmt_fin_wallet_credit_submitApply(self, credit_addApply_notCommit, credit_addApply_notCommit_85):
        
        getApplyList = credit_addApply_notCommit_85 # 单个信用额列表查询
        getApplyList02 = credit_addApply_notCommit # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-提交审核")
        def step_mgmt_fin_wallet_credit_submitApply():
        
            data = {
                "auditStatus": 1, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"], getApplyList02["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_submitApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量提交审核成功，非待提交状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][0]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额
                assert r.json()["data"]["list"][1]["walletCreditApplyId"] == getApplyList02["walletCreditApplyId"]
                assert r.json()["data"]["list"][1]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；4：不通过；7：待提交
                assert r.json()["data"]["list"][1]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][1]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][1]["applyAmount"] == getApplyList02["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][1]["currentApplyAmount"] == getApplyList02["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][1]["adjustedApplyAmount"] == getApplyList02["adjustedApplyAmount"] # 调整后信用额

        step_mgmt_fin_wallet_credit_submitApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("批量提交审核-成功路径: 待提交和其他状态申请批量提交后状态检查")
    @pytest.mark.parametrize("auditStatus", [1, 2, 3])
    def test_05_mgmt_fin_wallet_credit_submitApply(self, credit_addApply_notCommit_85, credit_addApply_notCommit, credit_addApply_isCommit, auditStatus):
        
        getApplyList = credit_addApply_notCommit_85 # 单个信用额列表查询
        getApplyList02 = credit_addApply_notCommit # 单个信用额列表查询
        getApplyList03 = None
        
        @allure.step("单个信用额列表查询")
        @stepreruns()
        def step_01_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList03
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": auditStatus, # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                 
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getApplyList03 = r.json()["data"]["list"][0]
       
        @allure.step("顾客信用额列表-提交审核")
        def step_mgmt_fin_wallet_credit_submitApply():
        
            data = {
                "auditStatus": 1, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"], getApplyList02["walletCreditApplyId"], getApplyList03["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_submitApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量提交审核成功，非待提交状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][2]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][2]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；4：不通过；7：待提交
                assert r.json()["data"]["list"][2]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][2]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][2]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][2]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][2]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额
                assert r.json()["data"]["list"][1]["walletCreditApplyId"] == getApplyList02["walletCreditApplyId"]
                assert r.json()["data"]["list"][1]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；4：不通过；7：待提交
                assert r.json()["data"]["list"][1]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][1]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][1]["applyAmount"] == getApplyList02["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][1]["currentApplyAmount"] == getApplyList02["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][1]["adjustedApplyAmount"] == getApplyList02["adjustedApplyAmount"] # 调整后信用额

        @allure.step("单个信用额列表查询:确认提交审核不成功")
        @stepreruns()
        def step_02_mgmt_fin_wallet_credit_getApplyList():
            
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": auditStatus, # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                 
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getApplyList03["walletCreditApplyId"] in [i["walletCreditApplyId"] for i in r.json()["data"]["list"]]

        step_01_mgmt_fin_wallet_credit_getApplyList()
        step_mgmt_fin_wallet_credit_submitApply()
        step_mgmt_fin_wallet_credit_getApplyList()
        step_02_mgmt_fin_wallet_credit_getApplyList()

