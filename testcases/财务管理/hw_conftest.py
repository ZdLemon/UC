# coding:utf-8

from api.basic_services._login import _login

from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search # 搜索商品
from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
from api.mall_mobile_application._mobile_order_carts_hasStore import _mobile_order_carts_hasStore # 云商/微店是否已开通服务中心
from api.mall_mobile_application._mobile_order_carts_canBuy import _mobile_order_carts_canBuy # 根据用户卡号查询购买信息
from api.mall_mobile_application._mobile_personalInfo_getMemberAddressList import _mobile_personalInfo_getMemberAddressList # 获取当前登录用户的配送地址列表接口
from api.mall_mobile_application._mobile_personalInfo_getRegInfosByParentCode import _mobile_personalInfo_getRegInfosByParentCode # 通过传parentCode获得相应的区域信息
from api.mall_mobile_application._mobile_personalInfo_addAddress import _mobile_personalInfo_addAddress # 新建会员配送地址
from api.mall_mobile_application._mobile_orderInfo_countOrderUpgrade import _mobile_orderInfo_countOrderUpgrade # 统计用户待升级订单
from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
from api.mall_center_pay._pay_notify_mockPaySuccess import _pay_notify_mockPaySuccess # 银联支付回调
from api.mall_mobile_application._mobile_payment_singlePay import _mobile_payment_singlePay # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息

from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
from api.mall_mobile_application._mobile_wallet_updateWalletPasswordInfo import _mobile_wallet_updateWalletPasswordInfo # 更新支付管理信息
from api.mall_mobile_application._mobile_wallet_sendSmsCode import _mobile_wallet_sendSmsCode # 发送短信验证码
from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
from api.mall_mobile_application._mobile_payment_getPayMethod import _mobile_payment_getPayMethod # 获取支付方式
from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay # 组合支付

from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import _mgmt_fin_wallet_applyAdjust # 手工录入款项审核-提交
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import _mgmt_fin_wallet_getAdjustList # 手工录入款项审核-列表
from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import _mgmt_fin_wallet_getAdjustDetail # 手工录入款项审核-详情
from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust # 手工录入款项审核-审核

from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 单个信用额列表查询
from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核

from api.mall_mobile_application._mobile_web_order_as_applyAfterSale import _mobile_web_order_as_applyAfterSale # 申请售后是否支持退货、换货、维修、返修
from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import _mobile_web_order_as_returnMonthVerify # 隔月退货验证
from api.mall_center_sys._mgmt_sys_getAllReNotice import _mgmt_sys_getAllReNotice # 获取退货须知集合
from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
from api.mall_mobile_application._mobile_web_order_return_getReturnType import _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import _mobile_web_order_as_upgradeOrderVerify # 升级单校验
from api.mall_mobile_application._mobile_order_return_applyReturn import _mobile_order_return_applyReturn # 申请退货/退款
from api.mall_mobile_application._mobile_web_order_return_getOrderReturnDetails import _mobile_web_order_return_getOrderReturnDetails # 获取退货详情

from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核
from api.mall_mobile_application._mobile_web_order_return_returnGoods import _mobile_web_order_return_returnGoods # 货品退回
from api.mall_mgmt_application._mgmt_order_return_auditGoods import _mgmt_order_return_auditGoods # 退货验货审核

from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
from api.mall_mgmt_application._mgmt_store_leader_getLeaderById import _mgmt_store_leader_getLeaderById # 根据ID获取负责人信息
from api.basic_services._auth_store_restPsw import _auth_store_restPsw # 重置服务中心密码
from api.mall_mgmt_application._mgmt_store_getStoreByCode import _mgmt_store_getStoreByCode # 根据服务中心编号获取服务中心
from api.mall_store_application._appStore_orderReturn_upgradeOrderVerify import _appStore_orderReturn_upgradeOrderVerify # 升级单校验
from api.mall_store_application._appStore_orderReturn_audit import _appStore_orderReturn_audit # 售后单审核

from api.mall_mobile_application._mobile_wallet_recharge import _mobile_wallet_recharge # 个人钱包充值

from api.mall_mobile_application._mobile_wallet_getBankCardInfo import _mobile_wallet_getBankCardInfo # 获取用户绑定的银行卡及详情信息
from api.mall_mobile_application._mobile_member_getProvideBankByCardNo import _mobile_member_getProvideBankByCardNo # 查询劳务发放银行卡信息
from api.mall_mobile_application._mobile_wallet_applyWalletWithdraw import _mobile_wallet_applyWalletWithdraw # 申请钱包提现
from api.mall_mgmt_application._mgmt_fin_wallet_getWithdrawList import data as data02, _mgmt_fin_wallet_getWithdrawList # 余额提现审批-列表
from api.mall_mgmt_application._mgmt_fin_wallet_auditTransferWithdraw import _mgmt_fin_wallet_auditTransferWithdraw # 余额提现审批-汇款
from api.mall_mobile_application._mobile_wallet_bind_bindPersonInfoList import _mobile_wallet_bind_bindPersonInfoList # 绑定银行卡-获取绑定人信息
from api.mall_mobile_application._mobile_wallet_bind_bank_card import _mobile_wallet_bind_bank_card # 绑定银行卡
from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
   
from setting import USERNAME02, username, name, username_vip, name_vip, store, store_85, productCode_02, username_85, store13, store85, productCode_SecondCoupon, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pytest
import time
import allure
import random, string
import datetime

@allure.title("username02 登录完美运营后台")
@pytest.fixture(scope="package", autouse=True)
def login_2():
    r = _login(username=USERNAME02).json()
    os.environ["access_token_2"] = r["data"]["access_token"]
    return r


