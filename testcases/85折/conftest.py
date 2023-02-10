# coding:utf-8

import pytest
from api.mall_center_sys._mgmt_sys_getAccountList import params as params01, _mgmt_sys_getAccountList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data as data03, _mgmt_inventory_disManualInputRemit_add
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify

from util.stepreruns import stepreruns
from setting import store_85, productCode, productCode_zh, productCode_SecondCoupon, username_85, username_vip
import os
from copy import deepcopy
import uuid
import time
import datetime
import allure
import random, string


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
    
    access_token = os.environ["access_token"]
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
    
    step_fin_api_voucher_voucher_generate() # 发放电子礼券 5元
    
    # 发放运费补贴券 15元
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
 
# 添加保证金

@pytest.fixture(scope="function")
def inventory_add():
    "使10>=保证金>0,以便进行组合支付"
    
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    id = None
    access_token = os.environ["access_token"]
                
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心信息"
        
        nonlocal getStoreByCode
        params = deepcopy(params03)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            getStoreByCode = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = deepcopy(params01)
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            getAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = deepcopy(params04)
        params["storeCode"] = getStoreByCode["store"]["code"]               
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            getBankAccountList = r.json()["data"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        "1:3押货余额及85折保证金余额查询"
        
        nonlocal getStoreWalletMsg
        params = deepcopy(params02)
        params["storeCode"] = getStoreByCode["store"]["code"]                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            getStoreWalletMsg = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_disManualInputRemit_add(): 
        "85折手工录入流水"
                
        data = deepcopy(data03)
        data["storeCode"] = getStoreByCode["store"]["code"]
        data["storeName"] = getStoreByCode["store"]["name"]
        data["companyCode"] = getStoreByCode["store"]["companyCode"]
        data["companyName"] = getAccountList[0]["accountName"]
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["changeReason"] = "其他"
        if remitMoney >= 0: # 服务中心付款
            data["payAccount"] = getBankAccountList[0]["account"]
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"]
            data["receiptBankName"] = getAccountList[0]["bankType"]
            data["remitMoney"] = remitMoney # >0
        elif remitMoney < 0: # 分公司付款
            data["payAccount"] = getAccountList[0]["account"]
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"]
            data["receiptBankName"] = getBankAccountList[0]["branch"]
            data["remitMoney"] = remitMoney # <0
        data["sourceType"] = 3 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
        data["inputRemark"] = f"录入其他款 {remitMoney}元"              
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_disManualInputRemit_pageList():
        "85折手工录入流水分页搜索列表,获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["storeCode"] = getStoreByCode["store"]["code"] 
        data["verifyStatus"] = 0 # 待审核列表             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            id = r.json()["data"]["list"][0]["id"]
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_disManualInputRemit_verify():
        "85折手工录入流水单个审核"
        
        params = deepcopy(params05)
        params["id"] = id
        params["verifyRemark"] = f"同意录入其它款 {remitMoney}元" # 审核备注
        params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
        
    step_mgmt_store_getStoreByCode()
    step_mgmt_sys_getAccountList()
    step_mgmt_store_getBankAccountList()
    step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
    id = None
    if getStoreWalletMsg["depositBalanceAmount"] != 10:
        remitMoney = 10 - getStoreWalletMsg["depositBalanceAmount"] # 输入金额
    else:
        remitMoney = 5
    step_mgmt_inventory_disManualInputRemit_add() 
    step_mgmt_inventory_disManualInputRemit_pageList()       
    step_mgmt_inventory_disManualInputRemit_verify()


@pytest.fixture(scope="function")
def inventory_add_1000():
    "使保证金>=1000,以便保证金支付"
    
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    id = None
    access_token = os.environ["access_token"]
                
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心信息"
        
        nonlocal getStoreByCode
        params = deepcopy(params03)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            getStoreByCode = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = deepcopy(params01)
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            getAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = deepcopy(params04)
        params["storeCode"] = getStoreByCode["store"]["code"]               
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            getBankAccountList = r.json()["data"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        "1:3押货余额及85折保证金余额查询"
        
        nonlocal getStoreWalletMsg
        params = deepcopy(params02)
        params["storeCode"] = getStoreByCode["store"]["code"]                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            getStoreWalletMsg = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_disManualInputRemit_add(): 
        "85折手工录入流水"
                
        data = deepcopy(data03)
        data["storeCode"] = getStoreByCode["store"]["code"]
        data["storeName"] = getStoreByCode["store"]["name"]
        data["companyCode"] = getStoreByCode["store"]["companyCode"]
        data["companyName"] = getAccountList[0]["accountName"]
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["changeReason"] = "其他"
        if remitMoney >= 0: # 服务中心付款
            data["payAccount"] = getBankAccountList[0]["account"]
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"]
            data["receiptBankName"] = getAccountList[0]["bankType"]
            data["remitMoney"] = remitMoney # >0
        elif remitMoney < 0: # 分公司付款
            data["payAccount"] = getAccountList[0]["account"]
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"]
            data["receiptBankName"] = getBankAccountList[0]["branch"]
            data["remitMoney"] = remitMoney # <0
        data["sourceType"] = 3 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
        data["inputRemark"] = f"录入其他款 {remitMoney}元"              
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_disManualInputRemit_pageList():
        "85折手工录入流水分页搜索列表,获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["storeCode"] = getStoreByCode["store"]["code"] 
        data["verifyStatus"] = 0 # 待审核列表             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            id = r.json()["data"]["list"][0]["id"]
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_disManualInputRemit_verify():
        "85折手工录入流水单个审核"
        
        params = deepcopy(params05)
        params["id"] = id
        params["verifyRemark"] = f"同意录入其它款 {remitMoney}元" # 审核备注
        params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
        
    step_mgmt_store_getStoreByCode()
    step_mgmt_sys_getAccountList()
    step_mgmt_store_getBankAccountList()
    step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
    id = None
    if getStoreWalletMsg["depositBalanceAmount"] < 1000:
        remitMoney = 1000 - getStoreWalletMsg["depositBalanceAmount"] # 输入金额
    else:
        remitMoney = 5
    step_mgmt_inventory_disManualInputRemit_add() 
    step_mgmt_inventory_disManualInputRemit_pageList()       
    step_mgmt_inventory_disManualInputRemit_verify()


# 85折押货 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
# 押货，押货修改，欠货不发

@pytest.fixture(scope="function")
def order_mortgage(inventory_add_1000):
    "完美运营后台下押货单,不发货"
    
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_audit import data as data05, _mgmt_inventory_dis_mortgage_order_audit
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import params as params06, _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import _mgmt_inventory_dis_mortgage_order_mortgage
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import params as params07, _mgmt_inventory_dis_mortgage_order_searchProductPage
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detailForModify_id import _mgmt_inventory_dis_mortgage_order_detailForModify_id
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_fetchFreightTemplate import _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate # 获取最新的运费计算模板
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_getMortgageAmount import _mgmt_inventory_dis_mortgage_order_getMortgageAmount # 查询店铺押货余额与限额
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling import _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling # 获取启用中的拼箱费上限
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo   
    
    orderId = None # 押货单id
    searchProductPage = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    orderSn = None # 押货单号
    payAmount = None # 押货金额
    access_token = os.environ["access_token"]
    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        "关键字搜索可押货商品"
        
        nonlocal searchProductPage
        params = deepcopy(params07)
        params["storeCode"] = store_85
        params["keyword"] = productCode              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break                
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        "获取最新的运费计算模板"
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        "获取最新的运费计算模板"
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        "获取启用中的拼箱费上限"
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : store_85,  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]
                
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": store_85, 
            "isDelivery": 1, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [{ # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": 2 # 押货商品数量
            }],
            "transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            orderId = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        "查询押货单是否超出库存限额"
        
        nonlocal checkIsAuditAmountOverLimit
        params = deepcopy(params06)
        params["orderId"] = orderId               
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_dis_mortgage_order_audit():
        "审核通过押货单"
        
        data = deepcopy(data05)
        data["orderId"] = orderId 
        data["auditRemarks"] = "同意押货单申请"
        data["auditResult"] = 1 # 审批结果 0不通过 1通过
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        "押货单详情，获取押货单编号"
        
        nonlocal orderSn, payAmount
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderSn = r.json()["data"]["orderSn"]
            payAmount= r.json()["data"]["payAmount"]

    # def step_esb_third_mortgage_syncDeliveryInfo():
    #     "押货单发货"
        
    #     data = {
    #         "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
    #         "mortgageItemReqDtoList": [
    #             {
    #                 "itemCode": productCode, # 商品编号
    #                 "num": 2, # 数量
    #                 "skuCode": ""
    #             }
    #         ],
    #         "mortgageOrderNo": orderSn, # 押货单号
    #         "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
    #         "status": 2,
    #         "type": 5 # 1:3是2,85折是5
    #     }
    #     with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
    #         assert r.status_code == 200            
    #         assert r.json()["resultMsg"] == "success"
            
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    # step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, payAmount, orderId


@pytest.fixture(scope="function")
def order_mortgage_isDelivery(inventory_add_1000):
    "完美运营后台下仅调账不发货押货单,不发货"
    
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_audit import data as data05, _mgmt_inventory_dis_mortgage_order_audit
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import params as params06, _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import _mgmt_inventory_dis_mortgage_order_mortgage
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import params as params07, _mgmt_inventory_dis_mortgage_order_searchProductPage
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detailForModify_id import _mgmt_inventory_dis_mortgage_order_detailForModify_id
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_fetchFreightTemplate import _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate # 获取最新的运费计算模板
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_getMortgageAmount import _mgmt_inventory_dis_mortgage_order_getMortgageAmount # 查询店铺押货余额与限额
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling import _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling # 获取启用中的拼箱费上限
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo   
    
    orderId = None # 押货单id
    searchProductPage = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    orderSn = None # 押货单号
    payAmount = None # 押货金额
    access_token = os.environ["access_token"]
    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        "关键字搜索可押货商品"
        
        nonlocal searchProductPage
        params = deepcopy(params07)
        params["storeCode"] = store_85
        params["keyword"] = productCode              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break                
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        "获取最新的运费计算模板"
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        "获取最新的运费计算模板"
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        "获取启用中的拼箱费上限"
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : store_85,  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]
                
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": store_85, 
            "isDelivery": 0, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [{ # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": 2 # 押货商品数量
            }],
            "transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            orderId = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        "查询押货单是否超出库存限额"
        
        nonlocal checkIsAuditAmountOverLimit
        params = deepcopy(params06)
        params["orderId"] = orderId               
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_dis_mortgage_order_audit():
        "审核通过押货单"
        
        data = deepcopy(data05)
        data["orderId"] = orderId 
        data["auditRemarks"] = "同意押货单申请"
        data["auditResult"] = 1 # 审批结果 0不通过 1通过
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        "押货单详情，获取押货单编号"
        
        nonlocal orderSn, payAmount
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderSn = r.json()["data"]["orderSn"]
            payAmount= r.json()["data"]["payAmount"]

    # def step_esb_third_mortgage_syncDeliveryInfo():
    #     "押货单发货"
        
    #     data = {
    #         "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
    #         "mortgageItemReqDtoList": [
    #             {
    #                 "itemCode": productCode, # 商品编号
    #                 "num": 2, # 数量
    #                 "skuCode": ""
    #             }
    #         ],
    #         "mortgageOrderNo": orderSn, # 押货单号
    #         "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
    #         "status": 2,
    #         "type": 5 # 1:3是2,85折是5
    #     }
    #     with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
    #         assert r.status_code == 200            
    #         assert r.json()["resultMsg"] == "success"
            
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    # step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, payAmount, orderId


