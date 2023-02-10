# coding:utf-8

from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search # 搜索商品
from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
from api.mall_mobile_application._mobile_personalInfo_getMemberAddressList import _mobile_personalInfo_getMemberAddressList # 获取当前登录用户的配送地址列表接口
from api.mall_mobile_application._mobile_personalInfo_getRegInfosByParentCode import _mobile_personalInfo_getRegInfosByParentCode # 通过传parentCode获得相应的区域信息
from api.mall_mobile_application._mobile_personalInfo_addAddress import _mobile_personalInfo_addAddress # 新建会员配送地址
from api.mall_mobile_application._mobile_orderInfo_countOrderUpgrade import _mobile_orderInfo_countOrderUpgrade # 统计用户待升级订单
from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
from api.mall_mobile_application._mobile_wallet_updateWalletPasswordInfo import _mobile_wallet_updateWalletPasswordInfo # 更新支付管理信息
from api.mall_mobile_application._mobile_wallet_sendSmsCode import _mobile_wallet_sendSmsCode # 发送短信验证码
from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
from api.mall_center_pay._pay_notify_mockPaySuccess import _pay_notify_mockPaySuccess # 银联支付回调
from api.mall_mobile_application._mobile_payment_singlePay import _mobile_payment_singlePay # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息

from api.mall_mobile_application._mobile_web_order_as_applyAfterSale import _mobile_web_order_as_applyAfterSale # 申请售后是否支持退货、换货、维修、返修
from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import _mobile_web_order_as_returnMonthVerify # 隔月退货验证
from api.mall_center_sys._mgmt_sys_getAllReNotice import _mgmt_sys_getAllReNotice # 获取退货须知集合
from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
from api.mall_mobile_application._mobile_web_order_return_getReturnType import _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import _mobile_web_order_as_upgradeOrderVerify # 升级单校验
from api.mall_mobile_application._mobile_order_return_applyReturn import _mobile_order_return_applyReturn # 申请退货/退款
from api.mall_mobile_application._mobile_web_order_return_getOrderReturnDetails import _mobile_web_order_return_getOrderReturnDetails # 获取退货详情

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryList import _mgmt_fin_voucher_second_coupon_queryList # 秒返券列表
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryDiffList import _mgmt_fin_voucher_second_coupon_queryDiffList #  秒返券调差列表
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_updateWithdrawconf import _mgmt_fin_voucher_second_coupon_updateWithdrawconf # 秒返券提现配置修改
from api.mall_mobile_application._mobile_wallet_applySecondCouponWithdraw import _mobile_wallet_applySecondCouponWithdraw # 秒返券申请提现
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import _mgmt_fin_voucher_second_coupon_queryWithdrawList # 秒返券提现列表
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_acceptWithdraw import _mgmt_fin_voucher_second_coupon_acceptWithdraw # 秒返券提现受理接口
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_revokeWithdraw import _mgmt_fin_voucher_second_coupon_revokeWithdraw # 秒返券提现撤销
from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawList import _mobile_wallet_querySecondCouponWithdrawList # 秒返券提现列表
from api.mall_mobile_application._mobile_wallet_second_coupon_revokeWithdraw import _mobile_wallet_second_coupon_revokeWithdraw # 秒返券提现撤销接口
 
from setting import USERNAME02, username, name, username_vip, name_vip, store, store_85, productCode_02, username_85, store13, store85, productCode_SecondCoupon, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pytest
import time
import allure
import random, string
from datetime import date, timedelta
import calendar


# 秒返券状态流转
   
