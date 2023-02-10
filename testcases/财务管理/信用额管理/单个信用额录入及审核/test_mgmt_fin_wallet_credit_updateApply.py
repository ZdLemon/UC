# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
from api.mall_mgmt_application._mgmt_fin_wallet_credit_updateApply import _mgmt_fin_wallet_credit_updateApply # 顾客信用额列表-修改
from setting import P1, P2, P3, username, mobile, store
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
import datetime


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/credit/updateApply")
class TestClass:
    """
    顾客信用额列表-修改
    /mgmt/fin/wallet/credit/updateApply
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("修改-成功路径: 修改主路径检查")
    def test_01_mgmt_fin_wallet_credit_updateApply(self, credit_addApply_notCommit):
        
        getApplyList = credit_addApply_notCommit # 单个信用额列表查询
        applyAmount_02 = credit_addApply_notCommit["applyAmount"] + 10

        @allure.step("顾客信用额列表-修改")
        def step_mgmt_fin_wallet_credit_updateApply():
        
            data = getApplyList
            data["applyAmount"] = applyAmount_02
            data["creditApplyId"] = getApplyList["walletCreditApplyId"]
            data["isCommit"] = 0 # 是否提交审核，1：是，0:否
            with _mgmt_fin_wallet_credit_updateApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("单个信用额列表查询:确认修改状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": getApplyList["cardNo"], # 会员卡号
                "auditStatus": 7, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][0]["auditStatus"] == 7 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待提交" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount_02 # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == 10 + getApplyList["adjustedApplyAmount"] # 调整后信用额

        step_mgmt_fin_wallet_credit_updateApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("修改-成功路径: 修改后提交审核状态检查")
    def test_02_mgmt_fin_wallet_credit_updateApply(self, credit_addApply_notCommit):
        
        getApplyList = credit_addApply_notCommit # 单个信用额列表查询
        applyAmount_02 = credit_addApply_notCommit["applyAmount"] + 10

        @allure.step("顾客信用额列表-修改")
        def step_mgmt_fin_wallet_credit_updateApply():
        
            data = getApplyList
            data["applyAmount"] = applyAmount_02
            data["creditApplyId"] = getApplyList["walletCreditApplyId"]
            data["isCommit"] = 1 # 是否提交审核，1：是，0:否
            with _mgmt_fin_wallet_credit_updateApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("单个信用额列表查询:确认修改状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": getApplyList["cardNo"], # 会员卡号
                "auditStatus": 1, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][0]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount_02 # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == 10 + getApplyList["adjustedApplyAmount"] # 调整后信用额
                    
        step_mgmt_fin_wallet_credit_updateApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("修改-成功路径: 负值修改后提交审核直接生效状态检查")
    def test_03_mgmt_fin_wallet_credit_updateApply(self, credit_addApply_notCommit):
        
        getApplyList = credit_addApply_notCommit # 单个信用额列表查询
        applyAmount_02 = credit_addApply_notCommit["applyAmount"] - 15

        @allure.step("顾客信用额列表-修改")
        def step_mgmt_fin_wallet_credit_updateApply():
        
            data = getApplyList
            data["applyAmount"] = applyAmount_02
            data["creditApplyId"] = getApplyList["walletCreditApplyId"]
            data["isCommit"] = 1 # 是否提交审核，1：是，0:否
            with _mgmt_fin_wallet_credit_updateApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("单个信用额列表查询:确认修改状态")
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
                assert r.json()["data"]["list"][0]["auditStatus"] == 2 # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "已生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount_02 # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == -15 + getApplyList["adjustedApplyAmount"] # 调整后信用额

        step_mgmt_fin_wallet_credit_updateApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("修改-失败路径: 仅支持待提交状态修改检查")
    @pytest.mark.parametrize("auditStatus", [1, 2, 3])
    def test_04_mgmt_fin_wallet_credit_updateApply(self, credit_addApply_isCommit, auditStatus):
        
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

        @allure.step("顾客信用额列表-修改")
        def step_mgmt_fin_wallet_credit_updateApply():
        
            data = getApplyList
            data["applyAmount"] = getApplyList["applyAmount"] + 5
            data["creditApplyId"] = getApplyList["walletCreditApplyId"]
            data["isCommit"] = 1 # 是否提交审核，1：是，0:否
            with _mgmt_fin_wallet_credit_updateApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 500
                assert r.json()["message"] == "修改信用申请待提交数据为空"

        @allure.title("单个信用额列表查询:确认修改不成功")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": auditStatus, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["walletCreditApplyId"] == getApplyList["walletCreditApplyId"]
                assert r.json()["data"]["list"][0]["auditStatus"] == getApplyList["auditStatus"] # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == getApplyList["auditStatusDesc"] # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == getApplyList["effectStatusDesc"] # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额

        step_01_mgmt_fin_wallet_credit_getApplyList()
        step_mgmt_fin_wallet_credit_updateApply()
        step_mgmt_fin_wallet_credit_getApplyList()




