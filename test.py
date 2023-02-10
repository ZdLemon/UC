# coding:utf-8

import pytest
from api.basic_services._login import _login
from api.basic_services._login_oauth_token import _login_oauth_token

from setting import username_pk, username_vip, username ,username_85, store, store_85, mysql_host, mysql_passwd, mysql_port, mysql_user, store, productCode_zh, productCode, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pymysql
 
import time
import uuid
import datetime
import calendar
import allure
import random, string


@pytest.fixture(scope="session", autouse=True)
def login():
    "hewei01 登录完美运营后台"
    r = _login().json()
    os.environ["access_token"] = r["data"]["access_token"]
    return r


@allure.title("云商总店登录商城-湖北分公司-签约邮储")
@pytest.fixture(scope="session", autouse=True)
def login_oauth_token():
    
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
    from api.mall_mobile_application._mobile_wallet_getGiftCouponByMemberIdAndStatus import _mobile_wallet_getGiftCouponByMemberIdAndStatus # 查询电子礼券发放信息
    from api.mall_mobile_application._mobile_wallet_queryFriSubsidyByMemberIdAndStatus import _mobile_wallet_queryFriSubsidyByMemberIdAndStatus # 查询运费补贴券发放信息 
        
    access_token = os.environ["access_token"]
    companyCode = "06000" # 分公司：湖北分公司
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

    # 发放电子礼券
    getGiftCouponByMemberIdAndStatus = 0
    
    @allure.title("查询电子礼券发放信息")    
    def step_mobile_wallet_getGiftCouponByMemberIdAndStatus():

        nonlocal getGiftCouponByMemberIdAndStatus
        data = {
            "pageNum":1,
            "pageSize":10,
            "giftCouponStatus":2 # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 6:已失效 不传或者null:全部
        }
        with _mobile_wallet_getGiftCouponByMemberIdAndStatus(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getGiftCouponByMemberIdAndStatus = r.json()["data"]["total"]
             
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
            
    # 发放电子礼券
    step_mobile_wallet_getGiftCouponByMemberIdAndStatus()
    if getGiftCouponByMemberIdAndStatus < 5:
        step_fin_api_voucher_voucher_generate()
    
    return r
 
 
@pytest.fixture(scope="session", autouse=True)
def login_store():
    "云商 45722864 登录店铺系统902804"
    r = _login(username=store, password="206822", channel="store").json()
    os.environ["store_token"] = r["data"]["access_token"]
    return r




# 店铺后台押货,定制品押货,押货退货,13押货转移

@allure.title("店铺后台押货")
@pytest.fixture(scope="function")
def purchase_commit():
    "店铺后台押货"
    
    from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
    from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
    from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
    from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

    from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
    from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
    from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
    from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
    
    store_token = os.environ["store_token"]
    access_token = os.environ["access_token"]
    negateProducts = None # 负库存产品
    products = None # 产品信息
    availableAmount = None # 可用余额
    products_list = [] # 押货产品
    productNum = 2 # 押货产品数量
    orderSn = None # 押货单号
    
    getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
    getStoreInfo = None # 获取服务中心信息
    getAccountList = None # 查询分公司银行账号
    getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
    getBankAccountList = None # 通过storeCode获取银行账户资料信息
    pageSearchList = None # 待审核流水信息

    @allure.step("提交押货单页面的负库存押货商品列表")
    def step_appStore_purchaseOrder_negateProducts():
        
        nonlocal negateProducts
        with _appStore_purchaseOrder_negateProducts(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            negateProducts = r.json()["data"]

    @allure.step("提交押货单页面的押货商品搜索")    
    def step_appStore_purchaseOrder_products():
        
        nonlocal products
        params = {
            "pageNum": 1,
            "pageSize": 40,
            "product": productCode
        }
        with _appStore_purchaseOrder_products(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    products = d

    @allure.step("押货金额")    
    def step_appStore_purchase_balanceAmount():
        
        nonlocal availableAmount
        with _appStore_purchase_balanceAmount(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]["availableAmount"]

    @allure.step("提交押货单")    
    def step_appStore_purchase_commit():
        
        nonlocal orderSn
        data = {
            "list": products_list,
            "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
        }
        with _appStore_purchase_commit(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            orderSn = r.json()["data"]

    @allure.step("按银行流水类型获取款项映射列表")
    def step_mgmt_inventory_remit_getSourceTypeByRemitType():
        
        nonlocal getSourceTypeByRemitType
        params = {
            "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
        }              
        with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSourceTypeByRemitType = r.json()["data"]

    @allure.step( "获取服务中心信息")            
    def step_mgmt_inventory_common_getStoreInfo():
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"] 

    @allure.step( "查询分公司银行账号")                    
    def step_mgmt_sys_getAccountList():
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreInfo["companyCode"],  # 公司编码
        }             
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getAccountList = r.json()["data"] 

    @allure.step("根据storeCode查询押货余额主表数据")
    def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
        
        nonlocal getMortgageAmountByStore
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getMortgageAmountByStore = r.json()["data"] 

    @allure.step("通过storeCode获取银行账户资料信息")
    def step_mgmt_store_getBankAccountList():
        
        nonlocal getBankAccountList
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getBankAccountList = r.json()["data"] 

    @allure.step("手工增押货款") 
    def step_mgmt_inventory_remit_addManualInputRemit():
        
        data = {
            "storeCode": getStoreInfo["code"], # 店铺编号
            "storeName": getStoreInfo["name"],
            "leaderName": getStoreInfo["leaderName"],
            "companyCode": getStoreInfo["companyCode"], # 分公司code
            "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            "changeReason": "汇押货款", # 调整原因
            "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
            "account": getBankAccountList[0]["account"], # 付款账号
            "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
            "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
            "receiptAccount": getAccountList[0]["account"], # 收款账号
            "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
        }           
        with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    @allure.step("手工录入流水分页搜索列表:获取待审核流水信息")
    def step_mgmt_inventory_remit_pageSearchList():
        
        nonlocal pageSearchList 
        data = deepcopy(data01)
        data["storeCode"] = getStoreInfo["code"]
        data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
        data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
        with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            pageSearchList = r.json()["data"]["list"]

    @allure.step("手工录入流水审核")
    def step_mgmt_inventory_remit_verifyManualInputRemit():
        
        params = pageSearchList[0]
        params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
        params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
        params["show"] = True
        params["type"] = 2               
        with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    step_appStore_purchaseOrder_negateProducts()
    step_appStore_purchaseOrder_products()
    
    if negateProducts != []:
        for d in negateProducts:
            products_list.append({
                "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                "productCode": d["productCode"], # 押货商品编码
                "productNum": -d["currentStock"] # 押货商品数量
            })
    else:
        products_list.append({
                "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                "productCode": products["productCode"], # 押货商品编码
                "productNum": productNum # 押货商品数量
            })
    
    step_appStore_purchase_balanceAmount()
    
    if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_remit_addManualInputRemit()
        step_mgmt_inventory_remit_pageSearchList()
        step_mgmt_inventory_remit_verifyManualInputRemit()
        
    step_appStore_purchase_commit()
    
    return orderSn