@pytest.fixture(scope="function")
def order_modify(order_mortgage):
    "完美运营后台修改押货单,不发货"
    
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import params as params07, _mgmt_inventory_dis_mortgage_order_searchProductPage
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_modify import data as data06, _mgmt_inventory_dis_mortgage_order_modify
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo
    

    searchProductPage = None, # 商品信息
    orderSn, payAmount, orderId = order_mortgage # 押货单号, 押货金额
    access_token = os.environ["access_token"]
    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        "关键字搜索可押货商品"
        
        nonlocal searchProductPage
        params = deepcopy(params07)
        params["storeCode"] = store_85
        params["keyword"] = productCode              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break 
            assert r.status_code == 200            
            assert r.json()["code"] == 200
                
    def step_mgmt_inventory_dis_mortgage_order_modify():
        "押货单修改"
        
        data = deepcopy(data06)
        data["orderSn"] = orderSn # 押货单号
        data["productList"][0]["mortgageNum"] = 1 # 商品数量(减一半)
        data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"] # 商品押货价
        data["productList"][0]["productCode"] = searchProductPage["productCode"] # 商品编码
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    # def step_esb_third_mortgage_syncDeliveryInfo():
    #     "押货单发货"
        
    #     data = {
    #         "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
    #         "mortgageItemReqDtoList": [
    #             {
    #                 "itemCode": productCode, # 商品编号
    #                 "num": 1, # 数量
    #                 "skuCode": ""
    #             }
    #         ],
    #         "mortgageOrderNo": orderSn, # 押货单号
    #         "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
    #         "status": 2,
    #         "type": 5 # 1:3是2,85折是5
    #     }
    #     with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
    #         assert r.status_code == 200            
    #         assert r.json()["resultMsg"] == "success"
            
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_order_modify()
    # step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, payAmount/2, orderId


@pytest.fixture(scope="function")
def order_modify_2(order_mortgage):
    "完美运营后台批量取消押货单"

    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_batchCancel import _mgmt_inventory_dis_mortgage_order_batchCancel # 押货单批量取消
    
    orderSn, payAmount, orderId = order_mortgage # 押货单号, 押货金额
    access_token = os.environ["access_token"]
                
    def step_mgmt_inventory_dis_mortgage_order_batchCancel():
        "押货单修改"
        
        data = {
            "orderSn": orderSn, # 押货单号
        }
        with _mgmt_inventory_dis_mortgage_order_batchCancel(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] == None
            assert r.json()["message"] == "操作成功"
               
    step_mgmt_inventory_dis_mortgage_order_batchCancel()
    
    return orderSn, payAmount, orderId


