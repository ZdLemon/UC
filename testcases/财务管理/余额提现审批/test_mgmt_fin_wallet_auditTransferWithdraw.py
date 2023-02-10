# coding:utf-8

from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息

from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import _mgmt_fin_wallet_applyAdjust # 手工录入款项审核-提交
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import _mgmt_fin_wallet_getAdjustList # 手工录入款项审核-列表
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import _mgmt_fin_wallet_getAdjustDetail # 手工录入款项审核-详情
from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust # 手工录入款项审核-审核

from api.mall_mobile_application._mobile_wallet_getBankCardInfo import _mobile_wallet_getBankCardInfo # 获取用户绑定的银行卡及详情信息
from api.mall_mobile_application._mobile_member_getProvideBankByCardNo import _mobile_member_getProvideBankByCardNo # 查询劳务发放银行卡信息
from api.mall_mobile_application._mobile_wallet_applyWalletWithdraw import _mobile_wallet_applyWalletWithdraw # 申请钱包提现
from api.mall_mgmt_application._mgmt_fin_wallet_getWithdrawList import data as data02, _mgmt_fin_wallet_getWithdrawList # 余额提现审批-列表
from api.mall_mgmt_application._mgmt_fin_wallet_auditTransferWithdraw import _mgmt_fin_wallet_auditTransferWithdraw # 余额提现审批-汇款
from api.mall_mobile_application._mobile_wallet_bind_bindPersonInfoList import _mobile_wallet_bind_bindPersonInfoList # 绑定银行卡-获取绑定人信息
from api.mall_mobile_application._mobile_wallet_bind_bank_card import _mobile_wallet_bind_bank_card # 绑定银行卡
from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
   
