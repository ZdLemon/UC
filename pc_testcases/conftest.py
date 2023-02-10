# coding:utf-8

import pytest
from api.basic_services._login import _login
from api.basic_services._login_oauth_token import _login_oauth_token

from setting import username_pk, username_vip, username ,username_85, store, store_85, mysql_host, mysql_passwd, mysql_port, mysql_user, store, productCode_zh, productCode, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pymysql
from datetime import date, timedelta


@pytest.fixture(scope="session", autouse=True)
def login():
    "hewei01 登录完美运营后台"
    r = _login().json()
    os.environ["access_token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def login_oauth_token():
    "云商 12597198 登录商城"
    r = _login_oauth_token().json()
    os.environ["token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def login_oauth_token_85():
    "云商 14498218 登录商城"
    r = _login_oauth_token(username=username_85).json()
    os.environ["token_85"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def vip_login():
    "vip顾客 26712599 登录商城"
    r = _login_oauth_token(username=username_vip).json()
    os.environ["vip_token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def pk_login():
    "普通顾客 3000004576 13259690093 登录商城"
    r = _login_oauth_token(username=username_pk).json()
    os.environ["pk_token"] = r["data"]["access_token"]
    return r



@pytest.fixture(scope="session", autouse=True)
def login_store():
    "云商 45722864 登录店铺系统902804"
    r = _login(username=store, password="206822", channel="store").json()
    os.environ["store_token"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def login_store_85():
    "云商 14498218 登录店铺系统902208"
    r = _login(username=store_85, password="133266", channel="store").json()
    os.environ["store_token_85"] = r["data"]["access_token"]
    return r


@pytest.fixture(scope="session", autouse=True)
def db_mall_center_finance():
    db = pymysql.connect(
        host=mysql_host, 
        user=mysql_user, 
        password=mysql_passwd,
        database="mall_center_finance"
    )
    yield db.cursor()
    db.close()


@pytest.fixture(scope="session", autouse=True)
def db_mall_center_inventory():
    db = pymysql.connect(
        host=mysql_host, 
        user=mysql_user, 
        password=mysql_passwd,
        database="mall_center_inventory"
    )
    yield db.cursor()
    db.close()

# 组合产品上下架

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
        with _mgmt_product_item_listVersion(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listVersion = r.json()["data"]["list"][0]
    
    def step_mgmt_product_item_onSaleVersion():
        "商品版本上架"
        
        params = {"productId": listVersion["productId"]}
        with _mgmt_product_item_onSaleVersion(params, os.environ["access_token"]) as r:
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
        with _mgmt_product_ctrl_listInfoAudit(data, os.environ["access_token"]) as r:
            # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
            assert r.json()["data"]["list"][0]["statusNote"] == "待审核"
            versionId = r.json()["data"]["list"][0]["id"]
    
    @stepreruns()
    def step_mgmt_product_ctrl_infoAudit():
        "产品审核商品版本"
        
        data = deepcopy(data02)
        data["versionId"] = versionId
        data["auditResult"] = 1
        with _mgmt_product_ctrl_infoAudit(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_product_item_listVersion()
    if listVersion["versionStatus"] == 8:
        step_mgmt_product_item_onSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()


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
        with _mgmt_product_item_listVersion(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listVersion = r.json()["data"]["list"][0]
    
    def step_mgmt_product_item_offSaleVersion():
            
        params = deepcopy(params01)
        params["productId"] = listVersion["productId"]                   
        with _mgmt_product_item_offSaleVersion(params, os.environ["access_token"]) as r:
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
        with _mgmt_product_ctrl_listInfoAudit(data, os.environ["access_token"]) as r:
            # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
            assert r.json()["data"]["list"][0]["statusNote"] == "待审核"
            versionId = r.json()["data"]["list"][0]["id"]
    
    @stepreruns()
    def step_mgmt_product_ctrl_infoAudit():
        "产品审核商品版本"
        
        data = deepcopy(data02)
        data["versionId"] = versionId
        data["auditResult"] = 1
        with _mgmt_product_ctrl_infoAudit(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_product_item_listVersion()
    if listVersion["versionStatus"] == 7:
        step_mgmt_product_item_offSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()


# 发放电子礼券，运费补贴券, 优惠券

@pytest.fixture(scope="function")
def voucher_generate_85(login_oauth_token_85):
    "14498218发放电子礼券"
    
    from api.mall_center_finance._fin_api_voucher_voucher_generate import _fin_api_voucher_voucher_generate
        
    params = {
        "amount": 15,  # 金额
        "memberId": login_oauth_token_85["data"]["userId"],  #  int顾客id
        "beginTime": "2022-05-01 00:00:00",
        "endTime": "2023-05-01 00:00:00",
        "num": 1
    }
    with _fin_api_voucher_voucher_generate(params, os.environ["access_token"]) as r:
        assert r.status_code == 200
        assert r.json()["code"] == 200
        assert r.json()["message"] == "操作成功"
    

@pytest.fixture(scope="function")
def voucher_generate(login_oauth_token):
    "45722864发放电子礼券"
    
    from api.mall_center_finance._fin_api_voucher_voucher_generate import _fin_api_voucher_voucher_generate
        
    params = {
        "amount": 15,  # 金额
        "memberId": login_oauth_token["data"]["userId"],  #  int顾客id
        "beginTime": "2022-05-01 00:00:00",
        "endTime": "2023-05-01 00:00:00",
        "num": 1
    }
    with _fin_api_voucher_voucher_generate(params, os.environ["access_token"]) as r:
        assert r.status_code == 200
        assert r.json()["code"] == 200
        assert r.json()["message"] == "操作成功"
 
 
@pytest.fixture(scope="function")
def returnOrder_inspect_85():
    "押货单退货，14498218发放运费补贴券"
    
    from api.mall_mgmt_application._mgmt_inventory_common_getReason import params as params10, _mgmt_inventory_common_getReason # 退换货原因
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import params as params12, _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchProduct import params as params13, _mgmt_inventory_dis_mortgage_returnOrder_searchProduct # 获取商品信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn import _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn # 新建押货退货单
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params as params14, _mgmt_inventory_dis_mortgage_returnOrder_listPage # 押货退货列表
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import params as params15, _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo # 展示审批保存信息
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_opinion import data as data10, _mgmt_inventory_dis_mortgage_returnOrder_opinion # 添加审批意见
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_audit import data as data12, _mgmt_inventory_dis_mortgage_returnOrder_audit # 审批
    from api.basic_services._storage_upload import files, _storage_upload # 退回时上传附件
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_process import data as data13, _mgmt_inventory_dis_mortgage_returnOrder_process # 退回处理
    from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_inspect import data as data14, _mgmt_inventory_dis_mortgage_returnOrder_inspect # 验货
    
    getReason = None # 退换货原因
    searchStore = None # 店铺信息
    searchProduct = None # 商品信息
    id = None # 押货退货单id
    listPage = None # 押货退货列表信息
    searchAuditInfo = None # 展示审批保存信息
    storage_upload = None # 退回时上传附件信息
    access_token = os.environ["access_token"]
    
    def test_mgmt_inventory_common_getReason():
        "获取各种退换货原因"
        
        nonlocal getReason
        params = deepcopy(params10)
        params["type:"] = 3 # 退货原因              
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]
    
    def test_mgmt_inventory_dis_mortgage_common_searchStore():
        "查询店铺信息"
        
        nonlocal searchStore
        params = deepcopy(params12)
        params["storeCode"] = store_85                   
        with _mgmt_inventory_dis_mortgage_common_searchStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchStore = r.json()["data"]
    
    def step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct():
        "商品编码搜索退货商品信息"
        
        nonlocal searchProduct
        params = deepcopy(params13) 
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
        params = deepcopy(params14) 
        params["storeCode"] = store_85               
        with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, access_token) as r:
            for d in r.json()["data"]["list"]:
                if d["id"] == id:
                    listPage = d
                    break

    def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
        "押货退货单详情"
        
        params = deepcopy(params15) 
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
        
        data = deepcopy(data10) 
        data["orderId"] = id
        data["content"] = f"同意{listPage['orderSn']}押货退货单申请"        
        with _mgmt_inventory_dis_mortgage_returnOrder_opinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_returnOrder_audit():
        "审批"
        
        data = deepcopy(data12)
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
        files = deepcopy(files) 
        files["clientKey"] = "mall-center-inventory" 
        files["file"] = "data/顺丰快递单.jpg"                
        with _storage_upload(files, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["datas"]["msg"] == "文件上传成功"
            storage_upload = r.json()["datas"]

    def step_mgmt_inventory_dis_mortgage_returnOrder_process():
        "退回处理"
        
        data = deepcopy(data13)
        data["orderId"] = id
        data["returnType"] = 2 # 退回类型 1自带 2邮寄
        data["expressProofUrl"] = storage_upload["fileUrlKey"]
        data["expressProofName"] = storage_upload["relativePath"][24:]
        with _mgmt_inventory_dis_mortgage_returnOrder_process(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    def step_mgmt_inventory_dis_mortgage_returnOrder_inspect():
        "验货"
        
        data = deepcopy(data14)
        data["orderId"] = id
        data["inspectResult"] = "1" # 验货意见 0不通过 1通过
        data["inspectRemark"] = f"押货退货单{listPage['orderSn']}验货没问题"
        data["orderReturnRealAmount"] = str(listPage['returnAmount'])
        data["productList"] = [{"returnRealNum": 2, "productCode": searchProduct["productCode"]}]
        data["returnRealAmount"] = str(listPage['returnAmount'])
        with _mgmt_inventory_dis_mortgage_returnOrder_inspect(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200


    test_mgmt_inventory_common_getReason()
    test_mgmt_inventory_dis_mortgage_common_searchStore()
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


@pytest.fixture(scope="function")
def addCouponGrant_85():
    "优惠券派发"
    
    from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params as params01,_mgmt_prmt_coupon_getListPage
    from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_clearImportMember import _mgmt_prmt_couponGrant_clearImportMember
    from api.mall_mgmt_application._mgmt_prmt_coupon_getBasicInfo import _mgmt_prmt_coupon_getBasicInfo
    from api.mall_mgmt_application._mgmt_prmt_selectMemberByCard import _mgmt_prmt_selectMemberByCard
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addUser import _mgmt_prmt_couponGrant_addUser
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_getImportMemberPage import _mgmt_prmt_couponGrant_getImportMemberPage
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addCouponGrant import _mgmt_prmt_couponGrant_addCouponGrant
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_examineGrant import _mgmt_prmt_couponGrant_examineGrant
    
    id = None # 优惠券id
    getBasicInfo = None # 优惠券详情
    selectMemberByCard = None # 会员信息
    addCouponGrant = None # 待审核派发id
    access_token = os.environ["access_token"]
    
    def step_mgmt_prmt_coupon_getListPage():
        "优惠券列表:获取id"
        
        nonlocal id
        params = deepcopy(params01)
        params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
        params["couponNumber"] = couponNumber
        with _mgmt_prmt_coupon_getListPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
                       
    def step_mgmt_prmt_getMemberIdentity():
        "获取所有顾客身份类型"
                        
        with _mgmt_prmt_getMemberIdentity(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                  
    def step_mgmt_prmt_couponGrant_clearImportMember():
        "清除缓存里导入的派发用户"
                        
        with _mgmt_prmt_couponGrant_clearImportMember(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                     
    def step_mgmt_prmt_coupon_getBasicInfo():
        "优惠券详情-基础信息"
        
        nonlocal getBasicInfo
        params ={"id": id}               
        with _mgmt_prmt_coupon_getBasicInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBasicInfo = r.json()["data"]
                      
    def step_mgmt_prmt_selectMemberByCard():
        "根据会员卡号去会员中心搜索会员信息"
        
        nonlocal selectMemberByCard
        params ={"cardNo": username_85}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]
                   
    def step_mgmt_prmt_couponGrant_addUser():
        "手动新增派发顾客"
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 1, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": store_85, # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                     
    def step_mgmt_prmt_couponGrant_getImportMemberPage():
        "分页查询导入用户(导入时)"
        
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "grantId": None,
            "user": None
        }               
        with _mgmt_prmt_couponGrant_getImportMemberPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                            
    def step_mgmt_prmt_couponGrant_addCouponGrant():
        "新增优惠券派发记录"
        
        nonlocal addCouponGrant
        data = {
            "type": 1, # 导入方式1等量派发2按需派发
            "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
            "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
            "everyCount": 1, # 每人发放数量
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
            "couponId": "1270722876147919236", # 优惠券id
            "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
        }               
        with _mgmt_prmt_couponGrant_addCouponGrant(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addCouponGrant = r.json()["data"]
        
    def step_mgmt_prmt_couponGrant_examineGrant():
        "新增优惠券派发记录"
        
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
    step_mgmt_prmt_selectMemberByCard()
    step_mgmt_prmt_couponGrant_addUser()
    step_mgmt_prmt_couponGrant_getImportMemberPage()
    step_mgmt_prmt_couponGrant_addCouponGrant()
    step_mgmt_prmt_couponGrant_examineGrant()


@pytest.fixture(scope="function")
def addCouponGrant():
    "优惠券派发"
    
    from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params as params01,_mgmt_prmt_coupon_getListPage
    from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_clearImportMember import _mgmt_prmt_couponGrant_clearImportMember
    from api.mall_mgmt_application._mgmt_prmt_coupon_getBasicInfo import _mgmt_prmt_coupon_getBasicInfo
    from api.mall_mgmt_application._mgmt_prmt_selectMemberByCard import _mgmt_prmt_selectMemberByCard
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addUser import _mgmt_prmt_couponGrant_addUser
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_getImportMemberPage import _mgmt_prmt_couponGrant_getImportMemberPage
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addCouponGrant import _mgmt_prmt_couponGrant_addCouponGrant
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_examineGrant import _mgmt_prmt_couponGrant_examineGrant
    
    id = None # 优惠券id
    getBasicInfo = None # 优惠券详情
    selectMemberByCard = None # 会员信息
    addCouponGrant = None # 待审核派发id
    access_token = os.environ["access_token"]
    
    def step_mgmt_prmt_coupon_getListPage():
        "优惠券列表:获取id"
        
        nonlocal id
        params = deepcopy(params01)
        params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
        params["couponNumber"] = couponNumber
        with _mgmt_prmt_coupon_getListPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
                       
    def step_mgmt_prmt_getMemberIdentity():
        "获取所有顾客身份类型"
                        
        with _mgmt_prmt_getMemberIdentity(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                  
    def step_mgmt_prmt_couponGrant_clearImportMember():
        "清除缓存里导入的派发用户"
                        
        with _mgmt_prmt_couponGrant_clearImportMember(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                     
    def step_mgmt_prmt_coupon_getBasicInfo():
        "优惠券详情-基础信息"
        
        nonlocal getBasicInfo
        params ={"id": id}               
        with _mgmt_prmt_coupon_getBasicInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBasicInfo = r.json()["data"]
                      
    def step_mgmt_prmt_selectMemberByCard():
        "根据会员卡号去会员中心搜索会员信息"
        
        nonlocal selectMemberByCard
        params ={"cardNo": username}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]
                   
    def step_mgmt_prmt_couponGrant_addUser():
        "手动新增派发顾客"
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 1, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": store_85, # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                     
    def step_mgmt_prmt_couponGrant_getImportMemberPage():
        "分页查询导入用户(导入时)"
        
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "grantId": None,
            "user": None
        }               
        with _mgmt_prmt_couponGrant_getImportMemberPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                            
    def step_mgmt_prmt_couponGrant_addCouponGrant():
        "新增优惠券派发记录"
        
        nonlocal addCouponGrant
        data = {
            "type": 1, # 导入方式1等量派发2按需派发
            "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
            "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
            "everyCount": 1, # 每人发放数量
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
            "couponId": "1270722876147919236", # 优惠券id
            "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
        }               
        with _mgmt_prmt_couponGrant_addCouponGrant(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addCouponGrant = r.json()["data"]
        
    def step_mgmt_prmt_couponGrant_examineGrant():
        "新增优惠券派发记录"
        
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
    step_mgmt_prmt_selectMemberByCard()
    step_mgmt_prmt_couponGrant_addUser()
    step_mgmt_prmt_couponGrant_getImportMemberPage()
    step_mgmt_prmt_couponGrant_addCouponGrant()
    step_mgmt_prmt_couponGrant_examineGrant()


@pytest.fixture(scope="function")
def addCouponGrant_vip():
    "优惠券派发"
    
    from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params as params01,_mgmt_prmt_coupon_getListPage
    from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_clearImportMember import _mgmt_prmt_couponGrant_clearImportMember
    from api.mall_mgmt_application._mgmt_prmt_coupon_getBasicInfo import _mgmt_prmt_coupon_getBasicInfo
    from api.mall_mgmt_application._mgmt_prmt_selectMemberByCard import _mgmt_prmt_selectMemberByCard
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addUser import _mgmt_prmt_couponGrant_addUser
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_getImportMemberPage import _mgmt_prmt_couponGrant_getImportMemberPage
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_addCouponGrant import _mgmt_prmt_couponGrant_addCouponGrant
    from api.mall_mgmt_application._mgmt_prmt_couponGrant_examineGrant import _mgmt_prmt_couponGrant_examineGrant
    
    id = None # 优惠券id
    getBasicInfo = None # 优惠券详情
    selectMemberByCard = None # 会员信息
    addCouponGrant = None # 待审核派发id
    access_token = os.environ["access_token"]
    
    def step_mgmt_prmt_coupon_getListPage():
        "优惠券列表:获取id"
        
        nonlocal id
        params = deepcopy(params01)
        params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
        params["couponNumber"] = couponNumber
        with _mgmt_prmt_coupon_getListPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            id = r.json()["data"]["list"][0]["id"]
                       
    def step_mgmt_prmt_getMemberIdentity():
        "获取所有顾客身份类型"
                        
        with _mgmt_prmt_getMemberIdentity(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                  
    def step_mgmt_prmt_couponGrant_clearImportMember():
        "清除缓存里导入的派发用户"
                        
        with _mgmt_prmt_couponGrant_clearImportMember(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                     
    def step_mgmt_prmt_coupon_getBasicInfo():
        "优惠券详情-基础信息"
        
        nonlocal getBasicInfo
        params ={"id": id}               
        with _mgmt_prmt_coupon_getBasicInfo(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBasicInfo = r.json()["data"]
                      
    def step_mgmt_prmt_selectMemberByCard():
        "根据会员卡号去会员中心搜索会员信息"
        
        nonlocal selectMemberByCard
        params ={"cardNo": username_vip}               
        with _mgmt_prmt_selectMemberByCard(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            selectMemberByCard = r.json()["data"]
                   
    def step_mgmt_prmt_couponGrant_addUser():
        "手动新增派发顾客"
        
        data = {
            "cardNo": selectMemberByCard["cardNo"], # 会员卡号
            "mobile": selectMemberByCard["mobile"], # 会员手机号
            "realName": selectMemberByCard["realName"], # 会员姓名
            "everyCount": 1, # 派发数量
            "type": 1, # 派发方式1等量2按需
            "code": store_85, # 使用门店
            "couponId": id # 优惠券id
        }               
        with _mgmt_prmt_couponGrant_addUser(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                     
    def step_mgmt_prmt_couponGrant_getImportMemberPage():
        "分页查询导入用户(导入时)"
        
        params = {
            "pageNum": 1,
            "pageSize": 10,
            "grantId": None,
            "user": None
        }               
        with _mgmt_prmt_couponGrant_getImportMemberPage(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                            
    def step_mgmt_prmt_couponGrant_addCouponGrant():
        "新增优惠券派发记录"
        
        nonlocal addCouponGrant
        data = {
            "type": 1, # 导入方式1等量派发2按需派发
            "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
            "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
            "everyCount": 1, # 每人发放数量
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
            "couponId": "1270722876147919236", # 优惠券id
            "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
        }               
        with _mgmt_prmt_couponGrant_addCouponGrant(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            addCouponGrant = r.json()["data"]
        
    def step_mgmt_prmt_couponGrant_examineGrant():
        "新增优惠券派发记录"
        
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
    step_mgmt_prmt_selectMemberByCard()
    step_mgmt_prmt_couponGrant_addUser()
    step_mgmt_prmt_couponGrant_getImportMemberPage()
    step_mgmt_prmt_couponGrant_addCouponGrant()
    step_mgmt_prmt_couponGrant_examineGrant()


# 秒返券生效

@pytest.fixture(scope="session")
def xxl_job_admin():
    "使昨天的秒返券生效"
    
    from api.basic_services._jobinfo_trigger import _jobinfo_trigger
    from api.basic_services._xxl_job_admin_login import xxl_job_admin_login
    
    r = xxl_job_admin_login()
    cookies = r.cookies.items()
    
    cookie = ""
    for name, value in cookies:
        cookie += f"{name}={value};"
    
    data = {
        "id": 109,
        "executorParam": {
            "startDate": f'{(date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")} 00:00:00', # 昨天"2022-04-07 00:00:00"
            "endDate": f'{(date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")} 23:59:59', # "2022-04-08 23:59:59"
        },
        "addressList": ""
    }
        
    _jobinfo_trigger(data=data, cookie=cookie)