@pytest.fixture(scope="function")
def order_stopDeliver(order_modify):
    "完美运营后台欠货不发"
    
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_stopDeliver import params as params08, _mgmt_inventory_dis_mortgage_order_stopDeliver
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detailForModify_id import _mgmt_inventory_dis_mortgage_order_detailForModify_id
    
    returnOrderSn = None # 退押货单号
    orderSn, payAmount, orderId = order_modify # 押货单号, 押货金额,押货单id
    access_token = os.environ["access_token"]
    
    def step_mgmt_inventory_dis_mortgage_order_stopDeliver():
        "押货单欠货不发"
        
        params = deepcopy(params08)
        params["orderSn"] = orderSn # 押货单号
        with _mgmt_inventory_dis_mortgage_order_stopDeliver(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_02_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        "押货单详情，获取退押货单号"
        
        nonlocal returnOrderSn
        params = {"id": orderId}
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            returnOrderSn = r.json()["data"]["returnOrderSn"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    step_mgmt_inventory_dis_mortgage_order_stopDeliver()
    step_02_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    
    return orderSn, returnOrderSn, payAmount


@pytest.fixture(scope="function")
def mortgageOrder_85_1(login_store_85, inventory_add_1000):
    "店铺运营后台下押货单: 保证金支付流水检查"
    
    from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params as params09, _appStore_store_dis_mortgageOrder_searchProductPage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data as data07, _appStore_store_dis_mortgageOrder_pushProductsToCart
    from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data08, _appStore_store_dis_mortgageOrder_mortgage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data09, _appStore_store_dis_mortgageOrder_prePayCheck
    from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params10, _appStore_store_dis_mortgageOrder_detail_id
    from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
    from api.mall_store_application._appStore_store_deposit_msg import params as params11, _appStore_store_deposit_msg
    
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo
    
    searchProductPage = None # 商品信息
    id = None # 押货单id
    payAmount = None # 押货单金额
    mortgageAmount = None # 押货价合计
    freightCost = None # 押货单运费
    pieceBoxCost = None # 押货拼箱费
    balance = None # 保证金余额
    orderSn = None # 押货单号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")        
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage
        params = deepcopy(params09) 
        params["keyword"] = productCode
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break  
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("推送购物车数据")   
    def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
        
        data = deepcopy(data07) 
        data[0]["mortgageNum"] = 2
        data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data[0]["productCode"] = searchProductPage["productCode"]
        with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货下单, 获取押货单Id")    
    def step_appStore_store_dis_mortgageOrder_mortgage():
        
        nonlocal id
        data = deepcopy(data08)
        data["productList"][0]["mortgageNum"] = 2
        data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"] # 85折押货价
        data["productList"][0]["productCode"] = searchProductPage["productCode"]
        data["storeCode"]= store_85
        data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
        with _appStore_store_dis_mortgageOrder_mortgage(data, store_token) as r:
            id = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情, 获取押货单金额")
    def step_01_appStore_store_dis_mortgageOrder_detail_id():
        
        nonlocal payAmount, mortgageAmount, freightCost, pieceBoxCost
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            payAmount = r.json()["data"]["payAmount"]
            mortgageAmount = r.json()["data"]["mortgageAmount"]
            freightCost = r.json()["data"]["freightCost"]
            pieceBoxCost = r.json()["data"]["pieceBoxCost"]

    @allure.step("获取服务中心可用押货保证金余额")            
    def step_appStore_store_deposit_msg():
        
        nonlocal balance
        params = deepcopy(params11)
        params["storeCode"] = store_85
        with _appStore_store_deposit_msg(params, store_token) as r:
            balance = r.json()["data"]["balance"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单支付前的金额校验")                
    def step_appStore_store_dis_mortgageOrder_prePayCheck():
        
        data = deepcopy(data09)
        data["orderId"] = id
        data["oweDepositAmount"] = 0
        data["payAmount"] = payAmount
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单支付")            
    def step_appStore_api_wallet_pay():
        
        data = {
            "accountName": "", # 户名(仅钱包支付不用传)
            "bankAccount": "", # 代扣账户(仅钱包支付不用传)
            "bankName": "", # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str({"balance":balance,"payAmount":payAmount,"payWays":[{"name":"押货保证金支付","payAmount":payAmount,"data":None}]}), # 扩展参数
            "payAmount": payAmount,
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 1, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
            "pxAmount": pieceBoxCost, # 拼箱费
            "storeCode": store_85, # 店铺编号
            "uniqueFlagNo": id, # 订单唯一标识
            "userId": login_store_85["data"]["userId"], # 用户ID
            "yfAmount": freightCost # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2

    @allure.step("押货单详情, 获取押货单号")
    def step_02_appStore_store_dis_mortgageOrder_detail_id():
        
        nonlocal orderSn
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            orderSn = r.json()["data"]["orderSn"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单发货")
    def step_esb_third_mortgage_syncDeliveryInfo():

        data = {
            "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
            "mortgageItemReqDtoList": [
                {
                    "itemCode": productCode, # 商品编号
                    "num": 2, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": orderSn, # 押货单号
            "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
   
    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_01_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_deposit_msg()
    step_appStore_store_dis_mortgageOrder_prePayCheck()
    step_appStore_api_wallet_pay()
    step_02_appStore_store_dis_mortgageOrder_detail_id()
    step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, payAmount


@pytest.fixture(scope="function")
def mortgageOrder_85_2(login_store_85):
    "店铺运营后台下押货单: 工行支付流水检查"
    
    from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params as params09, _appStore_store_dis_mortgageOrder_searchProductPage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data as data07, _appStore_store_dis_mortgageOrder_pushProductsToCart
    from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data08, _appStore_store_dis_mortgageOrder_mortgage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data09, _appStore_store_dis_mortgageOrder_prePayCheck
    from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params10, _appStore_store_dis_mortgageOrder_detail_id
    from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
    from api.mall_store_application._appStore_store_deposit_msg import params as params11, _appStore_store_deposit_msg
    from api.mall_store_application._appStore_store_getSignBankAccountList import params as params12, _appStore_store_getSignBankAccountList
    
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo
    
    searchProductPage = None # 商品信息
    id = None # 押货单id
    payAmount = None # 押货单金额
    balance = None # 保证金余额
    freightCost = None # 押货单运费
    pieceBoxCost = None # 押货拼箱费
    orderSn = None # 押货单号
    getSignBankAccountList = None # 签约银行信息
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]
            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        "关键字搜索可押货商品分页,获取商品信息"
        
        nonlocal searchProductPage
        params = deepcopy(params09) 
        params["keyword"] = productCode
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break  
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
        "推送购物车数据"
        
        data = deepcopy(data07) 
        data[0]["mortgageNum"] = 2
        data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data[0]["productCode"] = searchProductPage["productCode"]
        with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_appStore_store_dis_mortgageOrder_mortgage():
        "押货下单, 获取押货单Id"
        
        nonlocal id
        data = deepcopy(data08)
        data["productList"][0]["mortgageNum"] = 2
        data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data["productList"][0]["productCode"] = searchProductPage["productCode"]
        data["storeCode"]= store_85
        data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
        with _appStore_store_dis_mortgageOrder_mortgage(data, store_token) as r:
            id = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_01_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单金额"
        
        nonlocal payAmount, freightCost, pieceBoxCost
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            payAmount = r.json()["data"]["payAmount"]
            freightCost = r.json()["data"]["freightCost"]
            pieceBoxCost = r.json()["data"]["pieceBoxCost"]

    def step_appStore_store_deposit_msg():
        "获取服务中心可用押货保证金余额"
        
        nonlocal balance
        params = deepcopy(params11)
        params["storeCode"] = store_85
        with _appStore_store_deposit_msg(params, store_token) as r:
            balance = r.json()["data"]["balance"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
                
    def step_appStore_store_dis_mortgageOrder_prePayCheck():
        "押货单支付前的金额校验"
        
        data = deepcopy(data09)
        data["orderId"] = id
        data["oweDepositAmount"] = 0
        data["payAmount"] = payAmount
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_getSignBankAccountList():
        "获取签约银行列表"
        
        nonlocal getSignBankAccountList
        params = deepcopy(params12)   
        params["isSigned"] = 1 # 是否已签约，1/是，2/否             
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            getSignBankAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            
    def step_appStore_api_wallet_pay():
        "押货单支付"
        
        data = {
            "accountName": getSignBankAccountList[0]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance":balance,
                    "payAmount":payAmount,
                    "payWays":[
                        {
                            "name":getSignBankAccountList[0]["accountBank"],
                            "payAmount":payAmount,
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
            "payAmount": payAmount,
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 2, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
            "pxAmount": pieceBoxCost, # 拼箱费
            "storeCode": store_85, # 店铺编号
            "uniqueFlagNo": id, # 订单唯一标识
            "userId": login_store_85["data"]["userId"], # 用户ID
            "yfAmount": freightCost # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2

    def step_02_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单号"
        
        nonlocal orderSn
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            orderSn = r.json()["data"]["orderSn"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_esb_third_mortgage_syncDeliveryInfo():
        "押货单发货"
        
        data = {
            "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
            "mortgageItemReqDtoList": [
                {
                    "itemCode": productCode, # 商品编号
                    "num": 2, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": orderSn, # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
    
    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_01_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_deposit_msg()
    step_appStore_store_dis_mortgageOrder_prePayCheck()
    step_appStore_store_getSignBankAccountList()
    step_appStore_api_wallet_pay()
    step_02_appStore_store_dis_mortgageOrder_detail_id()
    step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, payAmount, getSignBankAccountList


@pytest.fixture(scope="function")
def mortgageOrder_85_3(login_store_85):
    "店铺运营后台下押货单: 建行支付流水检查"
    
    from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params as params09, _appStore_store_dis_mortgageOrder_searchProductPage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data as data07, _appStore_store_dis_mortgageOrder_pushProductsToCart
    from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data08, _appStore_store_dis_mortgageOrder_mortgage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data09, _appStore_store_dis_mortgageOrder_prePayCheck
    from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params10, _appStore_store_dis_mortgageOrder_detail_id
    from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
    from api.mall_store_application._appStore_store_deposit_msg import params as params11, _appStore_store_deposit_msg
    from api.mall_store_application._appStore_store_getSignBankAccountList import params as params12, _appStore_store_getSignBankAccountList
    
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo
    
    searchProductPage = None # 商品信息
    id = None # 押货单id
    payAmount = None # 押货单金额
    freightCost = None # 押货单运费
    pieceBoxCost = None # 押货拼箱费
    balance = None # 保证金余额
    orderSn = None # 押货单号
    getSignBankAccountList = None # 签约银行信息
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]
            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        "关键字搜索可押货商品分页,获取商品信息"
        
        nonlocal searchProductPage
        params = deepcopy(params09) 
        params["keyword"] = productCode
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break  
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
        "推送购物车数据"
        
        data = deepcopy(data07) 
        data[0]["mortgageNum"] = 2
        data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data[0]["productCode"] = searchProductPage["productCode"]
        with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_appStore_store_dis_mortgageOrder_mortgage():
        "押货下单, 获取押货单Id"
        
        nonlocal id
        data = deepcopy(data08)
        data["productList"][0]["mortgageNum"] = 2
        data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data["productList"][0]["productCode"] = searchProductPage["productCode"]
        data["storeCode"]= store_85
        data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
        with _appStore_store_dis_mortgageOrder_mortgage(data, store_token) as r:
            id = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_01_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单金额"
        
        nonlocal payAmount, freightCost, pieceBoxCost
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            payAmount = r.json()["data"]["payAmount"]
            freightCost = r.json()["data"]["freightCost"]
            pieceBoxCost = r.json()["data"]["pieceBoxCost"]

    def step_appStore_store_deposit_msg():
        "获取服务中心可用押货保证金余额"
        
        nonlocal balance
        params = deepcopy(params11)
        params["storeCode"] = store_85
        with _appStore_store_deposit_msg(params, store_token) as r:
            balance = r.json()["data"]["balance"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
                
    def step_appStore_store_dis_mortgageOrder_prePayCheck():
        "押货单支付前的金额校验"
        
        data = deepcopy(data09)
        data["orderId"] = id
        data["oweDepositAmount"] = 0
        data["payAmount"] = payAmount
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_getSignBankAccountList():
        "获取签约银行列表"
        
        nonlocal getSignBankAccountList
        params = deepcopy(params12)   
        params["isSigned"] = 1 # 是否已签约，1/是，2/否             
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            getSignBankAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            
    def step_appStore_api_wallet_pay():
        "押货单支付"
        
        data = {
                "accountName": getSignBankAccountList[1]["accountName"], # 户名(仅钱包支付不用传)
                "bankAccount": getSignBankAccountList[1]["account"], # 代扣账户(仅钱包支付不用传)
                "bankName": getSignBankAccountList[1]["accountBank"], # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str(
                    {
                        "balance":balance,
                        "payAmount":payAmount,
                        "payWays":[
                            {
                                "name":getSignBankAccountList[1]["accountBank"],
                                "payAmount":payAmount,
                                "data":{
                                    "accountName":getSignBankAccountList[1]["accountName"],
                                    "account":getSignBankAccountList[1]["account"],
                                    "accountBank":getSignBankAccountList[1]["accountBank"],
                                    "accountType":getSignBankAccountList[1]["accountType"],
                                    "isSigned":getSignBankAccountList[1]["isSigned"]
                                }
                            }
                        ]
                    }
                ), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 3, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "pxAmount": pieceBoxCost, # 拼箱费
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store_85["data"]["userId"], # 用户ID
                "yfAmount": freightCost # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2

    def step_02_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单号"
        
        nonlocal orderSn
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            orderSn = r.json()["data"]["orderSn"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_esb_third_mortgage_syncDeliveryInfo():
        "押货单发货"
        
        data = {
            "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
            "mortgageItemReqDtoList": [
                {
                    "itemCode": productCode, # 商品编号
                    "num": 2, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": orderSn, # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
    
    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_01_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_deposit_msg()
    step_appStore_store_dis_mortgageOrder_prePayCheck()
    step_appStore_store_getSignBankAccountList()
    step_appStore_api_wallet_pay()
    step_02_appStore_store_dis_mortgageOrder_detail_id()
    step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, payAmount, getSignBankAccountList


@pytest.fixture(scope="function")
def mortgageOrder_85_4(login_store_85, inventory_add):
    "店铺运营后台下押货单: 工行+保证金支付流水检查"
    
    from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params as params09, _appStore_store_dis_mortgageOrder_searchProductPage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data as data07, _appStore_store_dis_mortgageOrder_pushProductsToCart
    from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data08, _appStore_store_dis_mortgageOrder_mortgage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data09, _appStore_store_dis_mortgageOrder_prePayCheck
    from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params10, _appStore_store_dis_mortgageOrder_detail_id
    from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
    from api.mall_store_application._appStore_store_deposit_msg import params as params11, _appStore_store_deposit_msg
    from api.mall_store_application._appStore_store_getSignBankAccountList import params as params12, _appStore_store_getSignBankAccountList
    
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo
    
    searchProductPage = None # 商品信息
    id = None # 押货单id
    payAmount = None # 押货单金额
    freightCost = None # 押货单运费
    pieceBoxCost = None # 押货拼箱费
    balance = None # 保证金余额
    orderSn = None # 押货单号
    getSignBankAccountList = None # 签约银行信息
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]
            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        "关键字搜索可押货商品分页,获取商品信息"
        
        nonlocal searchProductPage
        params = deepcopy(params09) 
        params["keyword"] = productCode
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break  
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
        "推送购物车数据"
        
        data = deepcopy(data07) 
        data[0]["mortgageNum"] = 2
        data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data[0]["productCode"] = searchProductPage["productCode"]
        with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_appStore_store_dis_mortgageOrder_mortgage():
        "押货下单, 获取押货单Id"
        
        nonlocal id
        data = deepcopy(data08)
        data["productList"][0]["mortgageNum"] = 2
        data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data["productList"][0]["productCode"] = searchProductPage["productCode"]
        data["storeCode"]= store_85
        data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
        with _appStore_store_dis_mortgageOrder_mortgage(data, store_token) as r:
            id = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_01_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单金额"
        
        nonlocal payAmount, freightCost, pieceBoxCost
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            payAmount = r.json()["data"]["payAmount"]
            freightCost = r.json()["data"]["freightCost"]
            pieceBoxCost = r.json()["data"]["pieceBoxCost"]

    def step_appStore_store_deposit_msg():
        "获取服务中心可用押货保证金余额"
        
        nonlocal balance
        params = deepcopy(params11)
        params["storeCode"] = store_85
        with _appStore_store_deposit_msg(params, store_token) as r:
            balance = r.json()["data"]["balance"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
                
    def step_appStore_store_dis_mortgageOrder_prePayCheck():
        "押货单支付前的金额校验"
        
        data = deepcopy(data09)
        data["orderId"] = id
        data["oweDepositAmount"] = 0
        data["payAmount"] = payAmount
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_getSignBankAccountList():
        "获取签约银行列表"
        
        nonlocal getSignBankAccountList
        params = deepcopy(params12)   
        params["isSigned"] = 1 # 是否已签约，1/是，2/否             
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            getSignBankAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            
    def step_appStore_api_wallet_pay():
        "押货单支付"
        
        data = {
            "accountName": getSignBankAccountList[0]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance":balance,
                    "payAmount":payAmount,
                    "payWays":[
                        {
                            "name":"押货保证金支付",
                            "payAmount":balance,
                            "data":None
                        },
                        {
                            "name":getSignBankAccountList[0]["accountBank"],
                            "payAmount":payAmount-balance,
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
            "payAmount": payAmount,
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 4, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
            "pxAmount": pieceBoxCost, # 拼箱费
            "storeCode": store_85, # 店铺编号
            "uniqueFlagNo": id, # 订单唯一标识
            "userId": login_store_85["data"]["userId"], # 用户ID
            "yfAmount": freightCost # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2

    def step_02_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单号"
        
        nonlocal orderSn
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            orderSn = r.json()["data"]["orderSn"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_esb_third_mortgage_syncDeliveryInfo():
        "押货单发货"
        
        data = {
            "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
            "mortgageItemReqDtoList": [
                {
                    "itemCode": productCode, # 商品编号
                    "num": 2, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": orderSn, # 押货单号
            "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"

    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_01_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_deposit_msg()
    step_appStore_store_dis_mortgageOrder_prePayCheck()
    step_appStore_store_getSignBankAccountList()
    step_appStore_api_wallet_pay()
    step_02_appStore_store_dis_mortgageOrder_detail_id()
    step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, balance, payAmount, getSignBankAccountList

 
@pytest.fixture(scope="function")
def mortgageOrder_85_5(login_store_85, inventory_add):
    "店铺运营后台下押货单: 建行+保证金支付流水检查"
    
    from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params as params09, _appStore_store_dis_mortgageOrder_searchProductPage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data as data07, _appStore_store_dis_mortgageOrder_pushProductsToCart
    from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data08, _appStore_store_dis_mortgageOrder_mortgage
    from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data09, _appStore_store_dis_mortgageOrder_prePayCheck
    from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params10, _appStore_store_dis_mortgageOrder_detail_id
    from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
    from api.mall_store_application._appStore_store_deposit_msg import params as params11, _appStore_store_deposit_msg
    from api.mall_store_application._appStore_store_getSignBankAccountList import params as params12, _appStore_store_getSignBankAccountList
    
    from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo
    
    searchProductPage = None # 商品信息
    id = None # 押货单id
    payAmount = None # 押货单金额
    freightCost = None # 押货单运费
    pieceBoxCost = None # 押货拼箱费
    balance = None # 保证金余额
    orderSn = None # 押货单号
    getSignBankAccountList = None # 签约银行信息
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]
            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        "关键字搜索可押货商品分页,获取商品信息"
        
        nonlocal searchProductPage
        params = deepcopy(params09) 
        params["keyword"] = productCode
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            for d in r.json()["data"]["list"]:
                if d["productCode"] == productCode:
                    searchProductPage = d
                    break  
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
        "推送购物车数据"
        
        data = deepcopy(data07) 
        data[0]["mortgageNum"] = 2
        data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data[0]["productCode"] = searchProductPage["productCode"]
        with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_appStore_store_dis_mortgageOrder_mortgage():
        "押货下单, 获取押货单Id"
        
        nonlocal id
        data = deepcopy(data08)
        data["productList"][0]["mortgageNum"] = 2
        data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
        data["productList"][0]["productCode"] = searchProductPage["productCode"]
        data["storeCode"]= store_85
        data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
        with _appStore_store_dis_mortgageOrder_mortgage(data, store_token) as r:
            id = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_01_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单金额"
        
        nonlocal payAmount, freightCost, pieceBoxCost
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            payAmount = r.json()["data"]["payAmount"]
            freightCost = r.json()["data"]["freightCost"]
            pieceBoxCost = r.json()["data"]["pieceBoxCost"]

    def step_appStore_store_deposit_msg():
        "获取服务中心可用押货保证金余额"
        
        nonlocal balance
        params = deepcopy(params11)
        params["storeCode"] = store_85
        with _appStore_store_deposit_msg(params, store_token) as r:
            balance = r.json()["data"]["balance"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
                
    def step_appStore_store_dis_mortgageOrder_prePayCheck():
        "押货单支付前的金额校验"
        
        data = deepcopy(data09)
        data["orderId"] = id
        data["oweDepositAmount"] = 0
        data["payAmount"] = payAmount
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_appStore_store_getSignBankAccountList():
        "获取签约银行列表"
        
        nonlocal getSignBankAccountList
        params = deepcopy(params12)   
        params["isSigned"] = 1 # 是否已签约，1/是，2/否             
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            getSignBankAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            
    def step_appStore_api_wallet_pay():
        "押货单支付"
        
        data = {
            "accountName": getSignBankAccountList[1]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[1]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[1]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance":balance,
                    "payAmount":payAmount,
                    "payWays":[
                        {
                            "name":"押货保证金支付",
                            "payAmount":balance,
                            "data":None
                        },
                        {
                            "name":getSignBankAccountList[1]["accountBank"],
                            "payAmount":payAmount-balance,
                            "data":{
                                "accountName":getSignBankAccountList[1]["accountName"],
                                "account":getSignBankAccountList[1]["account"],
                                "accountBank":getSignBankAccountList[1]["accountBank"],
                                "accountType":getSignBankAccountList[1]["accountType"],
                                "isSigned":getSignBankAccountList[1]["isSigned"]
                            }
                        }
                    ]
                }
            ), # 扩展参数
            "payAmount": payAmount,
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 5, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
            "pxAmount": pieceBoxCost, # 拼箱费
            "storeCode": store_85, # 店铺编号
            "uniqueFlagNo": id, # 订单唯一标识
            "userId": login_store_85["data"]["userId"], # 用户ID
            "yfAmount": freightCost # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2

    def step_02_appStore_store_dis_mortgageOrder_detail_id():
        "押货单详情, 获取押货单号"
        
        nonlocal orderSn
        params = deepcopy(params10)
        params["id"] = id
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            orderSn = r.json()["data"]["orderSn"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    def step_esb_third_mortgage_syncDeliveryInfo():
        "押货单发货"
        
        data = {
            "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
            "mortgageItemReqDtoList": [
                {
                    "itemCode": productCode, # 商品编号
                    "num": 2, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": orderSn, # 押货单号
            "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"

    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_01_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_deposit_msg()
    step_appStore_store_dis_mortgageOrder_prePayCheck()
    step_appStore_store_getSignBankAccountList()
    step_appStore_api_wallet_pay()
    step_02_appStore_store_dis_mortgageOrder_detail_id()
    step_esb_third_mortgage_syncDeliveryInfo()
    
    return orderSn, balance, payAmount, getSignBankAccountList

# 85折押货退货

@pytest.fixture(scope="function")
def mortgageReturn_85_DTYH():
    "完美运营后台85折押货退货"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getReason import params as params01, _mgmt_inventory_common_getReason # 退换货原因
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import params as params02, _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchProduct import params as params03, _mgmt_inventory_dis_mortgage_returnOrder_searchProduct # 获取商品信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn import _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn # 新建押货退货单
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params as params04, _mgmt_inventory_dis_mortgage_returnOrder_listPage # 押货退货列表
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import params as params05, _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo # 展示审批保存信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_opinion import data as data01, _mgmt_inventory_dis_mortgage_returnOrder_opinion # 添加审批意见
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_audit import data as data02, _mgmt_inventory_dis_mortgage_returnOrder_audit # 审批
    from api.basic_services._storage_upload import files as files01, _storage_upload # 退回时上传附件
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_process import data as data03, _mgmt_inventory_dis_mortgage_returnOrder_process # 退回处理
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_inspect import data as data04, _mgmt_inventory_dis_mortgage_returnOrder_inspect # 验货
    
    getReason = None # 退换货原因
    searchStore = None # 店铺信息
    searchProduct = None # 商品信息
    id = None # 押货退货单id
    listPage = None # 押货退货列表信息
    searchAuditInfo = None # 展示审批保存信息
    storage_upload = None # 退回时上传附件信息
    access_token = os.environ["access_token"]
    
    def step_mgmt_inventory_common_getReason():
        "获取各种退换货原因"
        
        nonlocal getReason
        params = deepcopy(params01)
        params["type:"] = 3 # 退货原因              
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]
    
    def step_mgmt_inventory_dis_mortgage_common_searchStore():
        "查询店铺信息"
        
        nonlocal searchStore
        params = deepcopy(params02)
        params["storeCode"] = store_85                   
        with _mgmt_inventory_dis_mortgage_common_searchStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchStore = r.json()["data"]
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct():
        "商品编码搜索退货商品信息"
        
        nonlocal searchProduct
        params = deepcopy(params03) 
        params["storeCode"] = store_85
        params["productCode"] = productCode           
        with _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchProduct = r.json()["data"]
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn():
        "新建85折押货退货单"
        
        nonlocal id
        data = {
            "productList": [{
                "productCode": searchProduct["productCode"], # 商品编号
                "productName": searchProduct["productName"], # 商品名称
                "packing": searchProduct["packing"],
                "unit": searchProduct["unit"],
                "pieceBoxNorm": None,
                "pieceBoxPrice": None,
                "mortgagePrice": searchProduct["mortgagePrice"], # 85折押货价
                "retailPrice": searchProduct["retailPrice"], # 零售价
                "inventoryNum": searchProduct["inventoryNum"], # 库存数量
                "returnNum": 2, # 退货数量
                "remark": ""
            }],
            "orderMark": 0,
            "reasonFirst": getReason[1]["returnReason"],
            "reasonFirstRemark": "",
            "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
            "reasonSecondRemark": "",
            "storeCode": searchStore["storeCode"]
        }               
        with _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            id = r.json()["data"]

    @stepreruns()
    def step_mgmt_inventory_dis_mortgage_returnOrder_listPage():
        "押货退货分页列表:获取id"
        
        nonlocal listPage
        params = deepcopy(params04) 
        params["storeCode"] = store_85               
        with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, access_token) as r:
            for d in r.json()["data"]["list"]:
                if d["id"] == id:
                    listPage = d
                    break

    def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
        "押货退货单详情"
        
        params = deepcopy(params05) 
        params["id"] = id              
        with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["id"] == id
            assert r.json()["data"]["orderSn"] == listPage["orderSn"]

    def step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo():
        "展示审批保存信息"
        
        nonlocal searchAuditInfo       
        with _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchAuditInfo = r.json()["data"]["returnAddress"]

    def step_mgmt_inventory_dis_mortgage_returnOrder_opinion():
        "添加审批意见"
        
        data = deepcopy(data01) 
        data["orderId"] = id
        data["content"] = f"同意{listPage['orderSn']}押货退货单申请"        
        with _mgmt_inventory_dis_mortgage_returnOrder_opinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_returnOrder_audit():
        "审批"
        
        data = deepcopy(data02)
        data["id"] = id
        data["auditRemark"] = f"同意审批通过押货退货单{listPage['orderSn']}"
        data["auditResult"] = "1"
        data["reasonFirst"] = getReason[1]["returnReason"]
        data["reasonSecond"] = getReason[1]["reasonList"][1]["returnReason"]
        if searchAuditInfo:
            data["returnInfo"] = searchAuditInfo
            data["returnAddress"] = searchAuditInfo
        else:
            data["returnInfo"] = "我是退回地址"
            data["returnAddress"] = "我是退回地址"
        with _mgmt_inventory_dis_mortgage_returnOrder_audit(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_storage_upload():
        "上传文件：退回时上传附件"
        
        nonlocal storage_upload
        files = deepcopy(files01) 
        files["clientKey"] = "mall-center-inventory" 
        files["file"] = "data/顺丰快递单.jpg"                
        with _storage_upload(files, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["datas"]["msg"] == "文件上传成功"
            storage_upload = r.json()["datas"]

    def step_mgmt_inventory_dis_mortgage_returnOrder_process():
        "退回处理"
        
        data = deepcopy(data03)
        data["orderId"] = id
        data["returnType"] = 2 # 退回类型 1自带 2邮寄
        data["expressProofUrl"] = storage_upload["fileUrlKey"]
        data["expressProofName"] = storage_upload["relativePath"][24:]
        with _mgmt_inventory_dis_mortgage_returnOrder_process(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_returnOrder_inspect():
        "验货"
        
        data = deepcopy(data04)
        data["orderId"] = id
        data["inspectResult"] = "1" # 验货意见 0不通过 1通过
        data["inspectRemark"] = f"押货退货单{listPage['orderSn']}验货没问题"
        data["orderReturnRealAmount"] = str(listPage['returnAmount'])
        data["productList"] = [{"returnRealNum": 2, "productCode": searchProduct["productCode"]}]
        data["returnRealAmount"] = str(listPage['returnAmount'])
        with _mgmt_inventory_dis_mortgage_returnOrder_inspect(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_inventory_common_getReason()
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct()
    step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn()
    step_mgmt_inventory_dis_mortgage_returnOrder_listPage()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo()
    step_mgmt_inventory_dis_mortgage_returnOrder_opinion()
    step_mgmt_inventory_dis_mortgage_returnOrder_audit()
    step_storage_upload()
    step_mgmt_inventory_dis_mortgage_returnOrder_process()
    step_mgmt_inventory_dis_mortgage_returnOrder_inspect()
    
    return listPage["orderSn"]


@pytest.fixture(scope="function")
def mortgageReturn_85_TYH(): 
    "店铺系统85折押货退货"
    
    from api.mall_store_application._appStore_common_getReason import params as params01, _appStore_common_getReason # 获取各种退换货原因
    from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_searchPositiveProducts import params as params02, _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts # 获取服务中心正库存的商品信息
    from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_mortgageReturn import _appStore_store_dis_mortgage_returnOrder_mortgageReturn # 押货退货下单
    from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_listPage import params as params03, _appStore_store_dis_mortgage_returnOrder_listPage # 押货退货分页列表
    
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import params as params05, _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo # 展示审批保存信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_opinion import data as data01, _mgmt_inventory_dis_mortgage_returnOrder_opinion # 添加审批意见
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_audit import data as data02, _mgmt_inventory_dis_mortgage_returnOrder_audit # 审批
    
    from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_process import data as data03, _appStore_store_dis_mortgage_returnOrder_process # 退回处理
    
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_inspect import data as data04, _mgmt_inventory_dis_mortgage_returnOrder_inspect # 验货
    
    returnNum = 2 # 退货数量
    getReason = None # 获取各种退换货原因
    searchPositiveProducts = None # 正库存商品编号
    mortgageReturn = None # 押货退货单id
    orderSn = None # 押货退货单号
    listPage = None # 押货单信息
    searchAuditInfo = None # 展示审批保存信息
    store_token_85 = os.environ["store_token_85"]
    access_token = os.environ["access_token"]
    
    def step_appStore_common_getReason():
        "获取各种退换货原因"
        
        nonlocal getReason
        params = deepcopy(params01)
        with _appStore_common_getReason(params, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]
        
    def step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts():
        "获取服务中心正库存的商品信息"
        
        nonlocal searchPositiveProducts
        params = deepcopy(params02)
        with _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts(params, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["productCode"] == productCode:
                    searchPositiveProducts = d["productCode"]
    
    def step_appStore_store_dis_mortgage_returnOrder_mortgageReturn():
        "押货退货下单"
               
        nonlocal mortgageReturn
        data = {
            "reasonFirst": getReason[1]["returnReason"], # 一级原因
            "reasonFirstRemark": "", # 一级原因备注
            "productList": [{
                "productCode": searchPositiveProducts, # 商品编码
                "productNum": returnNum,
                "productRemarks": "",
                "remark": "", # 商品备注
                "returnNum": returnNum # 商品退货数量
            }], 
            "storeCode": store_85 # 服务中心编码
        }
        with _appStore_store_dis_mortgage_returnOrder_mortgageReturn(data, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            mortgageReturn = r.json()["data"]
            
    def step_appStore_store_dis_mortgage_returnOrder_listPage():
        "押货退货分页列表:获取押货退货单号"
        
        nonlocal orderSn, listPage
        params = deepcopy(params03)
        with _appStore_store_dis_mortgage_returnOrder_listPage(params, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["id"] == mortgageReturn:
                    orderSn = d["orderSn"]
                    listPage = d
    
    @stepreruns()
    def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
        "押货退货单详情"
        
        params = deepcopy(params05) 
        params["id"] = mortgageReturn              
        with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["id"] == mortgageReturn
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo():
        "展示审批保存信息"
        
        nonlocal searchAuditInfo       
        with _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchAuditInfo = r.json()["data"]["returnAddress"]
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_opinion():
        "添加审批意见"
        
        data = deepcopy(data01) 
        data["orderId"] = mortgageReturn
        data["content"] = f"同意{orderSn}押货退货单申请"        
        with _mgmt_inventory_dis_mortgage_returnOrder_opinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_audit():
        "审批"
        
        data = deepcopy(data02)
        data["id"] = mortgageReturn
        data["auditRemark"] = f"同意审批通过押货退货单{orderSn}"
        data["auditResult"] = "1"
        data["reasonFirst"] = getReason[1]["returnReason"]
        data["reasonSecond"] = getReason[1]["reasonList"][1]["returnReason"]
        if searchAuditInfo:
            data["returnInfo"] = searchAuditInfo
            data["returnAddress"] = searchAuditInfo
        else:
            data["returnInfo"] = "我是退回地址"
            data["returnAddress"] = "我是退回地址"
        with _mgmt_inventory_dis_mortgage_returnOrder_audit(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    def step_appStore_store_dis_mortgage_returnOrder_process():
        "退回处理"
            
        data = deepcopy(data03)
        data["returnType"] = 1 # 退回类型 1自带 2邮寄
        data["orderId"] = mortgageReturn
        with _appStore_store_dis_mortgage_returnOrder_process(data, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_inspect():
        "验货"
        
        data = deepcopy(data04)
        data["orderId"] = mortgageReturn
        data["inspectResult"] = "1" # 验货意见 0不通过 1通过
        data["inspectRemark"] = f"押货退货单{orderSn}验货没问题"
        data["orderReturnRealAmount"] = str(listPage['returnAmount'])
        data["productList"] = [{"returnRealNum": 2, "productCode": searchPositiveProducts}]
        data["returnRealAmount"] = str(listPage['returnAmount'])
        with _mgmt_inventory_dis_mortgage_returnOrder_inspect(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200  
                         
    step_appStore_common_getReason()
    step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts()
    step_appStore_store_dis_mortgage_returnOrder_mortgageReturn()
    step_appStore_store_dis_mortgage_returnOrder_listPage()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo()
    step_mgmt_inventory_dis_mortgage_returnOrder_opinion()
    step_mgmt_inventory_dis_mortgage_returnOrder_audit()
    step_appStore_store_dis_mortgage_returnOrder_process()
    step_mgmt_inventory_dis_mortgage_returnOrder_inspect()
    
    return orderSn

# 85折组合拆分套装

@pytest.fixture(scope="function")
def inventory_combine(onSaleVersion):
    "完美运营后台组合套装"
    
    from api.mall_mgmt_application._mgmt_dis_inventory_combine import data as data01, _mgmt_dis_inventory_combine
    from api.mall_mgmt_application._mgmt_dis_inventory_combine_detail import data as data02, _mgmt_dis_inventory_combine_detail
    
    combineIds = None
    combine_detail = None # 组合押货单号，退货单号，押货金额，退货金额 
    access_token = os.environ["access_token"]

    def step_mgmt_dis_inventory_combine():
        "套装组合: 获取combineIds"
        
        nonlocal combineIds
        data = deepcopy(data01)
        data["productCode"] = productCode_zh
        data["storeCode"] = store_85
        data["combineNum"] = 2
        with _mgmt_dis_inventory_combine(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combineIds = r.json()["data"]["combineId"]
    
    def step_mgmt_dis_inventory_combine_detail():
        "分页查询套装组合明细"
        
        nonlocal combine_detail
        data = deepcopy(data02)
        data["combineIds"] = [str(combineIds)]
        with _mgmt_dis_inventory_combine_detail(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combine_detail = r.json()["data"]["list"]
    
    step_mgmt_dis_inventory_combine()
    step_mgmt_dis_inventory_combine_detail()
    
    return combine_detail


@pytest.fixture(scope="function")
def inventory_split(inventory_combine, offSaleVersion):
    "完美运营后台拆分套装"
    
    from api.mall_mgmt_application._mgmt_dis_inventory_split import data as data01, _mgmt_dis_inventory_split
    from api.mall_mgmt_application._mgmt_dis_inventory_split_record_page import data as data02, _mgmt_dis_inventory_split_record_page
    from api.mall_mgmt_application._mgmt_dis_inventory_split_detail import data as data03, _mgmt_dis_inventory_split_detail
        
    access_token = os.environ["access_token"]
    id = None
    split_detail = None
    
    def test_mgmt_dis_inventory_split():
        "套装拆分"
        
        data = deepcopy(data01)
        data["productCodes"] = [productCode_zh]
        with _mgmt_dis_inventory_split(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_dis_inventory_split_record_page():
        "查询套装拆分列表:获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["product"] = productCode_zh
        with _mgmt_dis_inventory_split_record_page(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
    
    def step_mgmt_dis_inventory_split_detail():
        "套装拆明细"
        
        nonlocal split_detail
        data = deepcopy(data03)
        data["id"] = id
        with _mgmt_dis_inventory_split_detail(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            split_detail = r.json()["data"]["list"]
    
    test_mgmt_dis_inventory_split()
    step_mgmt_dis_inventory_split_record_page()
    step_mgmt_dis_inventory_split_detail()
    
    return split_detail


@pytest.fixture(scope="function")
def inventory_combine_confirm(onSaleVersion):
    "店铺系统套装组合"
    from api.mall_store_application._appStore_dis_inventory_combine_confirm import data as data01, _appStore_dis_inventory_combine_confirm
    from api.mall_store_application._appStore_dis_inventory_combine_record_page import params as params01, _appStore_dis_inventory_combine_record_page
    from api.mall_store_application._appStore_dis_inventory_combine_detail import params as params02, _appStore_dis_inventory_combine_detail
    
    id = None
    combine_detail = None # 组合明细
    store_token = os.environ["store_token_85"]
    
    def step_appStore_dis_inventory_combine_confirm():
        "套装组合"
        
        data = deepcopy(data01)
        data["combineNum"] = 2
        data["productCode"] = productCode_zh
        with _appStore_dis_inventory_combine_confirm(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            
    def step_appStore_dis_inventory_combine_record_page():
        "套装组合记录列表:获取Id"
        
        nonlocal id
        params = deepcopy(params01)
        with _appStore_dis_inventory_combine_record_page(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
    
    def step_appStore_dis_inventory_combine_detail():
        "套装组合明细"
        
        nonlocal combine_detail
        params = deepcopy(params02)
        params["id"] = id
        with _appStore_dis_inventory_combine_detail(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            combine_detail = r.json()["data"]
    
    step_appStore_dis_inventory_combine_confirm()
    step_appStore_dis_inventory_combine_record_page()
    step_appStore_dis_inventory_combine_detail()
    
    return combine_detail

# 85折充值 2->工行签约代扣 3->建行签约代扣

@pytest.fixture(scope="function")
def appStore_invest_2(login_store_85):
    "店铺系统-工行充值"
    
    from api.mall_store_application._appStore_store_getSignBankAccountList import params as params01, _appStore_store_getSignBankAccountList
    from api.mall_store_application._appStore_invest import _appStore_invest
    
    getSignBankAccountList = None # 签约银行列表
    payAmount = 10 # 充值金额
    payOrderNo = None # 充值流水号
    store_token = os.environ["store_token_85"]    
    
    def step_appStore_store_getSignBankAccountList():
        "获取签约银行列表"
        
        nonlocal getSignBankAccountList
        params = deepcopy(params01)                 
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["accountBank"] == "工商银行":
                    getSignBankAccountList = d
    
    def step_appStore_invest():
        "充值"

        nonlocal payOrderNo
        data = {
            "accountName": getSignBankAccountList["accountName"], # 户名不能为空
            "bankAccount": getSignBankAccountList["account"], # 代扣账户不能为空
            "bankName": getSignBankAccountList["accountBank"], # 开户银行名称
            "businessType": 3, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "payAmount": payAmount, # 充值金额
            "payChannel": "WEB", # 充值渠道 WEB/APP
            "payType": 2, # 2->工行签约代扣 3->建行签约代扣
            "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
            "userId": login_store_85["data"]["userId"] # 用户ID
        }                
        with _appStore_invest(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            payOrderNo = r.json()["data"]["payOrderNo"]
    
    step_appStore_store_getSignBankAccountList()
    step_appStore_invest()
    
    return payAmount, payOrderNo, getSignBankAccountList


@pytest.fixture(scope="function")
def appStore_invest_3(login_store_85):
    "店铺系统-建行充值"
    
    from api.mall_store_application._appStore_store_getSignBankAccountList import params as params01, _appStore_store_getSignBankAccountList
    from api.mall_store_application._appStore_invest import _appStore_invest
    
    getSignBankAccountList = None # 签约银行列表
    payAmount = 10 # 充值金额
    payOrderNo = None # 充值流水号
    store_token = os.environ["store_token_85"]    
    
    def step_appStore_store_getSignBankAccountList():
        "获取签约银行列表"
        
        nonlocal getSignBankAccountList
        params = deepcopy(params01)                 
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["accountBank"] == "建设银行":
                    getSignBankAccountList = d
    
    def step_appStore_invest():
        "充值"

        nonlocal payOrderNo
        data = {
            "accountName": getSignBankAccountList["accountName"], # 户名不能为空
            "bankAccount": getSignBankAccountList["account"], # 代扣账户不能为空
            "bankName": getSignBankAccountList["accountBank"], # 开户银行名称
            "businessType": 3, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "payAmount": payAmount, # 充值金额
            "payChannel": "WEB", # 充值渠道 WEB/APP
            "payType": 3, # 2->工行签约代扣 3->建行签约代扣
            "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
            "userId": login_store_85["data"]["userId"] # 用户ID
        }                
        with _appStore_invest(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            payOrderNo = r.json()["data"]["payOrderNo"]
    
    step_appStore_store_getSignBankAccountList()
    step_appStore_invest()
    
    return payAmount, payOrderNo, getSignBankAccountList

# 85折手工录入流水 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移

@pytest.fixture(scope="function")
def disManualInputRemit_add_3():
    "手工录入其他款"   
    from api.mall_center_sys._mgmt_sys_getAccountList import params as params01, _mgmt_sys_getAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data as data03, _mgmt_inventory_disManualInputRemit_add
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify  
    
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    id = None
    access_token = os.environ["access_token"]
    remitMoneys = [2, -1]
                        
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心信息"
        
        nonlocal getStoreByCode
        params = deepcopy(params03)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            getStoreByCode = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = deepcopy(params01)
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            getAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = deepcopy(params04)
        params["storeCode"] = getStoreByCode["store"]["code"]               
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            getBankAccountList = r.json()["data"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        "1:3押货余额及85折保证金余额查询"
        
        nonlocal getStoreWalletMsg
        params = deepcopy(params02)
        params["storeCode"] = getStoreByCode["store"]["code"]                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            getStoreWalletMsg = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_disManualInputRemit_add(): 
        "85折手工录入流水"
                
        data = deepcopy(data03)
        data["storeCode"] = getStoreByCode["store"]["code"]
        data["storeName"] = getStoreByCode["store"]["name"]
        data["companyCode"] = getStoreByCode["store"]["companyCode"]
        data["companyName"] = getAccountList[0]["accountName"]
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["changeReason"] = "其他"
        if remitMoney > 0: # 服务中心付款
            data["payAccount"] = getBankAccountList[0]["account"]
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"]
            data["receiptBankName"] = getAccountList[0]["bankType"]
        elif remitMoney < 0: # 分公司付款
            data["payAccount"] = getAccountList[0]["account"]
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"]
            data["receiptBankName"] = getBankAccountList[0]["branch"]
        data["remitMoney"] = remitMoney
        data["sourceType"] = 3 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
        data["inputRemark"] = f"录入其他款 {remitMoney}元"              
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_disManualInputRemit_pageList():
        "85折手工录入流水分页搜索列表,获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["storeCode"] = getStoreByCode["store"]["code"] 
        data["verifyStatus"] = 0 # 待审核列表             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            id = r.json()["data"]["list"][0]["id"]
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_disManualInputRemit_verify():
        "85折手工录入流水单个审核"
        
        params = deepcopy(params05)
        params["id"] = id
        params["verifyRemark"] = f"同意录入其它款 {remitMoney}元" # 审核备注
        params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            
    step_mgmt_store_getStoreByCode()
    step_mgmt_sys_getAccountList()
    step_mgmt_store_getBankAccountList()
    step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
    for remitMoney in remitMoneys:
        step_mgmt_inventory_disManualInputRemit_add() 
        step_mgmt_inventory_disManualInputRemit_pageList()       
        step_mgmt_inventory_disManualInputRemit_verify()
    
    return remitMoneys


@pytest.fixture(scope="function")
def disManualInputRemit_add_7():
    "手工增加押货款"   
    from api.mall_center_sys._mgmt_sys_getAccountList import params as params01, _mgmt_sys_getAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data as data03, _mgmt_inventory_disManualInputRemit_add
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify  
    
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    id = None
    access_token = os.environ["access_token"]
    remitMoney = 4
                        
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心信息"
        
        nonlocal getStoreByCode
        params = deepcopy(params03)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            getStoreByCode = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = deepcopy(params01)
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            getAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = deepcopy(params04)
        params["storeCode"] = getStoreByCode["store"]["code"]               
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            getBankAccountList = r.json()["data"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        "1:3押货余额及85折保证金余额查询"
        
        nonlocal getStoreWalletMsg
        params = deepcopy(params02)
        params["storeCode"] = getStoreByCode["store"]["code"]                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            getStoreWalletMsg = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_disManualInputRemit_add(): 
        "85折手工录入流水"
                
        data = deepcopy(data03)
        data["storeCode"] = getStoreByCode["store"]["code"]
        data["storeName"] = getStoreByCode["store"]["name"]
        data["companyCode"] = getStoreByCode["store"]["companyCode"]
        data["companyName"] = getAccountList[0]["accountName"]
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["changeReason"] = "汇押货款"
        data["payAccount"] = getBankAccountList[0]["account"] # 服务中心付款
        data["payAccountBankName"] = getBankAccountList[0]["branch"]
        data["receiptAccount"] = getAccountList[0]["account"] # 分公司收款
        data["receiptBankName"] = getAccountList[0]["bankType"]
        data["remitMoney"] = remitMoney
        data["sourceType"] = 7 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
        data["inputRemark"] = f"录入手动增加押货款 {remitMoney}元"              
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_disManualInputRemit_pageList():
        "85折手工录入流水分页搜索列表,获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["storeCode"] = getStoreByCode["store"]["code"] 
        data["verifyStatus"] = 0 # 待审核列表             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            id = r.json()["data"]["list"][0]["id"]
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_disManualInputRemit_verify():
        "85折手工录入流水单个审核"
        
        params = deepcopy(params05)
        params["id"] = id
        params["verifyRemark"] = f"同意录入手动增加押货款 {remitMoney}元" # 审核备注
        params["verifyResult"] = 1 # 1->通过 2-> 拒绝                
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            
    step_mgmt_store_getStoreByCode()
    step_mgmt_sys_getAccountList()
    step_mgmt_store_getBankAccountList()
    step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
    step_mgmt_inventory_disManualInputRemit_add() 
    step_mgmt_inventory_disManualInputRemit_pageList()       
    step_mgmt_inventory_disManualInputRemit_verify()
    
    return remitMoney


@pytest.fixture(scope="function")
def disManualInputRemit_add_8():
    "手工退押货款"   
    from api.mall_center_sys._mgmt_sys_getAccountList import params as params01, _mgmt_sys_getAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data as data03, _mgmt_inventory_disManualInputRemit_add
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify  
    
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    id = None
    access_token = os.environ["access_token"]
    remitMoney = -2 # 金额
                        
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心信息"
        
        nonlocal getStoreByCode
        params = deepcopy(params03)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            getStoreByCode = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = deepcopy(params01)
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            getAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = deepcopy(params04)
        params["storeCode"] = getStoreByCode["store"]["code"]               
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            getBankAccountList = r.json()["data"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        "1:3押货余额及85折保证金余额查询"
        
        nonlocal getStoreWalletMsg
        params = deepcopy(params02)
        params["storeCode"] = getStoreByCode["store"]["code"]                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            getStoreWalletMsg = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_disManualInputRemit_add(): 
        "85折手工录入流水"
                
        data = deepcopy(data03)
        data["storeCode"] = getStoreByCode["store"]["code"]
        data["storeName"] = getStoreByCode["store"]["name"]
        data["companyCode"] = getStoreByCode["store"]["companyCode"]
        data["companyName"] = getAccountList[0]["accountName"]
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["changeReason"] = "退押货款"
        data["payAccount"] = getAccountList[0]["account"] # 分公司付款
        data["payAccountBankName"] = getAccountList[0]["bankType"]
        data["receiptAccount"] = getBankAccountList[0]["account"] # 服务中心收款
        data["receiptBankName"] = getBankAccountList[0]["branch"]
        data["remitMoney"] = remitMoney
        data["sourceType"] = 8 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
        data["inputRemark"] = f"录入手动退押货款 {remitMoney}元"             
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_disManualInputRemit_pageList():
        "85折手工录入流水分页搜索列表,获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["storeCode"] = getStoreByCode["store"]["code"] 
        data["verifyStatus"] = 0 # 待审核列表             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            id = r.json()["data"]["list"][0]["id"]
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_disManualInputRemit_verify():
        "85折手工录入流水单个审核"
        
        params = deepcopy(params05)
        params["id"] = id
        params["verifyRemark"] = f"同意录入手动退押货款 {remitMoney}元" # 审核备注
        params["verifyResult"] = 1 # 1->通过 2-> 拒绝                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            
    step_mgmt_store_getStoreByCode()
    step_mgmt_sys_getAccountList()
    step_mgmt_store_getBankAccountList()
    step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
    step_mgmt_inventory_disManualInputRemit_add() 
    step_mgmt_inventory_disManualInputRemit_pageList()       
    step_mgmt_inventory_disManualInputRemit_verify()
    
    return remitMoney


@pytest.fixture(scope="function")
def disManualInputRemit_add_9():
    "押货保证金转移"   
    from api.mall_center_sys._mgmt_sys_getAccountList import params as params01, _mgmt_sys_getAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params as params02, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params03, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_store_getBankAccountList import params as params04, _mgmt_store_getBankAccountList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import data as data03, _mgmt_inventory_disManualInputRemit_add
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import data as data02, _mgmt_inventory_disManualInputRemit_pageList
    from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import params as params05, _mgmt_inventory_disManualInputRemit_verify  
    
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    id = None
    access_token = os.environ["access_token"]
    remitMoney = 1 # 金额
                        
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心信息"
        
        nonlocal getStoreByCode
        params = deepcopy(params03)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            getStoreByCode = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_sys_getAccountList():
        "查询分公司银行账号"
        
        nonlocal getAccountList
        params = deepcopy(params01)
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            getAccountList = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_store_getBankAccountList():
        "通过storeCode获取银行账户资料信息"
        
        nonlocal getBankAccountList
        params = deepcopy(params04)
        params["storeCode"] = getStoreByCode["store"]["code"]               
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            getBankAccountList = r.json()["data"]
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        "1:3押货余额及85折保证金余额查询"
        
        nonlocal getStoreWalletMsg
        params = deepcopy(params02)
        params["storeCode"] = getStoreByCode["store"]["code"]                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            getStoreWalletMsg = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200
    
    def step_mgmt_inventory_disManualInputRemit_add(): 
        "85折手工录入流水"
                
        data = deepcopy(data03)
        data["storeCode"] = getStoreByCode["store"]["code"]
        data["storeName"] = getStoreByCode["store"]["name"]
        data["companyCode"] = getStoreByCode["store"]["companyCode"]
        data["companyName"] = getAccountList[0]["accountName"]
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["changeReason"] = "汇押货款"
        data["payAccount"] = getBankAccountList[0]["account"] # 服务中心付款
        data["payAccountBankName"] = getBankAccountList[0]["branch"]
        data["receiptAccount"] = getAccountList[0]["account"] # 分公司收款
        data["receiptBankName"] = getAccountList[0]["bankType"]
        data["remitMoney"] = remitMoney
        data["sourceType"] = 9 # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移  
        data["inputRemark"] = f"录入保证金转移 {remitMoney}元"                  
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    def step_mgmt_inventory_disManualInputRemit_pageList():
        "85折手工录入流水分页搜索列表,获取id"
        
        nonlocal id
        data = deepcopy(data02)
        data["storeCode"] = getStoreByCode["store"]["code"] 
        data["verifyStatus"] = 0 # 待审核列表             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            id = r.json()["data"]["list"][0]["id"]
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_disManualInputRemit_verify():
        "85折手工录入流水单个审核"
        
        params = deepcopy(params05)
        params["id"] = id
        params["verifyRemark"] = f"同意录入保证金转移 {remitMoney}元" # 审核备注
        params["verifyResult"] = 1 # 1->通过 2-> 拒绝                   
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            
    step_mgmt_store_getStoreByCode()
    step_mgmt_sys_getAccountList()
    step_mgmt_store_getBankAccountList()
    step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
    step_mgmt_inventory_disManualInputRemit_add() 
    step_mgmt_inventory_disManualInputRemit_pageList()       
    step_mgmt_inventory_disManualInputRemit_verify()
    
    return remitMoney

# 线下汇款 自动识别，确认押货款，退款，不处理

@pytest.fixture(scope="function")
def pay_notify_mockBankflow():
    "线下汇款自动识别"
    
    from api.mall_center_pay._pay_notify_mockBankflow import data as data02, _pay_notify_mockBankflow
    from api.mall_mgmt_application._mgmt_store_listBankAccount import _mgmt_store_listBankAccount # 银行账号列表  
    
    access_token = os.environ["access_token"] 
    listBankAccount = None
        
    @allure.step("银行账号列表")
    def step_mgmt_store_listBankAccount():
        
        nonlocal listBankAccount
        params = {
            "opType": None, # 操作类型 1新增 2修改 3作废
            "verifyStatus": None, # 审核状态 3待审核, 不选则是全部
            "pageNum": 1, 
            "pageSize": 10,
            "storeCode": store_85, # 服务中心编号
            "isUsed": 1, # 作废标示 1生效 2作废
            "leaderCardNo": None, # 总店负责人卡号
            "isSigned": None # 是否已签约，1/是，2/否
        }             
        with _mgmt_store_listBankAccount(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                listBankAccount = r.json()["data"]["list"][0]
                        
    @allure.step("生成自动识别流水")    
    def step_pay_notify_mockBankflow():
        
        data = [{
            "accountName": listBankAccount["accountName"],
            "accountNo": listBankAccount["account"],
            "bankName": listBankAccount["branch"],
            "busiTime": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))}T00:00:00.261+0800",
            "companyNo": '34000',
            "receiptAccount": '2011054919200009545',
            "receiptBankName": "中国工商银行",
            "remark": None,
            "tradeAmount": '11',
            "tradeOrderNo": f"HK{str(time.time() * 1000)[:13]}",
        }]
        with _pay_notify_mockBankflow(data, access_token) as r:
            assert r.status_code == 200
            assert r.text == "SUCCESS"

    step_mgmt_store_listBankAccount()
    if listBankAccount:
        step_pay_notify_mockBankflow()
    
    return 11


@pytest.fixture(scope="function")
def unknownRemit_deal_5():
    "线下汇款无法识别款确认押货款"
    
    from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_pageList import data as data01, _mgmt_inventory_remit_unknownRemit_pageList
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params01, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_deal import _mgmt_inventory_remit_unknownRemit_deal
    
    access_token = os.environ["access_token"]  
    pageList = None # 待处理的未识别流水
    getStoreByCode = None # 服务中心信息 
    tradeAmount = 10 # 汇款金额 
    
    @stepreruns()
    def step_mgmt_inventory_remit_unknownRemit_pageList():
        "未知款项流水分页搜索列表"
        
        nonlocal pageList
        data = deepcopy(data01)
        data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
        data["companyCode"] = "34000"
        with _mgmt_inventory_remit_unknownRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["remitMoney"] == tradeAmount
            pageList = r.json()["data"]["list"][0]
  
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心"
        
        nonlocal getStoreByCode
        params = deepcopy(params01)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreByCode = r.json()["data"]
   
    def step_mgmt_inventory_remit_unknownRemit_deal():
        "无法识别款确认押货款"
        
        data = pageList
        data["businessMode"] = 2
        data["changeReason"] = "汇押货款"
        data["dealRemark"] = "我是处理备注信息"
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["show"] = True 
        data["sourceType"] = 5 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
        data["storeCode"] = getStoreByCode["store"]["code"]  
        data["storeCodeSearch"] = True  
        data["storeName"] = getStoreByCode["store"]["name"]
        data["type"] = 2  
        data["sourceTypeList"] = [
            {
                "id": 5,
                "createTime": None,
                "updateTime": None,
                "del": 0,
                "type": 5,
                "name": "无法识别款确认押货款",
                "changeReason": "汇押货款",
                "bizType": 1,
                "bizName": "银行汇款",
                "detailType": 2
            }, 
            {
                "id": 6,
                "createTime": None,
                "updateTime": None,
                "del": 0,
                "type": 6,
                "name": "无法识别款退款",
                "changeReason": "无",
                "bizType": 1,
                "bizName": "银行汇款",
                "detailType": 2
            }, 
            {
                "type": 15,
                "name": "无法识别款不处理（需有批示或批文时可选择）",
                "changeReason": "无"
            }
        ]
        with _mgmt_inventory_remit_unknownRemit_deal(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            assert r.json()["message"] == "操作成功"
    
    step_mgmt_inventory_remit_unknownRemit_pageList()
    step_mgmt_store_getStoreByCode()
    step_mgmt_inventory_remit_unknownRemit_deal()
    
    return pageList["remitMoney"]


@pytest.fixture(scope="function")
def unknownRemit_deal_6():
    "线下汇款无法识别款退款"
    
    from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_pageList import data as data01, _mgmt_inventory_remit_unknownRemit_pageList
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params01, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_deal import _mgmt_inventory_remit_unknownRemit_deal
    
    access_token = os.environ["access_token"]  
    pageList = None # 待处理的未识别流水
    getStoreByCode = None # 服务中心信息 
    tradeAmount = 10 # 汇款金额 
                          
    @stepreruns()
    def step_mgmt_inventory_remit_unknownRemit_pageList():
        "未知款项流水分页搜索列表"
        
        nonlocal pageList
        data = deepcopy(data01)
        data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
        data["companyCode"] = "34000"
        with _mgmt_inventory_remit_unknownRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["remitMoney"] == tradeAmount
            pageList = r.json()["data"]["list"][0]
   
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心"
        
        nonlocal getStoreByCode
        params = deepcopy(params01)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreByCode = r.json()["data"]
   
    def step_mgmt_inventory_remit_unknownRemit_deal():
        "无法识别款确认押货款"
        
        data = pageList
        data["businessMode"] = 2
        data["changeReason"] = "无"
        data["dealRemark"] = "我是处理备注信息"
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["show"] = True 
        data["sourceType"] = 6 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
        data["storeCode"] = getStoreByCode["store"]["code"]  
        data["storeCodeSearch"] = True  
        data["storeName"] = getStoreByCode["store"]["name"]
        data["type"] = 2  
        data["sourceTypeList"] = [
            {
                "id": 5,
                "createTime": None,
                "updateTime": None,
                "del": 0,
                "type": 5,
                "name": "无法识别款确认押货款",
                "changeReason": "汇押货款",
                "bizType": 1,
                "bizName": "银行汇款",
                "detailType": 2
            }, 
            {
                "id": 6,
                "createTime": None,
                "updateTime": None,
                "del": 0,
                "type": 6,
                "name": "无法识别款退款",
                "changeReason": "无",
                "bizType": 1,
                "bizName": "银行汇款",
                "detailType": 2
            }, 
            {
                "type": 15,
                "name": "无法识别款不处理（需有批示或批文时可选择）",
                "changeReason": "无"
            }
        ]
        with _mgmt_inventory_remit_unknownRemit_deal(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            assert r.json()["message"] == "操作成功"
           
    step_mgmt_inventory_remit_unknownRemit_pageList()
    step_mgmt_store_getStoreByCode()
    step_mgmt_inventory_remit_unknownRemit_deal()
    
    return pageList["remitMoney"]


@pytest.fixture(scope="function")
def unknownRemit_deal_15():
    "线下汇款无法识别款不处理"
    
    from api.mall_center_pay._pay_notify_mockBankflow import data as data02, _pay_notify_mockBankflow
    from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_pageList import data as data01, _mgmt_inventory_remit_unknownRemit_pageList
    from api.mall_mgmt_application._mgmt_store_getStoreByCode import params as params01, _mgmt_store_getStoreByCode
    from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_deal import _mgmt_inventory_remit_unknownRemit_deal
    
    access_token = os.environ["access_token"]  
    pageList = None # 待处理的未识别流水
    getStoreByCode = None # 服务中心信息 
    tradeAmount = 10 # 汇款金额 

    @stepreruns()
    def step_mgmt_inventory_remit_unknownRemit_pageList():
        "未知款项流水分页搜索列表"
        
        nonlocal pageList
        data = deepcopy(data01)
        data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
        data["companyCode"] = "34000"
        with _mgmt_inventory_remit_unknownRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["remitMoney"] == tradeAmount
            pageList = r.json()["data"]["list"][0]
   
    def step_mgmt_store_getStoreByCode():
        "根据服务中心编号获取服务中心"
        
        nonlocal getStoreByCode
        params = deepcopy(params01)
        params["code"] = store_85                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreByCode = r.json()["data"]
   
    def step_mgmt_inventory_remit_unknownRemit_deal():
        "无法识别款确认押货款"
        
        data = pageList
        data["businessMode"] = 2
        data["changeReason"] = "无"
        data["dealRemark"] = "我是处理备注信息"
        data["leaderName"] = getStoreByCode["user"]["realname"]
        data["show"] = True 
        data["sourceType"] = 15 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
        data["storeCode"] = getStoreByCode["store"]["code"]  
        data["storeCodeSearch"] = True  
        data["storeName"] = getStoreByCode["store"]["name"]
        data["type"] = 2  
        data["sourceTypeList"] = [
            {
                "id": 5,
                "createTime": None,
                "updateTime": None,
                "del": 0,
                "type": 5,
                "name": "无法识别款确认押货款",
                "changeReason": "汇押货款",
                "bizType": 1,
                "bizName": "银行汇款",
                "detailType": 2
            }, 
            {
                "id": 6,
                "createTime": None,
                "updateTime": None,
                "del": 0,
                "type": 6,
                "name": "无法识别款退款",
                "changeReason": "无",
                "bizType": 1,
                "bizName": "银行汇款",
                "detailType": 2
            }, 
            {
                "type": 15,
                "name": "无法识别款不处理（需有批示或批文时可选择）",
                "changeReason": "无"
            }
        ]
        with _mgmt_inventory_remit_unknownRemit_deal(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
            assert r.json()["message"] == "操作成功"
           
    step_mgmt_inventory_remit_unknownRemit_pageList()
    step_mgmt_store_getStoreByCode()
    step_mgmt_inventory_remit_unknownRemit_deal()
    
    return pageList["remitMoney"]

# 85折转分订单,85折转分结算前调整订单

@pytest.fixture(scope="function")
@pytest.mark.usefixtures("voucher_generate_85", "returnOrder_inspect_85", "addCouponGrant_85")
def orderCommit_85():
    "85折转分订单自购"
    
    from api.mall_mobile_application._mobile_order_before_by_cardNo import params as params01, _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
    from api.mall_mobile_application._mobile_product_discount_productList import data as data01, _mobile_product_discount_productList # 查询85折转分商品
    from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
    from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
    from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
    from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
    from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
    from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 85折订单信息
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品信息
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单号
    getOrderInfo = None # 详细订单信息
    number = 2 # 购买商品数量
    token_85 = os.environ["token_85"]
    
    def step_mobile_order_before_by_cardNo():
        "根据用户卡号查询是否可购买商品"
        
        nonlocal before_by_cardNo
        params = deepcopy(params01) 
        params["cardNo"] = username_85
        with _mobile_order_before_by_cardNo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
    
    def step_mobile_product_discount_productList():
        "查询85折转分商品"
        
        nonlocal productList
        data = deepcopy(data01)
        data["isSelected"] = 1
        data["selectedList"][0] = {"serialNo": "M7035","selectNums": 2}                    
        with _mobile_product_discount_productList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode:
                    productList = d

    def step_mobile_order_carts_getFreightList():
        "获取运费补贴券列表"
        
        nonlocal getFreightList
        data = {
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    def step_mobile_order_carts_getCouponList():
        "获取选中结算分组的可用和不可用优惠券列表"
        
        nonlocal getCouponList
        data = {
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }         
        with _mobile_order_carts_getCouponList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    def step_mobile_order_carts_getSecondList():
        "获取购物秒返券券列表"
        
        nonlocal getSecondList
        data = {
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }        
        with _mobile_order_carts_getSecondList(data, token_85) as r:            
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
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }        
        with _mobile_order_carts_getGiftList_2(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

    def step_mobile_order_carts_toSettlement():
        "选择商品去结算"
        
        data = {
            "addressId": None,
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "customerId":  before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 8 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
        with _mobile_order_carts_toSettlement(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_trade_orderCommit():
        "提交订单"
        
        nonlocal orderCommit
        data = {
            "addressId": None,
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "customerId": before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
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
        with _mobile_trade_orderCommit(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
        
        nonlocal getOrderInfo
        params = {"orderNo": orderCommit["orderNo"]}
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderInfo = r.json()["data"]

    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_productList()
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_mobile_order_carts_toSettlement()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    return getOrderInfo


@pytest.fixture(scope="function")
def orderCommit_85_vip():
    "85折转分订单代购"
    
    from api.mall_mobile_application._mobile_order_before_by_cardNo import params as params01, _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
    from api.mall_mobile_application._mobile_product_discount_productList import data as data01, _mobile_product_discount_productList # 查询85折转分商品
    from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
    from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
    from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
    from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
    from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
    from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 85折订单信息
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品信息
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单号
    getOrderInfo = None # 详细订单信息
    number = 2 # 购买商品数量
    token_85 = os.environ["token_85"]
    
    def step_mobile_order_before_by_cardNo():
        "根据用户卡号查询是否可购买商品"
        
        nonlocal before_by_cardNo
        params = deepcopy(params01) 
        params["cardNo"] = username_vip
        with _mobile_order_before_by_cardNo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
    
    def step_mobile_product_discount_productList():
        "查询85折转分商品"
        
        nonlocal productList
        data = deepcopy(data01)
        data["isSelected"] = 1
        data["selectedList"][0] = {"serialNo": "M7035","selectNums": 2}                    
        with _mobile_product_discount_productList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode:
                    productList = d

    def step_mobile_order_carts_getFreightList():
        "获取运费补贴券列表"
        
        nonlocal getFreightList
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    def step_mobile_order_carts_getCouponList():
        "获取选中结算分组的可用和不可用优惠券列表"
        
        nonlocal getCouponList
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }         
        with _mobile_order_carts_getCouponList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @stepreruns()
    def step_mobile_order_carts_getSecondList():
        "获取购物秒返券券列表"
        
        nonlocal getSecondList
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }        
        with _mobile_order_carts_getSecondList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == store_85:
                        getSecondList = d["secondCouponId"]

    def step_mobile_order_carts_getGiftList_2():
        "获取电子礼券列表"
        
        nonlocal getGiftList_2
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }        
        with _mobile_order_carts_getGiftList_2(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == store_85: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d

    def step_mobile_order_carts_toSettlement():
        "选择商品去结算"
        
        data = {
            "addressId": None,
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "customerId":  before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 8 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})       
        with _mobile_order_carts_toSettlement(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_trade_orderCommit():
        "提交订单"
        
        nonlocal orderCommit
        data = {
            "addressId": None,
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "customerId": before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
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
        with _mobile_trade_orderCommit(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
        
        nonlocal getOrderInfo
        params = {"orderNo": orderCommit["orderNo"]}
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderInfo = r.json()["data"]
            
    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_productList()
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_mobile_order_carts_toSettlement()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    return getOrderInfo


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("voucher_generate_85", "returnOrder_inspect_85", "addCouponGrant_85")
def BB_orderCommit_85():
    "85折转分结算前调整订单自购"
    
    from api.mall_mobile_application._mobile_order_before_by_cardNo import params as params01, _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
    from api.mall_mobile_application._mobile_product_discount_beforeSettlementProductList import data as data01, _mobile_product_discount_beforeSettlementProductList # 查询85折转分商品--结算前销售调整
    from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
    from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
    from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
    from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
    from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
    from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 85折订单信息
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品信息
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单号
    getOrderInfo = None # 详细订单信息
    number = 2 # 购买商品数量
    token_85 = os.environ["token_85"]
    
    def step_mobile_order_before_by_cardNo():
        "根据用户卡号查询是否可购买商品"
        
        nonlocal before_by_cardNo
        params = deepcopy(params01) 
        params["cardNo"] = username_85
        with _mobile_order_before_by_cardNo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
    
    def step_mobile_product_discount_beforeSettlementProductList():
        "查询85折转分商品--结算前销售调整"
        
        nonlocal productList
        data = deepcopy(data01)
        data["isSelected"] = 1
        data["selectedList"][0] = {"serialNo": "M7035","selectNums": 2}                    
        with _mobile_product_discount_beforeSettlementProductList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode:
                    productList = d

    def step_mobile_order_carts_getFreightList():
        "获取运费补贴券列表"
        
        nonlocal getFreightList
        data = {
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    def step_mobile_order_carts_getCouponList():
        "获取选中结算分组的可用和不可用优惠券列表"
        
        nonlocal getCouponList
        data = {
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }         
        with _mobile_order_carts_getCouponList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    def step_mobile_order_carts_getSecondList():
        "获取购物秒返券券列表"
        
        nonlocal getSecondList
        data = {
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 9,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }        
        with _mobile_order_carts_getSecondList(data, token_85) as r:            
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
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "sourceType": 9,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }        
        with _mobile_order_carts_getGiftList_2(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

    def step_mobile_order_carts_toSettlement():
        "选择商品去结算"
        
        data = {
            "addressId": None,
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "customerId":  before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 9 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        # if getCouponList: # 优惠卷
        #     data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
        with _mobile_order_carts_toSettlement(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_trade_orderCommit():
        "提交订单"
        
        nonlocal orderCommit
        data = {
            "addressId": None,
            "customerCard": username_85, # 给某个顾客下单的会员卡号
            "customerId": before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
            "isUpgrade": 0 # 是否升级单 0->否 1->是
        } 
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        # if getCouponList: # 优惠卷
        #     data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                   
        with _mobile_trade_orderCommit(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
        
        nonlocal getOrderInfo
        params = {"orderNo": orderCommit["orderNo"]}
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderInfo = r.json()["data"]

    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_beforeSettlementProductList()
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_mobile_order_carts_toSettlement()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    return getOrderInfo


@pytest.fixture(scope="function")
def BB_orderCommit_85_vip():
    "85折转分订单代购"
    
    from api.mall_mobile_application._mobile_order_before_by_cardNo import params as params01, _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
    from api.mall_mobile_application._mobile_product_discount_beforeSettlementProductList import data as data01, _mobile_product_discount_beforeSettlementProductList # 查询85折转分商品--结算前销售调整
    from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
    from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
    from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
    from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
    from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
    from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 85折订单信息
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品信息
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单号
    getOrderInfo = None # 详细订单信息
    number = 2 # 购买商品数量
    token_85 = os.environ["token_85"]
    
    def step_mobile_order_before_by_cardNo():
        "根据用户卡号查询是否可购买商品"
        
        nonlocal before_by_cardNo
        params = deepcopy(params01) 
        params["cardNo"] = username_vip
        with _mobile_order_before_by_cardNo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
    
    def step_mobile_product_discount_beforeSettlementProductList():
        "查询85折转分商品"
        
        nonlocal productList
        data = deepcopy(data01)
        data["isSelected"] = 1
        data["selectedList"][0] = {"serialNo": "M7035","selectNums": 2}                    
        with _mobile_product_discount_beforeSettlementProductList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode:
                    productList = d

    def step_mobile_order_carts_getFreightList():
        "获取运费补贴券列表"
        
        nonlocal getFreightList
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    def step_mobile_order_carts_getCouponList():
        "获取选中结算分组的可用和不可用优惠券列表"
        
        nonlocal getCouponList
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }         
        with _mobile_order_carts_getCouponList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @stepreruns()
    def step_mobile_order_carts_getSecondList():
        "获取购物秒返券列表"
        
        nonlocal getSecondList
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 9,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "storeCode": store_85
        }        
        with _mobile_order_carts_getSecondList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == store_85:
                        getSecondList = d["secondCouponId"]

    def step_mobile_order_carts_getGiftList_2():
        "获取电子礼券列表"
        
        nonlocal getGiftList_2
        data = {
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "sourceType": 9,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
        }        
        with _mobile_order_carts_getGiftList_2(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == store_85: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d

    def step_mobile_order_carts_toSettlement():
        "选择商品去结算"
        
        data = {
            "addressId": None,
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "customerId":  before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 9 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        # if getCouponList: # 优惠卷
        #     data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})       
        with _mobile_order_carts_toSettlement(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mobile_trade_orderCommit():
        "提交订单"
        
        nonlocal orderCommit
        data = {
            "addressId": None,
            "customerCard": username_vip, # 给某个顾客下单的会员卡号
            "customerId": before_by_cardNo["id"], # 给某个顾客下单的会员ID
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
            "storeCode": store_85, # 服务中心编码
            "ownerId": "", # 送货人ID
            "pv": productList["pv"] * number,
            "remarks": "", # 备注
            "returnRate": 0.12, # 返还比例
            "sharerId": None, # 分享人id
            "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
            "isUpgrade": 0 # 是否升级单 0->否 1->是
        } 
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        # if getCouponList: # 优惠卷
        #     data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                    
        with _mobile_trade_orderCommit(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
        
        nonlocal getOrderInfo
        params = {"orderNo": orderCommit["orderNo"]}
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderInfo = r.json()["data"]
            
    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_beforeSettlementProductList()
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_mobile_order_carts_toSettlement()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    return getOrderInfo


# 85折转分订单退货退款,85折转分结算前调整订单退货退款

@pytest.fixture(scope="function")
def applyReturn_85(orderCommit_85):
    "85折转分订单退货退款"
    
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import params as params01, _mobile_orderInfo_getOrderInfo # 85折订单信息
    from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
    from api.mall_mobile_application._mobile_web_order_return_getReturnType import params as params02, _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
    from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import params as params03, _mobile_web_order_as_returnMonthVerify # 隔月退货验证
    from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import data as data02, _mobile_web_order_as_upgradeOrderVerify # 升级单校验
    from api.mall_mobile_application._mobile_order_return_applyReturn import data as data03, _mobile_order_return_applyReturn # 申请退货/退款
    
    getOrderInfo = orderCommit_85 # 订单详细信息
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    returnMonthVerify = None # 隔月退货验证结果
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    token_85 = os.environ["token_85"]
    
    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
    
        params = deepcopy(params01) 
        params["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    def step_mobile_order_return_getReturnReasonByType():
        "退货/退款原因列表"
        
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    def step_mobile_web_order_return_getReturnType():
        "获取退货类型"
        
        nonlocal getReturnType
        params = deepcopy(params02) 
        with _mobile_web_order_return_getReturnType(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]
    
    def step_mobile_web_order_as_returnMonthVerify():
        "隔月退货验证"
        
        nonlocal returnMonthVerify
        params = deepcopy(params03) 
        params["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_web_order_as_returnMonthVerify(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    def step_mobile_web_order_as_upgradeOrderVerify():
        "升级单校验"
        
        nonlocal upgradeOrderVerify
        data = deepcopy(data02) 
        data["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_web_order_as_upgradeOrderVerify(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]      

    def step_mobile_order_return_applyReturn():
        "申请退货/退款"
        
        nonlocal applyReturn
        data = deepcopy(data03) 
        data["orderNo"] = getOrderInfo["orderNo"]
        data["reason1"] = getReturnReasonByType[0]["returnReason"]
        data["reason1Id"] = getReturnReasonByType[0]["id"]
        with _mobile_order_return_applyReturn(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
            
    step_mobile_orderInfo_getOrderInfo()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_returnMonthVerify()
    step_mobile_web_order_as_upgradeOrderVerify()
    step_mobile_order_return_applyReturn()

    
    return applyReturn, getOrderInfo


@pytest.fixture(scope="function")
def BB_applyReturn_85(BB_orderCommit_85):
    "85折转分结算前调整订单退货退款"
    
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import params as params01, _mobile_orderInfo_getOrderInfo # 85折订单信息
    from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
    from api.mall_mobile_application._mobile_web_order_return_getReturnType import params as params02, _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
    from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import params as params03, _mobile_web_order_as_returnMonthVerify # 隔月退货验证
    from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import data as data02, _mobile_web_order_as_upgradeOrderVerify # 升级单校验
    from api.mall_mobile_application._mobile_order_return_applyReturn import data as data03, _mobile_order_return_applyReturn # 申请退货/退款
    
    getOrderInfo = BB_orderCommit_85 # 订单详细信息
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    returnMonthVerify = None # 隔月退货验证结果
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    token_85 = os.environ["token_85"]
    
    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
    
        params = deepcopy(params01) 
        params["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    def step_mobile_order_return_getReturnReasonByType():
        "退货/退款原因列表"
        
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    def step_mobile_web_order_return_getReturnType():
        "获取退货类型"
        
        nonlocal getReturnType
        params = deepcopy(params02) 
        with _mobile_web_order_return_getReturnType(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]
    
    def step_mobile_web_order_as_returnMonthVerify():
        "隔月退货验证"
        
        nonlocal returnMonthVerify
        params = deepcopy(params03) 
        params["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_web_order_as_returnMonthVerify(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    def step_mobile_web_order_as_upgradeOrderVerify():
        "升级单校验"
        
        nonlocal upgradeOrderVerify
        data = deepcopy(data02) 
        data["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_web_order_as_upgradeOrderVerify(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]      

    def step_mobile_order_return_applyReturn():
        "申请退货/退款"
        
        nonlocal applyReturn
        data = deepcopy(data03) 
        data["orderNo"] = getOrderInfo["orderNo"]
        data["reason1"] = getReturnReasonByType[0]["returnReason"]
        data["reason1Id"] = getReturnReasonByType[0]["id"]
        with _mobile_order_return_applyReturn(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
            
    step_mobile_orderInfo_getOrderInfo()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_returnMonthVerify()
    step_mobile_web_order_as_upgradeOrderVerify()
    step_mobile_order_return_applyReturn()

    
    return applyReturn, getOrderInfo

# 当月补报截止日期前，退货上个月的订单

@pytest.fixture(scope="function")
def FGY_applyReturn_85():
    "85折转分订单退货退款"
    
    from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data as data01, _mobile_orderInfo_getClientOrderList # 客户端订单列表查询
    from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import params as params01, _mobile_orderInfo_getOrderInfo # 85折订单信息
    from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
    from api.mall_mobile_application._mobile_web_order_return_getReturnType import params as params02, _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
    from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import params as params03, _mobile_web_order_as_returnMonthVerify # 隔月退货验证
    from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import data as data02, _mobile_web_order_as_upgradeOrderVerify # 升级单校验
    from api.mall_mobile_application._mobile_order_return_applyReturn import data as data03, _mobile_order_return_applyReturn # 申请退货/退款
    
    getOrderInfo = None # 上个月订单信息
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    returnMonthVerify = None # 隔月退货验证结果
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    token_85 = os.environ["token_85"]
    
    def step_mobile_orderInfo_getClientOrderList():
        "查询85折订单信息"

        nonlocal getOrderInfo
        data = deepcopy(data01)
        data["orderStatus"] = [99]
        data["commitEndTime"] = f"{(datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m-%d')}" # 上个月最后一天
        data["commitStartTime"] = f"{(datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m')}-01" # 上一个月第一天      
        with _mobile_orderInfo_getClientOrderList(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["orderNo"].startswith("GH"):
                        getOrderInfo = i
    
    def step_mobile_orderInfo_getOrderInfo():
        "查询85折订单信息"
    
        params = deepcopy(params01)
        params["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_orderInfo_getOrderInfo(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    def step_mobile_order_return_getReturnReasonByType():
        "退货/退款原因列表"
        
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    def step_mobile_web_order_return_getReturnType():
        "获取退货类型"
        
        nonlocal getReturnType
        params = deepcopy(params02) 
        with _mobile_web_order_return_getReturnType(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]
    
    def step_mobile_web_order_as_returnMonthVerify():
        "隔月退货验证"
        
        nonlocal returnMonthVerify
        params = deepcopy(params03) 
        params["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_web_order_as_returnMonthVerify(params, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    def step_mobile_web_order_as_upgradeOrderVerify():
        "升级单校验"
        
        nonlocal upgradeOrderVerify
        data = deepcopy(data02) 
        data["orderNo"] = getOrderInfo["orderNo"]
        with _mobile_web_order_as_upgradeOrderVerify(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]      

    def step_mobile_order_return_applyReturn():
        "申请退货/退款"
        
        nonlocal applyReturn
        data = deepcopy(data03) 
        data["orderNo"] = getOrderInfo["orderNo"]
        data["reason1"] = getReturnReasonByType[0]["returnReason"]
        data["reason1Id"] = getReturnReasonByType[0]["id"]
        with _mobile_order_return_applyReturn(data, token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
            
    step_mobile_orderInfo_getClientOrderList()
    step_mobile_orderInfo_getOrderInfo()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_returnMonthVerify()
    step_mobile_web_order_as_upgradeOrderVerify()
    step_mobile_order_return_applyReturn()

    
    return applyReturn, getOrderInfo



