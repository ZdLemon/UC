# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
from setting import P1, P2, P3, username, mobile, store, username_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
import datetime


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/credit/addApply")
class TestClass:
    """
    顾客信用额列表-审核
    /mgmt/fin/wallet/credit/auditApply
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P1)
    @allure.title("审核-成功路径: 审核主路径检查")
    @pytest.mark.parametrize("auditStatus,ids", [(2, "已通过"), (3, "已驳回")])
    def test_01_mgmt_fin_wallet_credit_auditApply(self, auditStatus, ids, credit_addApply_isCommit):
        
        getApplyList = credit_addApply_isCommit # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-审核")
        def step_mgmt_fin_wallet_credit_auditApply():
        
            if auditStatus == 2:
                data = {
                    "auditStatus": auditStatus, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                    "auditRemark": f"同意信用额申请", # 审批备注
                    "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
                    "creditEffectTime": (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S") # 生效时间"2022-06-10 14:00:00"
                }
            elif auditStatus == 3:
                data = {
                    "auditStatus": auditStatus, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                    "auditRemark": f"不同意信用额申请", # 审批备注
                    "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
                    "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
                }
            with _mgmt_fin_wallet_credit_auditApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认审核状态")
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
                if auditStatus == 2:
                    assert r.json()["data"]["list"][0]["auditStatus"] == 2 # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                    assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                    assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                elif auditStatus == 3:
                    assert r.json()["data"]["list"][0]["auditStatus"] == 3 # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
                    assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已驳回" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                    assert r.json()["data"]["list"][0]["effectStatusDesc"] == "已生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额'

        step_mgmt_fin_wallet_credit_auditApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P1)
    @allure.title("审核-成功路径: 审核后到生效时间生效检查")
    def test_02_mgmt_fin_wallet_credit_auditApply(self, credit_addApply_isCommit):
        
        getApplyList = credit_addApply_isCommit # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-审核")
        def step_mgmt_fin_wallet_credit_auditApply():
        
            data = {
                "auditStatus": 2, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "auditRemark": f"同意信用额申请", # 审批备注
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
                "creditEffectTime": (datetime.datetime.now()+datetime.timedelta(seconds=2)).strftime("%Y-%m-%d %H:%M:%S") # 生效时间"2022-06-10 14:00:00"
            }
            with _mgmt_fin_wallet_credit_auditApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认审核生效状态")
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
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                # assert r.json()["data"]["list"][0]["effectStatusDesc"] == "已生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额'

        step_mgmt_fin_wallet_credit_auditApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("审核-成功路径: 审核后未到生效时间不生效检查")
    def test_03_mgmt_fin_wallet_credit_auditApply(self, credit_addApply_isCommit):
        
        getApplyList = credit_addApply_isCommit # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-审核")
        def step_mgmt_fin_wallet_credit_auditApply():
        
            data = {
                "auditStatus": 2, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "auditRemark": f"同意信用额申请", # 审批备注
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
                "creditEffectTime": (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S") # 生效时间"2022-06-10 14:00:00"
            }
            with _mgmt_fin_wallet_credit_auditApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认审核未生效状态")
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
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额'

        step_mgmt_fin_wallet_credit_auditApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P2)
    @allure.title("批量审核-成功路径: 待审核和其他状态申请批量审核后状态")
    @pytest.mark.parametrize("auditStatus", [2, 3, 7])
    def test_04_mgmt_fin_wallet_credit_auditApply(self, auditStatus, credit_addApply_notCommit, credit_addApply_isCommit):
        
        getApplyList = credit_addApply_isCommit
        getApplyList02 = {}
        
        @allure.step("单个信用额列表查询")
        @stepreruns()
        def step_01_mgmt_fin_wallet_credit_getApplyList():
            
            nonlocal getApplyList02
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
                getApplyList02 = r.json()["data"]["list"][0]

        @allure.step("顾客信用额列表-审核")
        def step_mgmt_fin_wallet_credit_auditApply():
        
            data = {
                "auditStatus": 2, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
                "auditRemark": f"同意信用额申请", # 审批备注
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"], getApplyList02["walletCreditApplyId"]], # 顾客信用额申请id集合
                "creditEffectTime": (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S") # 生效时间"2022-06-10 14:00:00"
            }
            with _mgmt_fin_wallet_credit_auditApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
 
        @allure.title("单个信用额列表查询:确认审核未生效状态")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
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
                assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
                assert r.json()["data"]["list"][0]["applyAmount"] == getApplyList["applyAmount"] # applyAmount
                assert r.json()["data"]["list"][0]["currentApplyAmount"] == getApplyList["currentApplyAmount"] # 现有信用额
                assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == getApplyList["adjustedApplyAmount"] # 调整后信用额'
                
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
                assert getApplyList02["walletCreditApplyId"] in [i["walletCreditApplyId"] for i in r.json()["data"]["list"]]

        step_01_mgmt_fin_wallet_credit_getApplyList()
        step_mgmt_fin_wallet_credit_auditApply()
        step_mgmt_fin_wallet_credit_getApplyList()
        step_02_mgmt_fin_wallet_credit_getApplyList()


