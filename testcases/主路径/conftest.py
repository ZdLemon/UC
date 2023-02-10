# coding:utf-8

from api.basic_services._login import _login
 
from setting import USERNAME02, store_85, productCode_SecondCoupon, couponNumber
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
    from api.mall_mobile_application._mobile_wallet_getGiftCouponByMemberIdAndStatus import _mobile_wallet_getGiftCouponByMemberIdAndStatus # 查询电子礼券发放信息
    from api.mall_mobile_application._mobile_wallet_queryFriSubsidyByMemberIdAndStatus import _mobile_wallet_queryFriSubsidyByMemberIdAndStatus # 查询运费补贴券发放信息 
    
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

    # 发放运费补贴券 15元
    queryFriSubsidyByMemberIdAndStatus = 0
    
    @allure.title("查询运费补贴券发放信息")    
    def step_mobile_wallet_queryFriSubsidyByMemberIdAndStatus():

        nonlocal queryFriSubsidyByMemberIdAndStatus
        data = {
            "pageNum":1,
            "pageSize":10,
            "giftCouponStatus":2 # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 6:已失效 不传或者null:全部
        }
        with _mobile_wallet_queryFriSubsidyByMemberIdAndStatus(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryFriSubsidyByMemberIdAndStatus = r.json()["data"]["total"]
         
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
    
    # 发放电子礼券 5元        
    step_mobile_wallet_getGiftCouponByMemberIdAndStatus() 
    if getGiftCouponByMemberIdAndStatus < 5:
        step_fin_api_voucher_voucher_generate() 
    
    # 发放运费补贴券 15元
    step_mobile_wallet_queryFriSubsidyByMemberIdAndStatus()
    if queryFriSubsidyByMemberIdAndStatus < 5:
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
    from api.mall_mobile_application._mobile_wallet_getGiftCouponByMemberIdAndStatus import _mobile_wallet_getGiftCouponByMemberIdAndStatus # 查询电子礼券发放信息
    from api.mall_mobile_application._mobile_wallet_queryFriSubsidyByMemberIdAndStatus import _mobile_wallet_queryFriSubsidyByMemberIdAndStatus # 查询运费补贴券发放信息 
        
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
 
 
@allure.title("85折云商总店登录商城-中山分公司-签约工行")
@pytest.fixture(scope="package", autouse=True)
def yunsh_login_ICBC_85():
    
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.mall_center_member._member_mgmt_getBusinessList import _member_mgmt_getBusinessList # 获取云商微店列表
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
        
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
    from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
    from api.basic_services._storage_upload import _storage_upload # 上传商品图片
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes import _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes # 获取所有匹配的商品编码列表
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchProductByCode import _mgmt_inventory_dis_mortgage_common_searchProductByCode # 按商品编码精确查询商品
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange import _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange # 押货换货下单
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_opinion import _mgmt_inventory_dis_mortgage_exchangeOrder_opinion # 添加审批意见
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_detail_id import _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id # 详情
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo # 展示审批保存信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_audit import _mgmt_inventory_dis_mortgage_exchangeOrder_audit # 审批
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_process import _mgmt_inventory_dis_mortgage_exchangeOrder_process # 退回
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_inspect import _mgmt_inventory_dis_mortgage_exchangeOrder_inspect # 验货
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_deliver import _mgmt_inventory_dis_mortgage_exchangeOrder_deliver # 发货
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_confirm import _mgmt_inventory_dis_mortgage_exchangeOrder_confirm # 确认收货
    
    access_token = os.environ["access_token_2"]
    listStore = None # 获取服务中心列表
    getBusinessList = None # 获取云商微店列表
    getByParms = None # 根据常用条件查询服务中心
    r = None
    token = None
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    queryMemberSignBankCard = None # 获取用户签约的银行卡及详情信息
    signPersonInfoList = None # 签约银行卡-获取签约人信息
    phoneNum = f"189{''.join(random.sample(string.digits, 8))}"
    queryPasswordExist = False # 是否设置了支付密码
    
    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : store_85,  # str服务中心编号
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

    @allure.step("根据常用条件查询服务中心")
    def step_mgmt_store_getByParms():
        
        nonlocal getByParms
        params = {
            "storeCode" : listStore["code"],  # str服务中心编号
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
            "storeName": getByParms["name"],
            "leaderName": getByParms["leaderName"],
            "frozenTime": None, # 冻结时间
            "frozenReason": "", # 冻结原因
            "cancelTime": None, # 取消时间
            "permission": "", # 1:3权限
            "businessMode": 2,
            "discountPermission": "1,2,3,4,5,8,9", # 85%权限
            "shopType": 1 # 门店类型
        }
        with _mgmt_store_updatePermission(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("登录")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=listStore["shopkeeperNo"]).json()
        token = r["data"]["access_token"]
        os.environ["token_85"] = r["data"]["access_token"]

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
        
    step_mgmt_store_listStore()
    step_member_mgmt_getBusinessList()
    step_mgmt_store_getByParms()
    step_mgmt_store_updatePermission()
    login_oauth_token()

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
            
    # 发放电子礼券 5元
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
    
    step_mobile_wallet_getGiftCouponByMemberIdAndStatus() # 发放电子礼券 5元
    if getGiftCouponByMemberIdAndStatus < 5:
        step_fin_api_voucher_voucher_generate() 
    
    # 发放运费补贴券 15元
    queryFriSubsidyByMemberIdAndStatus = 0
    searchStore = None # 获取服务中心简单信息
    getReason = None # 获取各种退换货原因
    uploads = [] # 上传商品图片
    searchMatchedProductCodes = None # 获取所有的商品编码列表
    searchProductByCode = None # 根据一或二级编码精确商品信息
    productNum = 2 # 押货退货数量
    mortgageExchange = None # 后台申请添加押货换货单
    opinion = None # 后台押货换货添加审批意见
    detail_id = None # 后台押货换货单详情
    searchAuditInfo = None # 展示审批保存信息
    
    # 发放运费补贴券 15元
    
    @allure.title("查询运费补贴券发放信息")    
    def step_mobile_wallet_queryFriSubsidyByMemberIdAndStatus():

        nonlocal queryFriSubsidyByMemberIdAndStatus
        data = {
            "pageNum":1,
            "pageSize":10,
            "giftCouponStatus":2 # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 6:已失效 不传或者null:全部
        }
        with _mobile_wallet_queryFriSubsidyByMemberIdAndStatus(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryFriSubsidyByMemberIdAndStatus = r.json()["data"]["total"]
      
    @allure.step("查询店铺信息")
    def step_mgmt_inventory_dis_mortgage_common_searchStore():
        
        nonlocal searchStore
        params = {
            "storeCode": listStore["code"], # 服务中心编号
        }             
        with _mgmt_inventory_dis_mortgage_common_searchStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchStore = r.json()["data"]

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

    @allure.step("获取所有匹配的商品编码列表")
    def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
        
        nonlocal searchMatchedProductCodes
        params = {
            "productCode": productCode_SecondCoupon, # 商品编码
        }              
        with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchMatchedProductCodes = r.json()["data"]

    @allure.step("按商品编码精确查询商品")
    def step_mgmt_inventory_dis_mortgage_common_searchProductByCode():
        
        nonlocal searchProductByCode
        params = {
            "productCode": productCode_SecondCoupon, # 商品编码
        }              
        with _mgmt_inventory_dis_mortgage_common_searchProductByCode(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchProductByCode = r.json()["data"]

    @allure.step("押货换货下单")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
        
        nonlocal mortgageExchange
        data = {
            "storeCode": store_85,
            "exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
            "reasonFirst": getReason[13]["returnReason"], # 一级原因
            "reasonFirstRemark": "我是一级原因的备注信息哦", # 一级原因备注
            "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
            "reasonSecondRemark": "我是二级原因的备注信息哦", # 二级原因备注
            "productList": [{
                "productCode": searchProductByCode["productCode"], # 商品编号
                "productName": searchProductByCode["productName"],
                "packing": searchProductByCode["retailPrice"],
                "unit": searchProductByCode["unit"],
                "retailPrice": searchProductByCode["retailPrice"], # 零售价
                "exchangeNum": productNum, # 数量
                "productionDate": "20220101", # 物品生产日期
                "productBatch": "12345", # 批次号
                "productSn": "", # 物品序列号/二维码
                "problemDesc": "进水了", # 问题描述
                "firstUseTime": "", # 第一次使用的时间
                "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
            }],
            "files": [] # 换货单附件，支持3个
        }           
        with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            mortgageExchange = r.json()["data"]

    @allure.step("添加审批意见")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
        
        nonlocal opinion
        data = {
            "orderId": mortgageExchange, # 押货或售后单id
            "content": "业务部门同意押货只换不退" # 审批内容
        }           
        with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            opinion = r.json()["data"]

    @allure.step("展示审批保存信息")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
        
        nonlocal searchAuditInfo        
        with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchAuditInfo = r.json()["data"]["returnAddress"]

    @allure.step("详情")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
        
        nonlocal detail_id
        params = {
            "id": mortgageExchange, # 押货或售后单id
        }          
        with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            detail_id = r.json()["data"]

    @allure.step("审批")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
        
        data = {
            "id": detail_id["id"],
            "exchangeType": detail_id["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
            "auditFileUrl": "", # 审批附件
            "auditFileName": "", # 审批附件名称
            "auditRemark": "服务中心部门同意押货只换不退申请哦", # 审批备注
            "auditResult": "1", # 审批意见 0不通过 1通过
            "disposalType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
            "reasonFirst": detail_id["reasonFirst"], # 一级原因
            "reasonFirstRemark": detail_id["reasonFirstRemark"], # 一级原因备注
            "reasonSecond": detail_id["reasonSecond"], # 二级原因
            "reasonSecondRemark": detail_id["reasonSecondRemark"], # 二级原因备注
            "productList": [{
                "id": detail_id["products"][0]["id"],
                "exchangeNum": detail_id["products"][0]["exchangeNum"], # 数量
                "dailyUseType": detail_id["products"][0]["dailyUseType"], # 日常使用时间 1早上 2中午 3晚上
                "firstUseTime": detail_id["products"][0]["firstUseTime"], # 第一次使用的时间
                "happenType": detail_id["products"][0]["happenType"], # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                "productBatch": detail_id["products"][0]["productBatch"], # 批次号
                "problemDesc": detail_id["products"][0]["problemDesc"], # 问题描述
                "productionDate": detail_id["products"][0]["productionDate"], # 物品生产日期
                "productSn": detail_id["products"][0]["productSn"], # 物品序列号/二维码
                "disposalType": detail_id["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "productCode": detail_id["products"][0]["productCode"] # 商品编号
            }],
            "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
        }          
        with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("上传商品图片")
    def step_05_storage_upload():
        
        nonlocal uploads
        uploads = []
        files = {
            "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
            "file": "data/退回01.jpg"
        }  
        with _storage_upload(files, access_token) as r:     
            assert r.status_code == 200
            assert r.json()["datas"]["msg"] == "文件上传成功"
            uploads.append(r.json()["datas"])

    @allure.step("退回")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
        
        data = {
            "orderId": detail_id["id"], # 换货单id
            "expressAmount": 0, # 物流金额
            "expressCompany": "", # 快递公司
            "expressNo": "", # 快递单号
            "expressProofUrl": "", # 快递凭证url
            "expressProofName": "", # 快递凭证名称
            "processRemark": "这是我的报废凭证，请过目", # 退回说明
            "returnType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 退回方式 1服务中心报废 2自带 3邮寄
            "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
            "disposalProofUrl": f"{uploads[0]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
        }      
        with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("验货")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
        
        data = {
            "expressSubsidy": 0, # 运费补贴
            "inspectRemark": "仓库验货部门验货没问题", # 验货备注
            "inspectResult": "1", # 验货结果 0不通过 1通过
            "orderId": detail_id["id"],
            "inspectProofUrl": []
        }       
        with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("发货")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
        
        data = {
            "orderId": detail_id["id"], # 换货单id
            "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
            "deliverType": 2, # 发货方式 1顾客自提 2邮寄
            "expressCompany": "小河物流", # 新品配送物流公司
            "expressNo": "xh123456" # 物流单号
        } 
        with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("确认收货")
    def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
        
        data = {
            "orderId": detail_id["id"], # 换货单id
        }  
        with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                                    
    step_mobile_wallet_queryFriSubsidyByMemberIdAndStatus()
    if queryFriSubsidyByMemberIdAndStatus < 5:
        # 新建
        step_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_common_getReason()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_common_searchProductByCode()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
        # 待审批
        step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_audit()
        # 待上传凭证
        step_05_storage_upload()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_process()
        # 待验货
        step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect()
        # 待发货
        step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver()
        # 确认收货
        step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm()
    
    return r
   

@allure.title("云商总店登录商城-吉林分公司-签约工行")
@pytest.fixture(scope="package", autouse=True)
def store_login_ICBC(yunsh_login_ICBC):
    
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.basic_services._auth_store_restPsw import _auth_store_restPsw # 重置服务中心密码
    from api.mall_mgmt_application._mgmt_store_leader_getLeaderById import _mgmt_store_leader_getLeaderById # 根据ID获取负责人信息
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    
    access_token = os.environ["access_token_2"]
    listStore = None # 获取服务中心列表
    getLeaderById = None # 根据ID获取负责人信息
    r = None
    token = None
    store_data = yunsh_login_ICBC["data"]

    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : store_data["storeCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : 1,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : 1,  # int是否总店 1总店 2分店
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

    @allure.step("重置服务中心密码")
    def step_auth_store_restPsw():
        
        data = {
            "storeCode": listStore["code"],
            "cardNo": listStore["leaderCardNo"]
        }
        with _auth_store_restPsw(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据ID获取负责人信息")
    def step_mgmt_store_leader_getLeaderById():
        
        nonlocal getLeaderById
        data = {
            "leaderId": listStore["leaderId"],
        }
        with _mgmt_store_leader_getLeaderById(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["certificatesType"] == 1: # 证件类型：1->身份证；2->其他
                getLeaderById = r.json()["data"]["certificatesNo"]
            else:
                getLeaderById = "888888"

    @allure.step("登录")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=listStore["code"], password=getLeaderById[-6:], channel="store").json()
        token = r["data"]["access_token"]
        os.environ["store_token_icbc"] = r["data"]["access_token"]


        step_mgmt_store_listStore()
        step_auth_store_restPsw()
        step_mgmt_store_leader_getLeaderById()
        login_oauth_token()

    return r
   

@allure.title("云商总店登录商城-吉林分公司-签约工行")
@pytest.fixture(scope="package", autouse=True)
def store_login_PSBC(yunsh_login_PSBC):
    
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.basic_services._auth_store_restPsw import _auth_store_restPsw # 重置服务中心密码
    from api.mall_mgmt_application._mgmt_store_leader_getLeaderById import _mgmt_store_leader_getLeaderById # 根据ID获取负责人信息
    from api.basic_services._login_oauth_token import _login_oauth_token # 登录
    
    access_token = os.environ["access_token_2"]
    listStore = None # 获取服务中心列表
    getLeaderById = None # 根据ID获取负责人信息
    r = None
    token = None
    store_data = yunsh_login_PSBC["data"]

    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStore
        params = {
            "storeCode" : store_data["storeCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : 1,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : 1,  # int是否总店 1总店 2分店
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

    @allure.step("重置服务中心密码")
    def step_auth_store_restPsw():
        
        data = {
            "storeCode": listStore["code"],
            "cardNo": listStore["leaderCardNo"]
        }
        with _auth_store_restPsw(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据ID获取负责人信息")
    def step_mgmt_store_leader_getLeaderById():
        
        nonlocal getLeaderById
        data = {
            "leaderId": listStore["leaderId"],
        }
        with _mgmt_store_leader_getLeaderById(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["certificatesType"] == 1: # 证件类型：1->身份证；2->其他
                getLeaderById = r.json()["data"]["certificatesNo"]
            else:
                getLeaderById = "888888"

    @allure.step("登录")
    def login_oauth_token():
        
        nonlocal r, token
        r = _login_oauth_token(username=listStore["code"], password=getLeaderById[-6:], channel="store").json()
        token = r["data"]["access_token"]
        os.environ["store_token_psbc"] = r["data"]["access_token"]


        step_mgmt_store_listStore()
        step_auth_store_restPsw()
        step_mgmt_store_leader_getLeaderById()
        login_oauth_token()

    return r
 


@allure.title("优惠券派发")
@pytest.fixture(scope="package", autouse=True)
def addCouponGrant(vip_login_3, yunsh_login_ICBC, yunsh_login_PSBC, yunsh_login_ICBC_85):
    
    from api.mall_mobile_application._mobile_coupon_selectMemberCoupons import _mobile_coupon_selectMemberCoupons # 查询用户优惠券发放信息 
    from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params as params01,_mgmt_prmt_coupon_getListPage # 优惠券列表
    from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity # 获取所有顾客身份类型
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_clearImportMember import _mgmt_prmt_couponGrant_clearImportMember # 清除缓存里导入的派发用户
    from api.mall_mgmt_application._mgmt_prmt_coupon_getBasicInfo import _mgmt_prmt_coupon_getBasicInfo # 优惠券详情-基础信息
    from api.mall_mgmt_application._mgmt_prmt_selectMemberByCard import _mgmt_prmt_selectMemberByCard # 根据会员卡号去会员中心搜索会员信息
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addUser import _mgmt_prmt_couponGrant_addUser # 手动新增派发顾客
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_getImportMemberPage import _mgmt_prmt_couponGrant_getImportMemberPage # 分页查询导入用户(导入时)
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addCouponGrant import _mgmt_prmt_couponGrant_addCouponGrant # 新增优惠券派发记录
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_examineGrant import _mgmt_prmt_couponGrant_examineGrant # 优惠券派发审核"
    
    id = None # 优惠券id
    getBasicInfo = None # 优惠券详情
    selectMemberByCard = None # 会员信息
    addCouponGrant = None # 待审核派发id
    access_token = os.environ["access_token"]
    vip_cardNo = vip_login_3["data"]["cardNo"]
    yunsh_cardNo_ICBC = yunsh_login_ICBC["data"]["cardNo"]
    yunsh_cardNo_PSBC = yunsh_login_PSBC["data"]["cardNo"]
    yunsh_login_ICBC_85 = yunsh_login_ICBC_85["data"]["cardNo"]
    vip_token_3 = os.environ["vip_token_3"]
    token_icbc = os.environ["token_icbc"]
    token_psbc = os.environ["token_psbc"]
    token_85 = os.environ["token_85"]

    # 查询各会员有多少优惠券
    selectMemberCoupons = 0
    selectMemberCoupons02 = 0
    selectMemberCoupons03 = 0
    selectMemberCoupons04 = 0
    
    @allure.title("查询用户优惠券发放信息:vip_token_3")    
    def step_01_mobile_coupon_selectMemberCoupons():

        nonlocal selectMemberCoupons
        params = {
            "pageNum": 1,
            "pageSize": 6,
            "state": 1, # 使用状态1未使用2已使用3已作废4已失效5占用中
            "selectType": 1 # 筛选条件1全部2快过期3立减券4满减券
        }
        with _mobile_coupon_selectMemberCoupons(params, vip_token_3) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberCoupons = r.json()["data"]["total"]

    @allure.title("查询用户优惠券发放信息:token_icbc")    
    def step_02_mobile_coupon_selectMemberCoupons():

        nonlocal selectMemberCoupons02
        params = {
            "pageNum": 1,
            "pageSize": 6,
            "state": 1, # 使用状态1未使用2已使用3已作废4已失效5占用中
            "selectType": 1 # 筛选条件1全部2快过期3立减券4满减券
        }
        with _mobile_coupon_selectMemberCoupons(params, token_icbc) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberCoupons02 = r.json()["data"]["total"]

    @allure.title("查询用户优惠券发放信息:token_psbc")    
    def step_03_mobile_coupon_selectMemberCoupons():

        nonlocal selectMemberCoupons03
        params = {
            "pageNum": 1,
            "pageSize": 6,
            "state": 1, # 使用状态1未使用2已使用3已作废4已失效5占用中
            "selectType": 1 # 筛选条件1全部2快过期3立减券4满减券
        }
        with _mobile_coupon_selectMemberCoupons(params, token_psbc) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberCoupons03 = r.json()["data"]["total"]

    @allure.title("查询用户优惠券发放信息:token_85")    
    def step_04_mobile_coupon_selectMemberCoupons():

        nonlocal selectMemberCoupons04
        params = {
            "pageNum": 1,
            "pageSize": 6,
            "state": 1, # 使用状态1未使用2已使用3已作废4已失效5占用中
            "selectType": 1 # 筛选条件1全部2快过期3立减券4满减券
        }
        with _mobile_coupon_selectMemberCoupons(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberCoupons04 = r.json()["data"]["total"]

    # 发放优惠券    
    @allure.step("优惠券列表:获取id")    
    def step_mgmt_prmt_coupon_getListPage():
        
        nonlocal id
        params = deepcopy(params01)
        params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
        params["couponNumber"] = couponNumber
        with _mgmt_prmt_coupon_getListPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]

    @allure.step("获取所有顾客身份类型")                         
    def step_mgmt_prmt_getMemberIdentity():
                        
        with _mgmt_prmt_getMemberIdentity(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("清除缓存里导入的派发用户")                    
    def step_mgmt_prmt_couponGrant_clearImportMember():
                        
        with _mgmt_prmt_couponGrant_clearImportMember(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("优惠券详情-基础信息")                       
    def step_mgmt_prmt_coupon_getBasicInfo():
        
        nonlocal getBasicInfo
        params ={"id": id}               
        with _mgmt_prmt_coupon_getBasicInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBasicInfo = r.json()["data"]

    @allure.step("根据会员卡号去会员中心搜索会员信息")                        
    def step_01_mgmt_prmt_selectMemberByCard():

        nonlocal selectMemberByCard
        params ={"cardNo": vip_cardNo}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]

    @allure.step("手动新增派发顾客")                    
    def step_01_mgmt_prmt_couponGrant_addUser():
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 2, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": "", # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据会员卡号去会员中心搜索会员信息")                        
    def step_02_mgmt_prmt_selectMemberByCard():

        nonlocal selectMemberByCard
        params ={"cardNo": yunsh_cardNo_ICBC}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]

    @allure.step("手动新增派发顾客")                    
    def step_02_mgmt_prmt_couponGrant_addUser():
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 2, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": "", # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据会员卡号去会员中心搜索会员信息")                        
    def step_03_mgmt_prmt_selectMemberByCard():

        nonlocal selectMemberByCard
        params ={"cardNo": yunsh_cardNo_PSBC}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]

    @allure.step("手动新增派发顾客")                    
    def step_03_mgmt_prmt_couponGrant_addUser():
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 2, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": "", # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据会员卡号去会员中心搜索会员信息")                        
    def step_04_mgmt_prmt_selectMemberByCard():

        nonlocal selectMemberByCard
        params ={"cardNo": yunsh_login_ICBC_85}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]

    @allure.step("手动新增派发顾客")                    
    def step_04_mgmt_prmt_couponGrant_addUser():
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 2, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": "", # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("分页查询导入用户(导入时)")                       
    def step_mgmt_prmt_couponGrant_getImportMemberPage():
        
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "grantId": None,
            "user": None
        }               
        with _mgmt_prmt_couponGrant_getImportMemberPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("新增优惠券派发记录")                          
    def step_mgmt_prmt_couponGrant_addCouponGrant():
        
        nonlocal addCouponGrant
        data = {
            "type": 1, # 导入方式1等量派发2按需派发
            "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
            "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
            "everyCount": 2, # 每人发放数量
            "fixedTime": "", # 定时派发时间(yyyy-MM-dd HH:mm:ss)
            "grantStartTime": None, # 定时派发开始时间(yyyy-MM-dd HH:mm:ss)
            "grantEndTime": None, # 定时派发结束时间(yyyy-MM-dd HH:mm:ss)
            "memberIdentities": [], # 用户身份集合
            "memberLevelList": [], # 顾客等级:0.新用户,1.一星优惠客户,2.二星优惠客户,3.三星优惠客户,4.四星优惠客户,5.客户代表,6.客户经理,7.中级客户经理,8.客户总监,9.高级客户总监,10.资深客户总监,11.客户总经理
            "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
            "limitMemberLevel": False, # 是否限制顾客等级
            "limitOrderTime": 0, # 限制购货月份:0-不限制,1-限制,2-从未购货
            "limitCardTime": 0, # 是否限制开卡时间0否1是2限制注册时间
            "limitRegTime": 0, # 是否限制注册月份:0-不限制,1-限制
            "startTime": None, # 开卡时间起(yyyy-MM)
            "endTime": None, # endTime
            "regStartTime": None, # 注册月份起区(yyyy-MM)
            "regEndTime": None, # 注册月份止区(yyyy-MM)
            "orderStartTime": None, # 购货月份起区(yyyy-MM)
            "orderEndTime": None, # 购货月份止区(yyyy-MM)
            "couponId": id, # 优惠券id
            "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
        }               
        with _mgmt_prmt_couponGrant_addCouponGrant(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addCouponGrant = r.json()["data"]

    @allure.step("优惠券派发审核")        
    def step_mgmt_prmt_couponGrant_examineGrant():
        
        data = {
            "enclosureVos":[], # 附件集合
            "examine": 3, # 审核是否通过3通过4不通过
            "grantId": addCouponGrant, # 优惠券派发id
            "remark": "同意发放优惠券" # 备注
        }               
        with _mgmt_prmt_couponGrant_examineGrant(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_prmt_coupon_getListPage()
    step_mgmt_prmt_getMemberIdentity()
    step_mgmt_prmt_couponGrant_clearImportMember()
    step_mgmt_prmt_coupon_getBasicInfo()
    step_01_mobile_coupon_selectMemberCoupons()
    if selectMemberCoupons < 5:
        step_01_mgmt_prmt_selectMemberByCard()
        step_01_mgmt_prmt_couponGrant_addUser()
    step_02_mobile_coupon_selectMemberCoupons()
    if selectMemberCoupons02 < 5:
        step_02_mgmt_prmt_selectMemberByCard()
        step_02_mgmt_prmt_couponGrant_addUser()
    step_03_mobile_coupon_selectMemberCoupons()
    if selectMemberCoupons03 < 5:
        step_03_mgmt_prmt_selectMemberByCard()
        step_03_mgmt_prmt_couponGrant_addUser()
    step_04_mobile_coupon_selectMemberCoupons()
    if selectMemberCoupons04 < 5:
        step_04_mgmt_prmt_selectMemberByCard()
        step_04_mgmt_prmt_couponGrant_addUser()
    if selectMemberCoupons < 5 or selectMemberCoupons02 < 5 or selectMemberCoupons03 < 5 or selectMemberCoupons04 < 5:
        step_mgmt_prmt_couponGrant_getImportMemberPage()
        step_mgmt_prmt_couponGrant_addCouponGrant()
        step_mgmt_prmt_couponGrant_examineGrant()

