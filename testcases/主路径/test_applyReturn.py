# coding:utf-8

from api.basic_services._login import _login

from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search # 搜索商品
from api.mall_mobile_application._mobile_product_discount_productList import _mobile_product_discount_productList # 查询85折转分商品
from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
from api.mall_mobile_application._mobile_order_before_by_cardNo import _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
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

from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import _mobile_orderInfo_getClientOrderList # 客户端订单列表查询接口
from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核
from api.mall_mobile_application._mobile_web_order_return_returnGoods import _mobile_web_order_return_returnGoods # 货品退回
from api.mall_mgmt_application._mgmt_order_return_auditGoods import _mgmt_order_return_auditGoods # 退货验货审核
from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情

from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表
from api.mall_mgmt_application._mgmt_store_leader_getLeaderById import _mgmt_store_leader_getLeaderById # 根据ID获取负责人信息
from api.basic_services._auth_store_restPsw import _auth_store_restPsw # 重置服务中心密码
from api.mall_mgmt_application._mgmt_store_getStoreByCode import _mgmt_store_getStoreByCode # 根据服务中心编号获取服务中心
from api.mall_store_application._appStore_orderReturn_upgradeOrderVerify import _appStore_orderReturn_upgradeOrderVerify # 升级单校验
from api.mall_store_application._appStore_orderReturn_audit import _appStore_orderReturn_audit # 售后单审核

from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表
from api.mall_mgmt_application._mgmt_order_as_applyAfterSale import _mgmt_order_as_applyAfterSale # 申请售后是否支持退货、换货
from api.mall_mgmt_application._mgmt_order_orderInfo import _mgmt_order_orderInfo # 订单信息
from api.mall_mgmt_application._mgmt_order_return_calcRefundAmount import _mgmt_order_return_calcRefundAmount # 计算订单退款金额
from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
from api.mall_mgmt_application._mgmt_order_return_applyReturn import _mgmt_order_return_applyReturn # 申请退货
from api.mall_mgmt_application._mgmt_order_return_countWaitAudit import _mgmt_order_return_countWaitAudit # 统计待审核退货单
from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核

from api.mall_mobile_application._mobile_wallet_recharge import _mobile_wallet_recharge # 个人钱包充值

from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore # 获取服务中心列表

from api.mall_mgmt_application._mgmt_product_item_listVersion import _mgmt_product_item_listVersion # 产品版本列表
from api.mall_mobile_application._mobile_product_discount_beforeSettlementProductList import _mobile_product_discount_beforeSettlementProductList # 查询85折转分商品--结算前销售调整

from api.mall_mgmt_application._mgmt_fin_wallet_getTransDetail import _mgmt_fin_wallet_getTransDetail # 完美钱包管理-交易详情
from api.mall_mgmt_application._mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans import _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans # 查询分公司银行流水(商城后台)
from api.mall_mgmt_application._mgmt_order_getOrderSettlementDetail import _mgmt_order_getOrderSettlementDetail # 交付结算详情
from api.mall_mgmt_application._mgmt_inventory_detail import _mgmt_inventory_detail # 查询库存明细
from api.mall_mgmt_application._mgmt_dis_inventory_detail import _mgmt_dis_inventory_detail # 查询库存明细
from api.mall_mgmt_application._mgmt_inventory_transferOrder_pageList import _mgmt_inventory_transferOrder_pageList # 分页列表-85折转分分公司流水
from api.mall_mgmt_application._mgmt_fin_voucher_getSecondCouponGetDetail import _mgmt_fin_voucher_getSecondCouponGetDetail # 秒返券获券明细
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_mortgageAmountChangePageList import _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList # 服务中心账款管理 -- 押货余额详情(详情分页列表)
  
from setting import store, productCode_SecondCoupon
from util.stepreruns import stepreruns
from util.getBaseMonthlyReportData import getBaseMonthlyReportData
import os
from copy import deepcopy
import pytest
import time
import allure
import random, string
import datetime
import calendar

# 订单退货-普客

