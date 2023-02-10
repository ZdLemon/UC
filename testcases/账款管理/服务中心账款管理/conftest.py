# coding:utf-8

import pytest
from api.basic_services._login import _login

from setting import username, USERNAME02, store, store_85, productCode_zh, productCode, couponNumber, productCode_SecondCoupon
from util.stepreruns import stepreruns
import os
from copy import deepcopy
 
import time
import uuid
import datetime
import calendar
import allure
import random, string


@allure.title("username02 登录完美运营后台")
@pytest.fixture(scope="package", autouse=True)
def login_2():
    r = _login(username=USERNAME02).json()
    os.environ["access_token_2"] = r["data"]["access_token"]
    return r


@allure.title("云商分店登录商城-湖北分公司-签约邮储")
@pytest.fixture(scope="package", autouse=True)
def yunsh_login_PSBC(login_2):
    
    from api.mall_mgmt_application._mgmt_store_listBankAccount import _mgmt_store_listBankAccount # 银行账号列表
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.mall_mgmt_application._mgmt_store_clerk_page import _mgmt_store_clerk_page # 查询店员列表
    from api.mall_mgmt_application._mgmt_store_clerk_remove import _mgmt_store_clerk_remove # 删除店员账号
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
    
    access_token = os.environ["access_token_2"]
    companyCode = "06000" # 分公司：湖北分公司
    store_listStore = [] # 银行账号列表
    listStores = [] # 获取服务中心列表
    clerk_pages = [] # 查询店员列表
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
            "companyCode": companyCode # 分公司
        }
        with _mgmt_store_listBankAccount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                store_listStore = r.json()["data"]["list"]

    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStores
        params = {
            "storeCode" : None,  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : 1,  # int网点类型1、正式网点
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : 2,  # int是否总店 1总店 2分店
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
                for d in r.json()["data"]["list"]:
                    listStores.append(d)

    @allure.step("查询店员列表")
    def step_mgmt_store_clerk_page():
        
        nonlocal clerk_pages
        params = {
            "storeCode": listStore["code"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_store_clerk_page(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    clerk_pages.append(d["userId"])

    @allure.step("删除店员账号")
    def step_mgmt_store_clerk_remove():
        
        data = {
            "storeCode": listStore["code"], # 服务中心编码（门店系统不需要填）
            "id": clerk_page # 店员ID
        }
        with _mgmt_store_clerk_remove(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
                     
          
    step_mgmt_store_listStore()
    if listStores:
        for listStore in listStores:
            step_mgmt_store_clerk_page()
            if clerk_pages:
                for clerk_page in clerk_pages:
                    step_mgmt_store_clerk_remove()
            step_member_mgmt_getBusinessList()
            step_member_mgmt_getMemberInfoById()
            if getMemberInfoById["cardStatus"] != 0 or getMemberInfoById["mobiles"]:
                continue
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
    
    return r
 
 
@allure.title("云商总店登录商城-湖北分公司-签约工行")
@pytest.fixture(scope="package", autouse=True)
def yunsh_login_ICBC(login_2):
    
    from api.mall_mgmt_application._mgmt_store_listBankAccount import _mgmt_store_listBankAccount # 银行账号列表
    from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
    from api.mall_mgmt_application._mgmt_store_clerk_page import _mgmt_store_clerk_page # 查询店员列表
    from api.mall_mgmt_application._mgmt_store_clerk_remove import _mgmt_store_clerk_remove # 删除店员账号
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
    
    access_token = os.environ["access_token_2"]
    companyCode = "06000" # 分公司：湖北分公司
    store_listStore = [] # 银行账号列表
    listStores = [] # 获取服务中心列表
    clerk_pages = [] # 查询店员列表
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
            "companyCode": companyCode # 分公司
        }
        with _mgmt_store_listBankAccount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                store_listStore = r.json()["data"]["list"]

    @allure.step("获取服务中心列表")
    def step_mgmt_store_listStore():
        
        nonlocal listStores
        params = {
            "storeCode" : None,  # str服务中心编号
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
                for d in r.json()["data"]["list"]:
                    listStores.append(d)

    @allure.step("查询店员列表")
    def step_mgmt_store_clerk_page():
        
        nonlocal clerk_pages
        params = {
            "storeCode": listStore["code"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_store_clerk_page(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    clerk_pages.append(d["userId"])

    @allure.step("删除店员账号")
    def step_mgmt_store_clerk_remove():
        
        data = {
            "storeCode": listStore["code"], # 服务中心编码（门店系统不需要填）
            "id": clerk_page # 店员ID
        }
        with _mgmt_store_clerk_remove(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
    if listStores:
        for listStore in listStores:
            step_mgmt_store_clerk_page()
            if clerk_pages:
                for clerk_page in clerk_pages:
                    step_mgmt_store_clerk_remove()
            step_member_mgmt_getBusinessList()
            step_member_mgmt_getMemberInfoById()
            if getMemberInfoById["cardStatus"] != 0 or getMemberInfoById["mobiles"]:
                continue
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
    
    return r

# 完美运营后台押货单
 
  
# 组合产品上下架

@allure.title("组合产品M70355上架")
@pytest.fixture(scope="function")
def onSaleVersion():
    """组合产品M70355上架"""
    
    from api.mall_mgmt_application._mgmt_product_item_listVersion import data as data01, _mgmt_product_item_listVersion # 商品版本列表
    from api.mall_mgmt_application._mgmt_product_item_onSaleVersion import _mgmt_product_item_onSaleVersion # 上架
    from api.mall_mgmt_application._mgmt_product_ctrl_listInfoAudit import data as data03 ,_mgmt_product_ctrl_listInfoAudit # 产品信息审核列表
    from api.mall_mgmt_application._mgmt_product_ctrl_infoAudit import data as data02, _mgmt_product_ctrl_infoAudit # 审核
    
    listVersion = None # 商品信息
    versionId = None # 待审核商品id

    def step_mgmt_product_item_listVersion():
        "商品版本列表: 获取商品Id"
        
        nonlocal  listVersion
        data = deepcopy(data01)
        data["serialNo"] = productCode_zh
        with _mgmt_product_item_listVersion(data, os.environ["access_token_2"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listVersion = r.json()["data"]["list"][0]
    
    def step_mgmt_product_item_onSaleVersion():
        "商品版本上架"
        
        params = {"productId": listVersion["productId"]}
        with _mgmt_product_item_onSaleVersion(params, os.environ["access_token_2"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "上架成功"
    
    @stepreruns()    
    def step_mgmt_product_ctrl_listInfoAudit():
        "待产品审核商品版本列表：获取id"
        
        nonlocal versionId
        data = deepcopy(data03)
        data["serialNo"] = productCode_zh
        data["auditStauts"] = 2
        with _mgmt_product_ctrl_listInfoAudit(data, os.environ["access_token_2"]) as r:
            # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
            assert r.json()["data"]["list"][0]["statusNote"] == "待审核"
            versionId = r.json()["data"]["list"][0]["id"]
    
    @stepreruns()
    def step_mgmt_product_ctrl_infoAudit():
        "产品审核商品版本"
        
        data = deepcopy(data02)
        data["versionId"] = versionId
        data["auditResult"] = 1
        with _mgmt_product_ctrl_infoAudit(data, os.environ["access_token_2"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_product_item_listVersion()
    if listVersion["versionStatus"] == 8:
        step_mgmt_product_item_onSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()


@allure.title("组合产品M70355下架")
@pytest.fixture(scope="function")
def offSaleVersion():
    """组合产品M70355下架"""
    
    from api.mall_mgmt_application._mgmt_product_item_listVersion import data as data01, _mgmt_product_item_listVersion # 商品版本列表
    from api.mall_mgmt_application._mgmt_product_item_offSaleVersion import params as params01, _mgmt_product_item_offSaleVersion # 下架
    from api.mall_mgmt_application._mgmt_product_ctrl_listInfoAudit import data as data03 ,_mgmt_product_ctrl_listInfoAudit # 产品信息审核列表
    from api.mall_mgmt_application._mgmt_product_ctrl_infoAudit import data as data02, _mgmt_product_ctrl_infoAudit # 审核
    
    listVersion = None # 商品信息
    versionId = None # 待审核商品id

    def step_mgmt_product_item_listVersion():
        "商品版本列表: 获取商品Id"
        
        nonlocal  listVersion
        data = deepcopy(data01)
        data["serialNo"] = productCode_zh
        with _mgmt_product_item_listVersion(data, os.environ["access_token_2"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listVersion = r.json()["data"]["list"][0]
    
    def step_mgmt_product_item_offSaleVersion():
            
        params = deepcopy(params01)
        params["productId"] = listVersion["productId"]                   
        with _mgmt_product_item_offSaleVersion(params, os.environ["access_token_2"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "下架成功"
    
    @stepreruns()    
    def step_mgmt_product_ctrl_listInfoAudit():
        "待产品审核商品版本列表：获取id"
        
        nonlocal versionId
        data = deepcopy(data03)
        data["serialNo"] = productCode_zh
        data["auditStauts"] = 2
        with _mgmt_product_ctrl_listInfoAudit(data, os.environ["access_token_2"]) as r:
            # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
            assert r.json()["data"]["list"][0]["statusNote"] == "待审核"
            versionId = r.json()["data"]["list"][0]["id"]
    
    @stepreruns()
    def step_mgmt_product_ctrl_infoAudit():
        "产品审核商品版本"
        
        data = deepcopy(data02)
        data["versionId"] = versionId
        data["auditResult"] = 1
        with _mgmt_product_ctrl_infoAudit(data, os.environ["access_token_2"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_product_item_listVersion()
    if listVersion["versionStatus"] == 7:
        step_mgmt_product_item_offSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()


# 线下汇款未识别款（3笔）
@allure.title("线下汇款无法识别款")
@pytest.fixture(scope="function")
def unknownRemit(login_2):
    "线下汇款无法识别款"
    
    from api.mall_center_pay._pay_notify_mockBankflow import data as data02, _pay_notify_mockBankflow
    
    access_token = os.environ["access_token_2"]  
    tradeAmount = 10 # 汇款金额 
                         
    def step_pay_notify_mockBankflow():
        "生成无法识别流水"
        
        data = deepcopy(data02)
        data[0]["accountName"] = "我是无法识别的银行账户"
        data[0]["accountNo"] = f"622123456789951753"
        data[0]["bankName"] = "中国工商银行深圳华南城支行"
        data[0]["tradeAmount"] = tradeAmount
        data[0]["tradeOrderNo"] = f"HK{str(time.time() * 1000)[:13]}"
        with _pay_notify_mockBankflow(data, access_token) as r:
            assert r.status_code == 200
            assert r.text == "SUCCESS"
      
    for i in range(3):
        time.sleep(1)
        step_pay_notify_mockBankflow()

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
    access_token = os.environ["access_token_2"]
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

    def step_appStore_purchaseOrder_negateProducts():
        "提交押货单页面的负库存押货商品列表"
        
        nonlocal negateProducts
        with _appStore_purchaseOrder_negateProducts(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            negateProducts = r.json()["data"]
    
    def step_appStore_purchaseOrder_products():
        "提交押货单页面的押货商品搜索"
        
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
    
    def step_appStore_purchase_balanceAmount():
        "押货金额"
        
        nonlocal availableAmount
        with _appStore_purchase_balanceAmount(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]["availableAmount"]
    
    def step_appStore_purchase_commit():
        "提交押货单"
        
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

    def step_mgmt_inventory_remit_getSourceTypeByRemitType():
        "按银行流水类型获取款项映射列表"
        
        nonlocal getSourceTypeByRemitType
        params = {
            "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
        }              
        with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSourceTypeByRemitType = r.json()["data"]
            
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"] 
                    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreInfo["companyCode"],  # 公司编码
        }             
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getAccountList = r.json()["data"] 

    def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
        "根据storeCode查询押货余额主表数据"
        
        nonlocal getMortgageAmountByStore
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getMortgageAmountByStore = r.json()["data"] 

    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getBankAccountList = r.json()["data"] 
 
    def step_mgmt_inventory_remit_addManualInputRemit():
        "手工增押货款"
        
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

    def step_mgmt_inventory_remit_pageSearchList():
        "手工录入流水分页搜索列表:获取待审核流水信息"
        
        nonlocal pageSearchList 
        data = deepcopy(data01)
        data["storeCode"] = getStoreInfo["code"]
        data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
        data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
        with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            pageSearchList = r.json()["data"]["list"]

    def step_mgmt_inventory_remit_verifyManualInputRemit():
        "手工录入流水审核"
        
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


@allure.title("店铺后台定制品押货")
@pytest.fixture(scope="function")
def purchase_commitCusOrder():
    "店铺后台定制品押货"
    
    from api.mall_store_application._appStore_purchaseOrder_getNegateCusProductsForWebAddPage import _appStore_purchaseOrder_getNegateCusProductsForWebAddPage # 提交定制押货单页面的负库存押货商品列表
    from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
    from api.mall_store_application._appStore_purchaseOrder_getCusProductsForWebAddPage import _appStore_purchaseOrder_getCusProductsForWebAddPage # 提交定制品押货单页面的押货商品搜索列表
    from api.basic_services._auth_getUserInfo import _auth_getUserInfo # 获取当前用户登录缓存信息
    from api.mall_store_application._appStore_purchase_commitCusOrder import _appStore_purchase_commitCusOrder # 提交定制品押货单

    from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
    from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
    from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
    from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核

    store_token = os.environ["store_token"]
    access_token = os.environ["access_token_2"]
    
    getNegateCusProductsForWebAddPage = [] # 负库存产品
    availableAmount = None # 可用余额
    getCusProductsForWebAddPage = None # 产品信息
    products_list = [] # 押货产品
    getUserInfo = None # 获取当前用户登录缓存信息
    productNum = 2 # 押货产品数量
    orderSn = None # 押货单号
    
    getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
    getStoreInfo = None # 获取服务中心信息
    getAccountList = None # 查询分公司银行账号
    getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
    getBankAccountList = None # 通过storeCode获取银行账户资料信息
    pageSearchList = None # 待审核流水信息
    
    def step_appStore_purchaseOrder_getNegateCusProductsForWebAddPage():
        "提交定制押货单页面的负库存押货商品列表"
        
        nonlocal getNegateCusProductsForWebAddPage
        with _appStore_purchaseOrder_getNegateCusProductsForWebAddPage(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getNegateCusProductsForWebAddPage = r.json()["data"]
    
    def step_appStore_purchase_balanceAmount():
        "押货金额"
        
        nonlocal availableAmount
        with _appStore_purchase_balanceAmount(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]["availableAmount"]
    
    def step_appStore_purchaseOrder_getCusProductsForWebAddPage():
        "提交定制品押货单页面的押货商品搜索列表"
        
        nonlocal getCusProductsForWebAddPage
        params = {
            "keyword": "" # 一或二级商品关键字
        }
        with _appStore_purchaseOrder_getCusProductsForWebAddPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getCusProductsForWebAddPage = r.json()["data"][0]

    def step_auth_getUserInfo():
        "获取当前用户登录缓存信息"
        
        nonlocal getUserInfo
        with _auth_getUserInfo(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getUserInfo = r.json()["data"] 

    def step_appStore_purchase_commitCusOrder():
        "提交定制品押货单"
        
        nonlocal orderSn
        data = {
            "productList": products_list,
            "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
        }
        with _appStore_purchase_commitCusOrder(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            orderSn = r.json()["data"]

    def step_mgmt_inventory_remit_getSourceTypeByRemitType():
        "按银行流水类型获取款项映射列表"
        
        nonlocal getSourceTypeByRemitType
        params = {
            "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
        }              
        with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSourceTypeByRemitType = r.json()["data"]
            
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"] 
                    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreInfo["companyCode"],  # 公司编码
        }             
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getAccountList = r.json()["data"] 

    def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
        "根据storeCode查询押货余额主表数据"
        
        nonlocal getMortgageAmountByStore
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getMortgageAmountByStore = r.json()["data"] 

    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getBankAccountList = r.json()["data"] 

    def step_mgmt_inventory_remit_addManualInputRemit():
        "手工增押货款"
        
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

    def step_mgmt_inventory_remit_pageSearchList():
        "手工录入流水分页搜索列表:获取待审核流水信息"
        
        nonlocal pageSearchList 
        data = deepcopy(data01)
        data["storeCode"] = getStoreInfo["code"]
        data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
        data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
        with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            pageSearchList = r.json()["data"]["list"]

    def step_mgmt_inventory_remit_verifyManualInputRemit():
        "手工录入流水审核"
        
        params = pageSearchList[0]
        params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
        params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
        params["show"] = True
        params["type"] = 2               
        with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    step_appStore_purchaseOrder_getNegateCusProductsForWebAddPage()
    step_appStore_purchaseOrder_getCusProductsForWebAddPage()
    if getNegateCusProductsForWebAddPage != []:
        for d in getNegateCusProductsForWebAddPage:
            products_list.append({
                "productCode": d["productCode"], # 押货商品编码
                "productMortgagePrice": d["productMortgagePrice"], # 商品押货价
                "productNum": -d["currentStock"], # 押货商品数量
                "productSecondCode": d["productSecCode"] # 二级编码
            })
    else:
        products_list.append({
                "productCode": getCusProductsForWebAddPage["productCode"], # 押货商品编码
                "productMortgagePrice": getCusProductsForWebAddPage["subProductList"][0]["productMortgagePrice"], # 商品押货价
                "productNum": productNum, # 押货商品数量
                "productSecondCode": getCusProductsForWebAddPage["subProductList"][0]["productSecCode"] # 二级编码
            })
        
    step_appStore_purchase_balanceAmount()
    
    if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_remit_addManualInputRemit()
        step_mgmt_inventory_remit_pageSearchList()
        step_mgmt_inventory_remit_verifyManualInputRemit()                       
    
    step_auth_getUserInfo()
    step_appStore_purchase_commitCusOrder()
    
    return orderSn


@allure.title("店铺后台押货退货")
@pytest.fixture(scope="function")
def purchaseReturnOrder(purchase_commitCusOrder):
    "店铺后台押货退货"
    
    from api.mall_store_application._appStore_purchaseReturnOrder_list import params as params01, _appStore_purchaseReturnOrder_list # 押货退货单列表
    from api.basic_services._auth_getUserInfo import _auth_getUserInfo # 获取当前用户登录缓存信息
    from api.mall_store_application._appStore_common_getReason import _appStore_common_getReason # 获取各种退换货原因
    from api.mall_store_application._appStore_purchaseReturnOrder_returnProducts import _appStore_purchaseReturnOrder_returnProducts # 提交退货单页面的押货退货商品搜索
    from api.mall_store_application._appStore_purchaseReturnOrder_save import _appStore_purchaseReturnOrder_save # 提交退货单
    from api.mall_store_application._appStore_purchaseReturnOrder_returnInfo import _appStore_purchaseReturnOrder_returnInfo # 提交退回信息

    from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 完美后台获取各种退换货原因
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_addOpinion import _mgmt_inventory_returnOrder_addOpinion # 后台押货退货添加审批意见
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_auditOrder import  _mgmt_inventory_returnOrder_auditOrder # 后台审批押货退货单
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_inspectOrder import  _mgmt_inventory_returnOrder_inspectOrder # 后台押货退货验货

    store_token = os.environ["store_token"]
    access_token = os.environ["access_token_2"]
    
    purchaseReturnOrder = None # 押货退货单列表信息
    getUserInfo = None # 获取当前用户登录缓存信息
    getReason = None # 获取各种退换货原因
    returnProducts = None # 提交退货单页面的押货退货商品搜索
    purchaseReturnOrder_save = None # 退货单信息
    productNum = 2 # 退货数量
    
    getReason_02 = None # 完美后台获取各种退换货原因
    getOrderDetail = None # 完美后台押货退货单详情
    addOpinion = None # 后台押货退货添加审批意见
    
    def step_appStore_purchaseReturnOrder_list():
        "押货退货单列表"
        
        nonlocal purchaseReturnOrder
        params = deepcopy(params01)
        with _appStore_purchaseReturnOrder_list(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            purchaseReturnOrder = r.json()["data"]["list"]
    
    def step_auth_getUserInfo():
        "获取当前用户登录缓存信息"
        
        nonlocal getUserInfo
        with _auth_getUserInfo(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getUserInfo = r.json()["data"] 

    def step_appStore_common_getReason():
        "获取各种退换货原因"
        
        nonlocal getReason
        params = {
            "type": 3, # 类型: 3退货 4换货
        }
        with _appStore_common_getReason(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]

    def step_appStore_purchaseReturnOrder_returnProducts():
        "提交退货单页面的押货退货商品搜索"
        
        nonlocal returnProducts
        params = {
            "product": productCode, # 产品名称/产品编号
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_purchaseReturnOrder_returnProducts(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["productCode"] == productCode:
                    returnProducts = d

    def step_appStore_purchaseReturnOrder_save():
        "提交退货单"
        
        nonlocal purchaseReturnOrder_save
        data = {
            "invtMortgageReturnOrderProductVOList": [{
                "productCode": productCode, # 物品编号
                "productNum": productNum # 退货数量
            }],
            "invtMortgageReturnOrderVO": {
                "reasonFirst": getReason[1]["returnReason"], # 一级原因
                "reasonFirstRemarks": "我就是想退货，你敢不同意吗" # 一级原因备注
            }
        }
        with _appStore_purchaseReturnOrder_save(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            purchaseReturnOrder_save = r.json()["data"]

    def step_mgmt_inventory_common_getReason():
        "完美后台获取各种退换货原因"
        
        nonlocal getReason_02
        params = {
            "type": 3, # 类型: 3退货 4换货
        }
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason_02 = r.json()["data"]

    def step_mgmt_inventory_returnOrder_addOpinion():
        "完美后台押货退货添加审批意见"
        
        nonlocal addOpinion
        data = {
            "orderId": purchaseReturnOrder_save["orderId"], # 押货或售后单id
            "content": f"同意这个退货申请{purchaseReturnOrder_save['orderSn']}" # 意见内容
        }
        with _mgmt_inventory_returnOrder_addOpinion(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            addOpinion = r.json()["data"]

    def step_mgmt_inventory_returnOrder_getOrderDetail():
        "完美后台押货退货单详情"
        
        nonlocal getOrderDetail
        params = {
            "orderId": purchaseReturnOrder_save["orderId"]
        }
        with _mgmt_inventory_returnOrder_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getOrderDetail = r.json()["data"]
                    
    def step_mgmt_inventory_returnOrder_auditOrder():
        "完美后台审批押货退货单"
        
        data = {
            "id": purchaseReturnOrder_save["orderId"], # 押货退货单id
            "auditRemarks": f"我只能同意退货申请{purchaseReturnOrder_save['orderSn']}", # 审核备注
            "auditFileName": "", # 审核附件名称
            "auditStatus": 1, # 审核结果 0不通过 1通过
            "auditFileUrl": "", # 审核附件url
            "reasonFirst": getReason_02[1]["returnReason"], # 一级原因
            "reasonFirstRemarks": "我就是想退货，你敢不同意吗", # 一级原因备注
            "reasonSecond": getReason_02[1]["reasonList"][1]["returnReason"], # 二级原因
            "reasonSecondRemarks": "算了，这次就允许你退货吧", # 二级原因备注
            "returnInfo": "深圳仓", # 退回地址信息
            "preAuditFileUrl": ""
        }
        with _mgmt_inventory_returnOrder_auditOrder(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_purchaseReturnOrder_returnInfo():
        "提交退回信息"
        
        data = {
            "returnType": 2, # 退回类型 1自带 2邮寄
            "expressCompany": "小何物流", # 物流公司
            "expressNo": str(round(time.time())), # 物流单号
            "expressFreightProof": "", # 物流费用凭证url
            "expressFreightProofName": "", # 物流费用凭证名称
            "processRemarks": "退回产品都要说明吗", # 退回处理说明
            "orderId": purchaseReturnOrder_save["orderId"] # 退货单id
        }
        with _appStore_purchaseReturnOrder_returnInfo(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_returnOrder_inspectOrder():
        "完美后台押货退货验货"
        
        data = {
            "orderId": purchaseReturnOrder_save["orderId"], # 退货单id
            "inspectStatus": 1, # 验货意见 0不通过 1通过
            "expressSubsidy": 100, # 运费补贴
            "inspectRemarks": "我验货通过了", # 验货备注
            "orderReturnRealAmount": getOrderDetail["orderVo"]["orderReturnAmount"], # orderReturnRealAmount
            "productList": [{
                "id": getOrderDetail["productVoList"][0]["id"], # 物品id
                "productRealNum": getOrderDetail["productVoList"][0]["productNum"], # 物品实退数量
                "productRealAmount": getOrderDetail["productVoList"][0]["productMortgagePrice"] * getOrderDetail["productVoList"][0]["productNum"] # 退货单实退金额总额
            }]
        }
        with _mgmt_inventory_returnOrder_inspectOrder(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    step_appStore_purchaseReturnOrder_list()
    step_auth_getUserInfo()
    step_appStore_common_getReason()
    step_appStore_purchaseReturnOrder_returnProducts()
    step_appStore_purchaseReturnOrder_save()
    step_mgmt_inventory_common_getReason()
    step_mgmt_inventory_returnOrder_getOrderDetail()
    step_mgmt_inventory_returnOrder_addOpinion()
    step_mgmt_inventory_returnOrder_auditOrder()
    step_appStore_purchaseReturnOrder_returnInfo()
    step_mgmt_inventory_returnOrder_inspectOrder()
    
    return purchaseReturnOrder_save["orderSn"]


@allure.title("套装组合")
@pytest.fixture(scope="function")
def combine_confirm(onSaleVersion, returnOrder_auditOrder_zh):
    "套装组合"
    
    from api.mall_store_application._appStore_inventory_combine_page import params as params01, _appStore_inventory_combine_page # 套装组合列表
    from api.mall_store_application._appStore_inventory_combine_preview import _appStore_inventory_combine_preview # 套装组合预览
    from api.mall_store_application._appStore_inventory_combine_confirm import _appStore_inventory_combine_confirm # 确认套装组合
    from api.mall_store_application._appStore_inventory_combine_history_page import _appStore_inventory_combine_history_page # 套装组合记录列表
    from api.mall_store_application._appStore_inventory_combine_detail import _appStore_inventory_combine_detail # 套装组合明细
    
    store_token = os.environ["store_token"]
    combine_page = None # 套装组合
    combine_detail = None # 套装组合明细
    history_page = None # 套装组合记录
    
    def test_appStore_inventory_combine_page():
        "套装组合列表:获取套装组合"
        
        nonlocal combine_page
        params = deepcopy(params01)
        with _appStore_inventory_combine_page(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            combine_page = r.json()["data"]["list"][0]
    
    def test_appStore_inventory_combine_preview():
        "套装组合预览"
        
        params = {
            "id": combine_page["id"], # 套装组合id
            "combineNum": combine_page["maxCombine"], # 套装组合数量
            "productCode": combine_page["productCode"]
        }
        with _appStore_inventory_combine_preview(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def test_appStore_inventory_combine_confirm():
        "确认套装组合"
        
        data = {
            "combineId": combine_page["id"], # 套装组合id
            "combineNum": 1, #combine_page["maxCombine"], # 套装组合数量
            "productCode": combine_page["productCode"]
        }
        with _appStore_inventory_combine_confirm(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def test_appStore_inventory_combine_history_page():
        "套装组合记录列表"
        
        nonlocal history_page
        params = {
            "pageNum": 1,
            "pageSize": 20,
            "beginTime": "", # 开始时间
            "endTime": "" # 结束时间
        }
        with _appStore_inventory_combine_history_page(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            history_page = r.json()["data"]["list"][0]

    def test_appStore_inventory_combine_detail():
        "套装组合明细"
        
        nonlocal combine_detail
        params = {
            "id": history_page["id"], # 套装组合id
        }
        with _appStore_inventory_combine_detail(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            combine_detail = r.json()["data"]

    test_appStore_inventory_combine_page()
    test_appStore_inventory_combine_preview()
    test_appStore_inventory_combine_confirm()
    test_appStore_inventory_combine_history_page()
    test_appStore_inventory_combine_detail()
    
    return combine_detail


@allure.title("店铺系统 13押货转移")
@pytest.fixture(scope="function")
def disInventoryTransfer_addTransfer(login_store_85):
    "店铺系统 13押货转移"
    
    from api.mall_store_application._appStore_store_disInventoryTransfer_addTransferList import _appStore_store_disInventoryTransfer_addTransferList # 库存列表
    from api.mall_store_application._appStore_store_disInventoryTransfer_addTransfer import _appStore_store_disInventoryTransfer_addTransfer # 新建库存转移记录
    from api.mall_store_application._appStore_store_disInventoryTransfer_getLastRecord import _appStore_store_disInventoryTransfer_getLastRecord # 根据服务中心查询最新库存转移记录
    from api.mall_store_application._appStore_store_disInventoryTransfer_getProductList import _appStore_store_disInventoryTransfer_getProductList # 根据记录id查询转移记录的商品明细
    from api.mall_store_application._appStore_store_disInventoryTransfer_recordById import _appStore_store_disInventoryTransfer_recordById # 根据id查询库存转移记录
    from api.mall_store_application._appStore_store_dis_mortgageOrder_getMortgageAmount import _appStore_store_dis_mortgageOrder_getMortgageAmount # 查询店铺押货余额与限额
    from api.mall_store_application._appStore_store_disInventoryTransfer_payCheck import _appStore_store_disInventoryTransfer_payCheck # 支付前的校验:押货价有变动amountIsUpdate=true
    from api.mall_store_application._appStore_store_deposit_msg import _appStore_store_deposit_msg # 获取服务中心可用押货保证金余额
    from api.mall_store_application._appStore_store_getSignBankAccountList import _appStore_store_getSignBankAccountList # 获取签约银行列表
    from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay # 支付
    from api.mall_store_application._appStore_store_disInventoryTransfer_cancelPay import _appStore_store_disInventoryTransfer_cancelPay # 取消支付
    from api.mall_store_application._appStore_store_disInventoryTransfer_recordList import _appStore_store_disInventoryTransfer_recordList # 库存转移记录列表
        
    store_token = os.environ["store_token_85"]
    addTransferList = None # 库存列表
    recordList = None # 库存转移记录列表
    getLastRecord = None # 根据服务中心查询最新库存转移记录
    getProductList = None # 根据记录id查询转移记录的商品明细
    recordById = None # 根据id查询库存转移记录
    getMortgageAmount = None # 查询店铺押货余额与限额
    payCheck = None # 支付前的校验:押货价有变动amountIsUpdate=true
    balance = None # 获取服务中心可用押货保证金余额
    getSignBankAccountList = None # 获取签约银行列表
    recordLists = [] # 库存转移记录列表-待支付

    @allure.step("库存转移记录列表：待支付")
    def step_01_appStore_store_disInventoryTransfer_recordList():
        
        nonlocal recordLists
        data = {
            "storeCode": store_85,
            "status": "2", # 状态 1已完成 2待支付 3已取消
            "pageNum":1,
            "pageSize":20
        }
        with _appStore_store_disInventoryTransfer_recordList(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    recordLists.append(i["id"])
      
    @allure.step("取消支付")
    def step_appStore_store_disInventoryTransfer_cancelPay():
        
        params = {
            "id": id
        }
        with _appStore_store_disInventoryTransfer_cancelPay(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("库存列表")
    def step_appStore_store_disInventoryTransfer_addTransferList():
        
        nonlocal addTransferList
        data = {
            "storeCode": store_85, # 服务中心编号
            "query": "", # 搜索条件
            "pageNum": 1,
            "pageSize": 10000,
            "productNumQuery": 2 # 传1大于0;0等于0;-1小于0;2不为0;不传为查全部
        }
        with _appStore_store_disInventoryTransfer_addTransferList(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            addTransferList = r.json()["data"]["list"][0]
            
    @allure.step("新建库存转移记录")
    def step_appStore_store_disInventoryTransfer_addTransfer():
        
        data = {
            "applyType": 1, # 提交途径 1门店提交 2后台提交
            "productList":[
                {
                    "eightFivePrice": addTransferList["orderPrice"], # 85折押货价
                    "oneThreePrice": addTransferList["securityPrice"], # 1:3押货价
                    "productCode": addTransferList["serialNo"], # 产品编号
                    "transferNum": 1 # 转移数量
                }
            ],
            "storeCode": store_85 # 服务中心编号
        }
        with _appStore_store_disInventoryTransfer_addTransfer(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    @allure.step("根据服务中心查询最新库存转移记录")
    def step_appStore_store_disInventoryTransfer_getLastRecord():
        
        nonlocal getLastRecord
        params = {
            "storeCode": store_85
        }
        with _appStore_store_disInventoryTransfer_getLastRecord(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getLastRecord = r.json()["data"]

    @allure.step("根据记录id查询转移记录的商品明细")
    def step_appStore_store_disInventoryTransfer_getProductList():
        
        nonlocal getProductList
        params = {
            "id": getLastRecord["id"]
        }
        with _appStore_store_disInventoryTransfer_getProductList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getProductList = r.json()["data"][0]

    @allure.step("根据id查询库存转移记录")
    def step_appStore_store_disInventoryTransfer_recordById():
        
        nonlocal recordById
        params = {
            "id": getLastRecord["id"]
        }
        with _appStore_store_disInventoryTransfer_recordById(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            recordById = r.json()["data"]

    @allure.step("查询店铺押货余额与限额")
    def step_appStore_store_dis_mortgageOrder_getMortgageAmount():
        
        nonlocal getMortgageAmount
        with _appStore_store_dis_mortgageOrder_getMortgageAmount(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]

    @allure.step("支付前的校验:押货价有变动amountIsUpdate=true")
    def step_appStore_store_disInventoryTransfer_payCheck():
        
        nonlocal payCheck
        params = {
            "uniqueFlagNo": recordById["orderNo"]
        }
        with _appStore_store_disInventoryTransfer_payCheck(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["amountIsUpdate"] is False
            payCheck = r.json()["data"]

    @allure.step("获取服务中心可用押货保证金余额")            
    def step_appStore_store_deposit_msg():
        
        nonlocal balance
        params = {
            "storeCode": store_85
        }
        with _appStore_store_deposit_msg(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            balance = r.json()["data"]["balance"]

    @allure.step("根据id查询库存转移记录")
    def step_02_appStore_store_disInventoryTransfer_recordById():
        
        nonlocal recordById
        params = {
            "id": getLastRecord["id"]
        }
        with _appStore_store_disInventoryTransfer_recordById(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            recordById = r.json()["data"]

    @allure.step("获取签约银行列表")
    def step_appStore_store_getSignBankAccountList():
        
        nonlocal getSignBankAccountList
        params = {
            "isSigned": 1 # 是否已签约，1/是，2/否
        }
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getSignBankAccountList = r.json()["data"]

    @allure.step("查询店铺押货余额与限额")
    def step_02_appStore_store_dis_mortgageOrder_getMortgageAmount():
        
        nonlocal getMortgageAmount
        with _appStore_store_dis_mortgageOrder_getMortgageAmount(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]

    @allure.step("支付前的校验:押货价有变动amountIsUpdate=true")
    def step_02_appStore_store_disInventoryTransfer_payCheck():
        
        nonlocal payCheck
        params = {
            "uniqueFlagNo": recordById["orderNo"]
        }
        with _appStore_store_disInventoryTransfer_payCheck(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["amountIsUpdate"] is False
            payCheck = r.json()["data"]

    @allure.step("支付")            
    def step_appStore_api_wallet_pay():
        
        data = {
            "accountName": getSignBankAccountList[0]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 1, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance":balance,
                    "payAmount":payCheck["differAmount"],
                    "payWays":[
                        {
                            "name":getSignBankAccountList[0]["accountBank"],
                            "payAmount":payCheck["differAmount"],
                            "data":{
                                "accountName":getSignBankAccountList[0]["accountName"],
                                "account":getSignBankAccountList[0]["account"],
                                "accountBank":getSignBankAccountList[0]["accountBank"],
                                "accountType":getSignBankAccountList[0]["accountType"],
                                "isSigned":getSignBankAccountList[0]["isSigned"]
                            }
                        }
                    ]
                }
            ), # 扩展参数
            "payAmount": payCheck["differAmount"],
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": getSignBankAccountList[0]["accountType"], # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
            "pxAmount": 0, # 拼箱费
            "storeCode": store_85, # 店铺编号
            "uniqueFlagNo": recordById["orderNo"], # 订单唯一标识
            "userId": login_store_85["data"]["userId"], # 用户ID
            "yfAmount": 0 # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2

    @allure.step("库存转移记录列表")
    def step_appStore_store_disInventoryTransfer_recordList():
        
        nonlocal recordList
        data = {
            "storeCode": store_85,
            "status": "1", # 状态 1已完成 2待支付 3已取消
            "pageNum":1,
            "pageSize":20
        }
        with _appStore_store_disInventoryTransfer_recordList(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            recordList = r.json()["data"]["list"][0]
                                                
    step_01_appStore_store_disInventoryTransfer_recordList()
    for id in recordLists:
        step_appStore_store_disInventoryTransfer_cancelPay()
    step_appStore_store_disInventoryTransfer_addTransferList()
    step_appStore_store_disInventoryTransfer_addTransfer()
    step_appStore_store_disInventoryTransfer_getLastRecord()
    step_appStore_store_disInventoryTransfer_getProductList()
    step_appStore_store_disInventoryTransfer_recordById()
    step_appStore_store_dis_mortgageOrder_getMortgageAmount()
    step_appStore_store_disInventoryTransfer_payCheck()
    step_appStore_store_deposit_msg()
    step_02_appStore_store_disInventoryTransfer_recordById()
    step_appStore_store_getSignBankAccountList()
    step_02_appStore_store_dis_mortgageOrder_getMortgageAmount()
    step_02_appStore_store_disInventoryTransfer_payCheck()
    step_appStore_api_wallet_pay()
    step_appStore_store_disInventoryTransfer_recordList()
    
    return addTransferList, recordList

# 完美后台押货,仅调账不发货押货单,押货修改,押货批量修改,欠货不发,押货退货(普通产品,组合产品),代客售后,13押货转移

@allure.title("运营后台押货")
@pytest.fixture(scope="function")
def auditMortgageOrder():
    "运营后台押货"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
    from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
    from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
    from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
    from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

    from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
    from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
    from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
    from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
    
    access_token = os.environ["access_token_2"]
    
    getStoreInfo = None # 获取服务中心信息
    availableAmount = None # 根据storeCode查询押货余额
    searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
    products_list = [] # 押货产品
    id = None # 押货单id
    getOrderDetail = None # 押货单详情
    productNum = 2 # 押货数量
    
    getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
    getStoreInfo = None # 获取服务中心信息
    getAccountList = None # 查询分公司银行账号
    getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
    getBankAccountList = None # 通过storeCode获取银行账户资料信息
    pageSearchList = None # 待审核流水信息
    
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"]
    
    def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
        "根据storeCode查询押货余额"  
        
        nonlocal availableAmount
        params = {
            "storeCode": store
        }
        with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]
    
    def step_mgmt_inventory_order_searchProductsForAddPage(): 
        "根据产品关键字搜索普通商品列表" 
        
        nonlocal searchProductsForAddPage
        params = deepcopy(params01)
        params["storeCode"] = store
        params["keyword"] = productCode
        with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:   
                    searchProductsForAddPage = d
    
    def step_mgmt_inventory_order_addMortgageOrder(): 
        "运营后台添加押货单" 
        
        nonlocal id
        data = {
            "invtMortgageOrderVO": {
                "storeCode": store,
                "isDelivery": 1, # 0不需要发货 1需要发货
                "remarks": "" # 押货备注
            },
            "invtMortgageOrderProductVOList": [
                {
                    "productCode": productCode, # 物品编号
                    "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                    "productNum": productNum # 数量
                }
            ]
        }
        with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id =  r.json()["data"]
    
    def step_mgmt_inventory_order_auditMortgageOrder():
        "运营后台审批押货单"
        
        data = {
            "id": id, # 押货单id
            "auditStatus": 1, # 审核结果 0不通过 1通过
            "auditRemarks": f"同意提交押货单申请" # 审核备注
        }
        with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 1
    
    def step_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情"
        
        nonlocal getOrderDetail
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderDetail = r.json()["data"]

    def step_mgmt_inventory_remit_getSourceTypeByRemitType():
        "按银行流水类型获取款项映射列表"
        
        nonlocal getSourceTypeByRemitType
        params = {
            "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
        }              
        with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSourceTypeByRemitType = r.json()["data"]
            
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"] 
                    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreInfo["companyCode"],  # 公司编码
        }             
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getAccountList = r.json()["data"] 

    def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
        "根据storeCode查询押货余额主表数据"
        
        nonlocal getMortgageAmountByStore
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getMortgageAmountByStore = r.json()["data"] 

    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getBankAccountList = r.json()["data"] 

    def step_mgmt_inventory_remit_addManualInputRemit():
        "手工增押货款"
        
        data = {
            "storeCode": getStoreInfo["code"], # 店铺编号
            "storeName": getStoreInfo["name"],
            "leaderName": getStoreInfo["leaderName"],
            "companyCode": getStoreInfo["companyCode"], # 分公司code
            "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            "changeReason": "汇押货款", # 调整原因
            "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
            "account": getBankAccountList[0]["account"], # 付款账号
            "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
            "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
            "receiptAccount": getAccountList[0]["account"], # 收款账号
            "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
        }           
        with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_remit_pageSearchList():
        "手工录入流水分页搜索列表:获取待审核流水信息"
        
        nonlocal pageSearchList 
        data = deepcopy(data01)
        data["storeCode"] = getStoreInfo["code"]
        data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
        data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
        with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            pageSearchList = r.json()["data"]["list"]

    def step_mgmt_inventory_remit_verifyManualInputRemit():
        "手工录入流水审核"
        
        params = pageSearchList[0]
        params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
        params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
        params["show"] = True
        params["type"] = 2               
        with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
        
    step_mgmt_inventory_common_getStoreInfo()
    step_mgmt_inventory_mortgageAmount_getAvailableAmount()
    step_mgmt_inventory_order_searchProductsForAddPage()
    
    products_list.append({
                    "productCode": productCode, # 物品编号
                    "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                    "productNum": productNum # 数量
    })
    
    if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_remit_addManualInputRemit()
        step_mgmt_inventory_remit_pageSearchList()
        step_mgmt_inventory_remit_verifyManualInputRemit()
        
    step_mgmt_inventory_order_addMortgageOrder()
    step_mgmt_inventory_order_auditMortgageOrder()
    step_mgmt_inventory_order_getOrderDetail()
    
    return getOrderDetail["orderVo"]["orderSn"]


@allure.title("运营后台押货组合产品，才能套装拆分")
@pytest.fixture(scope="function")
def auditMortgageOrder_zh():
    "运营后台押货组合产品，才能套装拆分"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
    from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
    from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
    from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
    from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

    from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
    from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
    from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
    from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
    
    access_token = os.environ["access_token_2"]
    
    getStoreInfo = None # 获取服务中心信息
    availableAmount = None # 根据storeCode查询押货余额
    searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
    products_list = [] # 押货产品
    id = None # 押货单id
    getOrderDetail = None # 押货单详情
    productNum = 2 # 押货数量
    
    getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
    getStoreInfo = None # 获取服务中心信息
    getAccountList = None # 查询分公司银行账号
    getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
    getBankAccountList = None # 通过storeCode获取银行账户资料信息
    pageSearchList = None # 待审核流水信息
    
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"]
    
    def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
        "根据storeCode查询押货余额"  
        
        nonlocal availableAmount
        params = {
            "storeCode": store
        }
        with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]
    
    def step_mgmt_inventory_order_searchProductsForAddPage(): 
        "根据产品关键字搜索普通商品列表" 
        
        nonlocal searchProductsForAddPage
        params = deepcopy(params01)
        params["storeCode"] = store
        params["keyword"] = productCode_zh
        with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode_zh:   
                    searchProductsForAddPage = d
    
    def step_mgmt_inventory_order_addMortgageOrder(): 
        "运营后台添加押货单" 
        
        nonlocal id
        data = {
            "invtMortgageOrderVO": {
                "storeCode": store,
                "isDelivery": 1, # 0不需要发货 1需要发货
                "remarks": "" # 押货备注
            },
            "invtMortgageOrderProductVOList": [
                {
                    "productCode": productCode_zh, # 物品编号
                    "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                    "productNum": productNum # 数量
                }
            ]
        }
        with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id =  r.json()["data"]
    
    def step_mgmt_inventory_order_auditMortgageOrder():
        "运营后台审批押货单"
        
        data = {
            "id": id, # 押货单id
            "auditStatus": 1, # 审核结果 0不通过 1通过
            "auditRemarks": f"同意提交押货单申请" # 审核备注
        }
        with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 1
    
    def step_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情"
        
        nonlocal getOrderDetail
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderDetail = r.json()["data"]

    def step_mgmt_inventory_remit_getSourceTypeByRemitType():
        "按银行流水类型获取款项映射列表"
        
        nonlocal getSourceTypeByRemitType
        params = {
            "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
        }              
        with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSourceTypeByRemitType = r.json()["data"]
            
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"] 
                    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreInfo["companyCode"],  # 公司编码
        }             
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getAccountList = r.json()["data"] 

    def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
        "根据storeCode查询押货余额主表数据"
        
        nonlocal getMortgageAmountByStore
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getMortgageAmountByStore = r.json()["data"] 

    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getBankAccountList = r.json()["data"] 

    def step_mgmt_inventory_remit_addManualInputRemit():
        "手工增押货款"
        
        data = {
            "storeCode": getStoreInfo["code"], # 店铺编号
            "storeName": getStoreInfo["name"],
            "leaderName": getStoreInfo["leaderName"],
            "companyCode": getStoreInfo["companyCode"], # 分公司code
            "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            "changeReason": "汇押货款", # 调整原因
            "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
            "account": getBankAccountList[0]["account"], # 付款账号
            "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
            "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
            "receiptAccount": getAccountList[0]["account"], # 收款账号
            "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
        }           
        with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_remit_pageSearchList():
        "手工录入流水分页搜索列表:获取待审核流水信息"
        
        nonlocal pageSearchList 
        data = deepcopy(data01)
        data["storeCode"] = getStoreInfo["code"]
        data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
        data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
        with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            pageSearchList = r.json()["data"]["list"]

    def step_mgmt_inventory_remit_verifyManualInputRemit():
        "手工录入流水审核"
        
        params = pageSearchList[0]
        params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
        params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
        params["show"] = True
        params["type"] = 2               
        with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
        
    step_mgmt_inventory_common_getStoreInfo()
    step_mgmt_inventory_mortgageAmount_getAvailableAmount()
    step_mgmt_inventory_order_searchProductsForAddPage()
    
    products_list.append({
                    "productCode": productCode_zh, # 物品编号
                    "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                    "productNum": productNum # 数量
    })
    
    if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_remit_addManualInputRemit()
        step_mgmt_inventory_remit_pageSearchList()
        step_mgmt_inventory_remit_verifyManualInputRemit()
        
    step_mgmt_inventory_order_addMortgageOrder()
    step_mgmt_inventory_order_auditMortgageOrder()
    step_mgmt_inventory_order_getOrderDetail()
    
    return getOrderDetail["orderVo"]["orderSn"]


@allure.title("运营后台仅调账不发货押货单")
@pytest.fixture(scope="function")
def auditMortgageOrder_isDelivery():
    "运营后台仅调账不发货押货单"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
    from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
    from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
    from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
    from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

    from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
    from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
    from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
    from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
    
    access_token = os.environ["access_token_2"]
    
    getStoreInfo = None # 获取服务中心信息
    availableAmount = None # 根据storeCode查询押货余额
    searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
    products_list = [] # 押货产品
    id = None # 押货单id
    getOrderDetail = None # 押货单详情
    productNum = 2 # 押货数量
    
    getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
    getStoreInfo = None # 获取服务中心信息
    getAccountList = None # 查询分公司银行账号
    getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
    getBankAccountList = None # 通过storeCode获取银行账户资料信息
    pageSearchList = None # 待审核流水信息
    
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"]
    
    def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
        "根据storeCode查询押货余额"  
        
        nonlocal availableAmount
        params = {
            "storeCode": store
        }
        with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]
    
    def step_mgmt_inventory_order_searchProductsForAddPage(): 
        "根据产品关键字搜索普通商品列表" 
        
        nonlocal searchProductsForAddPage
        params = deepcopy(params01)
        params["storeCode"] = store
        params["keyword"] = productCode
        with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:   
                    searchProductsForAddPage = d
    
    def step_mgmt_inventory_order_addMortgageOrder(): 
        "运营后台添加押货单" 
        
        nonlocal id
        data = {
            "invtMortgageOrderVO": {
                "storeCode": store,
                "isDelivery": 0, # 0不需要发货 1需要发货
                "orderRemarks": "",
                "remarks": "我要公司帮忙押货，因为店铺系统不会用" # 押货备注
            },
            "invtMortgageOrderProductVOList": [
                {
                    "productCode": productCode, # 物品编号
                    "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                    "productNum": productNum # 数量
                }
            ]
        }
        with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id =  r.json()["data"]
    
    def step_mgmt_inventory_order_auditMortgageOrder():
        "运营后台审批押货单"
        
        data = {
            "id": id, # 押货单id
            "auditStatus": 1, # 审核结果 0不通过 1通过
            "auditRemarks": f"同意提交押货单申请" # 审核备注
        }
        with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 1
    
    def step_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情"
        
        nonlocal getOrderDetail
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderDetail = r.json()["data"]

    def step_mgmt_inventory_remit_getSourceTypeByRemitType():
        "按银行流水类型获取款项映射列表"
        
        nonlocal getSourceTypeByRemitType
        params = {
            "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
        }              
        with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSourceTypeByRemitType = r.json()["data"]
            
    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["code"] == store
            getStoreInfo = r.json()["data"] 
                    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreInfo["companyCode"],  # 公司编码
        }             
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getAccountList = r.json()["data"] 

    def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
        "根据storeCode查询押货余额主表数据"
        
        nonlocal getMortgageAmountByStore
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getMortgageAmountByStore = r.json()["data"] 

    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = {
            "storeCode": getStoreInfo["code"]
        }            
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            getBankAccountList = r.json()["data"] 

    def step_mgmt_inventory_remit_addManualInputRemit():
        "手工增押货款"
        
        data = {
            "storeCode": getStoreInfo["code"], # 店铺编号
            "storeName": getStoreInfo["name"],
            "leaderName": getStoreInfo["leaderName"],
            "companyCode": getStoreInfo["companyCode"], # 分公司code
            "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            "changeReason": "汇押货款", # 调整原因
            "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
            "account": getBankAccountList[0]["account"], # 付款账号
            "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
            "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
            "receiptAccount": getAccountList[0]["account"], # 收款账号
            "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
        }           
        with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_remit_pageSearchList():
        "手工录入流水分页搜索列表:获取待审核流水信息"
        
        nonlocal pageSearchList 
        data = deepcopy(data01)
        data["storeCode"] = getStoreInfo["code"]
        data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
        data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
        with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            pageSearchList = r.json()["data"]["list"]

    def step_mgmt_inventory_remit_verifyManualInputRemit():
        "手工录入流水审核"
        
        params = pageSearchList[0]
        params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
        params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
        params["show"] = True
        params["type"] = 2               
        with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
        
    step_mgmt_inventory_common_getStoreInfo()
    step_mgmt_inventory_mortgageAmount_getAvailableAmount()
    step_mgmt_inventory_order_searchProductsForAddPage()
    
    products_list.append({
                    "productCode": productCode, # 物品编号
                    "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                    "productNum": productNum # 数量
    })
    
    if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_remit_addManualInputRemit()
        step_mgmt_inventory_remit_pageSearchList()
        step_mgmt_inventory_remit_verifyManualInputRemit()
        
    step_mgmt_inventory_order_addMortgageOrder()
    step_mgmt_inventory_order_auditMortgageOrder()
    step_mgmt_inventory_order_getOrderDetail()
    
    return getOrderDetail["orderVo"]["orderSn"]


@allure.title("普通押货单修改")
@pytest.fixture(scope="function")
def updateMortgageOrder(purchase_commit):
    "普通押货单修改"
    
    from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
    from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
    from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
    
    access_token = os.environ["access_token_2"]        
    orderSn = purchase_commit
    id = None
    produc = None # 押货单详情待修改产品信息
    availableAmount = None # 根据storeCode查询押货余额
    
    def step_mgmt_inventory_order_listMortgageOrder():
        "获取id"
        
        nonlocal id
        params = deepcopy(params01) 
        params["orderSn"] = orderSn
        with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
    
    def step_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情"
        
        nonlocal produc
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["productVoList"]:
                if d["productNum"] > 1:
                        produc = d
    
    def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
        "根据storeCode查询押货余额" 
        
        nonlocal availableAmount
        params = {
            "storeCode": store
        }
        with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]
    
    def step_mgmt_inventory_order_checkProductInventory(): 
        "店铺库存校验接口" 
        
        data = {
            "productDtoList":[ # 需要修改的商品
                {
                    "productCode": produc["productCode"], # 商品一级编码
                    "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                    "productNum":1 # 需要减少的商品数量(绝对值)
                }
            ],
            "storeCode": store # 店铺中心编号
        }
        with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == []

    def step_mgmt_inventory_order_updateMortgageOrder(): 
        "改押货单" 
        
        data = {
            "updateInvtMortgageOrderVO": {
                "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
                "id": id # 押货单id
            },
            "invtMortgageProductVOList": [
                {
                    "productCode": produc["productCode"], # 物品编码
                    "id": produc["id"], # 物品id
                    "productNum": 1, # 物品数量
                    "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                }
            ],
            "isBatchCancel": 0 # 批量取消标志
        }
        with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == None
            assert r.json()["message"] == "操作成功"
                
    step_mgmt_inventory_order_listMortgageOrder()
    step_mgmt_inventory_order_getOrderDetail()
    step_mgmt_inventory_mortgageAmount_getAvailableAmount()
    step_mgmt_inventory_order_checkProductInventory()
    step_mgmt_inventory_order_updateMortgageOrder()
    
    return orderSn


@allure.title("普通押货单批量修改")
@pytest.fixture(scope="function")
def updateMortgageOrder_0(purchase_commit):
    "普通押货单批量修改"
    
    from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
    from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
    from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
            
    access_token = os.environ["access_token_2"]
    orderSn = purchase_commit
    id = None
    produc = None # 押货单详情待修改产品信息
    availableAmount = None # 根据storeCode查询押货余额
    
    def step_mgmt_inventory_order_listMortgageOrder():
        "获取id"
        
        nonlocal id
        params = deepcopy(params01) 
        params["orderSn"] = orderSn
        with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
    
    def step_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情"
        
        nonlocal produc
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["productVoList"]:
                if d["productNum"] > 1:
                        produc = d
    
    def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
        "根据storeCode查询押货余额" 
        
        nonlocal availableAmount
        params = {
            "storeCode": store
        }
        with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]
    
    def step_mgmt_inventory_order_checkProductInventory(): 
        "店铺库存校验接口" 
        
        data = {
            "productDtoList":[ # 需要修改的商品
                {
                    "productCode": produc["productCode"], # 商品一级编码
                    "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                    "productNum": 2 # 需要减少的商品数量(绝对值)
                }
            ],
            "storeCode": store # 店铺中心编号
        }
        with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == []

    def step_mgmt_inventory_order_updateMortgageOrder(): 
        "改押货单" 
        
        data = {
            "updateInvtMortgageOrderVO": {
                "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
                "id": id # 押货单id
            },
            "invtMortgageProductVOList": [
                {
                    "productCode": produc["productCode"], # 物品编码
                    "id": produc["id"], # 物品id
                    "productNum": 0, # 物品数量
                    "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                }
            ],
            "isBatchCancel": 1 # 批量取消标志
        }
        with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == None
            assert r.json()["message"] == "操作成功"
                
    step_mgmt_inventory_order_listMortgageOrder()
    step_mgmt_inventory_order_getOrderDetail()
    step_mgmt_inventory_mortgageAmount_getAvailableAmount()
    step_mgmt_inventory_order_checkProductInventory()
    step_mgmt_inventory_order_updateMortgageOrder()
    
    return orderSn


@allure.title("普通押货单欠货停发")
@pytest.fixture(scope="function")
def updateMortgageOrder_1_0(updateMortgageOrder):
    "普通押货单欠货停发"
    
    from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
    from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
    from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
    from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
    
    access_token = os.environ["access_token_2"]        
    orderSn = updateMortgageOrder
    returnOrderSn = None # 欠货停发后生产的退押货单
    id = None
    produc = None # 押货单详情待修改产品信息
    availableAmount = None # 根据storeCode查询押货余额
    
    def step_mgmt_inventory_order_listMortgageOrder():
        "获取id"
        
        nonlocal id
        params = deepcopy(params01) 
        params["orderSn"] = orderSn
        with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
    
    def step_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情"
        
        nonlocal produc
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            produc = r.json()["data"]["productVoList"][0]
    
    def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
        "根据storeCode查询押货余额" 
        
        nonlocal availableAmount
        params = {
            "storeCode": store
        }
        with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableAmount = r.json()["data"]
    
    def step_mgmt_inventory_order_checkProductInventory(): 
        "店铺库存校验接口" 
        
        data = {
            "productDtoList":[ # 需要修改的商品
                {
                    "productCode": produc["productCode"], # 商品一级编码
                    "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                    "productNum":1 # 需要减少的商品数量(绝对值)
                }
            ],
            "storeCode": store # 店铺中心编号
        }
        with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == []

    def step_mgmt_inventory_order_updateMortgageOrder(): 
        "改押货单" 
        
        data = {
            "updateInvtMortgageOrderVO": {
                "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
                "id": id # 押货单id
            },
            "invtMortgageProductVOList": [
                {
                    "productCode": produc["productCode"], # 物品编码
                    "id": produc["id"], # 物品id
                    "productNum": 0, # 物品数量
                    "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                }
            ],
            "isBatchCancel": 1 # 批量取消标志
        }
        with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == None
            assert r.json()["message"] == "操作成功"

    def step_02_mgmt_inventory_order_getOrderDetail():
        "后台获取押货单详情:退押货单号"
        
        nonlocal returnOrderSn
        params = {
            "orderId": id
        }
        with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnOrderSn = r.json()["data"]["editLogList"][0]["returnOrderSn"]
                
    step_mgmt_inventory_order_listMortgageOrder()
    step_mgmt_inventory_order_getOrderDetail()
    step_mgmt_inventory_mortgageAmount_getAvailableAmount()
    step_mgmt_inventory_order_checkProductInventory()
    step_mgmt_inventory_order_updateMortgageOrder()
    step_02_mgmt_inventory_order_getOrderDetail()
    
    return returnOrderSn


@allure.title("完美后台押货退货单")
@pytest.fixture(scope="function")
def returnOrder_auditOrder():
    "完美后台押货退货单"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_getProductForAddPage import _mgmt_inventory_returnOrder_getProductForAddPage # 添加退货单时的商品搜索
    from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_addMortgageReturnOrder import _mgmt_inventory_returnOrder_addMortgageReturnOrder # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_addOpinion import _mgmt_inventory_returnOrder_addOpinion # 后台押货退货添加审批意见
    from api.mall_mgmt_application. _mgmt_inventory_returnOrder_auditOrder import  _mgmt_inventory_returnOrder_auditOrder # 后台审批押货退货单

    from api.mall_store_application._appStore_purchaseReturnOrder_returnInfo import _appStore_purchaseReturnOrder_returnInfo # 提交退回信息

    from api.mall_mgmt_application._mgmt_inventory_returnOrder_inspectOrder import  _mgmt_inventory_returnOrder_inspectOrder # 后台押货退货验货
    
    access_token = os.environ["access_token_2"]
    store_token = os.environ["store_token"]    
    getReason = None # 获取各种退换货原因 
    getStoreInfo = None # 获取服务中心信息
    getProductForAddPage = None # 添加退货单时的商品搜索
    productNum = 2 # 押货退货数量
    addMortgageReturnOrder = None # 押货退货单Id

    getOrderDetail = None # 完美后台押货退货单详情
    addOpinion = None # 后台押货退货添加审批意见
    
    def step_mgmt_inventory_common_getReason():
        "获取各种退换货原因"
        
        nonlocal getReason
        params = {
            "type": 3, 
        }              
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]

    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getStoreInfo = r.json()["data"]

    def step_mgmt_inventory_returnOrder_getProductForAddPage():
        "添加退货单时的商品搜索"
        
        nonlocal getProductForAddPage
        params = {
            "storeCode": store, # 服务中心编号
            "productCode": productCode, # 商品一级或二级编码
        }              
        with _mgmt_inventory_returnOrder_getProductForAddPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getProductForAddPage = r.json()["data"]

    def step_mgmt_inventory_order_checkProductInventory():
        "店铺库存校验接口"
        
        data = {
            "productDtoList":[ # 需要修改的商品
                {
                    "productCode": productCode, # 商品一级编码
                    "productSecCode":"", # 商品二级编码(非定制品不要传此字段)
                    "productNum": 2 # 需要减少的商品数量(绝对值)
                }
            ],
            "storeCode": store # 店铺中心编号
        }              
        with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == []

    def step_mgmt_inventory_returnOrder_addMortgageReturnOrder():
        "后台申请添加押货退货单"
        
        nonlocal addMortgageReturnOrder
        getProductForAddPage["productNum"] = productNum
        getProductForAddPage["productRemarks"] = "我是产品退货备注说明"
        data = {
            "invtMortgageReturnOrderProductVOList": [getProductForAddPage],
            "invtMortgageReturnOrderVO": {
                "orderMark": 0,
                "reasonFirst": getReason[1]["returnReason"],
                "reasonFirstRemarks": "我是一级备注原因哦哦哦哦哦哦",
                "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
                "reasonSecondRemarks": "我是二级备注原因哦哦哦哦哦哦",
                "storeCode": getStoreInfo["code"]
            }
        }              
        with _mgmt_inventory_returnOrder_addMortgageReturnOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addMortgageReturnOrder = r.json()["data"]

    def step_mgmt_inventory_returnOrder_addOpinion():
        "后台押货退货添加审批意见"
        
        nonlocal addOpinion
        data = {
            "orderId": addMortgageReturnOrder, # 押货或售后单id
            "content": f"同意这个退货申请" # 意见内容
        }
        with _mgmt_inventory_returnOrder_addOpinion(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            addOpinion = r.json()["data"]

    def step_mgmt_inventory_returnOrder_getOrderDetail():
        "后台押货退货单详情"
        
        nonlocal getOrderDetail
        params = {
            "orderId": addMortgageReturnOrder
        }
        with _mgmt_inventory_returnOrder_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getOrderDetail = r.json()["data"]
                    
    def step_mgmt_inventory_returnOrder_auditOrder():
        "后台审批押货退货单"
        
        data = {
            "id": addMortgageReturnOrder, # 押货退货单id
            "auditRemarks": f"我只能同意退货申请", # 审核备注
            "auditFileName": "", # 审核附件名称
            "auditStatus": 1, # 审核结果 0不通过 1通过
            "auditFileUrl": "", # 审核附件url
            "reasonFirst": getReason[1]["returnReason"], # 一级原因
            "reasonFirstRemarks": "我就是想退货，你敢不同意吗", # 一级原因备注
            "reasonSecond": getReason[1]["reasonList"][1]["returnReason"], # 二级原因
            "reasonSecondRemarks": "算了，这次就允许你退货吧", # 二级原因备注
            "returnInfo": "深圳仓", # 退回地址信息
            "preAuditFileUrl": ""
        }
        with _mgmt_inventory_returnOrder_auditOrder(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_purchaseReturnOrder_returnInfo():
        "提交退回信息"
        
        data = {
            "returnType": 2, # 退回类型 1自带 2邮寄
            "expressCompany": "小何物流", # 物流公司
            "expressNo": str(round(time.time())), # 物流单号
            "expressFreightProof": "", # 物流费用凭证url
            "expressFreightProofName": "", # 物流费用凭证名称
            "processRemarks": "退回产品都要说明吗", # 退回处理说明
            "orderId": addMortgageReturnOrder # 退货单id
        }
        with _appStore_purchaseReturnOrder_returnInfo(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_returnOrder_inspectOrder():
        "完美后台押货退货验货"
        
        data = {
            "orderId": addMortgageReturnOrder, # 退货单id
            "inspectStatus": 1, # 验货意见 0不通过 1通过
            "expressSubsidy": 100, # 运费补贴
            "inspectRemarks": "我验货通过了", # 验货备注
            "orderReturnRealAmount": getOrderDetail["orderVo"]["orderReturnAmount"], # orderReturnRealAmount
            "productList": [{
                "id": getOrderDetail["productVoList"][0]["id"], # 物品id
                "productRealNum": getOrderDetail["productVoList"][0]["productNum"], # 物品实退数量
                "productRealAmount": getOrderDetail["productVoList"][0]["productMortgagePrice"] * getOrderDetail["productVoList"][0]["productNum"] # 退货单实退金额总额
            }]
        }
        with _mgmt_inventory_returnOrder_inspectOrder(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            
    step_mgmt_inventory_common_getReason()
    step_mgmt_inventory_common_getStoreInfo()
    step_mgmt_inventory_returnOrder_getProductForAddPage()
    step_mgmt_inventory_order_checkProductInventory()
    step_mgmt_inventory_returnOrder_addMortgageReturnOrder()
    step_mgmt_inventory_returnOrder_addOpinion()
    step_mgmt_inventory_returnOrder_getOrderDetail()
    step_mgmt_inventory_returnOrder_auditOrder()
    step_appStore_purchaseReturnOrder_returnInfo()
    step_mgmt_inventory_returnOrder_inspectOrder()
    
    return getOrderDetail["orderVo"]["orderSn"]


@allure.title("完美后台押货退货单-组合产品,只有库存大于等于0时才退货")
@pytest.fixture(scope="function")
def returnOrder_auditOrder_zh():
    "完美后台押货退货单-组合产品,只有库存大于等于0时才退货"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
    from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_getProductForAddPage import _mgmt_inventory_returnOrder_getProductForAddPage # 添加退货单时的商品搜索
    from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_addMortgageReturnOrder import _mgmt_inventory_returnOrder_addMortgageReturnOrder # 店铺库存校验接口
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
    from api.mall_mgmt_application._mgmt_inventory_returnOrder_addOpinion import _mgmt_inventory_returnOrder_addOpinion # 后台押货退货添加审批意见
    from api.mall_mgmt_application. _mgmt_inventory_returnOrder_auditOrder import  _mgmt_inventory_returnOrder_auditOrder # 后台审批押货退货单

    from api.mall_store_application._appStore_purchaseReturnOrder_returnInfo import _appStore_purchaseReturnOrder_returnInfo # 提交退回信息

    from api.mall_mgmt_application._mgmt_inventory_returnOrder_inspectOrder import  _mgmt_inventory_returnOrder_inspectOrder # 后台押货退货验货
    
    access_token = os.environ["access_token_2"]
    store_token = os.environ["store_token"]    
    getReason = None # 获取各种退换货原因 
    getStoreInfo = None # 获取服务中心信息
    getProductForAddPage = [] # 添加退货单时的商品搜索
    addMortgageReturnOrder = None # 押货退货单Id
    productNum = 0 # 押货退货数量
    getOrderDetail = None # 完美后台押货退货单详情
    addOpinion = None # 后台押货退货添加审批意见
    
    @allure.step("运营后台押货M7035,确保组合成功")
    def auditMortgageOrder():
        "运营后台押货"
        
        from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
        from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
        from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
        from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
        from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
        from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

        from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
        from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
        from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
        from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
        from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
        from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
        from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
        from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
        
        access_token = os.environ["access_token_2"]
        
        getStoreInfo = None # 获取服务中心信息
        availableAmount = None # 根据storeCode查询押货余额
        searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
        products_list = [] # 押货产品
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 5 # 押货数量
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        pageSearchList = None # 待审核流水信息
        
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            "获取服务中心信息"
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"]
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
            "根据storeCode查询押货余额"  
            
            nonlocal availableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]
        
        @allure.step("根据产品关键字搜索普通商品列表")
        def step_mgmt_inventory_order_searchProductsForAddPage(): 
            "根据产品关键字搜索普通商品列表" 
            
            nonlocal searchProductsForAddPage
            params = deepcopy(params01)
            params["storeCode"] = store
            params["keyword"] = productCode
            with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:   
                        searchProductsForAddPage = d
        
        @allure.step("运营后台添加押货单")
        def step_mgmt_inventory_order_addMortgageOrder(): 
            "运营后台添加押货单" 
            
            nonlocal id
            data = {
                "invtMortgageOrderVO": {
                    "storeCode": store,
                    "isDelivery": 1, # 0不需要发货 1需要发货
                    "remarks": "" # 押货备注
                },
                "invtMortgageOrderProductVOList": [
                    {
                        "productCode": productCode, # 物品编号
                        "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
                    }
                ]
            }
            with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id =  r.json()["data"]
        
        @allure.step("运营后台审批押货单")
        def step_mgmt_inventory_order_auditMortgageOrder():
            "运营后台审批押货单"
            
            data = {
                "id": id, # 押货单id
                "auditStatus": 1, # 审核结果 0不通过 1通过
                "auditRemarks": f"同意提交押货单申请" # 审核备注
            }
            with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == 1
        
        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            "后台获取押货单详情"
            
            nonlocal getOrderDetail
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderDetail = r.json()["data"]

        @allure.step("按银行流水类型获取款项映射列表")
        def step_mgmt_inventory_remit_getSourceTypeByRemitType():
            "按银行流水类型获取款项映射列表"
            
            nonlocal getSourceTypeByRemitType
            params = {
                "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
            }              
            with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getSourceTypeByRemitType = r.json()["data"]
                
        def step_mgmt_inventory_common_getStoreInfo():
            "获取服务中心信息"
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"] 
                        
        def step_mgmt_sys_getAccountList():
            "查询分公司银行账号"
            
            nonlocal getAccountList
            params = {
                "companyCode" : getStoreInfo["companyCode"],  # 公司编码
            }             
            with _mgmt_sys_getAccountList(params, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getAccountList = r.json()["data"] 

        def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
            "根据storeCode查询押货余额主表数据"
            
            nonlocal getMortgageAmountByStore
            params = {
                "storeCode": getStoreInfo["code"]
            }            
            with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getMortgageAmountByStore = r.json()["data"] 

        def step_mgmt_store_getBankAccountList():
            "通过storeCode获取银行账户资料信息"
            
            nonlocal getBankAccountList
            params = {
                "storeCode": getStoreInfo["code"]
            }            
            with _mgmt_store_getBankAccountList(params, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getBankAccountList = r.json()["data"] 

        def step_mgmt_inventory_remit_addManualInputRemit():
            "手工增押货款"
            
            data = {
                "storeCode": getStoreInfo["code"], # 店铺编号
                "storeName": getStoreInfo["name"],
                "leaderName": getStoreInfo["leaderName"],
                "companyCode": getStoreInfo["companyCode"], # 分公司code
                "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                "changeReason": "汇押货款", # 调整原因
                "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                "receiptAccount": getAccountList[0]["account"], # 收款账号
                "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
            }           
            with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        def step_mgmt_inventory_remit_pageSearchList():
            "手工录入流水分页搜索列表:获取待审核流水信息"
            
            nonlocal pageSearchList 
            data = deepcopy(data01)
            data["storeCode"] = getStoreInfo["code"]
            data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
            with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageSearchList = r.json()["data"]["list"]

        def step_mgmt_inventory_remit_verifyManualInputRemit():
            "手工录入流水审核"
            
            params = pageSearchList[0]
            params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
            
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_searchProductsForAddPage()
        
        if searchProductsForAddPage["productInventoryNum"] < 5:
            productNum = 5 - searchProductsForAddPage["productInventoryNum"]
       
        products_list.append({
                        "productCode": productCode, # 物品编号
                        "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
        })
        
        if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
            step_mgmt_inventory_remit_getSourceTypeByRemitType()
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_sys_getAccountList()
            step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
            step_mgmt_store_getBankAccountList()
            step_mgmt_inventory_remit_addManualInputRemit()
            step_mgmt_inventory_remit_pageSearchList()
            step_mgmt_inventory_remit_verifyManualInputRemit()
            
        step_mgmt_inventory_order_addMortgageOrder()
        step_mgmt_inventory_order_auditMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        
        return getOrderDetail["orderVo"]["orderSn"]

    def step_mgmt_inventory_common_getReason():
        "获取各种退换货原因"
        
        nonlocal getReason
        params = {
            "type": 3, 
        }              
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]

    def step_mgmt_inventory_common_getStoreInfo():
        "获取服务中心信息"
        
        nonlocal getStoreInfo
        params = {
            "storeCode": store
        }              
        with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getStoreInfo = r.json()["data"]

    def step_mgmt_inventory_returnOrder_getProductForAddPage():
        "添加退货单时的商品搜索"
        
        nonlocal getProductForAddPage
        params = {
            "storeCode": store, # 服务中心编号
            "productCode": productCode_zh, # 商品一级或二级编码
        }              
        with _mgmt_inventory_returnOrder_getProductForAddPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getProductForAddPage = r.json()["data"]

    def step_mgmt_inventory_order_checkProductInventory():
        "店铺库存校验接口"
        
        data = {
            "productDtoList":[ # 需要修改的商品
                {
                    "productCode": productCode_zh, # 商品一级编码
                    "productSecCode":"", # 商品二级编码(非定制品不要传此字段)
                    "productNum": productNum  # 需要减少的商品数量(绝对值)
                }
            ],
            "storeCode": store # 店铺中心编号
        }              
        with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_returnOrder_addMortgageReturnOrder():
        "后台申请添加押货退货单"
        
        nonlocal addMortgageReturnOrder
        getProductForAddPage["productNum"] = productNum # 押货退货数量
        getProductForAddPage["productRemarks"] = "我是产品退货备注说明"
        data = {
            "invtMortgageReturnOrderProductVOList": [getProductForAddPage],
            "invtMortgageReturnOrderVO": {
                "orderMark": 0,
                "reasonFirst": getReason[1]["returnReason"],
                "reasonFirstRemarks": "我是一级备注原因哦哦哦哦哦哦",
                "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
                "reasonSecondRemarks": "我是二级备注原因哦哦哦哦哦哦",
                "storeCode": getStoreInfo["code"]
            }
        }              
        with _mgmt_inventory_returnOrder_addMortgageReturnOrder(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addMortgageReturnOrder = r.json()["data"]

    def step_mgmt_inventory_returnOrder_addOpinion():
        "后台押货退货添加审批意见"
        
        nonlocal addOpinion
        data = {
            "orderId": addMortgageReturnOrder, # 押货或售后单id
            "content": f"同意这个退货申请" # 意见内容
        }
        with _mgmt_inventory_returnOrder_addOpinion(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            addOpinion = r.json()["data"]

    def step_mgmt_inventory_returnOrder_getOrderDetail():
        "后台押货退货单详情"
        
        nonlocal getOrderDetail
        params = {
            "orderId": addMortgageReturnOrder
        }
        with _mgmt_inventory_returnOrder_getOrderDetail(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getOrderDetail = r.json()["data"]
                    
    def step_mgmt_inventory_returnOrder_auditOrder():
        "后台审批押货退货单"
        
        data = {
            "id": addMortgageReturnOrder, # 押货退货单id
            "auditRemarks": f"我只能同意退货申请", # 审核备注
            "auditFileName": "", # 审核附件名称
            "auditStatus": 1, # 审核结果 0不通过 1通过
            "auditFileUrl": "", # 审核附件url
            "reasonFirst": getReason[1]["returnReason"], # 一级原因
            "reasonFirstRemarks": "我就是想退货，你敢不同意吗", # 一级原因备注
            "reasonSecond": getReason[1]["reasonList"][1]["returnReason"], # 二级原因
            "reasonSecondRemarks": "算了，这次就允许你退货吧", # 二级原因备注
            "returnInfo": "深圳仓", # 退回地址信息
            "preAuditFileUrl": ""
        }
        with _mgmt_inventory_returnOrder_auditOrder(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_purchaseReturnOrder_returnInfo():
        "提交退回信息"
        
        data = {
            "returnType": 2, # 退回类型 1自带 2邮寄
            "expressCompany": "小何物流", # 物流公司
            "expressNo": str(round(time.time())), # 物流单号
            "expressFreightProof": "", # 物流费用凭证url
            "expressFreightProofName": "", # 物流费用凭证名称
            "processRemarks": "退回产品都要说明吗", # 退回处理说明
            "orderId": addMortgageReturnOrder # 退货单id
        }
        with _appStore_purchaseReturnOrder_returnInfo(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_returnOrder_inspectOrder():
        "完美后台押货退货验货"
        
        data = {
            "orderId": addMortgageReturnOrder, # 退货单id
            "inspectStatus": 1, # 验货意见 0不通过 1通过
            "expressSubsidy": 100, # 运费补贴
            "inspectRemarks": "我验货通过了", # 验货备注
            "orderReturnRealAmount": getOrderDetail["orderVo"]["orderReturnAmount"], # orderReturnRealAmount
            "productList": [{
                "id": getOrderDetail["productVoList"][0]["id"], # 物品id
                "productRealNum": getOrderDetail["productVoList"][0]["productNum"], # 物品实退数量
                "productRealAmount": getOrderDetail["productVoList"][0]["productMortgagePrice"] * getOrderDetail["productVoList"][0]["productNum"] # 退货单实退金额总额
            }]
        }
        with _mgmt_inventory_returnOrder_inspectOrder(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200 
            
    auditMortgageOrder()
    step_mgmt_inventory_common_getReason()
    step_mgmt_inventory_common_getStoreInfo()
    step_mgmt_inventory_returnOrder_getProductForAddPage()
    if getProductForAddPage["currentStock"] >= 0: # 只有当库存大于0时，才退组合产品
        productNum = getProductForAddPage["currentStock"] + 1 # 押货退货数量
        step_mgmt_inventory_order_checkProductInventory()
        step_mgmt_inventory_returnOrder_addMortgageReturnOrder()
        step_mgmt_inventory_returnOrder_addOpinion()
        step_mgmt_inventory_returnOrder_getOrderDetail()
        step_mgmt_inventory_returnOrder_auditOrder()
        step_appStore_purchaseReturnOrder_returnInfo()
        step_mgmt_inventory_returnOrder_inspectOrder()
    
        return getOrderDetail["orderVo"]["orderSn"]
    

@allure.title("代客售后-押货库存")
@pytest.fixture(scope="function")
def return_applyReturn(walletPay_to_me):
    "代客售后-押货库存"
    
    from api.mall_mgmt_application._mgmt_order_return_getOrderReturnList import _mgmt_order_return_getOrderReturnList # 退货单列表
    from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表
    from api.mall_mgmt_application._mgmt_order_orderInfo import _mgmt_order_orderInfo # 订单信息
    from api.mall_mgmt_application._mgmt_order_return_calcRefundAmount import _mgmt_order_return_calcRefundAmount # 计算订单退款金额
    from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
    from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
    from api.mall_mgmt_application._mgmt_order_return_applyReturn import _mgmt_order_return_applyReturn # 申请退货
    from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情
    from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
    from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核
    
    access_token = os.environ["access_token_2"]
    
    orderNo = None # 订单编号
    calcRefundAmount = None # 计算订单退款金额
    upgradeOrderVerify = None # 升级单校验
    getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
    applyReturn = None # 退货单
    
    def step_mgmt_order_return_getOrderReturnList():
        "退货单列表：是否有待审核的退货单"
            
        nonlocal orderNo, applyReturn
        params = {
            "returnType": 1, # 退货类型 1->当月退货 2->隔月退货
            "expressType": None, # 发货方式 1->服务中心自提 2->公司交付
            "applySource": None, # 申请来源 0->总公司代客售后 1->顾客申请 2->公司申请 3->商城1.0
            "companyCode": "", # 分公司编号
            "financeCompanyCode": "", # 财务分公司编号
            "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
            "storeCode": "", # 服务中心编号
            "customerCard": "", # 顾客卡号
            "creatorCard": username, # 开单人卡号
            "returnNo": "", # 退货单号
            "orderNo": "", # 订单号
            "isDeliver": None, # 是否发货 0->不发货 1->发货
            "isUpgrade": None, # 是否升级单 0->否 1->是
            "depositNo": "", # 对应定金订单号
            "currentPage": 1, 
            "pageSize": 10,
            "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
            "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
            "returnStatus": 1, # 服务状态 1->待审核 2->待退回 3->待验货 98->已取消 99->已完成
            "pageNum": 1,
        }           
        with _mgmt_order_return_getOrderReturnList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                orderNo = r.json()["data"]["list"][0]["orderNo"]
                applyReturn = r.json()["data"]["list"][0]["returnNo"] 
    
    @stepreruns()
    def step_mgmt_order_orderList():
        "订单列表：获取订单编号"
            
        nonlocal orderNo
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
            "orderNo": "",
            "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
            "stockType": 2, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
            "creatorCard": username, # 开单人卡号
            "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
            "isUpgrade": 0, # 是否升级单
            "commitStartTime": f"{time.strftime('%Y-%m', time.localtime(time.time()))}-01", # 开单开始时间
            "commitEndTime": time.strftime("%Y-%m-%d", time.localtime(time.time())), # 开单结束时间
        }           
        with _mgmt_order_orderList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"] is not None
            orderNo = r.json()["data"]["list"][0]["orderNo"]   
    
    def step_mgmt_order_orderInfo():
        "订单信息"
            
        params = {
            "orderNo": orderNo, # 订单编号
        }      
        with _mgmt_order_orderInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_order_return_calcRefundAmount(): 
        "计算订单退款金额"
        
        nonlocal calcRefundAmount   
        params = {
            "orderNo": orderNo, # 订单编号
        }      
        with _mgmt_order_return_calcRefundAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            calcRefundAmount = r.json()["data"]

    def step_mgmt_order_return_upgradeOrderVerify(): 
        "升级单校验"
        
        nonlocal upgradeOrderVerify   
        data = {
            "orderNo": orderNo, 
            "applySource": 0,
        }     
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
            upgradeOrderVerify = r.json()["data"]["resultType"]
    
    def step_sys_api_getAllReturnReasonByType(): 
        "通过退换货类型获取 一级,二级层级原因"
        
        nonlocal getAllReturnReasonByType   
        params = {
            "returnType": 1, # 退换货类型：1.商城退货，2.商城换货，3.服务中心押货退货，4.服务中心押货换货，5.展业包订货退货，6.展业包订货换货
        }   
        with _sys_api_getAllReturnReasonByType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getAllReturnReasonByType = r.json()["data"]

    def step_mgmt_order_return_applyReturn(): 
        "申请退货"
        
        nonlocal applyReturn 
        data = {
            "orderNo": orderNo, # 订单编号
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
            "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
            "reason1Remark": "我没钱了要退货", # 退货一级原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
            "reason2Remark": "给你特批退货吧", # 退货二级原因备注
            "applySource": 0 # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
        }   
        with _mgmt_order_return_applyReturn(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]

    def step_mgmt_order_return_getOrderReturnDetails(): 
        "退货详情"
        
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_order_return_saveComment():
        "新增或修改留言" 
        
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment": "我同意这个代客售后申请", # 留言内容
            "id": "" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_02_mgmt_order_return_upgradeOrderVerify(): 
        "升级单校验"
        
        nonlocal upgradeOrderVerify   
        data = {
            "orderNo": orderNo, 
        }     
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
            upgradeOrderVerify = r.json()["data"]["resultType"]
    
    def step_mgmt_order_return_auditOrderReturn(): 
        "分公司退货审核"
        
        data = {
            "serviceNo": applyReturn, # 售后单号
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意退款" # 审核意见
        }
        with _mgmt_order_return_auditOrderReturn(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    step_mgmt_order_return_getOrderReturnList()
    if applyReturn: 
        step_mgmt_order_return_getOrderReturnDetails()
        step_mgmt_order_return_saveComment()
        step_02_mgmt_order_return_upgradeOrderVerify()
        step_mgmt_order_return_auditOrderReturn()        
    step_mgmt_order_orderList()
    step_mgmt_order_orderInfo()
    step_mgmt_order_return_calcRefundAmount()
    step_mgmt_order_return_upgradeOrderVerify()
    step_sys_api_getAllReturnReasonByType()
    step_mgmt_order_return_applyReturn()
    step_mgmt_order_return_getOrderReturnDetails()
    step_mgmt_order_return_saveComment()
    step_02_mgmt_order_return_upgradeOrderVerify()
    step_mgmt_order_return_auditOrderReturn()
    
    return applyReturn


@allure.title("代客售后-押货库存-隔月退货")
@pytest.fixture(scope="function")
def return_applyReturn_2():
    "代客售后-押货库存-隔月退货"
    
    from api.mall_mgmt_application._mgmt_order_return_getOrderReturnList import _mgmt_order_return_getOrderReturnList # 退货单列表
    from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表
    from api.mall_mgmt_application._mgmt_order_orderInfo import _mgmt_order_orderInfo # 订单信息
    from api.mall_mgmt_application._mgmt_order_return_calcRefundAmount import _mgmt_order_return_calcRefundAmount # 计算订单退款金额
    from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
    from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
    from api.mall_mgmt_application._mgmt_order_return_applyReturn import _mgmt_order_return_applyReturn # 申请退货
    from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情
    from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
    from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核
    
    access_token = os.environ["access_token_2"]
    
    orderNo = None # 订单编号
    calcRefundAmount = None # 计算订单退款金额
    upgradeOrderVerify = None # 升级单校验
    getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
    applyReturn = None # 退货单

    @allure.step("退货单列表：是否有待审核的退货单")    
    def step_mgmt_order_return_getOrderReturnList():
            
        nonlocal orderNo, applyReturn
        params = {
            "returnType": 2, # 退货类型 1->当月退货 2->隔月退货
            "expressType": None, # 发货方式 1->服务中心自提 2->公司交付
            "applySource": None, # 申请来源 0->总公司代客售后 1->顾客申请 2->公司申请 3->商城1.0
            "companyCode": "", # 分公司编号
            "financeCompanyCode": "", # 财务分公司编号
            "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
            "storeCode": "", # 服务中心编号
            "customerCard": "", # 顾客卡号
            "creatorCard": username, # 开单人卡号
            "returnNo": "", # 退货单号
            "orderNo": "", # 订单号
            "isDeliver": None, # 是否发货 0->不发货 1->发货
            "isUpgrade": None, # 是否升级单 0->否 1->是
            "depositNo": "", # 对应定金订单号
            "currentPage": 1, 
            "pageSize": 10,
            "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
            "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
            "returnStatus": 1, # 服务状态 1->待审核 2->待退回 3->待验货 98->已取消 99->已完成
            "pageNum": 1,
        }           
        with _mgmt_order_return_getOrderReturnList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                orderNo = r.json()["data"]["list"][0]["orderNo"]
                applyReturn = r.json()["data"]["list"][0]["returnNo"]   

    @allure.step("订单列表：获取订单编号")         
    def step_mgmt_order_orderList():
            
        nonlocal orderNo
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
            "orderNo": "",
            "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
            "stockType": 2, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
            "creatorCard": username, # 开单人卡号
            "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
            "isUpgrade": 0, # 是否升级单
            "commitStartTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-1', # 开单开始时间
            "commitEndTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-28', # 开单结束时间
        }           
        with _mgmt_order_orderList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderNo = r.json()["data"]["list"][0]["orderNo"]   

    @allure.step("订单信息")      
    def step_mgmt_order_orderInfo():
            
        params = {
            "orderNo": orderNo, # 订单编号
        }      
        with _mgmt_order_orderInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("计算订单退款金额")  
    def step_mgmt_order_return_calcRefundAmount(): 
        
        nonlocal calcRefundAmount   
        params = {
            "orderNo": orderNo, # 订单编号
        }      
        with _mgmt_order_return_calcRefundAmount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            calcRefundAmount = r.json()["data"]

    @allure.step("升级单校验")  
    def step_mgmt_order_return_upgradeOrderVerify(): 
        
        nonlocal upgradeOrderVerify   
        data = {
            "orderNo": orderNo, 
            "applySource": 0,
        }     
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
            upgradeOrderVerify = r.json()["data"]["resultType"]

    @allure.step("通过退换货类型获取 一级,二级层级原因")      
    def step_sys_api_getAllReturnReasonByType(): 
        
        nonlocal getAllReturnReasonByType   
        params = {
            "returnType": 1, # 退换货类型：1.商城退货，2.商城换货，3.服务中心押货退货，4.服务中心押货换货，5.展业包订货退货，6.展业包订货换货
        }   
        with _sys_api_getAllReturnReasonByType(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getAllReturnReasonByType = r.json()["data"]

    @allure.step("申请退货")  
    def step_mgmt_order_return_applyReturn(): 
        
        nonlocal applyReturn 
        data = {
            "orderNo": orderNo, # 订单编号
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
            "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
            "reason1Remark": "我没钱了要退货", # 退货一级原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
            "reason2Remark": "给你特批退货吧", # 退货二级原因备注
            "applySource": 0 # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
        }   
        with _mgmt_order_return_applyReturn(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]

    @allure.step("退货详情")  
    def step_mgmt_order_return_getOrderReturnDetails(): 
        
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["orderReturn"]["returnType"] == 2 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderReturn"]["returnTypeDesc"] == "隔月退货"

    @allure.step("新增或修改留言")  
    def step_mgmt_order_return_saveComment():
        
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment": "我同意这个代客售后申请", # 留言内容
            "id": "" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("升级单校验")  
    def step_02_mgmt_order_return_upgradeOrderVerify(): 
        
        nonlocal upgradeOrderVerify   
        data = {
            "orderNo": orderNo, 
        }     
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
            upgradeOrderVerify = r.json()["data"]["resultType"]
 
    @allure.step("分公司退货审核")      
    def step_mgmt_order_return_auditOrderReturn(): 
        
        data = {
            "serviceNo": applyReturn, # 售后单号
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意退款" # 审核意见
        }
        with _mgmt_order_return_auditOrderReturn(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    step_mgmt_order_return_getOrderReturnList()
    if applyReturn: 
        step_mgmt_order_return_getOrderReturnDetails()
        step_mgmt_order_return_saveComment()
        step_02_mgmt_order_return_upgradeOrderVerify()
        step_mgmt_order_return_auditOrderReturn()        
    step_mgmt_order_orderList()
    step_mgmt_order_orderInfo()
    step_mgmt_order_return_calcRefundAmount()
    step_mgmt_order_return_upgradeOrderVerify()
    step_sys_api_getAllReturnReasonByType()
    step_mgmt_order_return_applyReturn()
    step_mgmt_order_return_getOrderReturnDetails()
    step_mgmt_order_return_saveComment()
    step_02_mgmt_order_return_upgradeOrderVerify()
    step_mgmt_order_return_auditOrderReturn()
    
    return applyReturn


@allure.title("完美运营后台 套装组合")
@pytest.fixture(scope="function")
def inventory_combine(onSaleVersion, returnOrder_auditOrder_zh):
    "完美运营后台 套装组合"

    from api.mall_mgmt_application._mgmt_inventory_combine_page import params as params01, _mgmt_inventory_combine_page # 分页查询套装组合列表
    from api.mall_mgmt_application._mgmt_inventory_combine_show import _mgmt_inventory_combine_show # 套装组合展示
    from api.mall_mgmt_application._mgmt_inventory_combine import _mgmt_inventory_combine # 套装组合
    from api.mall_mgmt_application._mgmt_inventory_combine_detail import _mgmt_inventory_combine_detail # 查询套装组合明细
                
    access_token = os.environ["access_token_2"]
    combine_page = None # 分页查询套装组合列表
    combine_show = None # 套装组合展示
    productNum = 10 # 押货数量
    combineNum = 2 # 套装组合数量 
    combine_detail = None # 查询套装组合明细
    
    @allure.step("分页查询套装组合列表") 
    def  step_mgmt_inventory_combine_page(): 
    
        nonlocal combine_page
        params = deepcopy(params01)
        params["combineState"] = 1 # 组合状态：1未组合、2已组合
        params["storeCode"] = store
        params["productCode"] = productCode_zh
        with _mgmt_inventory_combine_page(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                combine_page = r.json()["data"]["list"][0]

    @allure.step("套装组合展示") 
    def  step_mgmt_inventory_combine_show(): 
    
        nonlocal combine_show
        params = {
            "id" : combine_page["id"]
        }
        with _mgmt_inventory_combine_show(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combine_show = r.json()["data"]           

    @allure.step("套装组合") 
    def  step_mgmt_inventory_combine(): 
    
        data = {
            "combineId": combine_page["id"], # 套装组合id
            "combineNum": combineNum # 套装组合数量
        }
        with _mgmt_inventory_combine(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("查询套装组合明细") 
    def  step_mgmt_inventory_combine_detail(): 
    
        nonlocal combine_detail
        params = {
            "id" : combine_page["id"]
        }
        with _mgmt_inventory_combine_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combine_detail = r.json()["data"]           
    
    @allure.step("完美运营后台押货")
    def auditMortgageOrder():
        "运营后台押货"
        
        from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
        from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
        from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
        from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
        from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
        from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

        from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
        from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
        from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
        from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
        from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
        from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
        from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
        from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
        
        access_token = os.environ["access_token_2"]
        
        getStoreInfo = None # 获取服务中心信息
        availableAmount = None # 根据storeCode查询押货余额
        searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
        products_list = [] # 押货产品
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        pageSearchList = None # 待审核流水信息
        
        def step_mgmt_inventory_common_getStoreInfo():
            "获取服务中心信息"
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"]
        
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
            "根据storeCode查询押货余额"  
            
            nonlocal availableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]
        
        def step_mgmt_inventory_order_searchProductsForAddPage(): 
            "根据产品关键字搜索普通商品列表" 
            
            nonlocal searchProductsForAddPage
            params = deepcopy(params01)
            params["storeCode"] = store
            params["keyword"] = productCode
            with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:   
                        searchProductsForAddPage = d
        
        def step_mgmt_inventory_order_addMortgageOrder(): 
            "运营后台添加押货单" 
            
            nonlocal id
            data = {
                "invtMortgageOrderVO": {
                    "storeCode": store,
                    "isDelivery": 1, # 0不需要发货 1需要发货
                    "remarks": "" # 押货备注
                },
                "invtMortgageOrderProductVOList": [
                    {
                        "productCode": productCode, # 物品编号
                        "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
                    }
                ]
            }
            with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id =  r.json()["data"]
        
        def step_mgmt_inventory_order_auditMortgageOrder():
            "运营后台审批押货单"
            
            data = {
                "id": id, # 押货单id
                "auditStatus": 1, # 审核结果 0不通过 1通过
                "auditRemarks": f"同意提交押货单申请" # 审核备注
            }
            with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == 1
        
        def step_mgmt_inventory_order_getOrderDetail():
            "后台获取押货单详情"
            
            nonlocal getOrderDetail
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderDetail = r.json()["data"]

        def step_mgmt_inventory_remit_getSourceTypeByRemitType():
            "按银行流水类型获取款项映射列表"
            
            nonlocal getSourceTypeByRemitType
            params = {
                "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
            }              
            with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getSourceTypeByRemitType = r.json()["data"]
                
        def step_mgmt_inventory_common_getStoreInfo():
            "获取服务中心信息"
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"] 
                        
        def step_mgmt_sys_getAccountList():
            "查询分公司银行账号"
            
            nonlocal getAccountList
            params = {
                "companyCode" : getStoreInfo["companyCode"],  # 公司编码
            }             
            with _mgmt_sys_getAccountList(params, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getAccountList = r.json()["data"] 

        def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
            "根据storeCode查询押货余额主表数据"
            
            nonlocal getMortgageAmountByStore
            params = {
                "storeCode": getStoreInfo["code"]
            }            
            with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getMortgageAmountByStore = r.json()["data"] 

        def step_mgmt_store_getBankAccountList():
            "通过storeCode获取银行账户资料信息"
            
            nonlocal getBankAccountList
            params = {
                "storeCode": getStoreInfo["code"]
            }            
            with _mgmt_store_getBankAccountList(params, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getBankAccountList = r.json()["data"] 

        def step_mgmt_inventory_remit_addManualInputRemit():
            "手工增押货款"
            
            data = {
                "storeCode": getStoreInfo["code"], # 店铺编号
                "storeName": getStoreInfo["name"],
                "leaderName": getStoreInfo["leaderName"],
                "companyCode": getStoreInfo["companyCode"], # 分公司code
                "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                "changeReason": "汇押货款", # 调整原因
                "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                "receiptAccount": getAccountList[0]["account"], # 收款账号
                "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
            }           
            with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        def step_mgmt_inventory_remit_pageSearchList():
            "手工录入流水分页搜索列表:获取待审核流水信息"
            
            nonlocal pageSearchList 
            data = deepcopy(data01)
            data["storeCode"] = getStoreInfo["code"]
            data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
            with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageSearchList = r.json()["data"]["list"]

        def step_mgmt_inventory_remit_verifyManualInputRemit():
            "手工录入流水审核"
            
            params = pageSearchList[0]
            params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
            
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_searchProductsForAddPage()
        
        products_list.append({
                        "productCode": productCode, # 物品编号
                        "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
        })
        
        if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
            step_mgmt_inventory_remit_getSourceTypeByRemitType()
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_sys_getAccountList()
            step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
            step_mgmt_store_getBankAccountList()
            step_mgmt_inventory_remit_addManualInputRemit()
            step_mgmt_inventory_remit_pageSearchList()
            step_mgmt_inventory_remit_verifyManualInputRemit()
            
        step_mgmt_inventory_order_addMortgageOrder()
        step_mgmt_inventory_order_auditMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        
        return getOrderDetail["orderVo"]["orderSn"]

    step_mgmt_inventory_combine_page()
    step_mgmt_inventory_combine_show()
    if combine_show["before"][0]["productNum"] < 10:
        productNum = 10 - combine_show["before"][0]["productNum"]
        auditMortgageOrder()
    if combine_show["after"]["productNum"] > -combineNum:
        combineNum = -combine_show["after"]["productNum"]
    step_mgmt_inventory_combine()
    step_mgmt_inventory_combine_detail()
    
    return combine_detail


@allure.title("完美运营后台拆分单个套装")
@pytest.fixture(scope="function")
def bundle_splitBundle(auditMortgageOrder_zh, offSaleVersion):
    "完美运营后台拆分单个套装"
    
    from api.mall_mgmt_application._mgmt_product_bundle_getSaleOffBundleList import data as data01, _mgmt_product_bundle_getSaleOffBundleList # 查询拆分套装列表
    from api.mall_mgmt_application._mgmt_product_bundle_splitBundlePreview import _mgmt_product_bundle_splitBundlePreview # 拆分单个套装确认页
    from api.mall_mgmt_application._mgmt_product_bundle_splitPreview import _mgmt_product_bundle_splitPreview # 批量/单独拆分前明细预览
    from api.mall_mgmt_application._mgmt_product_bundle_splitBundle import _mgmt_product_bundle_splitBundle # 拆分单个套装
    from api.mall_mgmt_application._mgmt_product_bundle_splitDetailCount import _mgmt_product_bundle_splitDetailCount # 拆分明细数量统计--拆分后
    from api.mall_mgmt_application._mgmt_product_bundle_splitDetail import _mgmt_product_bundle_splitDetail # 拆分明细
    
    access_token = os.environ["access_token_2"]    
    getSaleOffBundleList = None # 查询拆分套装列表
    splitBundlePreview = None # 拆分单个套装确认页
    splitDetail = [] # 拆分明细
    
    @allure.step("获取套装拆分Id") 
    def  step_mgmt_product_bundle_getSaleOffBundleList():
        "获取套装拆分Id" 
            
        nonlocal getSaleOffBundleList
        data = deepcopy(data01)
        data["serialNo"] = productCode_zh 
        data["splitStatus"] = 1  # 拆分状态，1-未拆分，2-已拆分             
        with _mgmt_product_bundle_getSaleOffBundleList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getSaleOffBundleList = r.json()["data"]["list"][0]
            
    @allure.step("拆分单个套装确认页") 
    def  step_mgmt_product_bundle_splitBundlePreview(): 
        
        nonlocal splitBundlePreview
        params = {
            "productId" : getSaleOffBundleList["productId"],  # 套装id
        }                           
        with _mgmt_product_bundle_splitBundlePreview(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            splitBundlePreview = r.json()["data"]

    @allure.step("批量/单独拆分前明细预览") 
    def  step_mgmt_product_bundle_splitPreview(): 
        
        params = {
            "productIds" : getSaleOffBundleList["productId"],  # 套装id
        }                           
        with _mgmt_product_bundle_splitPreview(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("拆分单个套装") 
    def  step_mgmt_product_bundle_splitBundle(): 
        
        data = {
            "splitId" : getSaleOffBundleList["id"],  #拆分id
        }                           
        with _mgmt_product_bundle_splitBundle(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == {"successCount": splitBundlePreview["suitCount"], "failCount":0}

    @allure.step("拆分明细数量统计--拆分后") 
    def  step_mgmt_product_bundle_splitDetailCount(): 
        
        data = {
            "splitId" : getSaleOffBundleList["id"],  #拆分id
        }                           
        with _mgmt_product_bundle_splitDetailCount(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == {"storeCount": splitBundlePreview["storeCount"],"suitCount": splitBundlePreview["suitCount"]}

    @allure.step("拆分明细") 
    def  step_mgmt_product_bundle_splitDetail(): 
        
        nonlocal splitDetail
        params = {
            "splitId": getSaleOffBundleList["id"], # 拆分id
            "pageNum": 1,
            "pageSize": 100000
        }                          
        with _mgmt_product_bundle_splitDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            splitDetail = r.json()["data"]["list"]

    step_mgmt_product_bundle_getSaleOffBundleList()
    step_mgmt_product_bundle_splitBundlePreview()
    step_mgmt_product_bundle_splitPreview()
    step_mgmt_product_bundle_splitBundle()
    step_mgmt_product_bundle_splitDetailCount()
    step_mgmt_product_bundle_splitDetail()
    
    return splitDetail


@allure.title("完美运营后台-13押货转移")
@pytest.fixture(scope="function")
def addTransfer():
    "完美运营后台-13押货转移"
    
    from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_addTransferList import _mgmt_inventory_disInventoryTransfer_addTransferList # 库存列表
    from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_addTransfer import _mgmt_inventory_disInventoryTransfer_addTransfer # 新建库存转移
    from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_recordList import _mgmt_inventory_disInventoryTransfer_recordList # 库存转移记录列表
    from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_cancelPay import _mgmt_inventory_disInventoryTransfer_cancelPay # 取消支付
    
    access_token = os.environ["access_token_2"]
    addTransferList = None # 库存列表:大于0的库存
    recordList = None # 库存转移记录列表
    
    @allure.step("库存转移记录列表：查看是否存在待支付的转移记录")
    def step_01_mgmt_inventory_disInventoryTransfer_recordList():
        
        nonlocal recordList
        data = {
            "storeCode": store_85, # 服务中心编号
            "pageSize": 10, 
            "pageNum": 1,
        }                
        with _mgmt_inventory_disInventoryTransfer_recordList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in r.json()["data"]["list"]:
                if i["status"] == 2:
                    recordList = i

    @allure.step("取消支付")
    def step_mgmt_inventory_disInventoryTransfer_cancelPay():
        
        params = {
            "id": recordList["id"]
        }               
        with _mgmt_inventory_disInventoryTransfer_cancelPay(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    @allure.step("库存列表:大于0的库存")
    def step_02_mgmt_inventory_disInventoryTransfer_addTransferList():
        
        nonlocal addTransferList
        data = {
            "storeCode": store_85, # 服务中心编号
            "productNumQuery": 1, # 传1大于0;0等于0;-1小于0;2不为0;不传为查全部
            "pageSize": 100000, 
            "pageNum": 1,
        }                
        with _mgmt_inventory_disInventoryTransfer_addTransferList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addTransferList = r.json()["data"]["list"][0]

    @allure.step("新建库存转移")
    def step_mgmt_inventory_disInventoryTransfer_addTransfer():
        
        data = {
            "applyType": "2", # 提交途径 1门店提交 2后台提交
            "storeCode": store_85, # 服务中心编号
            "productList":[
                {
                    "transferNum": 1, # 转移数量
                    "oneThreePrice": addTransferList["securityPrice"], # 1:3押货价
                    "eightFivePrice": addTransferList["orderPrice"], # 85折押货价
                    "productCode": addTransferList["serialNo"] # 产品编号
                }
            ]
        }           
        with _mgmt_inventory_disInventoryTransfer_addTransfer(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
    
    @allure.step("库存转移记录列表")
    def step_mgmt_inventory_disInventoryTransfer_recordList():
        
        nonlocal recordList
        data = {
            "storeCode": store_85, # 服务中心编号
            "pageSize": 10, 
            "pageNum": 1,
        }                
        with _mgmt_inventory_disInventoryTransfer_recordList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            recordList = r.json()["data"]["list"][0]
                    
    step_01_mgmt_inventory_disInventoryTransfer_recordList()
    if recordList:
        step_mgmt_inventory_disInventoryTransfer_cancelPay()
    step_02_mgmt_inventory_disInventoryTransfer_addTransferList()
    step_mgmt_inventory_disInventoryTransfer_addTransfer()
    step_mgmt_inventory_disInventoryTransfer_recordList()
    
    return addTransferList, recordList

# 商城前端下单购货，退货

@allure.title("云商-钱包-自购订单")
@pytest.fixture(scope="function")
def walletPay_to_me(login_oauth_token, wallet_add_10000):
    "云商-钱包-自购订单"
    
    from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search # 搜索商品
    from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
    from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
    from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
    from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
    from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
    from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
    from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
    from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
    from api.mall_mobile_application._mobile_payment_getPayMethod import _mobile_payment_getPayMethod #  获取支付方式
    from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay # 支付
    from api.mall_mobile_application._mobile_payment_queryWalletPayOrder import _mobile_payment_queryWalletPayOrder # 查询支付成功信息
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息
            
    productList = None # 商品详情
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    availableBalance = None # 钱包可用余额
    associationPay = None # 支付方式-邮政储蓄银行信息
    orderCommit = None # 订单信息
    payOrderNo = None # 支付流水号
    queryWalletPayOrder = None # 支付成功信息
    getOrderInfo = None # 详细订单信息
    number = 2 # 购买商品数量
    user = login_oauth_token["data"] # 给某个顾客下单的信息（非下单人）
    token = os.environ["token"]
    
    def step_mobile_product_search():
        "搜索商品"

        nonlocal productList
        data = deepcopy(data01)
        data["keyword"] = productCode
        with _mobile_product_search(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            productList = r.json()["data"]["list"][0]

    def step_mobile_order_carts_getFreightList():
        "获取运费补贴券列表"
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    def step_mobile_order_carts_getCouponList():
        "获取选中结算分组的可用和不可用优惠券列表"
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": user["storeCode"]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    def step_mobile_order_carts_getSecondList():
        "获取购物秒返券券列表"
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": user["storeCode"]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1:
                        getSecondList = d["secondCouponId"]
    
    def step_mobile_order_carts_getGiftList_2():
        "获取电子礼券列表"
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

    def step_mobile_order_carts_toSettlement():
        "选择商品去结算"
                    
        data = {
            "addressId": None,
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "orderInvoice": None, # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": user["storeCode"], # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_trade_orderCommit():
        "提交订单"
                    
        nonlocal orderCommit
        data = {
            "addressId": None,
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId": user["userId"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "orderInvoice": None, # # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": user["storeCode"], # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "isUpgrade": 0 # 是否升级单 0->否 1->是
        } 
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                   
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    def step_mobile_wallet_queryPasswordExist():
        "是否设置了支付密码"
        
        with _mobile_wallet_queryPasswordExist(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    def step_mobile_wallet_getDetail():
        "获取钱包首页相关信息"
        
        nonlocal  availableBalance
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            availableBalance = r.json()["data"]["availableBalance"]
    
    def step_mobile_payment_getPayMethod():
        "获取支付方式"

        nonlocal associationPay
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType":"PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType":1 # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["bankName"] == "邮政储蓄银行":
                    associationPay = d

    def step_mobile_payment_associationPay():
        "支付"

        nonlocal payOrderNo
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            payOrderNo = r.json()["data"]["payOrderNo"]

    def step_mobile_payment_queryWalletPayOrder():
        "查询支付成功信息"

        nonlocal queryWalletPayOrder
        params = {
            "payNo": payOrderNo, # 订单编号(必填)
        }
        with _mobile_payment_queryWalletPayOrder(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryWalletPayOrder = r.json()["data"]

    def step_mobile_orderInfo_getOrderInfo():
        "通过订单号查询客户端订单信息"

        nonlocal getOrderInfo
        params = {
            "orderNo": orderCommit["orderNo"] # 订单编号(必填)
        }
        with _mobile_orderInfo_getOrderInfo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderInfo = r.json()["data"]
            
    step_mobile_product_search()
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_mobile_order_carts_toSettlement()
    step_mobile_trade_orderCommit()
    step_mobile_wallet_queryPasswordExist()
    step_mobile_wallet_getDetail()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_associationPay()
    step_mobile_payment_queryWalletPayOrder()
    step_mobile_orderInfo_getOrderInfo()
    
    return queryWalletPayOrder
    

@allure.title("云商-钱包-自购订单退货")
@pytest.fixture(scope="function")
def walletPay_to_me_applyReturn(walletPay_to_me):
    "云商-钱包-自购订单退货"
    
    from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data as data01, _mobile_orderInfo_getClientOrderList # 客户端订单列表查询
    from api.mall_mobile_application._mobile_web_order_as_applyAfterSale import _mobile_web_order_as_applyAfterSale # 申请售后是否支持退货、换货、维修、返修
    from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import _mobile_web_order_as_returnMonthVerify # 隔月退货验证
    from api.mall_center_sys._mgmt_sys_getAllReNotice import _mgmt_sys_getAllReNotice # 获取退货须知集合
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息
    from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
    from api.mall_mobile_application._mobile_web_order_return_getReturnType import _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
    from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import _mobile_web_order_as_upgradeOrderVerify # 升级单校验
    from api.mall_mobile_application._mobile_order_return_applyReturn import _mobile_order_return_applyReturn # 申请退货/退款
    
    queryWalletPayOrder = walletPay_to_me # 支付成功信息
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    token = os.environ["token"] # 云商
    
    @stepreruns()
    def step_mobile_orderInfo_getClientOrderList():
        "客户端订单列表查询"
        
        data = deepcopy(data01)
        data["orderNo"] = queryWalletPayOrder["orderNos"][0] # 订单号
        data["queryType"] = None # 查询类型(默认为null) null->原有订单(包含85折订单)查询 1->85折转分订单 2->85折转分补报订单 3->85折转分订单+85折转分补报订单
        data["orderStatus"] = [2] # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部        
        with _mobile_orderInfo_getClientOrderList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200 
            assert r.json()["data"]["list"][0]["orderNo"] == queryWalletPayOrder["orderNos"][0]
    
    def step_mobile_web_order_as_applyAfterSale():
        "申请售后是否支持退货、换货、维修、返修"

        params = {
            "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
        }
        with _mobile_web_order_as_applyAfterSale(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["expressType"] == 1 # 配送方式 1->服务中心自提 2->公司配送
            assert r.json()["data"]["isExchange"] == 0 # 是否支持换货：1->是；0->否
            assert r.json()["data"]["isRepair"] == 0 # 是否支持维修：1->是；0->否
            assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
            assert r.json()["data"]["isReturnRepair"] == 0 # 是否支持返修：1->是；0->否
            assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
            assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
            assert r.json()["data"]["orderNo"] == queryWalletPayOrder["orderNos"][0]

    def step_mobile_web_order_as_returnMonthVerify():
        "隔月退货验证"
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
        }
        with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    def step_mgmt_sys_getAllReNotice():
        "获取退货须知集合"
              
        with _mgmt_sys_getAllReNotice(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_orderInfo_getOrderInfo():
        "通过订单号查询客户端订单信息"
            
        params = {
            "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
        }
        with _mobile_orderInfo_getOrderInfo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_order_return_getReturnReasonByType():
        "退货/退款原因列表"
            
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    def step_mobile_web_order_return_getReturnType():
        "获取退货类型：1：当月退 2：隔月退"
            
        nonlocal getReturnType
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
        }
        with _mobile_web_order_return_getReturnType(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]

    def step_mobile_web_order_as_upgradeOrderVerify():
        "升级单校验"
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
        }
        with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]  

    def step_mobile_order_return_applyReturn():
        "申请退货/退款"
        
        nonlocal applyReturn
        data = {
            "attachmentUrlList": [], # 退货凭证URL列表
            "orderNo": queryWalletPayOrder["orderNos"][0], # 订单编号
            "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
            "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
            "reason1Remark": "" # 退货一级原因备注
        }
        with _mobile_order_return_applyReturn(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
    
    step_mobile_orderInfo_getClientOrderList()  
    step_mobile_web_order_as_applyAfterSale()
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_orderInfo_getOrderInfo()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    
    return queryWalletPayOrder, applyReturn
    

