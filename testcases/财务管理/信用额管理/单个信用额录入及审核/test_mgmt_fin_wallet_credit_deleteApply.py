# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
from api.mall_mgmt_application._mgmt_fin_wallet_credit_deleteApply import _mgmt_fin_wallet_credit_deleteApply # 顾客信用额列表-删除
from setting import P1, P2, P3, username, mobile, store
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
import datetime


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/credit/deleteApply")
class TestClass:
    """
    顾客信用额列表-删除
    /mgmt/fin/wallet/credit/deleteApply
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("删除-成功路径: 删除信用额检查")
    def test_01_mgmt_fin_wallet_credit_deleteApply(self, credit_addApply_notCommit):
        
        getApplyList = credit_addApply_notCommit # 单个信用额列表查询
        
        @allure.step("顾客信用额列表-删除")
        def step_mgmt_fin_wallet_credit_deleteApply():
        
            data = {
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_deleteApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "待生效批次删除成功，已生效批次不能删除已忽略"

        @allure.step("单个信用额列表查询:确认删除成功")
        @stepreruns()
        def step_mgmt_fin_wallet_credit_getApplyList():
            
            data = {
                "storeCode": None,
                "cardNo": None, # 会员卡号
                "auditStatus": 7, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
                "effectStatus": None, # 生效状态，1：未生效，2：已生效
                "effectTime": None, # 调整时间
                "pageNum": 1,
                "pageSize": 10
            }                 
            with _mgmt_fin_wallet_credit_getApplyList(data, self.access_token) as r:                
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    assert getApplyList["walletCreditApplyId"] not in [i["walletCreditApplyId"] for i in r.json()["data"]["list"]]
         
        step_mgmt_fin_wallet_credit_deleteApply()
        step_mgmt_fin_wallet_credit_getApplyList()

    @allure.severity(P3)
    @allure.title("删除-失败路径: 非待提交状态不允许删除检查")
    @pytest.mark.parametrize("auditStatus", [1, 2, 3])
    def test_02_mgmt_fin_wallet_credit_deleteApply(self, credit_addApply_isCommit, auditStatus):
        
        getApplyList = None # 单个信用额列表查询
        
        @allure.step("单个信用额列表查询")
        def step_01_mgmt_fin_wallet_credit_getApplyList():
            
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
                getApplyList = r.json()["data"]["list"][0]

        @allure.step("顾客信用额列表-删除")
        def step_mgmt_fin_wallet_credit_deleteApply():
        
            data = {
                "walletCreditApplyIdList": [getApplyList["walletCreditApplyId"]], # 顾客信用额申请id集合
            }
            with _mgmt_fin_wallet_credit_deleteApply(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "待生效批次删除成功，已生效批次不能删除已忽略"
        
        @allure.step("单个信用额列表查询:确认删除不成功")
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
        step_mgmt_fin_wallet_credit_deleteApply()
        step_02_mgmt_fin_wallet_credit_getApplyList()