from setting import P1, P2, P3, username_vip

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/getWithdrawList")
class TestClass:
    """
    余额提现审批-汇款
    /mgmt/fin/wallet/auditTransferWithdraw
    """
    def setup_class(self):
        self.access_token = os.environ["access_token_2"]
        self.vip_token = os.environ["vip_token_2"]
        self.walletWithdrawId = None
   
    @allure.severity(P2)
    @allure.title("余额提现审批汇款-成功路径: 汇款成功检查")
    def test_mgmt_fin_wallet_auditTransferWithdraw(self):
            
        getCurrentUserInfo = None # 个人用户信息
        walletWithdrawId = [] # 余额提现id
        getBankCardInfo = None  # 获取用户绑定的银行卡及详情信息
        bindPersonInfoList = None # 绑定银行卡-获取绑定人信息
        getDetail = None # 获取钱包首页相关信息
        withdrawAmount = "1.00" # 申请提现金额
        wallet_getList = None # 完美钱包管理-列表
        getAdjustList = [] # 手工录入款项审核-列表
        getAdjustDetail = None # 手工录入款项审核-详情
        token = os.environ["vip_token_2"] # 优惠顾客
        access_token = os.environ["access_token_2"]

        @allure.step("个人用户信息")
        def step_mobile_personalInfo_getCurrentUserInfo():

            nonlocal getCurrentUserInfo
            with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCurrentUserInfo = r.json()["data"]

        @allure.step( "余额提现审批列表:获取余额提现id")   
        def step_01_mgmt_fin_wallet_getWithdrawList():
            
            nonlocal walletWithdrawId
            data = deepcopy(data02)   
            data["cardNo"] = getCurrentUserInfo["cardNo"] 
            data["withdrawStatus"] = 2 # 提现状态,0:全部，1：待审核；2：待受理；4：汇款成功；5：汇款失败；6：已撤销               
            with _mgmt_fin_wallet_getWithdrawList(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"]== 200 
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:              
                        walletWithdrawId.append(d["walletWithdrawId"])

        @allure.step("余额提现审批:汇款成功")      
        def step_01_mgmt_fin_wallet_auditTransferWithdraw():
            
            data = {
                "auditRemark": "", # 审批备注
                "remittanceRemark": "提现", # 汇款备注
                "status": 2, # 审核状态-用于审核，撤销：2：通过；6：不通过；6：撤销
                "transferStatus": 4, # 汇款状态-用于汇款成功，汇款失败：4：汇款成功，5：汇款失败。
                "walletWithdrawId": id # 余额提现id
            }                 
            with _mgmt_fin_wallet_auditTransferWithdraw(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"]== 200 
            
        @allure.step("获取用户绑定的银行卡及详情信息")    
        def step_mobile_wallet_getBankCardInfo():

            nonlocal getBankCardInfo
            with _mobile_wallet_getBankCardInfo(token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    for d in r.json()["data"]:
                        if d["labourBankAccount"] == 1: # 是否劳务收入账号 0:劳务绑定 1:非劳务绑定
                            getBankCardInfo = d  

        @allure.step("查询劳务发放银行卡信息")  
        def step_mobile_member_getProvideBankByCardNo():

            params = {
                "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
                "platform": 5,
            }
            with _mobile_member_getProvideBankByCardNo(params, token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200          

        @allure.step("是否设置了支付密码")  
        def step_mobile_wallet_queryPasswordExist():
            
            with _mobile_wallet_queryPasswordExist(token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("获取钱包首页相关信息")  
        def step_mobile_wallet_getDetail():
            
            nonlocal getDetail
            with _mobile_wallet_getDetail(token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getDetail = r.json()["data"]

        @allure.step("绑定银行卡-获取绑定人信息")    
        def step_mobile_wallet_bind_bindPersonInfoList():

            nonlocal bindPersonInfoList
            with _mobile_wallet_bind_bindPersonInfoList(token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                bindPersonInfoList = r.json()["data"][0]

        @allure.step( "绑定银行卡")                     
        def step_mobile_wallet_bind_bank_card():
            
            data = {
                "bindName": bindPersonInfoList["bindName"], # 绑定人姓名
                "bindIdcard": bindPersonInfoList["bindIdcard"], # 绑定人身份证
                "bankName":"中国银行", # 银行名称
                "bankCode":"01", # 银行编码
                "bankAccount":"622123654789", # 银行账号
                "bankProvinceCode":"110000000000", # 银行所属省编码
                "bankCityCode":"110100000000", # 银行所属市编码
                "province":"北京市", # 银行省
                "city":"北京市", # 银行市
                "bankBranchName":"解放路支行", # 开户行名称
                "maincardSpouse":0, # 是否主卡或配偶 0：主卡 1：配偶
                "labourBankAccount":1 # 劳务收入账号类型 0:劳务绑定 1:非劳务绑定
            }         
            with _mobile_wallet_bind_bank_card(data, token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step( "申请钱包提现")                     
        def step_mobile_wallet_applyWalletWithdraw():
            
            data = {
                "bankCardId": getBankCardInfo["id"], # 主键id
                "withdrawAmount": withdrawAmount # 申请提现金额
            }            
            with _mobile_wallet_applyWalletWithdraw(data, token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == "提现申请成功"

        @allure.step( "余额提现审批列表:获取余额提现id")   
        def step_mgmt_fin_wallet_getWithdrawList():
            
            nonlocal walletWithdrawId
            data = deepcopy(data02)   
            data["cardNo"] = getCurrentUserInfo["cardNo"]                
            with _mgmt_fin_wallet_getWithdrawList(data, access_token) as r:
                assert r.json()["code"]== 200                
                walletWithdrawId = r.json()["data"]["list"][0]["walletWithdrawId"]

        @allure.step("余额提现审批:汇款成功")      
        def step_mgmt_fin_wallet_auditTransferWithdraw():
            
            data = {
                "auditRemark": "", # 审批备注
                "remittanceRemark": "提现", # 汇款备注
                "status": 2, # 审核状态-用于审核，撤销：2：通过；6：不通过；6：撤销
                "transferStatus": 4, # 汇款状态-用于汇款成功，汇款失败：4：汇款成功，5：汇款失败。
                "walletWithdrawId": walletWithdrawId # 余额提现id
            }                 
            with _mgmt_fin_wallet_auditTransferWithdraw(data, access_token) as r:
                assert r.json()["code"]== 200

        # 清空钱包款
        
        @allure.step("完美钱包管理-列表")
        def step_mgmt_fin_wallet_getList():
            
            nonlocal wallet_getList
            data = {
                "storeCode": None,
                "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
                "mobile": None, # 顾客手机号
                "companyCode": None, # 	分公司编号：吉林分公司
                "cardTypeList": [2], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
                "creditEnable": None, # 是否有信用额
                "negativeEnable": None, # 钱包余额为负
                "pageNum": 1,
                "pageSize": 100
            }   
            with _mgmt_fin_wallet_getList(data, access_token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    wallet_getList = r.json()["data"]["list"][0]
                
        @allure.step("手工录入款项审核列表:是否有待审核的申请")
        def step_01_mgmt_fin_wallet_getAdjustList():
            
            nonlocal getAdjustList
            data = {
                "adjustStatus": 1, # 审批状态：1：待审核；2：已通过；3：已驳回，6：已撤回
                "adjustMonth": None, # 录入月份
                "mobile": None, # 普通过客手机号
                "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
                "companyCode": None, # 分公司编号
                "pageNum": 1,
                "pageSize": 10
            }                  
            with _mgmt_fin_wallet_getAdjustList(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getAdjustList.append(i["walletAdjustId"])

        @allure.title("手工录入款项审核-详情")
        def step_01_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = {
                "id": id
            }        
            with _mgmt_fin_wallet_getAdjustDetail(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAdjustDetail = r.json()["data"]

        @allure.title("手工录入款项审核-审核")
        def step_01_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = "同意手工录入申请"   
            data["walletAdjustId"] = id   
            with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("手工录入流水-其他款")            
        def step_mgmt_fin_wallet_applyAdjust():
            "手工录入流水-其他款"

            data = {
                "walletId": wallet_getList["walletId"] , # 钱包id
                "companyCode": getDetail["companyNo"], # 分公司
                "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
                "adjustAmount": 2 - getDetail["actualBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
                "adjustReason": f'其他款 {2 - getDetail["actualBalance"]}元'
            }          
            with _mgmt_fin_wallet_applyAdjust(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("手工录入款项审核-列表")      
        def step_mgmt_fin_wallet_getAdjustList():
            "手工录入款项审核-列表"
            
            nonlocal getAdjustList
            data = {
                "adjustStatus": 1, # 审批状态：1：待审核；2：已通过；3：已驳回，6：已撤回
                "adjustMonth": None, # 录入月份
                "mobile": None, # 普通过客手机号
                "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
                "companyCode": None, # 分公司编号
                "pageNum": 1,
                "pageSize": 10
            }        
            with _mgmt_fin_wallet_getAdjustList(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["adjustStatus"] == 1
                getAdjustList = r.json()["data"]["list"][0]["walletAdjustId"]

        @allure.step("手工录入款项审核-详情") 
        def step_mgmt_fin_wallet_getAdjustDetail():
            
            nonlocal getAdjustDetail
            params = {
                "id": getAdjustList
            }       
            with _mgmt_fin_wallet_getAdjustDetail(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAdjustDetail = r.json()["data"]

        @allure.step("手工录入款项审核-审核") 
        def step_mgmt_fin_wallet_auditAdjust():
            
            data = getAdjustDetail
            data["status"] = "2"
            data["auditRemark"] = f'同意其他款 {2 - getDetail["actualBalance"]}元' 
            data["walletAdjustId"] = getAdjustList
            with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
  
        step_mobile_personalInfo_getCurrentUserInfo()
        step_01_mgmt_fin_wallet_getWithdrawList()
        if walletWithdrawId: # 是否有待汇款的提现申请
            for id in walletWithdrawId:
                step_01_mgmt_fin_wallet_auditTransferWithdraw()
        step_mobile_wallet_getBankCardInfo()
        step_mobile_member_getProvideBankByCardNo()
        step_mobile_wallet_queryPasswordExist()
        step_mobile_wallet_getDetail()
        if getDetail["actualBalance"] <1: # 钱包是否有实际余额
            # 清空钱包款+信用额
            step_mgmt_fin_wallet_getList()
            step_01_mgmt_fin_wallet_getAdjustList()
            if getAdjustList: # 是否有待审核的手工录入款
                for id in getAdjustList:
                    step_01_mgmt_fin_wallet_getAdjustDetail()
                    step_01_mgmt_fin_wallet_auditAdjust()

            step_mobile_wallet_getDetail()
            if getDetail["actualBalance"] <1: # 钱包是否有实际余额
                step_mgmt_fin_wallet_applyAdjust()
                step_mgmt_fin_wallet_getAdjustList()
                step_mgmt_fin_wallet_getAdjustDetail()
                step_mgmt_fin_wallet_auditAdjust()   
        
        if getBankCardInfo is None:
            step_mobile_wallet_bind_bindPersonInfoList()
            step_mobile_wallet_bind_bank_card()
            step_mobile_wallet_getBankCardInfo()
        step_mobile_wallet_applyWalletWithdraw()
        step_mgmt_fin_wallet_getWithdrawList()
        step_mgmt_fin_wallet_auditTransferWithdraw()