@allure.title("普通顾客登录商城-吉林分公司")
@pytest.fixture(scope="package", autouse=True)
def puk_login_2(login_2):
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
    from api.mall_center_member._member_mgmt_getMemberInfoById import _member_mgmt_getMemberInfoById # 根据顾客ID获取顾客详细信息
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    
    
    access_token = os.environ["access_token_2"]
    wallet_getLists = [] # 完美钱包管理-列表
    getMemberInfoById = None # 据顾客ID获取顾客详细信息
    r = None

    @allure.step("完美钱包管理-列表")
    def step_mgmt_fin_wallet_getList():
        
        nonlocal wallet_getLists
        data = {
            "storeCode": None,
            "cardNo": None, # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": "04000", # 	分公司编号：吉林分公司
            "cardTypeList": [1], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
            "creditEnable": None, # 是否有信用额
            "negativeEnable": None, # 钱包余额为负
            "pageNum": 1,
            "pageSize": 10
        }   
        with _mgmt_fin_wallet_getList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                wallet_getLists = r.json()["data"]["list"]

    @allure.step("据顾客ID获取顾客详细信息")
    def step_member_mgmt_getMemberInfoById():
        
        nonlocal getMemberInfoById
        params = {
            "id": wallet_getList["memberId"],
        }     
        with _member_mgmt_getMemberInfoById(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getMemberInfoById =  r.json()["data"]
  
    @allure.step("普通顾客登录商城")
    def login_oauth_token():
        
        nonlocal r
        r = _login_oauth_token(username=getMemberInfoById["cardNo"]).json()
        os.environ["puk_token_2"] = r["data"]["access_token"]


    step_mgmt_fin_wallet_getList()
    for wallet_getList in wallet_getLists:
        step_member_mgmt_getMemberInfoById()
        if (getMemberInfoById["cardStatus"] != 1 or 2) and getMemberInfoById["mobiles"] is None: # 有效卡，且没有关联手机号
            login_oauth_token()
            break
        else:
            continue
    
    return r


@allure.title("优惠顾客登录商城-吉林分公司")
@pytest.fixture(scope="package", autouse=True)
def vip_login_2(login_2):
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
    from api.mall_center_member._member_mgmt_getMemberInfoById import _member_mgmt_getMemberInfoById # 根据顾客ID获取顾客详细信息
    from api.mall_center_member._member_mgmt_resetMemberPassword import _member_mgmt_resetMemberPassword # 重置会员密码
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    from api.mall_center_finance._fin_api_voucher_voucher_generate import _fin_api_voucher_voucher_generate # 给会员生成电子礼券
       
    access_token = os.environ["access_token_2"]
    wallet_getLists = [] # 完美钱包管理-列表
    getMemberInfoById = None # 据顾客ID获取顾客详细信息
    resetMemberPassword = None # 重置会员密码
    r = None
    token = None

    @allure.step("完美钱包管理-列表")
    def step_mgmt_fin_wallet_getList():
        
        nonlocal wallet_getLists
        data = {
            "storeCode": None,
            "cardNo": None, # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": "04000", # 	分公司编号：吉林分公司
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
                wallet_getLists = r.json()["data"]["list"]

    @allure.step("据顾客ID获取顾客详细信息")
    def step_member_mgmt_getMemberInfoById():
        
        nonlocal getMemberInfoById
        params = {
            "id": wallet_getList["memberId"],
        }     
        with _member_mgmt_getMemberInfoById(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getMemberInfoById =  r.json()["data"]
  
    @allure.step("重置会员密码")
    def step_member_mgmt_resetMemberPassword():
        
        nonlocal resetMemberPassword
        data = {
            "id": wallet_getList["memberId"], # ID，主账号传会员ID，子账号传子账号ID
        }   
        with _member_mgmt_resetMemberPassword(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            resetMemberPassword = r.json()["data"]

    @allure.step("优惠顾客登录商城")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=wallet_getList["cardNo"]).json()
        token = r["data"]["access_token"]
        os.environ["vip_token_2"] = r["data"]["access_token"]

    @allure.step("给会员生成电子礼券")
    def step_fin_api_voucher_voucher_generate():
        
        params = {
            "amount": 5,  # 金额
            "memberId": wallet_getList["memberId"],  #  int顾客id
            "beginTime": "2022-07-01 00:00:00",
            "endTime": "2023-07-01 00:00:00",
            "num": 1
        }  
        with _fin_api_voucher_voucher_generate(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_fin_wallet_getList()
    for wallet_getList in wallet_getLists:
        step_member_mgmt_getMemberInfoById()
        if getMemberInfoById["cardStatus"] == 0 and getMemberInfoById["mobiles"] is None: # 有效卡，且没有关联手机号
            step_member_mgmt_resetMemberPassword()
            login_oauth_token()
            step_fin_api_voucher_voucher_generate()
            break
        else:
            continue
    
    return r


@allure.title("优惠顾客登录商城-青岛分公司")
@pytest.fixture(scope="package", autouse=True)
def vip_login_3(login_2):
    
    from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
    from api.mall_center_member._member_mgmt_getMemberInfoById import _member_mgmt_getMemberInfoById # 根据顾客ID获取顾客详细信息
    from api.mall_center_member._member_mgmt_resetMemberPassword import _member_mgmt_resetMemberPassword # 重置会员密码
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    from api.mall_center_finance._fin_api_voucher_voucher_generate import _fin_api_voucher_voucher_generate # 给会员生成电子礼券
    
    
    access_token = os.environ["access_token_2"]
    companyCode = "05000" # 分公司：青岛分公司
    wallet_getLists = [] # 完美钱包管理-列表
    getMemberInfoById = None # 据顾客ID获取顾客详细信息
    resetMemberPassword = None # 重置会员密码
    r = None
    token = None

    @allure.step("完美钱包管理-列表")
    def step_mgmt_fin_wallet_getList():
        
        nonlocal wallet_getLists
        data = {
            "storeCode": None,
            "cardNo": None, # 会员卡号
            "mobile": None, # 顾客手机号
            "companyCode": companyCode, # 	分公司编号：吉林分公司
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
                wallet_getLists = r.json()["data"]["list"]

    @allure.step("据顾客ID获取顾客详细信息")
    def step_member_mgmt_getMemberInfoById():
        
        nonlocal getMemberInfoById
        params = {
            "id": wallet_getList["memberId"],
        }     
        with _member_mgmt_getMemberInfoById(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getMemberInfoById =  r.json()["data"]
  
    @allure.step("重置会员密码")
    def step_member_mgmt_resetMemberPassword():
        
        nonlocal resetMemberPassword
        data = {
            "id": wallet_getList["memberId"], # ID，主账号传会员ID，子账号传子账号ID
        }   
        with _member_mgmt_resetMemberPassword(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            resetMemberPassword = r.json()["data"]

    @allure.step("优惠顾客登录商城")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=wallet_getList["cardNo"]).json()
        token = r["data"]["access_token"]
        os.environ["vip_token_3"] = r["data"]["access_token"]

    @allure.step("给会员生成电子礼券")
    def step_fin_api_voucher_voucher_generate():
        
        params = {
            "amount": 5,  # 金额
            "memberId": wallet_getList["memberId"],  #  int顾客id
            "beginTime": "2022-07-01 00:00:00",
            "endTime": "2023-07-01 00:00:00",
            "num": 1
        }  
        with _fin_api_voucher_voucher_generate(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200


    step_mgmt_fin_wallet_getList()
    for wallet_getList in wallet_getLists:
        step_member_mgmt_getMemberInfoById()
        if getMemberInfoById["cardStatus"] == 0 and getMemberInfoById["mobiles"] is None: # 有效卡，且没有关联手机号
            step_member_mgmt_resetMemberPassword()
            login_oauth_token()
            # step_fin_api_voucher_voucher_generate()
            break
        else:
            continue
    
    return r


@allure.title("云商总店登录商城-吉林分公司-签约工行")
@pytest.fixture(scope="package", autouse=True)
def yunsh_login_ICBC(login_2):
    
    from api.mall_mgmt_application._mgmt_store_listBankAccount import _mgmt_store_listBankAccount # 银行账号列表
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.mall_mgmt_application._mgmt_store_clerk_page import _mgmt_store_clerk_page # 查询店员列表
    from api.mall_center_member._member_mgmt_getBusinessList import _member_mgmt_getBusinessList # 获取云商微店列表
    from api.mall_center_member._member_mgmt_getMemberInfoById import _member_mgmt_getMemberInfoById # 根据顾客ID获取顾客详细信息
    from api.mall_center_member._member_mgmt_resetMemberPassword import _member_mgmt_resetMemberPassword # 重置会员密码
    from api.mall_mgmt_application._mgmt_store_getByParms import _mgmt_store_getByParms # 根据常用条件查询服务中心
    from api.mall_mgmt_application._mgmt_store_updatePermission import _mgmt_store_updatePermission # 服务中心权限编辑修改
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
    from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
    from api.mall_mobile_application._mobile_wallet_queryMemberSignBankCard import _mobile_wallet_queryMemberSignBankCard # 获取用户签约的银行卡及详情信息
    from api.mall_mobile_application._mobile_wallet_sign_signPersonInfoList import _mobile_wallet_sign_signPersonInfoList # 签约银行卡-获取签约人信息
    from api.mall_mobile_application._mobile_wallet_sendSmsCode import _mobile_wallet_sendSmsCode # 发送短信验证码
    from api.mall_mobile_application._mobile_wallet_signBankCard import _mobile_wallet_signBankCard # 签约银行卡
    from api.mall_mobile_application._mobile_wallet_unSignBankCard import _mobile_wallet_unSignBankCard # 解约银行卡
    from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
    from api.mall_mobile_application._mobile_wallet_updateWalletPasswordInfo import _mobile_wallet_updateWalletPasswordInfo # 更新支付管理信息
    
    from api.mall_center_finance._fin_api_voucher_voucher_generate import _fin_api_voucher_voucher_generate # 给会员生成电子礼券
    
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreSimpleInfo import _mgmt_inventory_common_getStoreSimpleInfo # 获取服务中心简单信息
    from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
    from api.mall_mgmt_application._mgmt_inventory_common_getProductByCode import _mgmt_inventory_common_getProductByCode # 根据一或二级编码精确商品信息
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_addMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder # 后台申请添加押货换货单
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_addOpinion import _mgmt_inventory_exchangeOrder_addOpinion # 后台押货换货添加审批意见
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_exchangeOrderDetail import _mgmt_inventory_exchangeOrder_exchangeOrderDetail # 后台押货换货单详情
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder # 后台审批押货换货单
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_processMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder # 后台押货换货单退回处理
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder # 后台押货换货单验货
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder # 后台押货换货单发货
    from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder # 后台押货换确认收货
    
    access_token = os.environ["access_token_2"]
    companyCode = "04000" # 吉林分公司
    store_listStore = [] # 银行账号列表
    listStore = None # 获取服务中心列表
    clerk_page = None # 查询店员列表
    getBusinessList = None # 获取云商微店列表
    getMemberInfoById = None # 根据顾客ID获取顾客详细信息
    getByParms = None # 根据常用条件查询服务中心
    r = None
    token = None
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    queryMemberSignBankCard = None # 获取用户签约的银行卡及详情信息
    signPersonInfoList = None # 签约银行卡-获取签约人信息
    phoneNum = f"189{''.join(random.sample(string.digits, 8))}"
    queryPasswordExist = False # 是否设置了支付密码
    
    getStoreSimpleInfo = None # 获取服务中心简单信息
    getReason = None # 获取各种退换货原因
    getProductByCode = None # 根据一或二级编码精确商品信息
    productNum = 2 # 押货退货数量
    addMortgageExchangeOrder = None # 后台申请添加押货换货单
    addOpinion = None # 后台押货换货添加审批意见
    exchangeOrderDetail = None # 后台押货换货单详情

    @allure.step("银行账号列表")
    def step_mgmt_store_listBankAccount():
        
        nonlocal store_listStore
        params = {
            "opType": None, # 操作类型 1新增 2修改 3作废
            "verifyStatus": None, # 审核状态 3待审核, 不选则是全部
            "pageNum": 1, 
            "pageSize": 100,
            "storeCode": None, # 服务中心编号
            "isUsed": 1, # 作废标示 1生效 2作废
            "leaderCardNo": None, # 总店负责人卡号
            "isSigned": None, # 是否已签约，1/是，2/否
            "companyCode": companyCode # 分公司：吉林分公司
        }
        with _mgmt_store_listBankAccount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                store_listStore = r.json()["data"]["list"]

    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : store["storeCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : 1,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : 1,  # int是否总店 1总店 2分店
            "level" : None,  # int星级
            "companyCode" : companyCode,  # str所属分公司编号 吉林分公司
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
            "businessMode": 1 # 保证金类型，1/1:3，2/85%
        }
        with _mgmt_store_listStore(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"] and r.json()["data"]["list"][0]["del"] == 0:
                listStore = r.json()["data"]["list"][0]

    @allure.step("查询店员列表")
    def step_mgmt_store_clerk_page():
        
        nonlocal clerk_page
        params = {
            "storeCode": listStore["code"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_store_clerk_page(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                clerk_page = r.json()["data"]["list"]

    @allure.step("获取云商微店列表")
    def step_member_mgmt_getBusinessList():
        
        nonlocal getBusinessList
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "companyNo": None, # 分公司编号
            "cardNo": listStore["shopkeeperNo"], # 会员卡号
            "businessType": None, # 顾客类型：1->云商；2->微店（云+）
            "mobile": None, # 注册手机号
            "aboutMobile": None, # 关联手机号
            "status": None, # 状态：0->正常；1->异常
            "promotionType": None, # 新卡升级方式 1：产品升级 2：pv升级
            "registerMode": None, # 注册方式
            "openCardMode": None, # 开卡方式
            "selfIdCardVaildStatus": None, # 本人身份证认证状态 0：未验证; 1：已验证
            "spouseIdCardVaildStatus": None, # 配偶身份证认证状态 0：未验证; 1：已验证
            "mobileVaildStatus": None, # 手机认证状态 0：未验证; 1：已验证
            "promotionTimeStart": None, # 新卡升级时间开始
            "promotionTimeEnd":None, # 新卡升级时间结束
            "promotionTime": None, # 新卡升级时间开始
            "promotionTime": None, # 新卡升级时间结束
            "openCardTime": None, # 开卡时间
            "registrationTime": None, # 转换开始时间,转换结束时间
        }    
        with _member_mgmt_getBusinessList(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getBusinessList = r.json()["data"]["list"][0]

    @allure.step("根据顾客ID获取顾客详细信息")
    def step_member_mgmt_getMemberInfoById():
        
        nonlocal getMemberInfoById
        params = {
            "id": getBusinessList["memberId"],
        }    
        with _member_mgmt_getMemberInfoById(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberInfoById = r.json()["data"]

    @allure.step("重置会员密码")
    def step_member_mgmt_resetMemberPassword():
        
        data = {
            "id": getBusinessList["memberId"], # ID，主账号传会员ID，子账号传子账号ID
        }   
        with _member_mgmt_resetMemberPassword(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据常用条件查询服务中心")
    def step_mgmt_store_getByParms():
        
        nonlocal getByParms
        params = {
            "storeCode" : getBusinessList["rdcNo"],  # str服务中心编号
        }
        with _mgmt_store_getByParms(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getByParms = r.json()["data"][0]

    @allure.step("服务中心权限编辑修改")
    def step_mgmt_store_updatePermission():
        
        data = {
            "storeCode": getByParms["code"], # 服务中心编号
            "storeName":"",
            "leaderName": getByParms["leaderName"],
            "frozenTime":None, # 冻结时间
            "frozenReason":None, # 冻结原因
            "cancelTime": None, # 取消时间
            "permission":"1,2,3,4,5", # 1:3押货权限
            "businessMode": 1, 
            "shopType": 1 # 门店类型
        }
        with _mgmt_store_updatePermission(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("登录")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=getBusinessList["cardNo"]).json()
        token = r["data"]["access_token"]
        os.environ["token_icbc"] = r["data"]["access_token"]

    # 签约工行卡
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

    @allure.step("获取用户签约的银行卡及详情信息")
    def step_mobile_wallet_queryMemberSignBankCard():
        
        nonlocal queryMemberSignBankCard
        with _mobile_wallet_queryMemberSignBankCard(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                queryMemberSignBankCard = r.json()["data"][0]

    @allure.step("签约银行卡-获取签约人信息")
    def step_mobile_wallet_sign_signPersonInfoList():
        
        nonlocal signPersonInfoList
        with _mobile_wallet_sign_signPersonInfoList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            signPersonInfoList = r.json()["data"][0]

    @allure.step("发送短信验证码")
    def step_mobile_wallet_sendSmsCode():
        
        data = {
            "businessType": "4", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": phoneNum
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("签约银行卡")
    def step_mobile_wallet_signBankCard():
        
        data = {
            "bindName": signPersonInfoList["bindName"], # 签约人姓名
            "bindIdcard": signPersonInfoList["bindIdcard"], # 签约人身份证号
            "bankType": "ICBC", # 银行类别，ICBC：工商银行 PSBC：邮政储蓄银行
            "bankAccount": f"622{''.join(random.sample(string.digits, 10))}", # 银行账号
            "tel": phoneNum,
            "smsCode": "666666",
            "maincardSpouse": signPersonInfoList["maincardSpouse"] # 是否主卡或配偶 0：主卡 1：配偶
        }
        with _mobile_wallet_signBankCard(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("发送短信验证码")
    def step_02_mobile_wallet_sendSmsCode():
        
        data = {
            "businessType": "5", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": queryMemberSignBankCard["tel"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("解约银行卡")
    def step_mobile_wallet_unSignBankCard():
        
        data = {
            "bindName": queryMemberSignBankCard["bindName"], # 签约人姓名
            "bindIdcard": queryMemberSignBankCard["bindIdcard"], # 签约人身份证号
            "bankType": queryMemberSignBankCard["bankType"], # 银行类别，ICBC：工商银行 PSBC：邮政储蓄银行
            "bankAccount": queryMemberSignBankCard["bankAccount"], # 银行账号
            "tel": queryMemberSignBankCard["tel"],
            "smsCode": "666666",
            "maincardSpouse": queryMemberSignBankCard["maincardSpouse"], # 是否主卡或配偶 0：主卡 1：配偶
            "id": queryMemberSignBankCard["id"]
        }
        with _mobile_wallet_unSignBankCard(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("是否设置了支付密码")   
    def step_mobile_wallet_queryPasswordExist():
        
        nonlocal queryPasswordExist
        with _mobile_wallet_queryPasswordExist(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryPasswordExist = r.json()["data"]

    @allure.title("发送短信验证码")    
    def step_03_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"1", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.title("更新支付管理信息")    
    def step_03_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 3, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
            "password": "123456",
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666"
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("发送短信验证码")    
    def step_04_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"3", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.title("更新支付管理信息")    
    def step_04_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 1, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
            "password": "123456",
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666",
            "passwordFlag": False
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("更新支付管理信息")    
    def step_05_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 4, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    # 发放电子礼券 5元
    
    @allure.step("给会员生成电子礼券")
    def step_fin_api_voucher_voucher_generate():
        
        params = {
            "amount": 5,  # 金额
            "memberId": getBusinessList["memberId"],  #  int顾客id
            "beginTime": "2022-07-01 00:00:00",
            "endTime": "2023-07-01 00:00:00",
            "num": 1
        }  
        with _fin_api_voucher_voucher_generate(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 发放运费补贴券 15元
    
    @allure.step("获取服务中心简单信息")
    def step_mgmt_inventory_common_getStoreSimpleInfo():
        
        nonlocal getStoreSimpleInfo
        params = {
            "storeCode": getBusinessList["rdcNo"], # 服务中心编号
        }             
        with _mgmt_inventory_common_getStoreSimpleInfo(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreSimpleInfo = r.json()["data"]

    @allure.step("获取各种退换货原因")
    def step_mgmt_inventory_common_getReason():
        
        nonlocal getReason
        params = {
            "type": 4, 
        }             
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReason = r.json()["data"]

    @allure.step("根据一或二级编码精确商品信息")
    def step_mgmt_inventory_common_getProductByCode():
        
        nonlocal getProductByCode
        params = {
            "productCode": productCode_SecondCoupon, # 商品编码
        }              
        with _mgmt_inventory_common_getProductByCode(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getProductByCode = r.json()["data"]

    @allure.step("后台申请添加押货换货单")
    def step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder():
        
        nonlocal addMortgageExchangeOrder
        data = {
            "storeCode": getBusinessList["rdcNo"],
            "exchangeType": 1, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
            "orderFileUrl": "", # 换货单附件，支持3个，用逗号隔开
            "productDisposalType": "", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
            "reasonFirst": getReason[13]["returnReason"], # 一级原因
            "reasonFirstRemarks": "我是一级原因的备注信息哦", # 一级原因备注
            "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
            "reasonSecondRemarks": "我是二级原因的备注信息哦", # 二级原因备注
            "productVoList": [{
                "productCode": getProductByCode["productCode"], # 物品编号
                "title": getProductByCode["productName"],
                "packing": getProductByCode["productPacking"],
                "meterUnit": getProductByCode["productUnit"],
                "retailPrice": getProductByCode["retailPrice"], # 物品零售价
                "productNum": productNum, # 物品换货数
                "productProductionDate": "20220101", # 物品生产日期
                "productBatch": "12345", # 批次号
                "productSn": "", # 物品序列号/二维码
                "productProblemDesc": "进水了", # 问题描述
                "firstUseTime": "", # 第一次使用的时间
                "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                "securityPrice": 20,
                "productDisposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
            }]
        }           
        with _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addMortgageExchangeOrder = r.json()["data"]

    @allure.step("后台押货换货添加审批意见")
    def step_mgmt_inventory_exchangeOrder_addOpinion():
        
        nonlocal addOpinion
        data = {
            "orderId": addMortgageExchangeOrder, # 押货或售后单id
            "content": "业务部门同意押货先退后换" # 审批内容
        }           
        with _mgmt_inventory_exchangeOrder_addOpinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addOpinion = r.json()["data"]

    @allure.step("后台押货换货单详情")
    def step_mgmt_inventory_exchangeOrder_exchangeOrderDetail():
        
        nonlocal exchangeOrderDetail
        params = {
            "orderId": addMortgageExchangeOrder, # 押货或售后单id
        }          
        with _mgmt_inventory_exchangeOrder_exchangeOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            exchangeOrderDetail = r.json()["data"]

    @allure.step("后台审批押货换货单")
    def step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder():
        
        data = {
            "id": exchangeOrderDetail["orderVo"]["id"],
            "exchangeType": exchangeOrderDetail["orderVo"]["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
            "auditFileUrl": "", # 审批附件
            "auditFileName": "", # 审批附件名称
            "auditRemarks": "服务中心部门同意押货只换不退申请哦", # 审批备注
            "auditStatus": "1", # 审批意见 0不通过 1通过
            "productDisposalType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
            "reasonFirst": exchangeOrderDetail["orderVo"]["reasonFirst"], # 一级原因
            "reasonFirstRemarks": exchangeOrderDetail["orderVo"]["reasonFirstRemarks"], # 一级原因备注
            "reasonSecond": exchangeOrderDetail["orderVo"]["reasonSecond"], # 二级原因
            "reasonSecondRemarks": exchangeOrderDetail["orderVo"]["reasonSecondRemarks"], # 二级原因备注
            "productVoList": [{
                "id": exchangeOrderDetail["productVos"][0]["id"], # 物品记录id
                "productNum": exchangeOrderDetail["productVos"][0]["productNum"], # 物品换货数
                "dailyUseType": exchangeOrderDetail["productVos"][0]["dailyUseType"],
                "firstUseTime": exchangeOrderDetail["productVos"][0]["firstUseTime"],
                "happenType": exchangeOrderDetail["productVos"][0]["happenType"],
                "productBatch": exchangeOrderDetail["productVos"][0]["productBatch"], # 批次号
                "productProblemDesc": exchangeOrderDetail["productVos"][0]["productProblemDesc"], # 问题描述
                "productProductionDate": exchangeOrderDetail["productVos"][0]["productProductionDate"], # 物品生产日期
                "productSn": exchangeOrderDetail["productVos"][0]["productSn"], # 物品序列号/二维码
                "productDisposalType": exchangeOrderDetail["productVos"][0]["productDisposalType"] # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
            }],
            "returnInfo": exchangeOrderDetail["orderVo"]["returnAddress"] if exchangeOrderDetail["orderVo"]["returnAddress"] else "广州仓" # 退回信息
        }          
        with _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("后台押货换货单退回处理")
    def step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder():
        
        data = {
            "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            "expressAmount": 100, # 物流金额
            "expressCompany": "小河物流", # 快递公司
            "expressNo": "xh123456789", # 快递单号
            "expressProofUrl": "", # 快递凭证url
            "expressProofName": "", # 快递凭证名称
            "processRemarks": "这是我的报废图片", # 退回说明
            "returnType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 退回方式 1服务中心报废 2自带 3邮寄
            "disposalProofName": "", # 报废凭证名称,最多9个，逗号隔开
            "disposalProofUrl": "" # 报废凭证,最多9个，逗号隔开
        }         
        with _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("后台押货换货单验货")
    def step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder():
        
        data = {
            "expressSubsidy": 100, # 运费补贴
            "inspectRemarks": "仓库验货部门验货没问题", # 验货备注
            "inspectStatus": "1", # 验货结果 0不通过 1通过
            "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            "inspectProof": [] # 验货凭证
        }         
        with _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("后台押货换货单发货")
    def step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder():
        
        data = {
            "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
            "deliverType": 2, # 发货方式 1顾客自提 2邮寄
            "expressCompany": "小河物流", # 新品配送物流公司
            "expressNo": "xh123456" # 物流单号
        }  
        with _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("后台押货换确认收货")
    def step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder():
        
        data = {
            "id": exchangeOrderDetail["orderVo"]["id"], # 换货单id
        }  
        with _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_store_listBankAccount()
    for store in store_listStore:
        step_mgmt_store_listStore()
        if listStore is None:
            continue
        else:
            step_mgmt_store_clerk_page()
            if clerk_page:
                clerk_page = None
                continue
            else:
                step_member_mgmt_getBusinessList()
                step_member_mgmt_getMemberInfoById()
                if getMemberInfoById["cardStatus"] != 0 or getMemberInfoById["mobiles"]:
                    continue
                else:
                    step_member_mgmt_resetMemberPassword()
                    step_mgmt_store_getByParms()
                    step_mgmt_store_updatePermission()
                    login_oauth_token()
                    break
    
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_queryMemberSignBankCard()
    if queryMemberSignBankCard is None: # 是否已签约银行
        step_mobile_wallet_sign_signPersonInfoList()
        step_mobile_wallet_sendSmsCode()
        step_mobile_wallet_signBankCard()
    else:
        if queryMemberSignBankCard["bankType"] != "ICBC":
            step_02_mobile_wallet_sendSmsCode()
            step_mobile_wallet_unSignBankCard()
            step_mobile_wallet_sign_signPersonInfoList()
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_signBankCard()
    
    step_mobile_wallet_queryPasswordExist() # 设置支付密码
    if queryPasswordExist:
        step_03_mobile_wallet_sendSmsCode()
        step_03_mobile_wallet_updateWalletPasswordInfo()
    else:
        step_04_mobile_wallet_sendSmsCode()
        step_04_mobile_wallet_updateWalletPasswordInfo()

    step_mobile_wallet_getDetail()  
    if getDetail["passwordFlag"] == 1: # 是否免密，1：开启免密；2：关闭免密
        step_05_mobile_wallet_updateWalletPasswordInfo()
            
    step_fin_api_voucher_voucher_generate() # 发放电子礼券 5元
    # 发放运费补贴券 15元
    # 新建
    step_mgmt_inventory_common_getStoreSimpleInfo()
    step_mgmt_inventory_common_getReason()
    step_mgmt_inventory_common_getProductByCode()
    step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder()
    # 待审批
    step_mgmt_inventory_exchangeOrder_addOpinion()
    step_mgmt_inventory_exchangeOrder_exchangeOrderDetail()
    step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder()
    # 待退回
    step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder()
    # 待验货
    step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder()
    # 待发货
    step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder()
    # 确认收货
    step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder()
    
    return r
   

@allure.title("云商总店登录商城-青岛分公司-签约邮储")
@pytest.fixture(scope="package", autouse=True)
def yunsh_login_PSBC(login_2):
    
    from api.mall_mgmt_application._mgmt_store_listBankAccount import _mgmt_store_listBankAccount # 银行账号列表
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.mall_mgmt_application._mgmt_store_clerk_page import _mgmt_store_clerk_page # 查询店员列表
    from api.mall_center_member._member_mgmt_getBusinessList import _member_mgmt_getBusinessList # 获取云商微店列表
    from api.mall_center_member._member_mgmt_getMemberInfoById import _member_mgmt_getMemberInfoById # 根据顾客ID获取顾客详细信息
    from api.mall_center_member._member_mgmt_resetMemberPassword import _member_mgmt_resetMemberPassword # 重置会员密码
    from api.mall_mgmt_application._mgmt_store_getByParms import _mgmt_store_getByParms # 根据常用条件查询服务中心
    from api.mall_mgmt_application._mgmt_store_updatePermission import _mgmt_store_updatePermission # 服务中心权限编辑修改
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
    from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
    from api.mall_mobile_application._mobile_wallet_queryMemberSignBankCard import _mobile_wallet_queryMemberSignBankCard # 获取用户签约的银行卡及详情信息
    from api.mall_mobile_application._mobile_wallet_sign_signPersonInfoList import _mobile_wallet_sign_signPersonInfoList # 签约银行卡-获取签约人信息
    from api.mall_mobile_application._mobile_wallet_sendSmsCode import _mobile_wallet_sendSmsCode # 发送短信验证码
    from api.mall_mobile_application._mobile_wallet_signBankCard import _mobile_wallet_signBankCard # 签约银行卡
    from api.mall_mobile_application._mobile_wallet_unSignBankCard import _mobile_wallet_unSignBankCard # 解约银行卡
    from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
    from api.mall_mobile_application._mobile_wallet_updateWalletPasswordInfo import _mobile_wallet_updateWalletPasswordInfo # 更新支付管理信息
    
    from api.mall_center_finance._fin_api_voucher_voucher_generate import _fin_api_voucher_voucher_generate # 给会员生成电子礼券
    
    access_token = os.environ["access_token_2"]
    companyCode = "05000" # 分公司：青岛分公司
    store_listStore = [] # 银行账号列表
    listStore = None # 获取服务中心列表
    clerk_page = None # 查询店员列表
    getBusinessList = None # 获取云商微店列表
    getMemberInfoById = None # 根据顾客ID获取顾客详细信息
    getByParms = None # 根据常用条件查询服务中心
    r = None
    token = None
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    queryMemberSignBankCard = None # 获取用户签约的银行卡及详情信息
    signPersonInfoList = None # 签约银行卡-获取签约人信息
    phoneNum = f"189{''.join(random.sample(string.digits, 8))}"
    queryPasswordExist = False # 是否设置了支付密码

    @allure.step("银行账号列表")
    def step_mgmt_store_listBankAccount():
        
        nonlocal store_listStore
        params = {
            "opType": None, # 操作类型 1新增 2修改 3作废
            "verifyStatus": None, # 审核状态 3待审核, 不选则是全部
            "pageNum": 1, 
            "pageSize": 100,
            "storeCode": None, # 服务中心编号
            "isUsed": 1, # 作废标示 1生效 2作废
            "leaderCardNo": None, # 总店负责人卡号
            "isSigned": None, # 是否已签约，1/是，2/否
            "companyCode": companyCode # 分公司：青岛分公司
        }
        with _mgmt_store_listBankAccount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                store_listStore = r.json()["data"]["list"]

    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : store["storeCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : 1,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : 1,  # int是否总店 1总店 2分店
            "level" : None,  # int星级
            "companyCode" : companyCode,  # str所属分公司编号 吉林分公司
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
            "businessMode": 1 # 保证金类型，1/1:3，2/85%
        }
        with _mgmt_store_listStore(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"] and r.json()["data"]["list"][0]["del"] == 0:
                listStore = r.json()["data"]["list"][0]

    @allure.step("查询店员列表")
    def step_mgmt_store_clerk_page():
        
        nonlocal clerk_page
        params = {
            "storeCode": listStore["code"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_store_clerk_page(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                clerk_page = r.json()["data"]["list"]

    @allure.step("获取云商微店列表")
    def step_member_mgmt_getBusinessList():
        
        nonlocal getBusinessList
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "companyNo": None, # 分公司编号
            "cardNo": listStore["shopkeeperNo"], # 会员卡号
            "businessType": None, # 顾客类型：1->云商；2->微店（云+）
            "mobile": None, # 注册手机号
            "aboutMobile": None, # 关联手机号
            "status": None, # 状态：0->正常；1->异常
            "promotionType": None, # 新卡升级方式 1：产品升级 2：pv升级
            "registerMode": None, # 注册方式
            "openCardMode": None, # 开卡方式
            "selfIdCardVaildStatus": None, # 本人身份证认证状态 0：未验证; 1：已验证
            "spouseIdCardVaildStatus": None, # 配偶身份证认证状态 0：未验证; 1：已验证
            "mobileVaildStatus": None, # 手机认证状态 0：未验证; 1：已验证
            "promotionTimeStart": None, # 新卡升级时间开始
            "promotionTimeEnd":None, # 新卡升级时间结束
            "promotionTime": None, # 新卡升级时间开始
            "promotionTime": None, # 新卡升级时间结束
            "openCardTime": None, # 开卡时间
            "registrationTime": None, # 转换开始时间,转换结束时间
        }    
        with _member_mgmt_getBusinessList(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getBusinessList = r.json()["data"]["list"][0]

    @allure.step("根据顾客ID获取顾客详细信息")
    def step_member_mgmt_getMemberInfoById():
        
        nonlocal getMemberInfoById
        params = {
            "id": getBusinessList["memberId"],
        }    
        with _member_mgmt_getMemberInfoById(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberInfoById = r.json()["data"]

    @allure.step("重置会员密码")
    def step_member_mgmt_resetMemberPassword():
        
        data = {
            "id": getBusinessList["memberId"], # ID，主账号传会员ID，子账号传子账号ID
        }   
        with _member_mgmt_resetMemberPassword(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据常用条件查询服务中心")
    def step_mgmt_store_getByParms():
        
        nonlocal getByParms
        params = {
            "storeCode" : getBusinessList["rdcNo"],  # str服务中心编号
        }
        with _mgmt_store_getByParms(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getByParms = r.json()["data"][0]

    @allure.step("服务中心权限编辑修改")
    def step_mgmt_store_updatePermission():
        
        data = {
            "storeCode": getByParms["code"], # 服务中心编号
            "storeName":"",
            "leaderName": getByParms["leaderName"],
            "frozenTime":None, # 冻结时间
            "frozenReason":None, # 冻结原因
            "cancelTime": None, # 取消时间
            "permission":"1,2,3,4,5", # 1:3押货权限
            "businessMode": 1, 
            "shopType": 1 # 门店类型
        }
        with _mgmt_store_updatePermission(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("登录")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=getBusinessList["cardNo"]).json()
        token = r["data"]["access_token"]
        os.environ["token_psbc"] = r["data"]["access_token"]

    # 签约邮储
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

    @allure.step("获取用户签约的银行卡及详情信息")
    def step_mobile_wallet_queryMemberSignBankCard():
        
        nonlocal queryMemberSignBankCard
        with _mobile_wallet_queryMemberSignBankCard(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                queryMemberSignBankCard = r.json()["data"][0]

    @allure.step("签约银行卡-获取签约人信息")
    def step_mobile_wallet_sign_signPersonInfoList():
        
        nonlocal signPersonInfoList
        with _mobile_wallet_sign_signPersonInfoList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            signPersonInfoList = r.json()["data"][0]

    @allure.step("发送短信验证码")
    def step_mobile_wallet_sendSmsCode():
        
        data = {
            "businessType": "4", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": phoneNum
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("签约银行卡")
    def step_mobile_wallet_signBankCard():
        
        data = {
            "bindName": signPersonInfoList["bindName"], # 签约人姓名
            "bindIdcard": signPersonInfoList["bindIdcard"], # 签约人身份证号
            "bankType": "PSBC", # 银行类别，ICBC：工商银行 PSBC：邮政储蓄银行
            "bankAccount": f"622{''.join(random.sample(string.digits, 10))}", # 银行账号
            "tel": phoneNum,
            "smsCode": "666666",
            "maincardSpouse": signPersonInfoList["maincardSpouse"] # 是否主卡或配偶 0：主卡 1：配偶
        }
        with _mobile_wallet_signBankCard(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("发送短信验证码")
    def step_02_mobile_wallet_sendSmsCode():
        
        data = {
            "businessType": "5", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": queryMemberSignBankCard["tel"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("解约银行卡")
    def step_mobile_wallet_unSignBankCard():
        
        data = {
            "bindName": queryMemberSignBankCard["bindName"], # 签约人姓名
            "bindIdcard": queryMemberSignBankCard["bindIdcard"], # 签约人身份证号
            "bankType": queryMemberSignBankCard["bankType"], # 银行类别，ICBC：工商银行 PSBC：邮政储蓄银行
            "bankAccount": queryMemberSignBankCard["bankAccount"], # 银行账号
            "tel": queryMemberSignBankCard["tel"],
            "smsCode": "666666",
            "maincardSpouse": queryMemberSignBankCard["maincardSpouse"], # 是否主卡或配偶 0：主卡 1：配偶
            "id": queryMemberSignBankCard["id"]
        }
        with _mobile_wallet_unSignBankCard(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("是否设置了支付密码")   
    def step_mobile_wallet_queryPasswordExist():
        
        nonlocal queryPasswordExist
        with _mobile_wallet_queryPasswordExist(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryPasswordExist = r.json()["data"]

    @allure.title("发送短信验证码")    
    def step_03_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"1", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.title("更新支付管理信息")    
    def step_03_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 3, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
            "password": "123456",
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666"
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("发送短信验证码")    
    def step_04_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"3", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.title("更新支付管理信息")    
    def step_04_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 1, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
            "password": "123456",
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666",
            "passwordFlag": False
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("更新支付管理信息")    
    def step_05_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 4, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
       
    @allure.step("给会员生成电子礼券")
    def step_fin_api_voucher_voucher_generate():
        
        params = {
            "amount": 5,  # 金额
            "memberId": getBusinessList["memberId"],  #  int顾客id
            "beginTime": "2022-07-01 00:00:00",
            "endTime": "2023-07-01 00:00:00",
            "num": 1
        }  
        with _fin_api_voucher_voucher_generate(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    step_mgmt_store_listBankAccount()
    for store in store_listStore:
        step_mgmt_store_listStore()
        if listStore is None:
            continue
        else:
            step_mgmt_store_clerk_page()
            if clerk_page:
                clerk_page = None
                continue
            else:
                step_member_mgmt_getBusinessList()
                step_member_mgmt_getMemberInfoById()
                if getMemberInfoById["cardStatus"] != 0 or getMemberInfoById["mobiles"]:
                    continue
                else:
                    step_member_mgmt_resetMemberPassword()
                    step_mgmt_store_getByParms()
                    step_mgmt_store_updatePermission()
                    login_oauth_token()
                    break

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_wallet_queryMemberSignBankCard()
    if queryMemberSignBankCard is None: # 是否已签约银行
        step_mobile_wallet_sign_signPersonInfoList()
        step_mobile_wallet_sendSmsCode()
        step_mobile_wallet_signBankCard()
    else:
        if queryMemberSignBankCard["bankType"] != "PSBC":
            step_02_mobile_wallet_sendSmsCode()
            step_mobile_wallet_unSignBankCard()
            step_mobile_wallet_sign_signPersonInfoList()
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_signBankCard()
    
    step_mobile_wallet_queryPasswordExist() # 设置支付密码
    if queryPasswordExist:
        step_03_mobile_wallet_sendSmsCode()
        step_03_mobile_wallet_updateWalletPasswordInfo()
    else:
        step_04_mobile_wallet_sendSmsCode()
        step_04_mobile_wallet_updateWalletPasswordInfo()

    step_mobile_wallet_getDetail()  
    if getDetail["passwordFlag"] == 1: # 是否免密，1：开启免密；2：关闭免密
        step_05_mobile_wallet_updateWalletPasswordInfo()
            
    step_fin_api_voucher_voucher_generate()
    
    return r
 