@allure.title("VIP顾客订单-待支付：秒返券占用中")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_2_3(vip_login_2):
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    getRegInfosByParentCode_1 = None # 通过传parentCode获得相应的区域信息-省份
    getRegInfosByParentCode_2 = None # 通过传parentCode获得相应的区域信息-城市
    getRegInfosByParentCode_3 = None # 通过传parentCode获得相应的区域信息-地区
    getRegInfosByParentCode_4 = None # 通过传parentCode获得相应的区域信息-街道
    addAddress = None # 新建会员配送地址
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("搜索商品")
    def step_mobile_product_search():

        nonlocal productList
        data = deepcopy(data01)
        data["keyword"] = productCode_SecondCoupon
        with _mobile_product_search(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode_SecondCoupon:
                        productList = i

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("通过传parentCode获得相应的区域信息:省份")
    def step_01_mobile_personalInfo_getRegInfosByParentCode():

        nonlocal getRegInfosByParentCode_1
        params = {
            "parentCode": 0, # 该地区的父编码,不传默认值时默获取省的信息，(使用于多级联动的效果) 省的parentCode默认为0
        }
        with _mobile_personalInfo_getRegInfosByParentCode(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getRegInfosByParentCode_1 = r.json()["data"][0]

    @allure.step("通过传parentCode获得相应的区域信息:城市")
    def step_02_mobile_personalInfo_getRegInfosByParentCode():

        nonlocal getRegInfosByParentCode_2
        params = {
            "parentCode": getRegInfosByParentCode_1["code"], # 该地区的父编码,不传默认值时默获取省的信息，(使用于多级联动的效果) 省的parentCode默认为0
        }
        with _mobile_personalInfo_getRegInfosByParentCode(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getRegInfosByParentCode_2 = r.json()["data"][0]

    @allure.step("通过传parentCode获得相应的区域信息:地区")
    def step_03_mobile_personalInfo_getRegInfosByParentCode():

        nonlocal getRegInfosByParentCode_3
        params = {
            "parentCode": getRegInfosByParentCode_2["code"], # 该地区的父编码,不传默认值时默获取省的信息，(使用于多级联动的效果) 省的parentCode默认为0
        }
        with _mobile_personalInfo_getRegInfosByParentCode(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getRegInfosByParentCode_3 = r.json()["data"][0]

    @allure.step("通过传parentCode获得相应的区域信息:街道")
    def step_04_mobile_personalInfo_getRegInfosByParentCode():

        nonlocal getRegInfosByParentCode_4
        params = {
            "parentCode": getRegInfosByParentCode_3["code"], # 该地区的父编码,不传默认值时默获取省的信息，(使用于多级联动的效果) 省的parentCode默认为0
        }
        with _mobile_personalInfo_getRegInfosByParentCode(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getRegInfosByParentCode_4 = r.json()["data"][0]

    @allure.step("新建会员配送地址")
    def step_mobile_personalInfo_addAddress():

        nonlocal addAddress
        data = {
            "contactName":"小程", # 联系人姓名
            "mobile": f"189{''.join(random.sample(string.digits, 8))}", # 手机号码
            "provinceCode": getRegInfosByParentCode_1["code"], # 省份编码
            "province": getRegInfosByParentCode_1["name"], # 省份
            "cityCode": getRegInfosByParentCode_2["code"], # 城市编码
            "city": getRegInfosByParentCode_2["name"], # 城市
            "districtCode": getRegInfosByParentCode_3["code"], # 区编码
            "district": getRegInfosByParentCode_3["name"], # 区
            "streetCode": getRegInfosByParentCode_4["code"], # 街道编码
            "street": getRegInfosByParentCode_4["name"], # 街道
            "address": f"解放路100号", # 详细地址
            "isDefault": 1 # 是否默认地址：0->不是；1->是
        }
        with _mobile_personalInfo_addAddress(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                addAddress = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["sourceStoreCode"] is None:
                        getSecondList = i

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": getMemberAddressList[0]["id"],
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": number,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
            "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }      
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]

    @allure.step("选择商品去结算")
    def step_02_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": getMemberAddressList[0]["id"],
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": 2, # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": number,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
            "ownerId": toSettlement["checkoutVO"]["ownerId"], # 送货人ID
            "orderInvoice": toSettlement["checkoutVO"]["orderInvoiceVo"], # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "pv": toSettlement["price"]["pv"],
            "remarks": "", # 备注
            "returnRate": toSettlement["price"]["returnRate"], # 返还比例
            "sharerId": toSettlement["sharerId"], # 分享人id
            "sourceType": toSettlement["sourceType"] # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList["secondCouponId"]})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]

    @allure.step("统计用户待升级订单")
    def step_mobile_orderInfo_countOrderUpgrade():

        nonlocal countOrderUpgrade
        params = {
            "customerId": getCurrentUserInfo["id"]
        }
        with _mobile_orderInfo_countOrderUpgrade(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                countOrderUpgrade = r.json()["data"]["status"] # 状态: 1->当月有其它未支付的升级单 2->当月有满600pv的订单 3->当月没有满600pv的订单

    @allure.step("提交订单")
    def step_mobile_trade_orderCommit():
                    
        nonlocal orderCommit
        data = {
            "addressId": getMemberAddressList[0]["id"],
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId": getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "orderInvoice": toSettlement["checkoutVO"]["orderInvoiceVo"], # # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "ownerId": toSettlement["checkoutVO"]["ownerId"], # 送货人ID
            "pv": toSettlement["price"]["pv"],
            "remarks": "", # 备注
            "returnRate": toSettlement["price"]["returnRate"], # 返还比例
            "sharerId": toSettlement["sharerId"], # 分享人id
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "isUpgrade": 0 if countOrderUpgrade == 3 else 1 # 是否升级单 0->否 1->是
        } 
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList["secondCouponId"]})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                   
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    @allure.step("单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付")
    def step_mobile_payment_singlePay():
        
        nonlocal singlePay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=订单应付金额+订单应付金额*费率信息
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false", # 支付成功前端跳转地址,微信支付必传字段信息
            "walletPassword": "" # 钱包密码,非免密必传字段
        }   
        with _mobile_payment_singlePay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            singlePay = r.json()["data"]
        
    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": singlePay["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"

    @allure.step("通过订单号查询客户端订单信息")
    @stepreruns()
    def step_mobile_orderInfo_getOrderInfo():

        nonlocal getOrderInfo
        params = {
            "orderNo": orderCommit["orderNo"] # 订单编号(必填)
        }
        with _mobile_orderInfo_getOrderInfo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["orderNo"] == orderCommit["orderNo"]
            getOrderInfo = r.json()["data"]
            
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_personalInfo_getMemberAddressList()
    if getMemberAddressList is None:
        step_01_mobile_personalInfo_getRegInfosByParentCode()
        step_02_mobile_personalInfo_getRegInfosByParentCode()
        step_03_mobile_personalInfo_getRegInfosByParentCode()
        step_04_mobile_personalInfo_getRegInfosByParentCode()
        step_mobile_personalInfo_addAddress()
        step_mobile_personalInfo_getMemberAddressList()        
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_payment_singlePay()
        # step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    return getSecondList


@allure.title("VIP顾客订单-已支付：秒返券已使用")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_2_1(vip_login_2):
        
    getSecondList = None # 秒返券列表
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
     
    @allure.step("搜索商品")
    def step_mobile_product_search():

        nonlocal productList
        data = deepcopy(data01)
        data["keyword"] = productCode_SecondCoupon
        with _mobile_product_search(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode_SecondCoupon:
                        productList = i

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["sourceStoreCode"] is None:
                        getSecondList = i
       
    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": number,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
            "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }      
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]

    @allure.step("选择商品去结算")
    def step_02_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": None,
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": number,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
            "ownerId": toSettlement["checkoutVO"]["ownerId"], # 送货人ID
            "orderInvoice": toSettlement["checkoutVO"]["orderInvoiceVo"], # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "pv": toSettlement["price"]["pv"],
            "remarks": "", # 备注
            "returnRate": toSettlement["price"]["returnRate"], # 返还比例
            "sharerId": toSettlement["sharerId"], # 分享人id
            "sourceType": toSettlement["sourceType"] # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList["secondCouponId"]})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]

    @allure.step("选择商品去结算")
    def step_03_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": None,
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": number,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
            "ownerId": toSettlement["checkoutVO"]["ownerId"], # 送货人ID
            "orderInvoice": toSettlement["checkoutVO"]["orderInvoiceVo"], # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": toSettlement["checkoutVO"]["storeCode"] if toSettlement["checkoutVO"]["storeCode"] else store, # 服务中心编码
            "pv": toSettlement["price"]["pv"],
            "remarks": "", # 备注
            "returnRate": toSettlement["price"]["returnRate"], # 返还比例
            "sharerId": toSettlement["sharerId"], # 分享人id
            "sourceType": toSettlement["sourceType"] # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
        }
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList["secondCouponId"]})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]

    @allure.step("统计用户待升级订单")
    def step_mobile_orderInfo_countOrderUpgrade():

        nonlocal countOrderUpgrade
        params = {
            "customerId": getCurrentUserInfo["id"]
        }
        with _mobile_orderInfo_countOrderUpgrade(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                countOrderUpgrade = r.json()["data"]["status"] # 状态: 1->当月有其它未支付的升级单 2->当月有满600pv的订单 3->当月没有满600pv的订单

    @allure.step("提交订单")
    def step_mobile_trade_orderCommit():
                    
        nonlocal orderCommit
        data = {
            "addressId": None,
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId": getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "orderInvoice": toSettlement["checkoutVO"]["orderInvoiceVo"], # # 发票信息
            "couponList": [], # 使用的优惠卷
            "giftList": [], # 使用的电子礼券
            "freightList": [], # 使用的运费补贴礼券
            "secondCouponList": [], # 使用的秒返券
            "storeCode": toSettlement["checkoutVO"]["storeCode"] if toSettlement["checkoutVO"]["storeCode"] else store, # 服务中心编码
            "ownerId": toSettlement["checkoutVO"]["ownerId"], # 送货人ID
            "pv": toSettlement["price"]["pv"],
            "remarks": "", # 备注
            "returnRate": toSettlement["price"]["returnRate"], # 返还比例
            "sharerId": toSettlement["sharerId"], # 分享人id
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "isUpgrade": 0 if countOrderUpgrade == 3 else 1 # 是否升级单 0->否 1->是
        } 
        if getFreightList: # 运费补贴券
            data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
        if getCouponList: # 优惠卷
            data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
        if getSecondList: # 秒返券
            data["secondCouponList"].append({"secondCouponId": getSecondList["secondCouponId"]})
        if getGiftList_2: # 电子礼券
            data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                   
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]

    @allure.step("单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付")
    def step_mobile_payment_singlePay():
        
        nonlocal singlePay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=订单应付金额+订单应付金额*费率信息
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false", # 支付成功前端跳转地址,微信支付必传字段信息
            "walletPassword": "123456" # 钱包密码,非免密必传字段
        }   
        with _mobile_payment_singlePay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            singlePay = r.json()["data"]
        
    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": singlePay["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"

    @allure.step("通过订单号查询客户端订单信息")
    @stepreruns()
    def step_mobile_orderInfo_getOrderInfo():

        nonlocal getOrderInfo
        params = {
            "orderNo": orderCommit["orderNo"] # 订单编号(必填)
        }
        with _mobile_orderInfo_getOrderInfo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["orderNo"] == orderCommit["orderNo"]
            getOrderInfo = r.json()["data"]
    
    # 设置支付密码
    
    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.title("是否设置了支付密码")   
    def step_mobile_wallet_queryPasswordExist():
        
        nonlocal queryPasswordExist
        with _mobile_wallet_queryPasswordExist(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            queryPasswordExist = r.json()["data"]

    @allure.title("发送短信验证码")    
    def step_01_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"1", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
        
    @allure.title("更新支付管理信息")    
    def step_01_mobile_wallet_updateWalletPasswordInfo():

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
    def step_02_mobile_wallet_sendSmsCode():

        data = {
            "businessType":"3", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
            "phoneNum": getCurrentUserInfo["mobile"]
        }
        with _mobile_wallet_sendSmsCode(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.title("更新支付管理信息")    
    def step_02_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 1, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
            "password": "123456",
            "passwordFlag": None, # 是否开启免密 设置支付密码必传字段
            "confirmPassword": "123456",
            "telNum": getCurrentUserInfo["mobile"],
            "smsVerificationCode": "666666"
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
          
    @allure.title("更新支付管理信息")    
    def step_03_mobile_wallet_updateWalletPasswordInfo():

        data = {
            "managerType": 4, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
            "password": "123456",
        }
        with _mobile_wallet_updateWalletPasswordInfo(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
               
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_personalInfo_getMemberAddressList()
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        
        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 钱包是否有余额
            step_mobile_wallet_queryPasswordExist()
            if queryPasswordExist: # 设置了支付密码，则更新密码,并设置免密支付
                step_01_mobile_wallet_sendSmsCode()
                step_01_mobile_wallet_updateWalletPasswordInfo()
            else: # 没有则设置支付密码,并设置免密支付
                step_02_mobile_wallet_sendSmsCode()
                step_02_mobile_wallet_updateWalletPasswordInfo()
 
            if getDetail["passwordFlag"] == 1: # 是否免密，1：开启免密；2：关闭免密
                step_03_mobile_wallet_updateWalletPasswordInfo()
                
        step_mobile_payment_singlePay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
     
    return getSecondList


@allure.title("云商-已退货：秒返券退货失效")
@pytest.fixture(scope="package", autouse=True)
def yunsh_Second_2_5(yunsh_login_PSBC):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券列表
    
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":10,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]
                
    # 退货
    @allure.step("申请售后是否支持退货、换货、维修、返修") 
    @stepreruns()     
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
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
            assert r.json()["data"]["orderNo"] == getSecondList["sourceOrderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    @allure.step("获取退货须知集合") 
    def step_mgmt_sys_getAllReNotice():
              
        with _mgmt_sys_getAllReNotice(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("退货/退款原因列表") 
    def step_mobile_order_return_getReturnReasonByType():
            
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    @allure.step("获取退货类型：1：当月退 2：隔月退") 
    def step_mobile_web_order_return_getReturnType():
            
        nonlocal getReturnType
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
        }
        with _mobile_web_order_return_getReturnType(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]

    @allure.step("升级单校验") 
    def step_mobile_web_order_as_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]  

    @allure.step("申请退货/退款") 
    def step_mobile_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "attachmentUrlList": [], # 退货凭证URL列表
            "orderNo": getSecondList["sourceOrderNo"], # 订单编号
            "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
            "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
            "reason1Remark": "" # 退货一级原因备注
        }
        with _mobile_order_return_applyReturn(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
           
    @allure.step("获取退货详情") 
    def step_mobile_web_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mobile_web_order_return_getOrderReturnDetails(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_web_order_as_applyAfterSale() # 退货退款
        step_mobile_web_order_as_returnMonthVerify()
        step_mgmt_sys_getAllReNotice()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_upgradeOrderVerify()              
        step_mobile_order_return_applyReturn()
        step_mobile_web_order_return_getOrderReturnDetails()
    
    return getSecondList


@allure.title("VIP顾客订单-退货待审核：秒返券退货中锁定")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_2_8(vip_login_2):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券列表
    token = os.environ["vip_token_2"]
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情

    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":10,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修") 
    @stepreruns()     
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_applyAfterSale(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            # assert r.json()["data"]["expressType"] == 1 # 配送方式 1->服务中心自提 2->公司配送
            assert r.json()["data"]["isExchange"] == 0 # 是否支持换货：1->是；0->否
            assert r.json()["data"]["isRepair"] == 0 # 是否支持维修：1->是；0->否
            assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
            assert r.json()["data"]["isReturnRepair"] == 0 # 是否支持返修：1->是；0->否
            assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
            assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
            assert r.json()["data"]["orderNo"] == getSecondList["sourceOrderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    @allure.step("获取退货须知集合") 
    def step_mgmt_sys_getAllReNotice():
              
        with _mgmt_sys_getAllReNotice(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("退货/退款原因列表") 
    def step_mobile_order_return_getReturnReasonByType():
            
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    @allure.step("获取退货类型：1：当月退 2：隔月退") 
    def step_mobile_web_order_return_getReturnType():
            
        nonlocal getReturnType
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
        }
        with _mobile_web_order_return_getReturnType(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]

    @allure.step("升级单校验") 
    def step_mobile_web_order_as_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]  

    @allure.step("申请退货/退款") 
    def step_mobile_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "attachmentUrlList": [], # 退货凭证URL列表
            "orderNo": getSecondList["sourceOrderNo"], # 订单编号
            "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
            "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
            "reason1Remark": "" # 退货一级原因备注
        }
        with _mobile_order_return_applyReturn(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
           
    @allure.step("获取退货详情") 
    def step_mobile_web_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mobile_web_order_return_getOrderReturnDetails(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_web_order_as_applyAfterSale() # 退货退款
        step_mobile_web_order_as_returnMonthVerify()
        step_mgmt_sys_getAllReNotice()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_upgradeOrderVerify()              
        step_mobile_order_return_applyReturn()
        step_mobile_web_order_return_getOrderReturnDetails()
  
    
    return getSecondList


@allure.title("VIP顾客-提现待审核：秒返券提现中")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_2_7(vip_login_2):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券提现配置修改")
    def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
        
        data = {
            "id": 1,
            "maxNum": 100, # 每月提现次数上限
            "minAmount": 1, # 单次提现合计金额下限
            "remark": """
        
        1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
        2. 来源订单提交售后后：
            a、此订单关联的未使用购物秒返券需锁定
            b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
        
        3.1.0需求：
        拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
        1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
        2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
        """ # 提现说明
        }
        
        with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券申请提现")
    def step_mobile_wallet_applySecondCouponWithdraw():

        data = {
            "secondCouponIdList": [getSecondList["secondCouponId"]]
        }
        with _mobile_wallet_applySecondCouponWithdraw(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()       
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_wallet_applySecondCouponWithdraw()
    
    return getSecondList


@allure.title("VIP顾客-提现：秒返券已提现")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_2_6(vip_login_2):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券
    queryWithdrawList = None # 秒返券提现列表
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券提现配置修改")
    def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
        
        data = {
            "id": 1,
            "maxNum": 100, # 每月提现次数上限
            "minAmount": 1, # 单次提现合计金额下限
            "remark": """
        
        1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
        2. 来源订单提交售后后：
            a、此订单关联的未使用购物秒返券需锁定
            b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
        
        3.1.0需求：
        拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
        1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
        2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
        """ # 提现说明
        }
        
        with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券申请提现")
    def step_mobile_wallet_applySecondCouponWithdraw():

        data = {
            "secondCouponIdList": [getSecondList["secondCouponId"]]
        }
        with _mobile_wallet_applySecondCouponWithdraw(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("秒返券提现列表,获取Id")
    def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
        
        nonlocal queryWithdrawList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile":None, # 会员手机号
            "memberType":None, # 顾客类型
            "withdrawBatch":None, # 批次号
            "withdrawTime":None, # 提现时间yyyy-MM，提供给APP和小程序使用
            "withdrawStatus":1, # 提现状态，1：待受理；2：已受理；3：已撤销
            "pageNum":1,
            "pageSize":10
        } 
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                queryWithdrawList = r.json()["data"]["list"][0]

    @allure.title("秒返券提现受理")
    def step_mgmt_fin_voucher_second_coupon_acceptWithdraw():
        
        data = {
            "batchMonth": queryWithdrawList["withdrawNo"][2:8], # 业绩月份YYYYMM
            "remark":"同意提现", # 备注
            "idList":[queryWithdrawList["id"]] # 主键id集合
        }   
        with _mgmt_fin_voucher_second_coupon_acceptWithdraw(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()       
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_wallet_applySecondCouponWithdraw()
    step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
    if queryWithdrawList:
        step_mgmt_fin_voucher_second_coupon_acceptWithdraw()
    
    return getSecondList


@allure.title("云商-提现：秒返券已提现")
@pytest.fixture(scope="package", autouse=True)
def yunsh_Second_2_6(yunsh_login_PSBC):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券
    queryWithdrawList = None # 秒返券提现列表
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券提现配置修改")
    def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
        
        data = {
            "id": 1,
            "maxNum": 100, # 每月提现次数上限
            "minAmount": 1, # 单次提现合计金额下限
            "remark": """
        
        1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
        2. 来源订单提交售后后：
            a、此订单关联的未使用购物秒返券需锁定
            b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
        
        3.1.0需求：
        拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
        1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
        2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
        """ # 提现说明
        }
        
        with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券申请提现")
    def step_mobile_wallet_applySecondCouponWithdraw():

        data = {
            "secondCouponIdList": [getSecondList["secondCouponId"]]
        }
        with _mobile_wallet_applySecondCouponWithdraw(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("秒返券提现列表,获取Id")
    def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
        
        nonlocal queryWithdrawList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile":None, # 会员手机号
            "memberType":None, # 顾客类型
            "withdrawBatch":None, # 批次号
            "withdrawTime":None, # 提现时间yyyy-MM，提供给APP和小程序使用
            "withdrawStatus":1, # 提现状态，1：待受理；2：已受理；3：已撤销
            "pageNum":1,
            "pageSize":10
        } 
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                queryWithdrawList = r.json()["data"]["list"][0]

    @allure.title("秒返券提现受理")
    def step_mgmt_fin_voucher_second_coupon_acceptWithdraw():
        
        data = {
            "batchMonth": queryWithdrawList["withdrawNo"][2:8], # 业绩月份YYYYMM
            "remark":"同意提现", # 备注
            "idList":[queryWithdrawList["id"]] # 主键id集合
        }   
        with _mgmt_fin_voucher_second_coupon_acceptWithdraw(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()       
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_wallet_applySecondCouponWithdraw()
    step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
    if queryWithdrawList:
        step_mgmt_fin_voucher_second_coupon_acceptWithdraw()
    
    return getSecondList


@allure.title("VIP顾客订单-未使用：秒返券后台提现撤销")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_7_2_houtai(vip_login_2):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券
    queryWithdrawList = None # 秒返券提现列表
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券提现配置修改")
    def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
        
        data = {
            "id": 1,
            "maxNum": 100, # 每月提现次数上限
            "minAmount": 1, # 单次提现合计金额下限
            "remark": """
        
        1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
        2. 来源订单提交售后后：
            a、此订单关联的未使用购物秒返券需锁定
            b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
        
        3.1.0需求：
        拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
        1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
        2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
        """ # 提现说明
        }
        
        with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券申请提现")
    def step_mobile_wallet_applySecondCouponWithdraw():

        data = {
            "secondCouponIdList": [getSecondList["secondCouponId"]]
        }
        with _mobile_wallet_applySecondCouponWithdraw(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("秒返券提现列表,获取Id")
    def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
        
        nonlocal queryWithdrawList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "mobile":None, # 会员手机号
            "memberType":None, # 顾客类型
            "withdrawBatch":None, # 批次号
            "withdrawTime":None, # 提现时间yyyy-MM，提供给APP和小程序使用
            "withdrawStatus":1, # 提现状态，1：待受理；2：已受理；3：已撤销
            "pageNum":1,
            "pageSize":10
        } 
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                queryWithdrawList = r.json()["data"]["list"][0]

    @allure.title("秒返券提现撤销")
    def step_mgmt_fin_voucher_second_coupon_revokeWithdraw():
        
        data = {
            "id": queryWithdrawList["id"] # 主键
        }   
        with _mgmt_fin_voucher_second_coupon_revokeWithdraw(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()       
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_wallet_applySecondCouponWithdraw()
    step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
    if queryWithdrawList:
        step_mgmt_fin_voucher_second_coupon_revokeWithdraw()
    
    return getSecondList


@allure.title("VIP顾客订单-未使用：秒返券商城前端提现撤销")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_7_2_qiantai(vip_login_2):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券
    querySecondCouponWithdrawList = None # 秒返券提现列表
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券提现配置修改")
    def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
        
        data = {
            "id": 1,
            "maxNum": 100, # 每月提现次数上限
            "minAmount": 1, # 单次提现合计金额下限
            "remark": """
        
        1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
        2. 来源订单提交售后后：
            a、此订单关联的未使用购物秒返券需锁定
            b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
        
        3.1.0需求：
        拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
        1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
        2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
        """ # 提现说明
        }
        
        with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券申请提现")
    def step_mobile_wallet_applySecondCouponWithdraw():

        data = {
            "secondCouponIdList": [getSecondList["secondCouponId"]]
        }
        with _mobile_wallet_applySecondCouponWithdraw(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    @allure.title("秒返券提现列表,获取Id")
    def step_mobile_wallet_querySecondCouponWithdrawList():
        
        nonlocal querySecondCouponWithdrawList
        data = {
            "pageNum": 1,
            "pageSize": 10
        }
        with _mobile_wallet_querySecondCouponWithdrawList(data, token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["withdrawStatus"] == 1: # 提现状态，1：待受理；2：已受理；3：已撤销
                        querySecondCouponWithdrawList = i

    @allure.title("秒返券提现撤销")
    def step_mobile_wallet_second_coupon_revokeWithdraw():
        
        data = {
            "id": querySecondCouponWithdrawList["id"] # 主键
        }   
        with _mobile_wallet_second_coupon_revokeWithdraw(data, token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()       
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_wallet_applySecondCouponWithdraw()
    step_mobile_wallet_querySecondCouponWithdrawList()
    if querySecondCouponWithdrawList:
        step_mobile_wallet_second_coupon_revokeWithdraw()
    
    return getSecondList

# 秒返券调差

@allure.title("云商：秒返券已使用，来源订单退货")
@pytest.fixture(scope="package", autouse=True)
def yunsh_Second_1_diff(yunsh_login_PSBC):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券列表
    
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [1], # 已使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":10,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["soReturnFlagDesc"] != "是":
                        getSecondList = i
                
    # 退货
    @allure.step("申请售后是否支持退货、换货、维修、返修")
    @stepreruns()    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
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
            assert r.json()["data"]["orderNo"] == getSecondList["sourceOrderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    @allure.step("获取退货须知集合") 
    def step_mgmt_sys_getAllReNotice():
              
        with _mgmt_sys_getAllReNotice(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("退货/退款原因列表") 
    def step_mobile_order_return_getReturnReasonByType():
            
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    @allure.step("获取退货类型：1：当月退 2：隔月退") 
    def step_mobile_web_order_return_getReturnType():
            
        nonlocal getReturnType
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
        }
        with _mobile_web_order_return_getReturnType(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]

    @allure.step("升级单校验") 
    def step_mobile_web_order_as_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]  

    @allure.step("申请退货/退款") 
    def step_mobile_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "attachmentUrlList": [], # 退货凭证URL列表
            "orderNo": getSecondList["sourceOrderNo"], # 订单编号
            "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
            "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
            "reason1Remark": "" # 退货一级原因备注
        }
        with _mobile_order_return_applyReturn(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
           
    @allure.step("获取退货详情") 
    def step_mobile_web_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mobile_web_order_return_getOrderReturnDetails(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_web_order_as_applyAfterSale() # 退货退款
        step_mobile_web_order_as_returnMonthVerify()
        step_mgmt_sys_getAllReNotice()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_upgradeOrderVerify()              
        step_mobile_order_return_applyReturn()
        step_mobile_web_order_return_getOrderReturnDetails()
    
    return getSecondList


@allure.title("云商：秒返券已提现，来源订单退货")
@pytest.fixture(scope="package", autouse=True)
def yunsh_Second_6_diff(yunsh_login_PSBC):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券列表
    
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [6], # 已提现
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":10,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["soReturnFlagDesc"] != "是":
                        getSecondList = i
                        break
                
    # 退货
    @allure.step("申请售后是否支持退货、换货、维修、返修") 
    @stepreruns()     
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
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
            assert r.json()["data"]["orderNo"] == getSecondList["sourceOrderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    @allure.step("获取退货须知集合") 
    def step_mgmt_sys_getAllReNotice():
              
        with _mgmt_sys_getAllReNotice(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("退货/退款原因列表") 
    def step_mobile_order_return_getReturnReasonByType():
            
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    @allure.step("获取退货类型：1：当月退 2：隔月退") 
    def step_mobile_web_order_return_getReturnType():
            
        nonlocal getReturnType
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
        }
        with _mobile_web_order_return_getReturnType(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]

    @allure.step("升级单校验") 
    def step_mobile_web_order_as_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getSecondList["sourceOrderNo"] # 订单号
        }
        with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]  

    @allure.step("申请退货/退款") 
    def step_mobile_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "attachmentUrlList": [], # 退货凭证URL列表
            "orderNo": getSecondList["sourceOrderNo"], # 订单编号
            "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
            "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
            "reason1Remark": "" # 退货一级原因备注
        }
        with _mobile_order_return_applyReturn(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
           
    @allure.step("获取退货详情") 
    def step_mobile_web_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mobile_web_order_return_getOrderReturnDetails(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_web_order_as_applyAfterSale() # 退货退款
        step_mobile_web_order_as_returnMonthVerify()
        step_mgmt_sys_getAllReNotice()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_upgradeOrderVerify()              
        step_mobile_order_return_applyReturn()
        step_mobile_web_order_return_getOrderReturnDetails()
    
    return getSecondList


@allure.title("云商：秒返券已使用，来源订单+使用订单退货")
@pytest.fixture(scope="package", autouse=True)
def yunsh_Second_1_diff_2(yunsh_login_PSBC):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券列表-来源订单未退货
    queryDiffList = [] # 秒返券调差列表
    total = 0 # 秒返券调差列表
    
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [1], # 已使用
            "soReturnFlag": None, # 是否已退货
            "pageNum":1,
            "pageSize":10,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券调差列表")    
    def step_mgmt_fin_voucher_second_coupon_queryDiffList():

        nonlocal queryDiffList, total
        data = {
            "cardNo": None, # 会员卡号
            "diffWay": None, # 处理方案，1：扣减相应金额；2：补回相应金额
            "sourceOrderNo": getSecondList["sourceOrderNo"], # 来源订单号
            "pageNum": 1,
            "pageSize": 10
        }
        with _mgmt_fin_voucher_second_coupon_queryDiffList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:                
                queryDiffList = r.json()["data"]["list"]
            total = r.json()["data"]["total"]
                
    # 退货
    @allure.step("申请售后是否支持退货、换货、维修、返修")   
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": orderNo # 订单号
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
            assert r.json()["data"]["orderNo"] == orderNo

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": orderNo # 订单号
        }
        with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            returnMonthVerify = r.json()["data"]

    @allure.step("获取退货须知集合") 
    def step_mgmt_sys_getAllReNotice():
              
        with _mgmt_sys_getAllReNotice(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("退货/退款原因列表") 
    def step_mobile_order_return_getReturnReasonByType():
            
        nonlocal getReturnReasonByType
        with _mobile_order_return_getReturnReasonByType(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnReasonByType = r.json()["data"]

    @allure.step("获取退货类型：1：当月退 2：隔月退") 
    def step_mobile_web_order_return_getReturnType():
            
        nonlocal getReturnType
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
        }
        with _mobile_web_order_return_getReturnType(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getReturnType = r.json()["data"]

    @allure.step("升级单校验") 
    def step_mobile_web_order_as_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": orderNo # 订单号
        }
        with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]["resultType"]  

    @allure.step("申请退货/退款") 
    def step_mobile_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "attachmentUrlList": [], # 退货凭证URL列表
            "orderNo": orderNo, # 订单编号
            "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
            "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
            "reason1Remark": "" # 退货一级原因备注
        }
        with _mobile_order_return_applyReturn(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]
           
    @allure.step("获取退货详情") 
    def step_mobile_web_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mobile_web_order_return_getOrderReturnDetails(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mgmt_fin_voucher_second_coupon_queryDiffList()
        if total == 0:
            orderNo = getSecondList["sourceOrderNo"]
            step_mobile_web_order_as_applyAfterSale() # 来源订单退货退款
            step_mobile_web_order_as_returnMonthVerify()
            step_mgmt_sys_getAllReNotice()
            step_mobile_order_return_getReturnReasonByType()
            step_mobile_web_order_return_getReturnType()
            step_mobile_web_order_as_upgradeOrderVerify()              
            step_mobile_order_return_applyReturn()
            step_mobile_web_order_return_getOrderReturnDetails()
            
            orderNo = getSecondList["useOrderNo"]
            step_mobile_web_order_as_applyAfterSale() # 使用订单退货退款
            step_mobile_web_order_as_returnMonthVerify()
            step_mgmt_sys_getAllReNotice()
            step_mobile_order_return_getReturnReasonByType()
            step_mobile_web_order_return_getReturnType()
            step_mobile_web_order_as_upgradeOrderVerify()              
            step_mobile_order_return_applyReturn()
            step_mobile_web_order_return_getOrderReturnDetails()
        elif total == 1:
            orderNo = getSecondList["useOrderNo"]
            step_mobile_web_order_as_applyAfterSale() # 使用订单退货退款
            step_mobile_web_order_as_returnMonthVerify()
            step_mgmt_sys_getAllReNotice()
            step_mobile_order_return_getReturnReasonByType()
            step_mobile_web_order_return_getReturnType()
            step_mobile_web_order_as_upgradeOrderVerify()              
            step_mobile_order_return_applyReturn()
            step_mobile_web_order_return_getOrderReturnDetails()
    
    return getSecondList

