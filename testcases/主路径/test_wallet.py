# coding:utf-8

from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
from api.mall_center_pay._pay_notify_mockPaySuccess import _pay_notify_mockPaySuccess # 银联支付回调

from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
from api.mall_mobile_application._mobile_wallet_updateWalletPasswordInfo import _mobile_wallet_updateWalletPasswordInfo # 更新支付管理信息
from api.mall_mobile_application._mobile_wallet_sendSmsCode import _mobile_wallet_sendSmsCode # 发送短信验证码
from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息

from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import _mgmt_fin_wallet_applyAdjust # 手工录入款项审核-提交
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import _mgmt_fin_wallet_getAdjustList # 手工录入款项审核-列表
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import _mgmt_fin_wallet_getAdjustDetail # 手工录入款项审核-详情
from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust # 手工录入款项审核-审核

from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
from api.mall_mobile_application._mobile_wallet_queryMemberSignBankCard import _mobile_wallet_queryMemberSignBankCard # 获取用户签约的银行卡及详情信息
from api.mall_mobile_application._mobile_wallet_recharge import _mobile_wallet_recharge # 个人钱包充值

from api.mall_mobile_application._mobile_wallet_getBankCardInfo import _mobile_wallet_getBankCardInfo # 获取用户绑定的银行卡及详情信息
from api.mall_mobile_application._mobile_member_getProvideBankByCardNo import _mobile_member_getProvideBankByCardNo # 查询劳务发放银行卡信息
from api.mall_mobile_application._mobile_wallet_applyWalletWithdraw import _mobile_wallet_applyWalletWithdraw # 申请钱包提现
from api.mall_mgmt_application._mgmt_fin_wallet_getWithdrawList import data as data02, _mgmt_fin_wallet_getWithdrawList # 余额提现审批-列表
from api.mall_mgmt_application._mgmt_fin_wallet_auditTransferWithdraw import _mgmt_fin_wallet_auditTransferWithdraw # 余额提现审批-汇款
from api.mall_mobile_application._mobile_wallet_bind_bindPersonInfoList import _mobile_wallet_bind_bindPersonInfoList # 绑定银行卡-获取绑定人信息
from api.mall_mobile_application._mobile_wallet_bind_bank_card import _mobile_wallet_bind_bank_card # 绑定银行卡
from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表

from api.mall_mgmt_application._mgmt_fin_wallet_getTransDetail import _mgmt_fin_wallet_getTransDetail # 完美钱包管理-交易详情
from api.mall_mgmt_application._mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans import _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans # 查询分公司银行流水(商城后台)
from api.mall_mgmt_application._mgmt_pay_verifyAcct_query import _mgmt_pay_verifyAcct_query # 查询支付渠道对账结果信息
from api.mall_mgmt_application._mgmt_fin_wallet_fee_queryFinWalletFee import _mgmt_fin_wallet_fee_queryFinWalletFee # 手续费明细表查询(商城后台)
from api.mall_mgmt_application._mgmt_inventory_detail import _mgmt_inventory_detail # 查询库存明细
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_mortgageAmountChangePageList import _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList # 服务中心账款管理 -- 押货余额详情(详情分页列表)
from api.mall_mgmt_application._mgmt_fin_voucher_getSecondCouponGetDetail import _mgmt_fin_voucher_getSecondCouponGetDetail # 秒返券获券明细
   
from setting import USERNAME02, username, name, username_vip, name_vip, store, store_85, productCode_02, username_85, store13, store85, productCode_SecondCoupon, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pytest
import time
import allure
import random, string
import datetime

# 充值-银联-签约工行-签约邮储
# 提现-VIP顾客
# 手工录入流水 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他

# 钱包充值提现

