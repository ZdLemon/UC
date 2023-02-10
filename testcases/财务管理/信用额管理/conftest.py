# coding:utf-8

from util.stepreruns import stepreruns
from setting import username, username_85
import os
from copy import deepcopy
import time
import pytest
import allure
import datetime


@pytest.fixture(scope="function")
@allure.title("新增信用额10元,并提交审核")
def credit_addApply_isCommit():
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
    
    access_token = os.environ["access_token_2"]
    getApplyList = None # 单个信用额列表查询
    getCreditAmountByCardNo = None # 根据会员卡号获取顾客姓名和现有信用额
    applyAmount = 10
    id = [] # 待审核的申请id
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_01_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal id
        data = {
            "storeCode": None,
            "cardNo": username, # 会员卡号
            "auditStatus": 1, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                 
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    id.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": id, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
            
    @allure.step("根据会员卡号获取顾客姓名和现有信用额")
    def step_mgmt_fin_wallet_getCreditAmountByCardNo():
        
        nonlocal getCreditAmountByCardNo
        params = {
            "cardNo": username
        }             
        with _mgmt_fin_wallet_getCreditAmountByCardNo(params, access_token) as r:
            assert r.json()["code"] == 200
            assert r.status_code == 200
            getCreditAmountByCardNo = r.json()["data"]
            
    @allure.step("顾客信用额列表-新增")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "applyAmount": applyAmount, # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCreditAmountByCardNo["realname"],
            "creditAmount": getCreditAmountByCardNo["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("单个信用额列表查询:确认新增状态")
    @stepreruns()
    def step_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal getApplyList
        data = {
            "storeCode": None,
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["auditStatus"] == 1 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待审核" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
            assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount # applyAmount
            assert r.json()["data"]["list"][0]["currentApplyAmount"] == getCreditAmountByCardNo["creditAmount"] # 现有信用额
            assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == applyAmount + getCreditAmountByCardNo["creditAmount"] # 调整后信用额
            getApplyList =  r.json()["data"]["list"][0]

    step_01_mgmt_fin_wallet_credit_getApplyList()
    if id:
        step_mgmt_fin_wallet_credit_auditApply()
            
    step_mgmt_fin_wallet_getCreditAmountByCardNo()
    step_mgmt_fin_wallet_credit_addApply()
    step_mgmt_fin_wallet_credit_getApplyList()
    
    return getApplyList


@pytest.fixture(scope="function")
@allure.title("新增信用额10元，不提交审核")
def credit_addApply_notCommit():
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
    
    access_token = os.environ["access_token_2"]
    getApplyList = None # 单个信用额列表查询
    getCreditAmountByCardNo = None # 根据会员卡号获取顾客姓名和现有信用额
    applyAmount = 10
    id = [] # 待审核的申请id
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_01_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal id
        data = {
            "storeCode": None,
            "cardNo": username, # 会员卡号
            "auditStatus": 1, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                 
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    id.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": id, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
            
    @allure.step("根据会员卡号获取顾客姓名和现有信用额")
    def step_mgmt_fin_wallet_getCreditAmountByCardNo():
        
        nonlocal getCreditAmountByCardNo
        params = {
            "cardNo": username
        }             
        with _mgmt_fin_wallet_getCreditAmountByCardNo(params, access_token) as r:
            assert r.json()["code"] == 200
            assert r.status_code == 200
            getCreditAmountByCardNo = r.json()["data"]
            
    @allure.step("顾客信用额列表-新增")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "applyAmount": applyAmount, # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCreditAmountByCardNo["realname"],
            "creditAmount": getCreditAmountByCardNo["creditAmount"], # 已有信用额
            "isCommit": 0 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("单个信用额列表查询:确认新增状态")
    @stepreruns()
    def step_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal getApplyList
        data = {
            "storeCode": None,
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["auditStatus"] == 7 # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
            assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待提交" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
            assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
            assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount # applyAmount
            assert r.json()["data"]["list"][0]["currentApplyAmount"] == getCreditAmountByCardNo["creditAmount"] # 现有信用额
            assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == applyAmount + getCreditAmountByCardNo["creditAmount"] # 调整后信用额
            getApplyList =  r.json()["data"]["list"][0]

    step_01_mgmt_fin_wallet_credit_getApplyList()
    if id:
        step_mgmt_fin_wallet_credit_auditApply()
            
    step_mgmt_fin_wallet_getCreditAmountByCardNo()
    step_mgmt_fin_wallet_credit_addApply()
    step_mgmt_fin_wallet_credit_getApplyList()
    
    return getApplyList


@pytest.fixture(scope="function")
@allure.title("新增信用额10元，不提交审核")
def credit_addApply_notCommit_85():
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
    
    access_token = os.environ["access_token_2"]
    getApplyList = None # 单个信用额列表查询
    getCreditAmountByCardNo = None # 根据会员卡号获取顾客姓名和现有信用额
    applyAmount = 10
    id = [] # 待审核的申请id
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_01_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal id
        data = {
            "storeCode": None,
            "cardNo": username_85, # 会员卡号
            "auditStatus": 1, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                 
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    id.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": id, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
            
    @allure.step("根据会员卡号获取顾客姓名和现有信用额")
    def step_mgmt_fin_wallet_getCreditAmountByCardNo():
        
        nonlocal getCreditAmountByCardNo
        params = {
            "cardNo": username_85
        }             
        with _mgmt_fin_wallet_getCreditAmountByCardNo(params, access_token) as r:
            assert r.json()["code"] == 200
            assert r.status_code == 200
            getCreditAmountByCardNo = r.json()["data"]
            
    @allure.step("顾客信用额列表-新增")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "applyAmount": applyAmount, # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCreditAmountByCardNo["realname"],
            "creditAmount": getCreditAmountByCardNo["creditAmount"], # 已有信用额
            "isCommit": 0 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("单个信用额列表查询:确认新增状态")
    @stepreruns()
    def step_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal getApplyList
        data = {
            "storeCode": None,
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["auditStatus"] == 7 # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
            assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待提交" # 审核状态：1：待审核；2：已通过；3：不通过；7：待提交
            assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
            assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount # applyAmount
            assert r.json()["data"]["list"][0]["currentApplyAmount"] == getCreditAmountByCardNo["creditAmount"] # 现有信用额
            assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == applyAmount + getCreditAmountByCardNo["creditAmount"] # 调整后信用额
            getApplyList =  r.json()["data"]["list"][0]

    step_01_mgmt_fin_wallet_credit_getApplyList()
    if id:
        step_mgmt_fin_wallet_credit_auditApply()
            
    step_mgmt_fin_wallet_getCreditAmountByCardNo()
    step_mgmt_fin_wallet_credit_addApply()
    step_mgmt_fin_wallet_credit_getApplyList()
    
    return getApplyList


@pytest.fixture(scope="function")
@allure.title("新增信用额-5元，并提交审核")
def credit_addApply_isCommit_5():
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
    
    access_token = os.environ["access_token_2"]
    getApplyList = None # 单个信用额列表查询
    getCreditAmountByCardNo = None # 根据会员卡号获取顾客姓名和现有信用额
    applyAmount = -5
    id = [] # 待审核的申请id
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_01_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal id
        data = {
            "storeCode": None,
            "cardNo": username, # 会员卡号
            "auditStatus": 1, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                 
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    id.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": id, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
            
    @allure.step("根据会员卡号获取顾客姓名和现有信用额")
    def step_mgmt_fin_wallet_getCreditAmountByCardNo():
        
        nonlocal getCreditAmountByCardNo
        params = {
            "cardNo": username
        }             
        with _mgmt_fin_wallet_getCreditAmountByCardNo(params, access_token) as r:
            assert r.json()["code"] == 200
            assert r.status_code == 200
            getCreditAmountByCardNo = r.json()["data"]
            
    @allure.step("顾客信用额列表-新增")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "applyAmount": applyAmount, # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCreditAmountByCardNo["realname"],
            "creditAmount": getCreditAmountByCardNo["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("单个信用额列表查询:确认新增状态")
    @stepreruns()
    def step_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal getApplyList
        data = {
            "storeCode": None,
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["auditStatus"] == 2 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            assert r.json()["data"]["list"][0]["auditStatusDesc"] == "已通过" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            assert r.json()["data"]["list"][0]["effectStatusDesc"] == "已生效" # 生效状态，1：未生效，2：已生效
            assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount # applyAmount
            assert r.json()["data"]["list"][0]["currentApplyAmount"] == getCreditAmountByCardNo["creditAmount"] # 现有信用额
            assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == applyAmount + getCreditAmountByCardNo["creditAmount"] # 调整后信用额
            getApplyList =  r.json()["data"]["list"][0]

    step_01_mgmt_fin_wallet_credit_getApplyList()
    if id:
        step_mgmt_fin_wallet_credit_auditApply()
            
    step_mgmt_fin_wallet_getCreditAmountByCardNo()
    step_mgmt_fin_wallet_credit_addApply()
    step_mgmt_fin_wallet_credit_getApplyList()
    
    return getApplyList


@pytest.fixture(scope="function")
@allure.title("新增信用额-5元，不提交审核")
def credit_addApply_notCommit_5():
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getCreditAmountByCardNo import _mgmt_fin_wallet_getCreditAmountByCardNo # 根据会员卡号获取顾客姓名和现有信用额
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
    from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
    
    access_token = os.environ["access_token_2"]
    getApplyList = None # 单个信用额列表查询
    getCreditAmountByCardNo = None # 根据会员卡号获取顾客姓名和现有信用额
    applyAmount = -5
    id = [] # 待审核的申请id
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_01_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal id
        data = {
            "storeCode": None,
            "cardNo": username, # 会员卡号
            "auditStatus": 1, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                 
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    id.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": id, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
            
    @allure.step("根据会员卡号获取顾客姓名和现有信用额")
    def step_mgmt_fin_wallet_getCreditAmountByCardNo():
        
        nonlocal getCreditAmountByCardNo
        params = {
            "cardNo": username
        }             
        with _mgmt_fin_wallet_getCreditAmountByCardNo(params, access_token) as r:
            assert r.json()["code"] == 200
            assert r.status_code == 200
            getCreditAmountByCardNo = r.json()["data"]
            
    @allure.step("顾客信用额列表-新增")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "applyAmount": applyAmount, # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCreditAmountByCardNo["realname"],
            "creditAmount": getCreditAmountByCardNo["creditAmount"], # 已有信用额
            "isCommit": 0 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("单个信用额列表查询:确认新增状态")
    @stepreruns()
    def step_mgmt_fin_wallet_credit_getApplyList():
        
        nonlocal getApplyList
        data = {
            "storeCode": None,
            "cardNo": getCreditAmountByCardNo["cardNo"], # 会员卡号
            "auditStatus": None, # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            "effectStatus": None, # 生效状态，1：未生效，2：已生效
            "effectTime": None, # 调整时间
            "pageNum": 1,
            "pageSize": 10
        }                
        with _mgmt_fin_wallet_credit_getApplyList(data, access_token) as r:                
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["auditStatus"] == 7 # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            assert r.json()["data"]["list"][0]["auditStatusDesc"] == "待提交" # 审核状态：1：待审核；2：已通过；9：不通过；7：待提交
            assert r.json()["data"]["list"][0]["effectStatusDesc"] == "未生效" # 生效状态，1：未生效，2：已生效
            assert r.json()["data"]["list"][0]["applyAmount"] == applyAmount # applyAmount
            assert r.json()["data"]["list"][0]["currentApplyAmount"] == getCreditAmountByCardNo["creditAmount"] # 现有信用额
            assert r.json()["data"]["list"][0]["adjustedApplyAmount"] == applyAmount + getCreditAmountByCardNo["creditAmount"] # 调整后信用额
            getApplyList =  r.json()["data"]["list"][0]

    step_01_mgmt_fin_wallet_credit_getApplyList()
    if id:
        step_mgmt_fin_wallet_credit_auditApply()
            
    step_mgmt_fin_wallet_getCreditAmountByCardNo()
    step_mgmt_fin_wallet_credit_addApply()
    step_mgmt_fin_wallet_credit_getApplyList()
    
    return getApplyList