@allure.title("普通顾客购货-银联支付-公司配送订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_puk_2():
        
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
    getPayMethod = None # 获取支付方式
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["puk_token_2"]
    
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

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
      
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
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()
    step_mobile_orderInfo_countOrderUpgrade()
    step_mobile_trade_orderCommit()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_singlePay()
    step_pay_notify_mockPaySuccess()
    step_mobile_orderInfo_getOrderInfo()
     
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
    access_token = os.environ["access_token_2"]
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
        }
        with _mobile_web_order_as_applyAfterSale(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["expressType"] == 2 # 配送方式 1->服务中心自提 2->公司配送
            assert r.json()["data"]["isExchange"] == 0 # 是否支持换货：1->是；0->否
            assert r.json()["data"]["isRepair"] == 0 # 是否支持维修：1->是；0->否
            assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
            assert r.json()["data"]["isReturnRepair"] == 0 # 是否支持返修：1->是；0->否
            assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
            assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
 
    # 退货审核
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
    
    @allure.step("新增/修改留言") 
    def step_mgmt_order_return_saveComment():
            
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment":"同意这个售后申请", # 留言内容
            "id":"" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("升级单校验") 
    def step_mgmt_order_return_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "applySource": getOrderReturnDetails["orderReturn"]["applySource"], # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        }
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]
     
    @allure.step("分公司退货审核") 
    def step_mgmt_order_return_auditOrderReturn():
            
        data = {
            "serviceNo": applyReturn, # 售后单号
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意", # 审核意见
            "attachmentUrlList": [], # 审核附件URL列表
            "subsidyFreight": "", # 运费补贴
            "reason1Id": getAllReturnReasonByType[1]["id"], # 一级退货原因id
            "reason1Remark": "我是一级备注哦", # 一级退货原因备注
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 一级退货原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 二级退货原因id
            "reason2Remark": "我是二级备注哦", # 二级退货原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"] # 二级退货原因
        }
        with _mgmt_order_return_auditOrderReturn(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 退回
    @allure.step("货品退回") 
    def step_mobile_web_order_return_returnGoods():
        
        data = {
            "returnExpressType": 1, # 退回方式 1->物流发货 2->自带
            "serviceNo": applyReturn, # 售后单号
            "returnExpressNo": "xh123456789", # 快递运单号
            "attachmentUrlList": [], # 退回凭证URL列表
            "returnExpressName": "小河物流" # 快递公司名称
        }
        with _mobile_web_order_return_returnGoods(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 验货
    @allure.step("退货验货审核") 
    def step_mgmt_order_return_auditGoods():
            
        data = {
            "serviceNo": applyReturn, # 售后单号
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意", # 审核意见
            "attachmentUrlList": [], # 审核附件URL列表
            "subsidyFreight": "20" # 运费补贴
        }
        with _mgmt_order_return_auditGoods(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                 
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    if getOrderReturnDetails["orderReturn"]["returnStatus"] == 1: # 退货状态 1->待审核 2->待退回 3->待验货 97->已取消(已拒绝) 98->已取消 99->已完成
        step_sys_api_getAllReturnReasonByType() # 退货审核
        step_mgmt_order_return_saveComment()
        step_mgmt_order_return_upgradeOrderVerify()
        step_mgmt_order_return_auditOrderReturn()
        step_mobile_web_order_return_returnGoods() # 退回
        step_mgmt_order_return_auditGoods() # 验货
        step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    walletId = None # 完美钱包管理-列表:获取钱包id
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": None, # 会员卡号
            "mobile": getOrderInfo["creatorPhone"], # 顾客手机号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    @allure.step("完美钱包详情表-退款")
    def step_02_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 5, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }   
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 7 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "原路退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 7 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式
    
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    step_02_mgmt_fin_wallet_getTransDetail()    

    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo":"", # 会员卡号
            "mobile": getOrderInfo["creatorPhone"], # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 7, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] == getOrderInfo["creatorPhone"] # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == "" # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == getOrderInfo["creatorName"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == getOrderInfo["creatorType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 7 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "原路退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                           
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()


@allure.title("普通顾客购货-银联支付-服务中心自提订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_puk_1():
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getPayMethod = None # 获取支付方式
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["puk_token_2"]
    
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

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
      
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
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_orderInfo_countOrderUpgrade()
    step_mobile_trade_orderCommit()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_singlePay()
    step_pay_notify_mockPaySuccess()
    step_mobile_orderInfo_getOrderInfo()
     
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    listStore = None # 获取服务中心列表
    getStoreByCode = None # 根据服务中心编号获取服务中心-负责人身份证号码
    store_token = None # 店铺系统登录
    access_token = os.environ["access_token_2"]
  
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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

    # 审核
    @allure.step("获取服务中心列表") 
    def step_mgmt_store_listStore():
              
        nonlocal listStore
        params = {
            "storeCode" : getOrderInfo["storeCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : None,  # int网点类型1、微店 2、微店(账务未清)3、微店(办理结店中)4、微店(结店)5、冻结资格6、办理结点中7、取消（账务未结清）8、新批未运作9、正式网点10、结店（保店二年1、结店12、结店（保店一年13、结店（保店三年）
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : None,  # int是否总店 0总店 1分店
            "level" : None,  # int星级
            "companyCode" : "",  # str所属分公司编号
            "isServiceShop" : None,  # int是否服务网店
            "isSignContract" : None,  # int是否签订合同
            "areaCode" : "",  # str区县code
            "cityCode" : "",  # str城市code
            "provinceCode" : "",  # str省份code
            "ratifyDate" : "",  # str批准最早时间
            "ratifyDate" : "",  #  str批准最晚时间
            "regionCode" : "",   #
            "ratifyEndTime" : "",  #
            "ratifyStartTime" : "",   #
            "pageNum": 1,  # int页码
            "pageSize": 20,  # int页数量
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
            "cardNo": listStore["shopkeeperNo"]
        }
        with _auth_store_restPsw(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据服务中心编号获取服务中心") 
    def step_mgmt_store_getStoreByCode():
              
        nonlocal getStoreByCode
        params = {
            "code" : listStore["code"],  # str服务中心编号
        }
        with _mgmt_store_getStoreByCode(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getStoreByCode= r.json()["data"]["user"]["certificatesNo"]

    @allure.step("登录店铺系统") 
    def login_store():

        nonlocal store_token
        r = _login(username=listStore["code"], password=getStoreByCode[-6:], channel="store").json()
        store_token = r["data"]["access_token"]

    @allure.step("升级单校验") 
    def step_appStore_orderReturn_upgradeOrderVerify():
              
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getOrderInfo["orderNo"], 
        }
        with _appStore_orderReturn_upgradeOrderVerify(data, store_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]

    @allure.step("售后单审核") 
    def step_appStore_orderReturn_audit():
              
        data = {
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意自提订单退货", # 备注
            "getStatus": 1,
            "serviceNo": applyReturn # 售后单号
        }
        with _appStore_orderReturn_audit(data, store_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mgmt_store_listStore() # 店铺审核
    step_auth_store_restPsw()
    step_mgmt_store_getStoreByCode()
    login_store()
    step_appStore_orderReturn_upgradeOrderVerify()
    step_appStore_orderReturn_audit()
    step_mobile_web_order_return_getOrderReturnDetails()
    
    # 完美钱包详情
    
    walletId = None # 完美钱包管理-列表:获取钱包id
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": None, # 会员卡号
            "mobile": getOrderInfo["creatorPhone"], # 顾客手机号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    @allure.step("完美钱包详情表-退款")
    def step_02_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 5, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }   
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 7 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "原路退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 7 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式
    
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    step_02_mgmt_fin_wallet_getTransDetail() 
     
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo":"", # 会员卡号
            "mobile": getOrderInfo["creatorPhone"], # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 7, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] == getOrderInfo["creatorPhone"] # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == "" # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == getOrderInfo["creatorName"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == getOrderInfo["creatorType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 7 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "原路退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                            
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["returnCompleteTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

# 订单退货-优惠顾客

@allure.title("优惠顾客购货-银联支付-公司配送订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_vip_2():
        
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
    getPayMethod = None # 获取支付方式
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["vip_token_3"]
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

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
      
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
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()
    step_mobile_orderInfo_countOrderUpgrade()
    step_mobile_trade_orderCommit()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_singlePay()
    step_pay_notify_mockPaySuccess()
    step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
        }
        with _mobile_web_order_as_applyAfterSale(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["expressType"] == 2 # 配送方式 1->服务中心自提 2->公司配送
            assert r.json()["data"]["isExchange"] == 0 # 是否支持换货：1->是；0->否
            assert r.json()["data"]["isRepair"] == 0 # 是否支持维修：1->是；0->否
            assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
            assert r.json()["data"]["isReturnRepair"] == 0 # 是否支持返修：1->是；0->否
            assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
            assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
 
    # 退货审核
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
    
    @allure.step("新增/修改留言") 
    def step_mgmt_order_return_saveComment():
            
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment":"同意这个售后申请", # 留言内容
            "id":"" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("升级单校验") 
    def step_mgmt_order_return_upgradeOrderVerify():
            
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "applySource": getOrderReturnDetails["orderReturn"]["applySource"], # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        }
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]
     
    @allure.step("分公司退货审核") 
    def step_mgmt_order_return_auditOrderReturn():
            
        data = {
            "serviceNo": applyReturn, # 售后单号
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意", # 审核意见
            "attachmentUrlList": [], # 审核附件URL列表
            "subsidyFreight": "", # 运费补贴
            "reason1Id": getAllReturnReasonByType[1]["id"], # 一级退货原因id
            "reason1Remark": "我是一级备注哦", # 一级退货原因备注
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 一级退货原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 二级退货原因id
            "reason2Remark": "我是二级备注哦", # 二级退货原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"] # 二级退货原因
        }
        with _mgmt_order_return_auditOrderReturn(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 退回
    @allure.step("货品退回") 
    def step_mobile_web_order_return_returnGoods():
        
        data = {
            "returnExpressType": 1, # 退回方式 1->物流发货 2->自带
            "serviceNo": applyReturn, # 售后单号
            "returnExpressNo": "xh123456789", # 快递运单号
            "attachmentUrlList": [], # 退回凭证URL列表
            "returnExpressName": "小河物流" # 快递公司名称
        }
        with _mobile_web_order_return_returnGoods(data, token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 验货
    @allure.step("退货验货审核") 
    def step_mgmt_order_return_auditGoods():
            
        data = {
            "serviceNo": applyReturn, # 售后单号
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意", # 审核意见
            "attachmentUrlList": [], # 审核附件URL列表
            "subsidyFreight": "20" # 运费补贴
        }
        with _mgmt_order_return_auditGoods(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                 
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    if getOrderReturnDetails["orderReturn"]["returnStatus"] == 1: # 退货状态 1->待审核 2->待退回 3->待验货 97->已取消(已拒绝) 98->已取消 99->已完成
        step_sys_api_getAllReturnReasonByType() # 退货审核
        step_mgmt_order_return_saveComment()
        step_mgmt_order_return_upgradeOrderVerify()
        step_mgmt_order_return_auditOrderReturn()
        step_mobile_web_order_return_returnGoods() # 退回
        step_mgmt_order_return_auditGoods() # 验货
        step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    walletId = None # 完美钱包管理-列表:获取钱包id
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    @allure.step("完美钱包详情表-退款")
    def step_02_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 5, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }   
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 7 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "原路退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 7 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式
    
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    step_02_mgmt_fin_wallet_getTransDetail() 
     
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
            "mobile": None, # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 7, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == getOrderInfo["creatorCard"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == getOrderInfo["creatorName"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == getOrderInfo["creatorType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "VIP会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 7 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "原路退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                            
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()


@allure.title("优惠顾客购货-银联支付-服务中心自提订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_vip_1():
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getPayMethod = None # 获取支付方式
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["vip_token_3"]
    
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

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
      
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
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_orderInfo_countOrderUpgrade()
    step_mobile_trade_orderCommit()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_singlePay()
    step_pay_notify_mockPaySuccess()
    step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    listStore = None # 获取服务中心列表
    getLeaderById = None # 根据ID获取负责人信息
    getStoreByCode = None # 根据服务中心编号获取服务中心-负责人身份证号码
    store_token = None # 店铺系统登录
    access_token = os.environ["access_token_2"]
  
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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

    # 审核
    @allure.step("获取服务中心列表") 
    def step_mgmt_store_listStore():
              
        nonlocal listStore
        params = {
            "storeCode" : getOrderInfo["storeCode"],  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "address" : "",  # 地址关键字，模糊搜索
            "leaderName" : "",  # str负责人姓名
            "shopType" : None,  # int网点类型1、微店 2、微店(账务未清)3、微店(办理结店中)4、微店(结店)5、冻结资格6、办理结点中7、取消（账务未结清）8、新批未运作9、正式网点10、结店（保店二年1、结店12、结店（保店一年13、结店（保店三年）
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : None,  # int是否总店 0总店 1分店
            "level" : None,  # int星级
            "companyCode" : "",  # str所属分公司编号
            "isServiceShop" : None,  # int是否服务网店
            "isSignContract" : None,  # int是否签订合同
            "areaCode" : "",  # str区县code
            "cityCode" : "",  # str城市code
            "provinceCode" : "",  # str省份code
            "ratifyDate" : "",  # str批准最早时间
            "ratifyDate" : "",  #  str批准最晚时间
            "regionCode" : "",   #
            "ratifyEndTime" : "",  #
            "ratifyStartTime" : "",   #
            "pageNum": 1,  # int页码
            "pageSize": 20,  # int页数量
            "businessMode": None # 保证金类型，1/1:3，2/85%
        }
        with _mgmt_store_listStore(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listStore = r.json()["data"]["list"][0]

    @allure.step("根据ID获取负责人信息") 
    def step_mgmt_store_leader_getLeaderById():
              
        nonlocal getLeaderById
        data = {
            "leaderId": listStore["leaderId"],
        }
        with _mgmt_store_leader_getLeaderById(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getLeaderById = r.json()["data"]["certificatesType"]

    @allure.step("重置服务中心密码") 
    def step_auth_store_restPsw():
              
        data = {
            "storeCode": listStore["code"],
            "cardNo": listStore["shopkeeperNo"]
        }
        with _auth_store_restPsw(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("根据服务中心编号获取服务中心") 
    def step_mgmt_store_getStoreByCode():
              
        nonlocal getStoreByCode
        params = {
            "code" : listStore["code"],  # str服务中心编号
        }
        with _mgmt_store_getStoreByCode(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getStoreByCode= r.json()["data"]["user"]["certificatesNo"]

    @allure.step("登录店铺系统") 
    def login_store():

        nonlocal store_token
        r = _login(username=listStore["code"], password=password, channel="store").json()
        store_token = r["data"]["access_token"]

    @allure.step("升级单校验") 
    def step_appStore_orderReturn_upgradeOrderVerify():
              
        nonlocal upgradeOrderVerify
        data = {
            "orderNo": getOrderInfo["orderNo"], 
        }
        with _appStore_orderReturn_upgradeOrderVerify(data, store_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            upgradeOrderVerify = r.json()["data"]

    @allure.step("售后单审核") 
    def step_appStore_orderReturn_audit():
              
        data = {
            "auditStatus": "1", # 审核状态 1->通过 2->不通过
            "remarks": "同意自提订单退货", # 备注
            "getStatus": 1,
            "serviceNo": applyReturn # 售后单号
        }
        with _appStore_orderReturn_audit(data, store_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mgmt_store_listStore() # 店铺审核
    step_mgmt_store_leader_getLeaderById()
    step_auth_store_restPsw()
    step_mgmt_store_getStoreByCode()
    if getLeaderById == 1:
        password = getStoreByCode[-6:]
    else:
        password = "888888"
    login_store()
    step_appStore_orderReturn_upgradeOrderVerify()
    step_appStore_orderReturn_audit()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    walletId = None # 完美钱包管理-列表:获取钱包id
    access_token = os.environ["access_token_2"]
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    @allure.step("完美钱包详情表-退款")
    def step_02_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 5, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }   
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 7 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "原路退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 7 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式
    
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    step_02_mgmt_fin_wallet_getTransDetail() 
     
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
            "mobile": None, # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 7, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == getOrderInfo["creatorCard"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == getOrderInfo["creatorName"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == getOrderInfo["creatorType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "VIP会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 7 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "原路退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                            
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["returnCompleteTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    
# 订单退货-云商-自购

@allure.title("云商自购-钱包支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_800():
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                              
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": toSettlement["price"]["productPrice"] - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
            
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        
        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if toSettlement["price"]["productPrice"] > getDetail["availableBalance"]: # 如果钱包款不够，则增加钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        # if getDetail["creditAmount"] > 0: # 清空信用额
        #     step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_mobile_orderInfo_getOrderInfo()
        
        step_mobile_web_order_as_applyAfterSale() # 退货退款
        step_mobile_web_order_as_returnMonthVerify()
        step_mgmt_sys_getAllReNotice()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_upgradeOrderVerify()              
        step_mobile_order_return_applyReturn()
        step_mobile_web_order_return_getOrderReturnDetails()
        step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["returnCompleteTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商自购-银联支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_103():
            
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    
    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]

    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
        
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    # 清空钱包款   
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {- getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额   
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 支付                       
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                         
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()        
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 清空钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()        
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
        step_mobile_web_order_as_applyAfterSale() # 退货退款
        step_mobile_web_order_as_returnMonthVerify()
        step_mgmt_sys_getAllReNotice()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_upgradeOrderVerify()              
        step_mobile_order_return_applyReturn()
        step_mobile_web_order_return_getOrderReturnDetails()
        step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商自购-签约工行支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_201():
            
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_icbc"]
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    # 清空钱包款   
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {- getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额   
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 支付                             
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 201, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                   
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 如果钱包款不够，则增加钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()        
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess() # 仅银联支付时运行
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    
    
@allure.title("云商自购-签约邮储支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_203():
           
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_psbc"]
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    # 清空钱包款   
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {- getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额   
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                           
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 203, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                   
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 如果钱包款不够，则增加钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()            
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess() # 仅银联支付时运行
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商自购-银联+钱包组合支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_103_800():
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_psbc"]
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    # 清空钱包款   
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意其他款 {- getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额   
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                      
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()      
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()
        
        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0 and getDetail["availableBalance"] > toSettlement["price"]["productPrice"]: # 钱包有余额且>商品金额
            adjustAmount = - round(getDetail["availableBalance"] - toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        elif getDetail["availableBalance"] > 0 and toSettlement["price"]["productPrice"] == getDetail["availableBalance"]: # 钱包有余额且=商品金额
            adjustAmount = - round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()     
        elif getDetail["availableBalance"] > 0 and getDetail["availableBalance"] < toSettlement["price"]["productPrice"]: # 钱包有余额且<商品金额
            pass          
        elif getDetail["availableBalance"] == 0: # 钱包有余额且<商品金额
            adjustAmount = round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()  
        elif getDetail["availableBalance"] < 0: # 钱包余额为负
            adjustAmount = - getDetail["availableBalance"] + round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商自购-签约工行+钱包组合支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_201_800():
       
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_icbc"]
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    # 清空钱包款   
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意其他款 {- getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额   
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 支付                             
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 201, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()
        
        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0 and getDetail["availableBalance"] > toSettlement["price"]["productPrice"]: # 钱包有余额且>商品金额
            adjustAmount = - round(getDetail["availableBalance"] - toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        elif getDetail["availableBalance"] > 0 and toSettlement["price"]["productPrice"] == getDetail["availableBalance"]: # 钱包有余额且=商品金额
            adjustAmount = - round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()     
        elif getDetail["availableBalance"] > 0 and getDetail["availableBalance"] < toSettlement["price"]["productPrice"]: # 钱包有余额且<商品金额
            pass          
        elif getDetail["availableBalance"] == 0: # 钱包有余额且<商品金额
            adjustAmount = round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()  
        elif getDetail["availableBalance"] < 0: # 钱包余额为负
            adjustAmount = - getDetail["availableBalance"] + round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess() # 仅银联支付时运行
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商自购-签约邮储+钱包组合支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_1_203_800():
       
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请
    token = os.environ["token_psbc"]
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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    # 清空钱包款   
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意其他款 {- getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额   
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 支付                             
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 203, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()
        
        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0 and getDetail["availableBalance"] > toSettlement["price"]["productPrice"]: # 钱包有余额且>商品金额
            adjustAmount = - round(getDetail["availableBalance"] - toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        elif getDetail["availableBalance"] > 0 and toSettlement["price"]["productPrice"] == getDetail["availableBalance"]: # 钱包有余额且=商品金额
            adjustAmount = - round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()     
        elif getDetail["availableBalance"] > 0 and getDetail["availableBalance"] < toSettlement["price"]["productPrice"]: # 钱包有余额且<商品金额
            pass          
        elif getDetail["availableBalance"] == 0: # 钱包有余额且<商品金额
            adjustAmount = round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()  
        elif getDetail["availableBalance"] < 0: # 钱包余额为负
            adjustAmount = - getDetail["availableBalance"] + round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess() # 仅银联支付时运行
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    
# 订单退货-云商-代购

@allure.title("云商代购-钱包支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_800(vip_login_2):
       
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                         
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": toSettlement["price"]["productPrice"] - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

            
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()
        # if getMemberAddressList is None:
        #     step_01_mobile_personalInfo_getRegInfosByParentCode()
        #     step_02_mobile_personalInfo_getRegInfosByParentCode()
        #     step_03_mobile_personalInfo_getRegInfosByParentCode()
        #     step_04_mobile_personalInfo_getRegInfosByParentCode()
        #     step_mobile_personalInfo_addAddress()
        #     step_mobile_personalInfo_getMemberAddressList()        
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if toSettlement["price"]["productPrice"] > getDetail["availableBalance"]: # 如果钱包款不够，则增加钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        # if getDetail["creditAmount"] > 0: # 清空信用额
        #     step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()     
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商代购-银联支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_103(vip_login_2):
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                          
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                   
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()      
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 清空钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()          
        step_mobile_wallet_getDetail() 
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商代购-签约工行支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_201(vip_login_2):
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_icbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                   
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 201, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                   
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()
        # if getMemberAddressList is None:
        #     step_01_mobile_personalInfo_getRegInfosByParentCode()
        #     step_02_mobile_personalInfo_getRegInfosByParentCode()
        #     step_03_mobile_personalInfo_getRegInfosByParentCode()
        #     step_04_mobile_personalInfo_getRegInfosByParentCode()
        #     step_mobile_personalInfo_addAddress()
        #     step_mobile_personalInfo_getMemberAddressList()        
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 清空钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()        
        step_mobile_wallet_getDetail()     
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商代购-签约邮储支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_203(vip_login_2):
      
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                  
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 203, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("通过订单号查询客户端订单信息")
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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                   
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()        
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 清空钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()        
        step_mobile_wallet_getDetail()     
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修") 
    @stepreruns()   
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商代购-银联+钱包组合支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_103_800(vip_login_2):
       
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                          
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

            
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()      
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0 and getDetail["availableBalance"] > toSettlement["price"]["productPrice"]: # 钱包有余额且>商品金额
            adjustAmount = - round(getDetail["availableBalance"] - toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        elif getDetail["availableBalance"] > 0 and toSettlement["price"]["productPrice"] == getDetail["availableBalance"]: # 钱包有余额且=商品金额
            adjustAmount = - round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()     
        elif getDetail["availableBalance"] > 0 and getDetail["availableBalance"] < toSettlement["price"]["productPrice"]: # 钱包有余额且<商品金额
            pass          
        elif getDetail["availableBalance"] == 0: # 钱包有余额且<商品金额
            adjustAmount = round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()  
        elif getDetail["availableBalance"] < 0: # 钱包余额为负
            adjustAmount = - getDetail["availableBalance"] + round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail() 
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商代购-签约工行+钱包支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_201_800(vip_login_2):
      
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_icbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                   
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 201, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {adjustAmount}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

            
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0 and getDetail["availableBalance"] > toSettlement["price"]["productPrice"]: # 钱包有余额且>商品金额
            adjustAmount = - round(getDetail["availableBalance"] - toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        elif getDetail["availableBalance"] > 0 and toSettlement["price"]["productPrice"] == getDetail["availableBalance"]: # 钱包有余额且=商品金额
            adjustAmount = - round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()     
        elif getDetail["availableBalance"] > 0 and getDetail["availableBalance"] < toSettlement["price"]["productPrice"]: # 钱包有余额且<商品金额
            pass          
        elif getDetail["availableBalance"] == 0: # 钱包有余额且<商品金额
            adjustAmount = round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()  
        elif getDetail["availableBalance"] < 0: # 钱包余额为负
            adjustAmount = - getDetail["availableBalance"] + round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()     
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        # step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("云商代购-签约邮储+钱包支付订单退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
def test_applyReturn_yunsh_2_203_800(vip_login_2):
      
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                  
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 203, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

            
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()       
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0 and getDetail["availableBalance"] > toSettlement["price"]["productPrice"]: # 钱包有余额且>商品金额
            adjustAmount = - round(getDetail["availableBalance"] - toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        elif getDetail["availableBalance"] > 0 and toSettlement["price"]["productPrice"] == getDetail["availableBalance"]: # 钱包有余额且=商品金额
            adjustAmount = - round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()     
        elif getDetail["availableBalance"] > 0 and getDetail["availableBalance"] < toSettlement["price"]["productPrice"]: # 钱包有余额且<商品金额
            pass          
        elif getDetail["availableBalance"] == 0: # 钱包有余额且<商品金额
            adjustAmount = round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()  
        elif getDetail["availableBalance"] < 0: # 钱包余额为负
            adjustAmount = - getDetail["availableBalance"] + round(toSettlement["price"]["productPrice"] * 0.5, 1)
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        
        step_mobile_wallet_getDetail()     
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_mobile_orderInfo_getOrderInfo()
    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()

# 当月退-上个月的订单

@allure.title("云商自购-订单-当月退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
@pytest.mark.skipif(getBaseMonthlyReportData() == 16, reason="15日之后，则是隔月退货，不执行")
def test_applyReturn_yunsh_commitStartTime_1():
      
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getClientOrderList = None # 客户端订单列表查询接口

    getOrderInfo = None # 详细订单信息
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("客户端订单列表查询接口")
    def step_mobile_orderInfo_getClientOrderList():
                    
        nonlocal getClientOrderList
        data = {
            "orderNo": "", # 订单编号
            "customerPhone": "", # 顾客手机号
            "customerCard": "", # 顾客卡号
            "customerName": "", # 顾客姓名
            "commitEndTime": f"{(datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m-%d')}", # 上个月最后一天
            "commitStartTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-01', # 上一个月第一天，交易开始时间2022-04-01
            "orderStatus": [2], # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部
            "orderType": "1", # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单
            "orderWay": "1", # 下单方式 1->自购订单 2->代购订单 默认空为全部
            "pageNum": 1,
            "pageSize": 10,
            "serialNo": "", # 商品编码
            "title": "", # 商品名称
            "queryType": None # 查询类型(默认为null) null->原有订单(包含85折订单)查询 1->85折转分订单 2->85折转分补报订单 3->85折转分订单+85折转分补报订单
        }                 
        with _mobile_orderInfo_getClientOrderList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getClientOrderList = r.json()["data"]["list"][0]

    @allure.step("搜索商品")
    def step_mobile_product_search():

        nonlocal productList
        data = deepcopy(data01)
        data["keyword"] = getClientOrderList["orderProductVOList"][0]["serialNo"]
        with _mobile_product_search(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == getClientOrderList["orderProductVOList"][0]["serialNo"]:
                        productList = i
 
    @allure.step("通过订单号查询客户端订单信息")
    @stepreruns()
    def step_mobile_orderInfo_getOrderInfo():

        nonlocal getOrderInfo
        params = {
            "orderNo": getClientOrderList["orderNo"] # 订单编号(必填)
        }
        with _mobile_orderInfo_getOrderInfo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["orderNo"] == getClientOrderList["orderNo"]
            getOrderInfo = r.json()["data"]

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_orderInfo_getClientOrderList()
    step_mobile_product_search()
    step_mobile_orderInfo_getOrderInfo()

    # 退货    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()


@allure.title("云商代购-订单-当月退货退款")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/order/return/applyReturn")
@pytest.mark.skipif(getBaseMonthlyReportData() == 16, reason="15日之后，则是隔月退货，不执行")
def test_applyReturn_yunsh_commitStartTime_2():
      
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getClientOrderList = None # 客户端订单列表查询接口

    getOrderInfo = None # 详细订单信息
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("客户端订单列表查询接口")
    def step_mobile_orderInfo_getClientOrderList():
                    
        nonlocal getClientOrderList
        data = {
            "orderNo": "", # 订单编号
            "customerPhone": "", # 顾客手机号
            "customerCard": "", # 顾客卡号
            "customerName": "", # 顾客姓名
            "commitEndTime": f"{(datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m-%d')}", # 上个月最后一天
            "commitStartTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-01', # 上一个月第一天，交易开始时间2022-04-01
            "orderStatus": [2], # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部
            "orderType": "1", # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单
            "orderWay": "2", # 下单方式 1->自购订单 2->代购订单 默认空为全部
            "pageNum": 1,
            "pageSize": 10,
            "serialNo": "", # 商品编码
            "title": "", # 商品名称
            "queryType": None # 查询类型(默认为null) null->原有订单(包含85折订单)查询 1->85折转分订单 2->85折转分补报订单 3->85折转分订单+85折转分补报订单
        }                 
        with _mobile_orderInfo_getClientOrderList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getClientOrderList = r.json()["data"]["list"][0]

    @allure.step("搜索商品")
    def step_mobile_product_search():

        nonlocal productList
        data = deepcopy(data01)
        data["keyword"] = getClientOrderList["orderProductVOList"][0]["serialNo"]
        with _mobile_product_search(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == getClientOrderList["orderProductVOList"][0]["serialNo"]:
                        productList = i
 
    @allure.step("通过订单号查询客户端订单信息")
    @stepreruns()
    def step_mobile_orderInfo_getOrderInfo():

        nonlocal getOrderInfo
        params = {
            "orderNo": getClientOrderList["orderNo"] # 订单编号(必填)
        }
        with _mobile_orderInfo_getOrderInfo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["orderNo"] == getClientOrderList["orderNo"]
            getOrderInfo = r.json()["data"]

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_orderInfo_getClientOrderList()
    step_mobile_product_search()
    step_mobile_orderInfo_getOrderInfo()

    # 退货    
    returnMonthVerify = "" # 隔月退货验证结果
    getReturnReasonByType = None # 退货/退款原因列表
    getReturnType = None # 获取退货类型：1：当月退 2：隔月退
    upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    @allure.step("申请售后是否支持退货、换货、维修、返修")    
    def step_mobile_web_order_as_applyAfterSale():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            assert r.json()["data"]["returnType"] == 1 # 退货类型 1->当月退货 2->隔月退货
            assert r.json()["data"]["orderNo"] == getOrderInfo["orderNo"]

    @allure.step("隔月退货验证") 
    def step_mobile_web_order_as_returnMonthVerify():
            
        nonlocal returnMonthVerify
        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"] # 订单号
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
            "orderNo": getOrderInfo["orderNo"], # 订单编号
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
    
    step_mobile_web_order_as_applyAfterSale() # 退货退款
    step_mobile_web_order_as_returnMonthVerify()
    step_mgmt_sys_getAllReNotice()
    step_mobile_order_return_getReturnReasonByType()
    step_mobile_web_order_return_getReturnType()
    step_mobile_web_order_as_upgradeOrderVerify()              
    step_mobile_order_return_applyReturn()
    step_mobile_web_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            # assert r.json()["data"]["list"][0]["changeAfter"] ==  # 可用押货余额
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
            # assert r.json()["data"]["list"][0]["createTime"] == getOrderReturnDetails["orderReturn"]["refundTime"] # 交易时间
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

# 订单退货-完美运营后台代客售后

@allure.title("云商代购-银联支付订单-完美运营后台代客售后")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/applyReturn")
def test_applyReturn_applySource_yunsh_2_103(vip_login_2):
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    hasStore = None # 云商/微店是否已开通服务中心
    canBuy = None # 根据用户卡号查询购买信息
    queryPasswordExist = False # 是否设置了支付密码
    getDetail = None # 获取钱包首页相关信息
    getPayMethod = None # 获取支付方式
    associationPay = None # 组合支付
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["token_psbc"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    getAdjustList = [] # 手工录入款项审核-列表
    getAdjustDetail = None # 手工录入款项审核-详情
    
    walletCreditApplyId = [] # 单个信用额列表查询:是否有待审核的申请

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

    @allure.step("云商/微店是否已开通服务中心")
    def step_mobile_order_carts_hasStore():

        nonlocal hasStore
        with _mobile_order_carts_hasStore(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            hasStore = r.json()["data"]

    @allure.step("根据用户卡号查询购买信息")
    def step_mobile_order_carts_canBuy():

        nonlocal canBuy
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 用户卡号
            "serialNo": productList["serialNo"] # 商品编码
        }
        with _mobile_order_carts_canBuy(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            canBuy = r.json()["data"]

    @allure.step("获取当前登录用户的配送地址列表")
    def step_mobile_personalInfo_getMemberAddressList():

        nonlocal getMemberAddressList
        with _mobile_personalInfo_getMemberAddressList(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getMemberAddressList = r.json()["data"]

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": getCurrentUserInfo["leaderStoreCode"],
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["giftCouponStatus"] == 2 and d["shopCode"] == getCurrentUserInfo["leaderStoreCode"]: # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 ,服务中心/微店编码
                        getGiftList_2 = d
                        break

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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
                          
    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
    
    @allure.step("组合支付")
    def step_mobile_payment_associationPay():

        nonlocal associationPay
        data = {
            "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
            "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
            "orderNoList": [orderCommit["orderNo"]],
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
            "feeRate": 0, # 手续费率
            "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
            "walletPassword": "123456", # 钱包充值密码,非免密必传字段
            "orderNo": orderCommit["orderNo"]
        }
        with _mobile_payment_associationPay(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            associationPay = r.json()["data"]

    @allure.step("银联支付回调")
    def step_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": associationPay["payOrderNo"],
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

    # 清空钱包款
    
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
            "walletId": getCurrentUserInfo["id"] , # 钱包id
            "companyCode": getDetail["companyNo"], # 分公司
            "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
            "adjustAmount": - getDetail["availableBalance"], # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
            "adjustReason": f'其他款 {- getDetail["availableBalance"]}元'
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
        data["auditRemark"] = f'同意其他款 {toSettlement["price"]["productPrice"] - getDetail["availableBalance"]}元' 
        data["walletAdjustId"] = getAdjustList
        with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 清空信用额
    
    @allure.step("单个信用额列表查询:是否有待审核的申请")
    def step_mgmt_fin_wallet_credit_getApplyList():
        "单个信用额列表查询:是否有待审核的申请"
        
        nonlocal walletCreditApplyId
        data = {
            "storeCode": None,
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
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
                    walletCreditApplyId.append(i["walletCreditApplyId"]) 

    @allure.step("审核不通过")
    def step_mgmt_fin_wallet_credit_auditApply():
    
        data = {
            "auditStatus": 3, # 审核结果:1：待审核；2：已通过；3：已驳回；7：待提交
            "auditRemark": "不同意信用额申请", # 审批备注
            "walletCreditApplyIdList": walletCreditApplyId, # 顾客信用额申请id集合
            "creditEffectTime": "" # 生效时间"2022-06-10 14:00:00"
        }
        with _mgmt_fin_wallet_credit_auditApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "批量审核成功，非待审核状态记录已忽略"
        
    @allure.step("顾客信用额列表-新增：清空信用额-负数直接生效无需审核")
    def step_mgmt_fin_wallet_credit_addApply():
    
        data = {
            "cardNo": getCurrentUserInfo["cardNo"], # 会员卡号
            "applyAmount": -getDetail["creditAmount"], # 调整新增信用额度
            "instalment": 0, # 是否分期，1：是，0：否
            "realname": getCurrentUserInfo["realname"],
            "creditAmount": getDetail["creditAmount"], # 已有信用额
            "isCommit": 1 # 是否提交审核，1：是，0:否
        } 
        with _mgmt_fin_wallet_credit_addApply(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    # 充值-钱包为负时
    wallet_recharge = None # 个人钱包充值
    
    @allure.title("个人钱包充值") 
    def step_mobile_wallet_recharge():
    
        nonlocal wallet_recharge
        data = {
            "actualRechargeAmt": - getDetail["actualBalance"], # 实付金额
            "channelCode": 103, # 充值渠道 充值方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 203：邮政储蓄银行 204：交通银行 205：平安代扣
            "feeRate": 0, # 费率
            "payType": "PC", # 支付类型,H5、APP、PC
            "rechargeAmount": - getDetail["actualBalance"], # 充值金额
            "walletPassword": "", # 钱包充值密码(传加密后数据),非免密必传字段
            "jumpUrl": "//uc-test.perfect99.com/recharge?result=1&rechargeAmount=10" # 支付成功前端跳转地址,微信支付必传字段信息
        }    
        with _mobile_wallet_recharge(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            wallet_recharge = r.json()["data"]

    @allure.step("银联支付回调")
    def step_02_pay_notify_mockPaySuccess():

        params = {
            "payOrderNo": wallet_recharge["payOrderNo"],
        }
        with _pay_notify_mockPaySuccess(params, token) as r:            
            assert r.status_code == 200
            assert r.text == "SUCCESS"
                   
    step_mobile_product_search()
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_carts_hasStore()
    step_mobile_order_carts_canBuy()
    if hasStore is None and canBuy["quotaNumber"] == -1 and canBuy["memberStatus"] == 0:
        step_mobile_personalInfo_getMemberAddressList()      
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_01_mobile_order_carts_toSettlement()
        step_02_mobile_order_carts_toSettlement()
        step_03_mobile_order_carts_toSettlement()
        step_mobile_orderInfo_countOrderUpgrade()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        if queryPasswordExist:
            step_mobile_wallet_sendSmsCode()
            step_mobile_wallet_updateWalletPasswordInfo()
        step_mobile_wallet_getDetail()

        # 清空钱包款+信用额
        step_01_mgmt_fin_wallet_getAdjustList()
        if getAdjustList: # 是否有待审核的手工录入款
            for id in getAdjustList:
                step_01_mgmt_fin_wallet_getAdjustDetail()
                step_01_mgmt_fin_wallet_auditAdjust()
        step_mgmt_fin_wallet_credit_getApplyList()
        if walletCreditApplyId: # 是否有待审核的信用额申请
            step_mgmt_fin_wallet_credit_auditApply()

        step_mobile_wallet_getDetail()
        if getDetail["availableBalance"] > 0: # 清空钱包款
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
        if getDetail["creditAmount"] > 0: # 清空信用额
            step_mgmt_fin_wallet_credit_addApply()
        if getDetail["actualBalance"] < 0: # 给钱包充值
            step_mobile_wallet_recharge()
            step_02_pay_notify_mockPaySuccess()          
        step_mobile_wallet_getDetail() 
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
    
    getAllReturnReasonByType = None # 退货/退款原因列表
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    
    # 退货
    
    @allure.step("计算订单退款金额")    
    def step_mgmt_order_return_calcRefundAmount():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
        }
        with _mgmt_order_return_calcRefundAmount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == getOrderInfo["totalAmount"]

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

    @allure.step("升级单校验") 
    def step_mgmt_order_return_upgradeOrderVerify():
            
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "applySource": 0, # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        }
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] == 0

    @allure.step("申请退货") 
    def step_mgmt_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
            "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
            "reason1Remark": "我是退货一级原因备注信息哦", # 退货一级原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
            "reason2Remark": "我是退货二级原因备注信息哦", # 退货二级原因备注
            "applySource": "0" # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
        }
        with _mgmt_order_return_applyReturn(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]

    @allure.step("统计待审核退货单") 
    def step_mgmt_order_return_countWaitAudit():
        
        params = {
            "applySource": None, # 申请来源 1->顾客申请 2->公司申请
            "companyCode": "", # 分公司编号
            "companyName": "", # 分公司名称
            "creatorCard": "", # 开单人卡号
            "customerCard": "", # 顾客卡号
            "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
            "returnNo": "", # 退货单号
            "orderNo": getOrderInfo["orderNo"],
            "returnType": None, # 退货类型 1->当月退货 2->隔月退货
            "storeCode": "", # 服务中心编号
            "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
            "currentPage": 1,
            "pageSize": 10,
            "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
            "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
        }
        with _mgmt_order_return_countWaitAudit(params, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 0

    @allure.step("新增/修改留言") 
    def step_mgmt_order_return_saveComment():
        
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment":"我同意这个代客售后申请", # 留言内容
            "id":"" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
                 
    @allure.step("退货详情") 
    def step_mgmt_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
    
    step_mgmt_order_return_calcRefundAmount() # 退货退款
    step_sys_api_getAllReturnReasonByType()
    step_mgmt_order_return_upgradeOrderVerify()              
    step_mgmt_order_return_applyReturn()
    step_mgmt_order_return_countWaitAudit()
    step_mgmt_order_return_saveComment()
    step_mgmt_order_return_upgradeOrderVerify()
    step_mgmt_order_return_auditOrderReturn()
    step_mgmt_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": getOrderInfo["creatorId"], # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1      
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()


@allure.title("优惠顾客购货-银联支付-服务中心自提订单-完美运营后台代客售后")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/applyReturn")
def test_applyReturn_applySource_vip_1():
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getPayMethod = None # 获取支付方式
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["vip_token_3"]
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

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
      
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
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_orderInfo_countOrderUpgrade()
    step_mobile_trade_orderCommit()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_singlePay()
    step_pay_notify_mockPaySuccess()
    step_mobile_orderInfo_getOrderInfo()
        
    # 退货
    getAllReturnReasonByType = None # 退货/退款原因列表
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
        
    @allure.step("计算订单退款金额")    
    def step_mgmt_order_return_calcRefundAmount():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
        }
        with _mgmt_order_return_calcRefundAmount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == getOrderInfo["totalAmount"]

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

    @allure.step("升级单校验") 
    def step_mgmt_order_return_upgradeOrderVerify():
            
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "applySource": 0, # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        }
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] == 0

    @allure.step("申请退货") 
    def step_mgmt_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
            "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
            "reason1Remark": "我是退货一级原因备注信息哦", # 退货一级原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
            "reason2Remark": "我是退货二级原因备注信息哦", # 退货二级原因备注
            "applySource": "0" # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
        }
        with _mgmt_order_return_applyReturn(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]

    @allure.step("统计待审核退货单") 
    def step_mgmt_order_return_countWaitAudit():
        
        params = {
            "applySource": None, # 申请来源 1->顾客申请 2->公司申请
            "companyCode": "", # 分公司编号
            "companyName": "", # 分公司名称
            "creatorCard": "", # 开单人卡号
            "customerCard": "", # 顾客卡号
            "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
            "returnNo": "", # 退货单号
            "orderNo": getOrderInfo["orderNo"],
            "returnType": None, # 退货类型 1->当月退货 2->隔月退货
            "storeCode": "", # 服务中心编号
            "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
            "currentPage": 1,
            "pageSize": 10,
            "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
            "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
        }
        with _mgmt_order_return_countWaitAudit(params, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 0

    @allure.step("新增/修改留言") 
    def step_mgmt_order_return_saveComment():
        
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment":"我同意这个代客售后申请", # 留言内容
            "id":"" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
                 
    @allure.step("退货详情") 
    def step_mgmt_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
    
    step_mgmt_order_return_calcRefundAmount() # 退货退款
    step_sys_api_getAllReturnReasonByType()
    step_mgmt_order_return_upgradeOrderVerify()              
    step_mgmt_order_return_applyReturn()
    step_mgmt_order_return_countWaitAudit()
    step_mgmt_order_return_saveComment()
    step_mgmt_order_return_upgradeOrderVerify()
    step_mgmt_order_return_auditOrderReturn()
    step_mgmt_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    walletId = None # 完美钱包管理-列表:获取钱包id
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    @allure.step("完美钱包详情表-退款")
    def step_02_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 5, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }   
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 7 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "原路退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 7 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式
    
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    step_02_mgmt_fin_wallet_getTransDetail() 
     
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
            "mobile": None, # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 7, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] is None # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == getOrderInfo["creatorCard"] # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == getOrderInfo["creatorName"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == getOrderInfo["creatorType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "VIP会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -getOrderInfo["totalAmount"] # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 7 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "原路退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                            
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["total"] == 1             
            assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
            assert r.json()["data"]["list"][0]["couponStatus"] == 3
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
  

@allure.title("普通顾客购货-银联支付-服务中心自提订单-完美运营后台代客售后")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/applyReturn")
def test_applyReturn_applySource_puk_1():
        
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getMemberAddressList = None # 获取当前登录用户的配送地址列表
    countOrderUpgrade = None # 统计用户待升级订单
    toSettlement = None # 选择商品去结算
    getPayMethod = None # 获取支付方式
    singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量
    token = os.environ["puk_token_2"]
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

    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }],
        }         
        with _mobile_order_carts_getFreightList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getFreightList = r.json()["data"][0]

    @allure.step("获取选中结算分组的可用和不可用优惠券列表")
    def step_mobile_order_carts_getCouponList():
                    
        nonlocal getCouponList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }         
        with _mobile_order_carts_getCouponList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["availableList"]:
                getCouponList = r.json()["data"]["availableList"][0]

    @allure.step("获取购物秒返券券列表")
    def step_mobile_order_carts_getSecondList():
                    
        nonlocal getSecondList
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"]:
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [{
                "activityPrice": productList["retailPrice"],
                "imgUrl": productList["imgUrl"],
                "isActivateItem": productList["isActivateItem"],
                "isActivity": "",
                "number": number,
                "productType": productList["productType"],
                "pv": productList["pv"],
                "quantity": 1,
                "releList": [],
                "retailPrice": productList["retailPrice"],
                "serialNo": productList["serialNo"],
                "title": productList["title"]
            }]
        }        
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            data["secondCouponList"].append({"secondCouponId": getSecondList})
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
            "isUpgrade": 0 if countOrderUpgrade != 1 else 1 # 是否升级单 0->否 1->是
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

    @allure.title("获取支付方式")    
    def step_mobile_payment_getPayMethod():

        nonlocal getPayMethod
        data = {
            "orderNoList":[orderCommit["orderNo"]], # 订单号集合
            "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
            "sourceType": toSettlement["sourceType"] # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
        }
        with _mobile_payment_getPayMethod(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getPayMethod =  r.json()["data"]
      
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
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_orderInfo_countOrderUpgrade()
    step_mobile_trade_orderCommit()
    step_mobile_payment_getPayMethod()
    step_mobile_payment_singlePay()
    step_pay_notify_mockPaySuccess()
    step_mobile_orderInfo_getOrderInfo()
     
    # 退货
    getAllReturnReasonByType = None # 退货/退款原因列表
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
        
    @allure.step("计算订单退款金额")    
    def step_mgmt_order_return_calcRefundAmount():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
        }
        with _mgmt_order_return_calcRefundAmount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == getOrderInfo["totalAmount"]

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

    @allure.step("升级单校验") 
    def step_mgmt_order_return_upgradeOrderVerify():
            
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "applySource": 0, # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        }
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["resultType"] == 0

    @allure.step("申请退货") 
    def step_mgmt_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
            "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
            "reason1Remark": "我是退货一级原因备注信息哦", # 退货一级原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
            "reason2Remark": "我是退货二级原因备注信息哦", # 退货二级原因备注
            "applySource": "0" # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
        }
        with _mgmt_order_return_applyReturn(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]

    @allure.step("统计待审核退货单") 
    def step_mgmt_order_return_countWaitAudit():
        
        params = {
            "applySource": None, # 申请来源 1->顾客申请 2->公司申请
            "companyCode": "", # 分公司编号
            "companyName": "", # 分公司名称
            "creatorCard": "", # 开单人卡号
            "customerCard": "", # 顾客卡号
            "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
            "returnNo": "", # 退货单号
            "orderNo": getOrderInfo["orderNo"],
            "returnType": None, # 退货类型 1->当月退货 2->隔月退货
            "storeCode": "", # 服务中心编号
            "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
            "currentPage": 1,
            "pageSize": 10,
            "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
            "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
        }
        with _mgmt_order_return_countWaitAudit(params, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 0

    @allure.step("新增/修改留言") 
    def step_mgmt_order_return_saveComment():
        
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment":"我同意这个代客售后申请", # 留言内容
            "id":"" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
                 
    @allure.step("退货详情") 
    def step_mgmt_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
    
    step_mgmt_order_return_calcRefundAmount() # 退货退款
    step_sys_api_getAllReturnReasonByType()
    step_mgmt_order_return_upgradeOrderVerify()              
    step_mgmt_order_return_applyReturn()
    step_mgmt_order_return_countWaitAudit()
    step_mgmt_order_return_saveComment()
    step_mgmt_order_return_upgradeOrderVerify()
    step_mgmt_order_return_auditOrderReturn()
    step_mgmt_order_return_getOrderReturnDetails()
    step_mobile_orderInfo_getOrderInfo()
    
    # 完美钱包详情
    
    walletId = None # 完美钱包管理-列表:获取钱包id
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": None, # 会员卡号
            "mobile": getOrderInfo["creatorPhone"], # 顾客手机号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    @allure.step("完美钱包详情表-退款")
    def step_02_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 5, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        }   
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 7 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "原路退款" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 7 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退款" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == -getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "银联" # 支付方式
    
    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()
    step_02_mgmt_fin_wallet_getTransDetail() 
     
    # 分公司银行流水
    @allure.step("查询分公司银行流水")
    def step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans():
        
        data = {
            "transTime": time.strftime('%Y-%m',time.localtime(time.time())), # # 月份
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号不能为空
            "timerange":[time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time()))],
            "cardNo":"", # 会员卡号
            "mobile": getOrderInfo["creatorPhone"], # 普客手机号
            "memberTypeList":[], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
            "transType": 7, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            "autoType": 1, # 自动/手工，参数说明 1：自动；2：手工
            "pageNum": 1,
            "pageSize": 10,
            "startTime": time.strftime('%Y-%m-%d 00:00:00',time.localtime(time.time())), # 到账开始时间
            "endTime": time.strftime('%Y-%m-%d 23:59:59',time.localtime(time.time())) # 到账结束时间
        }
        with _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data, access_token) as r:
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transNo"].startswith(f"BI{time.strftime('%Y%m%d',time.localtime(time.time()))}") # 交易流水号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["mobile"] == getOrderInfo["creatorPhone"] # 普客手机号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["cardNo"] == "" # 会员卡号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["realname"] == getOrderInfo["creatorName"] # 顾客姓名
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberType"] == getOrderInfo["creatorType"] # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["memberTypeDesc"] == "会员" # 顾客类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transAmount"] == -getOrderInfo["totalAmount"] # 转账金额
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transType"] == 7 # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["transTypeDesc"] == "原路退款" # 账款类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["payTimeDesc"][:10] == time.strftime('%Y-%m-%d',time.localtime(time.time())) # 到账时间
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankAccount"] is None # 银行账号
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeCode"] == "BCM" # 银行类型
            assert r.json()["data"]["billTransDtlPage"]["list"][0]["bankTypeName"] == "交通银行" # 银行类型名称
                            
    step_mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - productList["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()


@allure.title("完美运营后台代客售后-13隔月退货")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/applyReturn")
@pytest.mark.skipif(getBaseMonthlyReportData() != 16, reason="16日之前（不含16日），则是当月退货，不执行")
def test_applyReturn_applySource_returnType_SG():
        
    orderList = None # 订单列表
    getOrderInfo = None # 订单信息
    getAllReturnReasonByType = None # 退货/退款原因列表
    applyReturn = None # 退货单号
    getOrderReturnDetails = None # 获取退货详情
    access_token = os.environ["access_token_2"]

    @allure.step("订单列表")    
    def step_mgmt_order_orderList():

        nonlocal orderList
        params = {
            "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
            "customerType": 3, # 顾客类型 1->普通顾客 2->优惠顾客 3->微店 4->云商
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "stockType": None, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
            "isUpgrade": 0, # 是否升级单
            "pageNum": 1,
            "pageSize": 10,
            "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
            "commitStartTime": f'{(datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")}-01',
            "commitEndTime": f'{(datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")}-28',
        }
        with _mgmt_order_orderList(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderList = r.json()["data"]["list"][0]

    @allure.step("申请售后是否支持退货、换货")    
    def step_mgmt_order_as_applyAfterSale():

        params = {
            "orderNo": orderList["orderNo"]
        }
        with _mgmt_order_as_applyAfterSale(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["expressType"] == 1 # 配送方式 1->服务中心自提 2->公司配送
            assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
            assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
            assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
            assert r.json()["data"]["returnType"] == 2 # 退货类型 1->当月退货 2->隔月退货

    @allure.step("订单信息")    
    def step_mgmt_order_orderInfo():

        nonlocal getOrderInfo
        params = {
            "orderNo": orderList["orderNo"]
        }
        with _mgmt_order_orderInfo(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderInfo = r.json()["data"]
        
    @allure.step("计算订单退款金额")    
    def step_mgmt_order_return_calcRefundAmount():

        params = {
            "orderNo": getOrderInfo["orderNo"] # 订单号
        }
        with _mgmt_order_return_calcRefundAmount(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == getOrderInfo["totalAmount"]

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

    @allure.step("升级单校验") 
    def step_mgmt_order_return_upgradeOrderVerify():
            
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "applySource": 0, # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        }
        with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("申请退货") 
    def step_mgmt_order_return_applyReturn():
        
        nonlocal applyReturn
        data = {
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
            "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
            "reason1Remark": "我是退货一级原因备注信息哦", # 退货一级原因备注
            "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
            "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
            "reason2Remark": "我是退货二级原因备注信息哦", # 退货二级原因备注
            "applySource": "0" # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
        }
        with _mgmt_order_return_applyReturn(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            applyReturn = r.json()["data"]

    @allure.step("统计待审核退货单") 
    def step_mgmt_order_return_countWaitAudit():
        
        params = {
            "applySource": None, # 申请来源 1->顾客申请 2->公司申请
            "companyCode": "", # 分公司编号
            "companyName": "", # 分公司名称
            "creatorCard": "", # 开单人卡号
            "customerCard": "", # 顾客卡号
            "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
            "returnNo": "", # 退货单号
            "orderNo": getOrderInfo["orderNo"],
            "returnType": None, # 退货类型 1->当月退货 2->隔月退货
            "storeCode": "", # 服务中心编号
            "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
            "currentPage": 1,
            "pageSize": 10,
            "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
            "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
        }
        with _mgmt_order_return_countWaitAudit(params, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == 0

    @allure.step("新增/修改留言") 
    def step_mgmt_order_return_saveComment():
        
        data = {
            "serviceNo": applyReturn, # 退货/换货单号
            "comment":"我同意这个代客售后申请", # 留言内容
            "id":"" # 留言id
        }
        with _mgmt_order_return_saveComment(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
                 
    @allure.step("退货详情") 
    def step_mgmt_order_return_getOrderReturnDetails():
            
        nonlocal getOrderReturnDetails
        params = {
            "returnNo": applyReturn, # 退货单号
        }
        with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getOrderReturnDetails = r.json()["data"]
    
    step_mgmt_order_orderList()
    step_mgmt_order_as_applyAfterSale()
    step_mgmt_order_orderInfo()
    step_mgmt_order_return_calcRefundAmount() # 退货退款
    step_sys_api_getAllReturnReasonByType()
    step_mgmt_order_return_upgradeOrderVerify()              
    step_mgmt_order_return_applyReturn()
    step_mgmt_order_return_countWaitAudit()
    step_mgmt_order_return_saveComment()
    step_mgmt_order_return_upgradeOrderVerify()
    step_mgmt_order_return_auditOrderReturn()
    step_mgmt_order_return_getOrderReturnDetails()
    step_mgmt_order_orderInfo()
    
    # 完美钱包详情
    
    walletId = None # 完美钱包管理-列表:获取钱包id
    
    @allure.step("完美钱包管理-列表:获取钱包id")
    def test_mgmt_fin_wallet_getList():
    
        nonlocal walletId
        data = {
            "storeCode": None,
            "cardNo": getOrderInfo["creatorCard"], # 会员卡号
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
            if r.json()["data"]["list"]:
                walletId = r.json()["data"]["list"][0]["walletId"]
    
    @allure.step("完美钱包详情表-退货")
    @stepreruns(times=30)
    def step_01_mgmt_fin_wallet_getTransDetail():
        
        data = {
            "walletId": walletId, # 钱包id
            "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
            "receptionTransType": 2, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
            "orderNo": getOrderInfo["orderNo"], # 订单编号
            "creditEnable":None, # 是否有信用额
            "pageNum":1,
            "pageSize":10,
            "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
            "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
        } 
        with _mgmt_fin_wallet_getTransDetail(data, access_token) as r:
            assert r.json()["data"]["page"]["list"][0]["backstageTransType"] == 3 # 后端交易类型
            assert r.json()["data"]["page"]["list"][0]["backstageTransTypeDesc"] == "退货转入" # 后端交易类型 1:充值 2:购货转入 3:退货转入 6:提现 7:原路退款 8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12:押货款与钱包互转 13:其他 14:信用额增加 15:信用额扣减
            assert r.json()["data"]["page"]["list"][0]["bankAccount"] is None # 银行卡号
            assert r.json()["data"]["page"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 公司编码
            assert r.json()["data"]["page"]["list"][0]["orderNo"] == getOrderInfo["orderNo"] # 订单号-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["orderNoList"] == [{"orderNo": getOrderInfo["orderNo"], "orderPableAmt": getOrderInfo["totalAmount"]}] # 订单对象-批量的订单可能有多个
            assert r.json()["data"]["page"]["list"][0]["receptionTransType"] == 3 # 前端交易类型
            assert r.json()["data"]["page"]["list"][0]["receptionTransTypeDesc"] == "退货" # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
            assert r.json()["data"]["page"]["list"][0]["transAmt"] == getOrderReturnDetails["orderReturn"]["refundAmount"] # 交易金额
            assert r.json()["data"]["page"]["list"][0]["transMethod"] == "完美钱包" # 支付方式

    test_mgmt_fin_wallet_getList()
    step_01_mgmt_fin_wallet_getTransDetail()

    # 库存产品增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_inventory_detail():
        
        params = {
            "outIn": None, # 出入库：1入库 2出库
            "source": None, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            "monthTime": None, # 月份，格式为：yyyyMM
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "productCode": getOrderReturnDetails["orderReturnProducts"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_inventory_detail(params, access_token) as r:
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 日期
            assert r.json()["data"]["page"]["list"][0]["source"] == 4 # 类型 1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单
            assert r.json()["data"]["page"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 单号
            assert r.json()["data"]["page"]["list"][0]["outIn"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存增减
            assert r.json()["data"]["page"]["list"][0]["productNum"] == r.json()["data"]["page"]["list"][1]["productNum"] + getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 库存结余
    
    step_mgmt_inventory_detail()

    # 押货余额详情表
    @allure.step("服务中心账款管理 -- 押货余额详情(详情分页列表)")
    def step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList():
        
        data = {
            "storeCode": getOrderReturnDetails["orderReturn"]["storeCode"], # 服务中心编号
            "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
            "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
            "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
            "bizNo": getOrderReturnDetails["orderReturn"]["returnNo"], # 业务单号
            "pageNum":1,
            "pageSize":10,
            "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
            "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
        }
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["tenType"] == 18  # 交易类型
            assert r.json()["data"]["list"][0]["sevenBankTypeName"] == "无" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == - getOrderReturnDetails["orderReturnProducts"][0]["securityPrice"] * getOrderReturnDetails["orderReturnProducts"][0]["quantity"] # 增减额度
            assert r.json()["data"]["list"][0]["businessId"] == getOrderReturnDetails["orderReturn"]["returnNo"] # 对应单号或流水号
    
    step_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList()

    # 购物礼券获券明细
    @allure.step("秒返券获券明细")
    def step_mgmt_fin_voucher_getSecondCouponGetDetail():
        
        data = {
            "cardNo": "", # 会员卡号
            "memberType": None, # 顾客类型
            "sourceOrderNo": getOrderInfo["orderNo"], # 来源订单号
            "getType": None, # 交易类型，1：购物获得；2：月结更新
            "sourceStoreCode": None, # 服务中心编号
            "couponStatus": None, # 券状态
            "pageNum": 1,
            "pageSize": 10,
            "getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss 当月第一天
            "getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss，当月最后一天
            "transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
            "transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
        }
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, access_token) as r:  
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                assert r.json()["data"]["total"] == 1             
                assert r.json()["data"]["list"][0]["cardNo"] == getOrderInfo["customerCard"]
                assert r.json()["data"]["list"][0]["couponStatus"] == 3
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "退货失效"
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderStatusChangeVOList"][1]["createTime"])/1000))
                assert r.json()["data"]["list"][0]["getType"] == 1
                assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
                assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
                assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
                assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
                assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
                assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
                assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
        
    step_mgmt_fin_voucher_getSecondCouponGetDetail()