@allure.title("云商-银联-充值-103元")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/wallet/recharge")
def test_wallet_recharge_yuns_103():   

    getCurrentUserInfo = None # 个人用户信息
    rechargeAmount = 103 # 充值金额 
    wallet_recharge = None # 个人钱包充值
    token = os.environ["token_icbc"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]
     
    @allure.step("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": rechargeAmount, # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": rechargeAmount, # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
  
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_recharge()
    step_pay_notify_mockPaySuccess()

    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
        
    @allure.step("完美钱包详情表-充值")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 1, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 1 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "充值" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == "" # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 1 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "汇入" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == rechargeAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 1, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == rechargeAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 1 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "充值" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 手续费明细表
    listStore = None # 获取服务中心列表
    
    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : getCurrentUserInfo["leaderStoreCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : None,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : None,  # int是否总店 1总店 2分店
            "level" : None,  # int星级
            "companyCode" : None,  # str所属分公司编号 吉林分公司
            "isServiceShop" : None,  # int是否服务网店
            "isSignContract" : None,  # int是否签订合同
            "areaCode" : "",  # str区县code
            "cityCode" : "",  # str城市code
            "provinceCode" : "",  # str省份code
            "ratifyDate" : None,  # str批准最早时间
            "ratifyDate" : None,  #  str批准最晚时间
            "regionCode" : "",   #
            "ratifyEndTime" : None,  #
            "ratifyStartTime" : None,   #
            "pageNum": 1,  # int页码
            "pageSize": 10,  # int页数量
            "businessMode": None # 保证金类型，1/1:3，2/85%
        }
        with _mgmt_store_listStore(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listStore = r.json()["data"]["list"][0]

    @allure.step("手续费明细表查询(商城后台)")
    def step_mgmt_fin_wallet_fee_queryFinWalletFee():
        
        data = {
            "feeMonth": time.strftime("%Y-%m",time.localtime(time.time())), # 月份
            "companyCode":None, # 分公司编码
            "cardNo": wallet_getList["cardNo"], # 顾客卡号
            "feeType":None, # 手续费类型，101：微信；102：支付宝；103：银联；201：工商银行；202：建设银行；203：邮政存蓄银行；204：交通银行；205：平安代扣
            "memberType": wallet_getList["cardType"], # 会员类型 会员类别：1->普通顾客；2->优惠顾客；3->云商；4->微店（云+）；5->店员；6->子账号
            "pageNum":1,
            "pageSize":10
        }
        with _mgmt_fin_wallet_fee_queryFinWalletFee(data, access_token) as r:
            assert r.json()["data"]["list"][0]["feeMonth"] == time.strftime("%Y-%m",time.localtime(time.time()))  # 所属月份
            assert r.json()["data"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["list"][0]["realname"] == wallet_getList["realname"] # 姓名
            assert r.json()["data"]["list"][0]["storeCode"] == getCurrentUserInfo["leaderStoreCode"] # 店号
            assert r.json()["data"]["list"][0]["leaderCardNo"] == listStore["leaderCardNo"] # 负责人卡号
            assert r.json()["data"]["list"][0]["leaderName"] == listStore["leaderName"] # 负责人姓名
            assert r.json()["data"]["list"][0]["feeType"] == 103 # 手续费类型
            assert r.json()["data"]["list"][0]["feeTypeDesc"] == "银联" # 手续费类型
            assert r.json()["data"]["list"][0]["transAmount"] == rechargeAmount # 金额
            assert r.json()["data"]["list"][0]["refundFlag"] == False # 是否退款
            assert r.json()["data"]["list"][0]["transFee"] == 0 # 银行实际交易手续费
            assert r.json()["data"]["list"][0]["orderNoList"] is None # 订单编号
            assert r.json()["data"]["list"][0]["feeNo"].startswith(f"FE{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
    
    step_mgmt_store_listStore()
    step_mgmt_fin_wallet_fee_queryFinWalletFee()


@allure.title("云商-签约工行-充值-201元")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/wallet/recharge")
def test_wallet_recharge_yuns_201():   

    getCurrentUserInfo = None # 个人用户信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    rechargeAmount = 201 # 充值金额 
    wallet_recharge = None # 个人钱包充值
    token = os.environ["token_icbc"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("是否设置了支付密码")   
    def step_mobile_wallet_queryPasswordExist():
        
        nonlocal queryPasswordExist
        with _mobile_wallet_queryPasswordExist(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryPasswordExist = r.json()["data"]

    @allure.step("发送短信验证码")    
    def step_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"1", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.step("更新支付管理信息")    
    def step_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": getCurrentUserInfo["memberType"],
            "password": "123456",
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666"
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.step("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": rechargeAmount, # 实付金额
            "channelCode": 201, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": rechargeAmount, # 充值金额
            "walletPassword": "123456", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_queryPasswordExist()
    step_mobile_wallet_sendSmsCode()
    step_mobile_wallet_updateWalletPasswordInfo()
    step_mobile_wallet_getDetail()
    step_mobile_wallet_recharge()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    queryMemberSignBankCard = None # 获取用户签约的银行卡及详情信息
    access_token = os.environ["access_token_2"]
    
    @allure.step("获取用户签约的银行卡及详情信息")
    def test_mobile_wallet_queryMemberSignBankCard():
    
        nonlocal queryMemberSignBankCard                 
        with _mobile_wallet_queryMemberSignBankCard(token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryMemberSignBankCard = r.json()["data"][0]

    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-充值")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 1, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 1 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "充值" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] == queryMemberSignBankCard["bankAccount"] # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 1 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "汇入" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == rechargeAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == queryMemberSignBankCard["bankName"] # 支付方式

    test_mobile_wallet_queryMemberSignBankCard()
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 1, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == rechargeAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 1 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "充值" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] == queryMemberSignBankCard["bankAccount"] # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == queryMemberSignBankCard["bankType"] # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == queryMemberSignBankCard["bankName"] # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 手续费明细表
    listStore = None # 获取服务中心列表
    
    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : getCurrentUserInfo["leaderStoreCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : None,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : None,  # int是否总店 1总店 2分店
            "level" : None,  # int星级
            "companyCode" : None,  # str所属分公司编号 吉林分公司
            "isServiceShop" : None,  # int是否服务网店
            "isSignContract" : None,  # int是否签订合同
            "areaCode" : "",  # str区县code
            "cityCode" : "",  # str城市code
            "provinceCode" : "",  # str省份code
            "ratifyDate" : None,  # str批准最早时间
            "ratifyDate" : None,  #  str批准最晚时间
            "regionCode" : "",   #
            "ratifyEndTime" : None,  #
            "ratifyStartTime" : None,   #
            "pageNum": 1,  # int页码
            "pageSize": 10,  # int页数量
            "businessMode": None # 保证金类型，1/1:3，2/85%
        }
        with _mgmt_store_listStore(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listStore = r.json()["data"]["list"][0]

    @allure.step("手续费明细表查询(商城后台)")
    def step_mgmt_fin_wallet_fee_queryFinWalletFee():
        
        data = {
            "feeMonth": time.strftime("%Y-%m",time.localtime(time.time())), # 月份
            "companyCode":None, # 分公司编码
            "cardNo": wallet_getList["cardNo"], # 顾客卡号
            "feeType":None, # 手续费类型，101：微信；102：支付宝；103：银联；201：工商银行；202：建设银行；203：邮政存蓄银行；204：交通银行；205：平安代扣
            "memberType": wallet_getList["cardType"], # 会员类型 会员类别：1->普通顾客；2->优惠顾客；3->云商；4->微店（云+）；5->店员；6->子账号
            "pageNum":1,
            "pageSize":10
        }
        with _mgmt_fin_wallet_fee_queryFinWalletFee(data, access_token) as r:
            assert r.json()["data"]["list"][0]["feeMonth"] == time.strftime("%Y-%m",time.localtime(time.time()))  # 所属月份
            assert r.json()["data"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["list"][0]["realname"] == wallet_getList["realname"] # 姓名
            assert r.json()["data"]["list"][0]["storeCode"] == getCurrentUserInfo["leaderStoreCode"] # 店号
            assert r.json()["data"]["list"][0]["leaderCardNo"] == listStore["leaderCardNo"] # 负责人卡号
            assert r.json()["data"]["list"][0]["leaderName"] == listStore["leaderName"] # 负责人姓名
            assert r.json()["data"]["list"][0]["feeType"] == queryMemberSignBankCard["payWayId"] # 手续费类型
            assert r.json()["data"]["list"][0]["feeTypeDesc"] == queryMemberSignBankCard["bankName"] # 手续费类型
            assert r.json()["data"]["list"][0]["transAmount"] == rechargeAmount # 金额
            assert r.json()["data"]["list"][0]["refundFlag"] == False # 是否退款
            assert r.json()["data"]["list"][0]["transFee"] == 0 # 银行实际交易手续费
            assert r.json()["data"]["list"][0]["orderNoList"] is None # 订单编号
            assert r.json()["data"]["list"][0]["feeNo"].startswith(f"FE{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
    
    step_mgmt_store_listStore()
    step_mgmt_fin_wallet_fee_queryFinWalletFee()
  

@allure.title("云商-签约邮储-充值-203元")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/wallet/recharge")
def test_wallet_recharge_yuns_203():   

    getCurrentUserInfo = None # 个人用户信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    rechargeAmount = 203 # 充值金额 
    wallet_recharge = None # 个人钱包充值
    token = os.environ["token_psbc"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.title("是否设置了支付密码")   
    def step_mobile_wallet_queryPasswordExist():
        
        nonlocal queryPasswordExist
        with _mobile_wallet_queryPasswordExist(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryPasswordExist = r.json()["data"]

    @allure.title("发送短信验证码")    
    def step_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"1", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.title("更新支付管理信息")    
    def step_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": getCurrentUserInfo["memberType"],
            "password": "123456",
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666"
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": rechargeAmount, # 实付金额
            "channelCode": 203, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": rechargeAmount, # 充值金额
            "walletPassword": "123456", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_queryPasswordExist()
    step_mobile_wallet_sendSmsCode()
    step_mobile_wallet_updateWalletPasswordInfo()
    step_mobile_wallet_getDetail()
    step_mobile_wallet_recharge()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    queryMemberSignBankCard = None # 获取用户签约的银行卡及详情信息
    access_token = os.environ["access_token_2"]
    
    @allure.step("获取用户签约的银行卡及详情信息")
    def test_mobile_wallet_queryMemberSignBankCard():
    
        nonlocal queryMemberSignBankCard                 
        with _mobile_wallet_queryMemberSignBankCard(token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryMemberSignBankCard = r.json()["data"][0]

    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-充值")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 1, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 1 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "充值" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] == queryMemberSignBankCard["bankAccount"] # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 1 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "汇入" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == rechargeAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == queryMemberSignBankCard["bankName"] # 支付方式

    test_mobile_wallet_queryMemberSignBankCard()
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 1, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == rechargeAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 1 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "充值" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] == queryMemberSignBankCard["bankAccount"] # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == queryMemberSignBankCard["bankType"] # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == queryMemberSignBankCard["bankName"] # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 手续费明细表
    listStore = None # 获取服务中心列表
    
    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : getCurrentUserInfo["leaderStoreCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : None,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : None,  # int是否总店 1总店 2分店
            "level" : None,  # int星级
            "companyCode" : None,  # str所属分公司编号 吉林分公司
            "isServiceShop" : None,  # int是否服务网店
            "isSignContract" : None,  # int是否签订合同
            "areaCode" : "",  # str区县code
            "cityCode" : "",  # str城市code
            "provinceCode" : "",  # str省份code
            "ratifyDate" : None,  # str批准最早时间
            "ratifyDate" : None,  #  str批准最晚时间
            "regionCode" : "",   #
            "ratifyEndTime" : None,  #
            "ratifyStartTime" : None,   #
            "pageNum": 1,  # int页码
            "pageSize": 10,  # int页数量
            "businessMode": None # 保证金类型，1/1:3，2/85%
        }
        with _mgmt_store_listStore(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listStore = r.json()["data"]["list"][0]

    @allure.step("手续费明细表查询(商城后台)")
    def step_mgmt_fin_wallet_fee_queryFinWalletFee():
        
        data = {
            "feeMonth": time.strftime("%Y-%m",time.localtime(time.time())), # 月份
            "companyCode":None, # 分公司编码
            "cardNo": wallet_getList["cardNo"], # 顾客卡号
            "feeType":None, # 手续费类型，101：微信；102：支付宝；103：银联；201：工商银行；202：建设银行；203：邮政存蓄银行；204：交通银行；205：平安代扣
            "memberType": wallet_getList["cardType"], # 会员类型 会员类别：1->普通顾客；2->优惠顾客；3->云商；4->微店（云+）；5->店员；6->子账号
            "pageNum":1,
            "pageSize":10
        }
        with _mgmt_fin_wallet_fee_queryFinWalletFee(data, access_token) as r:
            assert r.json()["data"]["list"][0]["feeMonth"] == time.strftime("%Y-%m",time.localtime(time.time()))  # 所属月份
            assert r.json()["data"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["list"][0]["realname"] == wallet_getList["realname"] # 姓名
            assert r.json()["data"]["list"][0]["storeCode"] == getCurrentUserInfo["leaderStoreCode"] # 店号
            assert r.json()["data"]["list"][0]["leaderCardNo"] == listStore["leaderCardNo"] # 负责人卡号
            assert r.json()["data"]["list"][0]["leaderName"] == listStore["leaderName"] # 负责人姓名
            assert r.json()["data"]["list"][0]["feeType"] == queryMemberSignBankCard["payWayId"] # 手续费类型
            assert r.json()["data"]["list"][0]["feeTypeDesc"] == queryMemberSignBankCard["bankName"] # 手续费类型
            assert r.json()["data"]["list"][0]["transAmount"] == rechargeAmount # 金额
            assert r.json()["data"]["list"][0]["refundFlag"] == False # 是否退款
            assert r.json()["data"]["list"][0]["transFee"] == 0 # 银行实际交易手续费
            assert r.json()["data"]["list"][0]["orderNoList"] is None # 订单编号
            assert r.json()["data"]["list"][0]["feeNo"].startswith(f"FE{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
    
    step_mgmt_store_listStore()
    step_mgmt_fin_wallet_fee_queryFinWalletFee()


@allure.title("VIP顾客-提现-1元")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/wallet/applyWalletWithdraw")
def test_applyWalletWithdraw():
   
    
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
    step_mobile_wallet_getBankCardInfo()
    step_mobile_wallet_applyWalletWithdraw()
    step_mgmt_fin_wallet_getWithdrawList()
    step_mgmt_fin_wallet_auditTransferWithdraw()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]

    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-提现")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 4, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 6 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "提现" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] == getBankCardInfo["bankAccount"] # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == "" # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 6 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "提现" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -float(withdrawAmount) # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 6, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "VIP会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -float(withdrawAmount) # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 6 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "提现" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] == getBankCardInfo["bankAccount"] # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] is None # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] is None # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()
          

# 手工录入流水 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他

@allure.title("手工录入流水-还欠款1元")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/applyAdjust")
def test_applyAdjust_1():
    
    getCurrentUserInfo = None # 个人用户信息
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    getDetail = None # 获取钱包首页相关信息
    adjustAmount = 1 # 还欠款1元
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]
  
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

    @allure.step("手工录入流水")            
    def step_mgmt_fin_wallet_applyAdjust():

        data = {
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 1, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'还欠款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意还欠款 {adjustAmount}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_getDetail()
    step_01_mgmt_fin_wallet_getAdjustList()
    if getAdjustList: # 是否有待审核的手工录入款
        for id in getAdjustList:
            step_01_mgmt_fin_wallet_getAdjustDetail()
            step_01_mgmt_fin_wallet_auditAdjust()
    step_mgmt_fin_wallet_applyAdjust()
    step_mgmt_fin_wallet_getAdjustList()
    step_mgmt_fin_wallet_getAdjustDetail()
    step_mgmt_fin_wallet_auditAdjust()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-手工录入流水-还欠款")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 9, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 9 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "还欠款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 9 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "汇入" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == adjustAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 9, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 2, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == adjustAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 9 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "还欠款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] is None # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] is None # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()
        

@allure.title("手工录入流水-补银行流水2元")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/applyAdjust")
def test_applyAdjust_2():
    
    getCurrentUserInfo = None # 个人用户信息
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    getDetail = None # 获取钱包首页相关信息
    adjustAmount = 2 # 补银行流水2元
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]
  
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

    @allure.step("手工录入流水")            
    def step_mgmt_fin_wallet_applyAdjust():

        data = {
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "transMethod": 203, # 邮政储蓄银行
            "type": 2, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'补银行流水 {adjustAmount}元'
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
        data["auditRemark"] = f'同意补银行流水 {adjustAmount}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_getDetail()
    step_01_mgmt_fin_wallet_getAdjustList()
    if getAdjustList: # 是否有待审核的手工录入款
        for id in getAdjustList:
            step_01_mgmt_fin_wallet_getAdjustDetail()
            step_01_mgmt_fin_wallet_auditAdjust()
    step_mgmt_fin_wallet_applyAdjust()
    step_mgmt_fin_wallet_getAdjustList()
    step_mgmt_fin_wallet_getAdjustDetail()
    step_mgmt_fin_wallet_auditAdjust()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-手工录入流水-补银行流水")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 10, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 10 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "补银行流水" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 10 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "汇入" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == adjustAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "邮政储蓄银行" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 10, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 2, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == adjustAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 10 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "补银行流水" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "PSBC" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "邮政储蓄银行" # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()
        

@allure.title("手工录入流水-手工退款-3元")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/applyAdjust")
def test_applyAdjust_3():

    getCurrentUserInfo = None # 个人用户信息
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    getDetail = None # 获取钱包首页相关信息
    adjustAmount = -3 # 手工退款3元
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]
  
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

    @allure.step("手工录入流水")            
    def step_mgmt_fin_wallet_applyAdjust():

        data = {
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 3, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'手工退款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意手工退款 {adjustAmount}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_getDetail()
    step_01_mgmt_fin_wallet_getAdjustList()
    if getAdjustList: # 是否有待审核的手工录入款
        for id in getAdjustList:
            step_01_mgmt_fin_wallet_getAdjustDetail()
            step_01_mgmt_fin_wallet_auditAdjust()
    step_mgmt_fin_wallet_applyAdjust()
    step_mgmt_fin_wallet_getAdjustList()
    step_mgmt_fin_wallet_getAdjustDetail()
    step_mgmt_fin_wallet_auditAdjust()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-手工录入流水-手工退款")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 11, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 11 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "手工退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 11 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == adjustAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 11, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 2, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == adjustAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 11 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "手工退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] is None # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] is None # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()


@allure.title("手工录入流水-押货款与钱包互转4元")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/applyAdjust")
def test_applyAdjust_4():

    getCurrentUserInfo = None # 个人用户信息
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    getDetail = None # 获取钱包首页相关信息
    adjustAmount = 4 # 押货款与钱包互转4元
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]
  
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

    @allure.step("手工录入流水")            
    def step_mgmt_fin_wallet_applyAdjust():

        data = {
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 4, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'押货款与钱包互转 {adjustAmount}元'
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
        data["auditRemark"] = f'押货款与钱包互转 {adjustAmount}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_getDetail()
    step_01_mgmt_fin_wallet_getAdjustList()
    if getAdjustList: # 是否有待审核的手工录入款
        for id in getAdjustList:
            step_01_mgmt_fin_wallet_getAdjustDetail()
            step_01_mgmt_fin_wallet_auditAdjust()
    step_mgmt_fin_wallet_applyAdjust()
    step_mgmt_fin_wallet_getAdjustList()
    step_mgmt_fin_wallet_getAdjustDetail()
    step_mgmt_fin_wallet_auditAdjust()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-手工录入流水-押货款与钱包互转")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 12, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 12 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "押货款与钱包互转" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 12 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "转款" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == adjustAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 12, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 2, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == adjustAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 12 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "押货款与钱包互转" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] is None # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] is None # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()
        

@allure.title("手工录入流水-其他5元")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/applyAdjust")
def test_applyAdjust_5():
    
    getCurrentUserInfo = None # 个人用户信息
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    getDetail = None # 获取钱包首页相关信息
    adjustAmount = 5 # 其他5元
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]
  
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

    @allure.step("手工录入流水")            
    def step_mgmt_fin_wallet_applyAdjust():

        data = {
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他 {adjustAmount}元'
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
        data["auditRemark"] = f'其他 {adjustAmount}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_getDetail()
    step_01_mgmt_fin_wallet_getAdjustList()
    if getAdjustList: # 是否有待审核的手工录入款
        for id in getAdjustList:
            step_01_mgmt_fin_wallet_getAdjustDetail()
            step_01_mgmt_fin_wallet_auditAdjust()
    step_mgmt_fin_wallet_applyAdjust()
    step_mgmt_fin_wallet_getAdjustList()
    step_mgmt_fin_wallet_getAdjustDetail()
    step_mgmt_fin_wallet_auditAdjust()
    
    # 完美钱包详情

    wallet_getList = None # 完美钱包管理-列表
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal wallet_getList
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": None, # 	分公司编号
            "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }                   
        with _mgmt_fin_wallet_getList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_getList = r.json()["data"]["list"][0]
             
    @allure.step("完美钱包详情表-手工录入流水-其他")
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": wallet_getList["walletId"], # 钱包id
            "reportField": None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": None, # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            "backstageTransType": 13, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": None, # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }     
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 13 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "其他" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] is None # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 13 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "其他" # 前端交易类型 1:汇入, 2:,汇入,3:退货,6:提现,7:退款,8:购货,9:汇入,10:汇入,11:退款,12:转款,13:其他,14:信用额增加,15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == adjustAmount # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": wallet_getList["companyNo"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": wallet_getList["cardNo"], # 会员卡号
            "mobile": "", # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 13, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 2, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == wallet_getList["companyNo"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == wallet_getList["cardNo"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == wallet_getList["realname"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == wallet_getList["cardType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == wallet_getList["cardTypeDesc"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == adjustAmount # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 13 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "其他" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] is None # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] is None # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()
        
