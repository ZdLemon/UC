# coding:utf-8

from api.mall_mobile_application._mobile_product_discount_productList import _mobile_product_discount_productList # 查询85折转分商品
from api.mall_mobile_application._mobile_order_before_by_cardNo import _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口

from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息
from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息

from api.mall_mgmt_application._mgmt_product_item_listVersion import _mgmt_product_item_listVersion # 产品版本列表
from api.mall_mobile_application._mobile_product_discount_beforeSettlementProductList import _mobile_product_discount_beforeSettlementProductList # 查询85折转分商品--结算前销售调整

from api.mall_mgmt_application._mgmt_dis_inventory_detail import _mgmt_dis_inventory_detail # 查询库存明细
from api.mall_mgmt_application._mgmt_order_getOrderSettlementDetail import _mgmt_order_getOrderSettlementDetail # 交付结算详情
from api.mall_mgmt_application._mgmt_fin_voucher_getSecondCouponGetDetail import _mgmt_fin_voucher_getSecondCouponGetDetail # 秒返券获券明细
from api.mall_mgmt_application._mgmt_inventory_transferOrder_pageList import _mgmt_inventory_transferOrder_pageList # 分页列表-85折转分分公司流水

from setting import productCode_SecondCoupon
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

# 转分订单-（自购，代购）
# 转分结算前调整订单-（自购，代购）

# 85折转分订单,85折转分结算前调整订单

@allure.title("85云商自购-转分订单")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/trade/orderCommit")
def test_orderCommit_yunsh_1_85(yunsh_login_ICBC_85):
    "85折转分订单自购"
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    token = os.environ["token_85"]
    access_token = os.environ["access_token_2"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("根据用户卡号查询是否可购买商品")
    def step_mobile_order_before_by_cardNo():
        
        nonlocal before_by_cardNo
        params = {
            "cardNo": getCurrentUserInfo["cardNo"], # 顾客卡号
        } 
        with _mobile_order_before_by_cardNo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
            
    @allure.step("查询85折转分商品")
    def step_mobile_product_discount_productList():
        
        nonlocal productList
        data = {
            "isDesc": 1, # 是否降序 1-是 0-否,默认为1
            "isProductNum": 1, # 只看有库存 1-是
            "isSelected": 1, # 只看已选 1-是(已选列表必传)
            "keyword": "", # 关键字
            "pageNum": 1,
            "pageSize": 10,
            "selectedList": [{ # 已选商品列表
                "serialNo": productCode_SecondCoupon, # 商品编码
                "selectNums": number # 数量
            }],
            "serialNo": None, # 商品编码
            "showId": "", # 分类id
            "sortBy": 0 # 0-库存，1-商品编码，2-单价与pv，3-数量(已选商品列表必传)，4-金额小计(已选商品列表必传),默认为0
        }                  
        with _mobile_product_discount_productList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode_SecondCoupon:
                    productList = d

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "sourceType": 8 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]
    
    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
            }]
        }        
        with _mobile_order_carts_getSecondList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                for d in r.json()["data"]:
                    if d["isUsed"] == 1 and (d["sourceStoreCode"] == getCurrentUserInfo["leaderStoreCode"] or d["sourceStoreCode"] is None):
                        getSecondList = d["secondCouponId"]
    
    @allure.step("获取电子礼券列表")
    def step_mobile_order_carts_getGiftList_2():
        
        nonlocal getGiftList_2
        data = {
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
        }         
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

    @allure.step("选择商品去结算")
    def step_03_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": None,
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.step("提交订单")
    def step_mobile_trade_orderCommit():
                    
        nonlocal orderCommit
        data = {
            "addressId": None,
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
            }],
            "isUpgrade": 0, # 是否升级单 0->否 1->是
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
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]
 
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
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_productList() 
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()    
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_wallet_getDetail()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    # 交付结算详情表
    orderPrice = None # 押货价
    
    @allure.step("商品版本列表:获取押货价")
    def step_mgmt_product_item_listVersion():

        nonlocal orderPrice
        data = {
        "versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        "pageNum": 1,
        "pageSize": 10,
        "serialNo": getOrderInfo["orderProductVOList"][0]["serialNo"], # 商品编码
        "title": None, # 商品名称
        "catalogId": None, # 类型id
        "saleCompanyId": None, # 销售主体id
        "orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
        "directSale": None, # 是否直销，1-是，0-否
        "orderWay": None, # 下单方式 1-自购,2-代购
        "deliverWay": None, # 交付方式 1-公司交付,2-门店交付
        "startTime": "", # 开始时间时间戳
        "endTime": "" # 结束时间时间戳
    }
        with _mgmt_product_item_listVersion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if d["serialNo"] == getOrderInfo["orderProductVOList"][0]["serialNo"]:
                        orderPrice = d["orderPrice"]
                        break

    @allure.step(" 交付结算列表: 转分订单流水检查")
    def step_mgmt_order_getOrderSettlementDetail():
            
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time())), # 业绩月份202204
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "orderNo": getOrderInfo["orderNo"], # 订单编号/售后单号
            "orderType": 1, # 订单类型 1->商城报单 2->商城退单
            "isDifference": None, # 交付差额是否为负 0->否 1->是
            "tradingStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # 交易开始时间2022-04-01
            "tradingEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # 交易结束时间
            "pageNum": 1,
            "pageSize": 10
        }           
        with _mgmt_order_getOrderSettlementDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["orderNo"] == getOrderInfo["orderNo"]  # 订单号/售后单号
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 订单类型
            assert r.json()["data"]["list"][0]["orderTypeDesc"] == "商城报单" # 订单类型
            assert r.json()["data"]["list"][0]["retailPrice"] == getOrderInfo["orderAmount"] # 零售价金额
            assert r.json()["data"]["list"][0]["securityAmount"] == float(orderPrice) * int(getOrderInfo["orderProductVOList"][0]["quantity"]) # 押货价金额
            assert r.json()["data"]["list"][0]["retailPrice"] - r.json()["data"]["list"][0]["securityAmount"] == r.json()["data"]["list"][0]["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
            assert r.json()["data"]["list"][0]["orderAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secCouponAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["giftCouponAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["expressSubsidyAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionDiscount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["totalAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["orderAmount"] - r.json()["data"]["list"][0]["totalAmount"] == r.json()["data"]["list"][0]["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
            assert r.json()["data"]["list"][0]["receiveAmount"] - r.json()["data"]["list"][0]["payDifference"] == r.json()["data"]["list"][0]["difAmount"] # 店应收回款 - 店应补差额 = 交付差额
        
    step_mgmt_product_item_listVersion()
    step_mgmt_order_getOrderSettlementDetail()

    # 85折转分分公司流水
    @allure.step("分页列表-85折转分分公司流水")
    def step_mgmt_inventory_transferOrder_pageList():
                
        data = {
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号
            "customerCardNo": getOrderInfo["customerCard"], # 会员卡号
            "openOrderCardNo": getOrderInfo["creatorCard"], # 开单人卡号
            "storeCode": None, # 服务中心编号
            "openOrderManType": None, # 开单人类型 3->云商 4->微店
            "orderType": None, # 账款类型 1->报单 ，2->退单
            "month": time.strftime("%Y%m",time.localtime(time.time())), # 月份(yyyyMM)
            "pageNum": 1,
            "pageSize": 10,
            "verifyStartDay": "", # 审核开始时间(yyyy-MM-dd)
            "verifyEndDay": "" # 审核结束时间(yyyy-MM-dd)
        }            
        with _mgmt_inventory_transferOrder_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["list"][0]["storeCode"] == getOrderInfo["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == getOrderInfo["creatorCard"] # 开单人卡号           
            assert r.json()["data"]["list"][0]["openOrderManType"] == getOrderInfo["creatorType"] # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == getOrderInfo["creatorName"] # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == getOrderInfo["customerCard"] # 会员卡号
            assert r.json()["data"]["list"][0]["customerName"] == getOrderInfo["customerName"] # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == getOrderInfo["customerType"] # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ,2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 使用购物礼券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["verifyTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
            assert r.json()["data"]["list"][0]["storeName"] == getOrderInfo["storeName"] # 服务中心名称
    
    step_mgmt_inventory_transferOrder_pageList()
    
    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_dis_inventory_detail():
                
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 3, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 3 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -getOrderInfo["orderProductVOList"][0]["quantity"] # 交付数量
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    step_mgmt_dis_inventory_detail()

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
            assert r.json()["data"]["list"][0]["couponStatus"] == 1
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "待生效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderCompleteTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("85云商代购-转分订单")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/trade/orderCommit")
def test_orderCommit_yunsh_2_85(yunsh_login_ICBC_85, vip_login_2):
    "85折转分订单自购"
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    token = os.environ["token_85"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("根据用户卡号查询是否可购买商品")
    def step_mobile_order_before_by_cardNo():
        
        nonlocal before_by_cardNo
        params = {
            "cardNo": user["cardNo"], # 顾客卡号
        } 
        with _mobile_order_before_by_cardNo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
            
    @allure.step("查询85折转分商品")
    def step_mobile_product_discount_productList():
        
        nonlocal productList
        data = {
            "isDesc": 1, # 是否降序 1-是 0-否,默认为1
            "isProductNum": 1, # 只看有库存 1-是
            "isSelected": 1, # 只看已选 1-是(已选列表必传)
            "keyword": "", # 关键字
            "pageNum": 1,
            "pageSize": 10,
            "selectedList": [{ # 已选商品列表
                "serialNo": productCode_SecondCoupon, # 商品编码
                "selectNums": number # 数量
            }],
            "serialNo": None, # 商品编码
            "showId": "", # 分类id
            "sortBy": 0 # 0-库存，1-商品编码，2-单价与pv，3-数量(已选商品列表必传)，4-金额小计(已选商品列表必传),默认为0
        }                  
        with _mobile_product_discount_productList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode_SecondCoupon:
                    productList = d

    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "sourceType": 8 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]
    
    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
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
    def step_03_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": None,
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.step("提交订单")
    def step_mobile_trade_orderCommit():
                    
        nonlocal orderCommit
        data = {
            "addressId": None,
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
            }],
            "isUpgrade": 0, # 是否升级单 0->否 1->是
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
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]
 
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
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_productList() 
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()    
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_wallet_getDetail()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    # 交付结算详情表
    orderPrice = None # 押货价
    
    @allure.step("商品版本列表:获取押货价")
    def step_mgmt_product_item_listVersion():

        nonlocal orderPrice
        data = {
        "versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        "pageNum": 1,
        "pageSize": 10,
        "serialNo": getOrderInfo["orderProductVOList"][0]["serialNo"], # 商品编码
        "title": None, # 商品名称
        "catalogId": None, # 类型id
        "saleCompanyId": None, # 销售主体id
        "orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
        "directSale": None, # 是否直销，1-是，0-否
        "orderWay": None, # 下单方式 1-自购,2-代购
        "deliverWay": None, # 交付方式 1-公司交付,2-门店交付
        "startTime": "", # 开始时间时间戳
        "endTime": "" # 结束时间时间戳
    }
        with _mgmt_product_item_listVersion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if d["serialNo"] == getOrderInfo["orderProductVOList"][0]["serialNo"]:
                        orderPrice = d["orderPrice"]
                        break

    @allure.step(" 交付结算列表: 转分订单流水检查")
    def step_mgmt_order_getOrderSettlementDetail():
            
        params = {
            "orderMonth": time.strftime("%Y%m",time.localtime(time.time())), # 业绩月份202204
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "orderNo": getOrderInfo["orderNo"], # 订单编号/售后单号
            "orderType": 1, # 订单类型 1->商城报单 2->商城退单
            "isDifference": None, # 交付差额是否为负 0->否 1->是
            "tradingStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # 交易开始时间2022-04-01
            "tradingEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # 交易结束时间
            "pageNum": 1,
            "pageSize": 10
        }           
        with _mgmt_order_getOrderSettlementDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["orderNo"] == getOrderInfo["orderNo"]  # 订单号/售后单号
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 订单类型
            assert r.json()["data"]["list"][0]["orderTypeDesc"] == "商城报单" # 订单类型
            assert r.json()["data"]["list"][0]["retailPrice"] == getOrderInfo["orderAmount"] # 零售价金额
            assert r.json()["data"]["list"][0]["securityAmount"] == float(orderPrice) * int(getOrderInfo["orderProductVOList"][0]["quantity"]) # 押货价金额
            assert r.json()["data"]["list"][0]["retailPrice"] - r.json()["data"]["list"][0]["securityAmount"] == r.json()["data"]["list"][0]["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
            assert r.json()["data"]["list"][0]["orderAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secCouponAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["giftCouponAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["expressSubsidyAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionDiscount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["totalAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["orderAmount"] - r.json()["data"]["list"][0]["totalAmount"] == r.json()["data"]["list"][0]["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
            assert r.json()["data"]["list"][0]["receiveAmount"] - r.json()["data"]["list"][0]["payDifference"] == r.json()["data"]["list"][0]["difAmount"] # 店应收回款 - 店应补差额 = 交付差额
        
    step_mgmt_product_item_listVersion()
    step_mgmt_order_getOrderSettlementDetail()

    # 85折转分分公司流水
    @allure.step("分页列表-85折转分分公司流水")
    def step_mgmt_inventory_transferOrder_pageList():
                
        data = {
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号
            "customerCardNo": getOrderInfo["customerCard"], # 会员卡号
            "openOrderCardNo": getOrderInfo["creatorCard"], # 开单人卡号
            "storeCode": None, # 服务中心编号
            "openOrderManType": None, # 开单人类型 3->云商 4->微店
            "orderType": None, # 账款类型 1->报单 ，2->退单
            "month": time.strftime("%Y%m",time.localtime(time.time())), # 月份(yyyyMM)
            "pageNum": 1,
            "pageSize": 10,
            "verifyStartDay": "", # 审核开始时间(yyyy-MM-dd)
            "verifyEndDay": "" # 审核结束时间(yyyy-MM-dd)
        }            
        with _mgmt_inventory_transferOrder_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["list"][0]["storeCode"] == getOrderInfo["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == getOrderInfo["creatorCard"] # 开单人卡号           
            assert r.json()["data"]["list"][0]["openOrderManType"] == getOrderInfo["creatorType"] # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == getOrderInfo["creatorName"] # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == getOrderInfo["customerCard"] # 会员卡号
            assert r.json()["data"]["list"][0]["customerName"] == getOrderInfo["customerName"] # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == getOrderInfo["customerType"] # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ,2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 使用购物礼券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["verifyTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
            assert r.json()["data"]["list"][0]["storeName"] == getOrderInfo["storeName"] # 服务中心名称
    
    step_mgmt_inventory_transferOrder_pageList()
        
    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_dis_inventory_detail():
                
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 3, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 3 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -getOrderInfo["orderProductVOList"][0]["quantity"] # 交付数量
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    step_mgmt_dis_inventory_detail()

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
            assert r.json()["data"]["list"][0]["couponStatus"] == 1
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "待生效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderCompleteTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail() 


@allure.title("85云商自购-转分结算前调整订单")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/trade/orderCommit")
@pytest.mark.skipif(getBaseMonthlyReportData() != 3, reason="如果不在公开补报时间内,不执行")
def test_orderCommit_yunsh_1_85_BB(yunsh_login_ICBC_85):
    "85折转分订单自购"
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    token = os.environ["token_85"]
    access_token = os.environ["access_token_2"]

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("根据用户卡号查询是否可购买商品")
    def step_mobile_order_before_by_cardNo():
        
        nonlocal before_by_cardNo
        params = {
            "cardNo": getCurrentUserInfo["cardNo"], # 顾客卡号
        } 
        with _mobile_order_before_by_cardNo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]

    @allure.step("查询85折转分商品--结算前销售调整")
    def step_mobile_product_discount_beforeSettlementProductList():
        
        nonlocal productList
        data = {
            "isDesc": 1, # 是否降序 1-是 0-否,默认为1
            "isProductNum": 1, # 只看有库存 1-是
            "isSelected": 1, # 只看已选 1-是(已选列表必传)
            "keyword": "", # 关键字
            "pageNum": 1,
            "pageSize": 10,
            "selectedList": [{ # 已选商品列表
                "serialNo": productCode_SecondCoupon, # 商品编码
                "selectNums": number # 数量
            }],
            "serialNo": None, # 商品编码
            "showId": "", # 分类id
            "sortBy": 0 # 0-库存，1-商品编码，2-单价与pv，3-数量(已选商品列表必传)，4-金额小计(已选商品列表必传),默认为0
        }                  
        with _mobile_product_discount_beforeSettlementProductList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode_SecondCoupon:
                    productList = d
            
    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "sourceType": 9 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]
    
    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
        }         
        with _mobile_order_carts_getGiftList_2(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]:
                getGiftList_2 = r.json()["data"][0]

    @allure.step("选择商品去结算")
    def step_03_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": None,
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.step("提交订单")
    def step_mobile_trade_orderCommit():
                    
        nonlocal orderCommit
        data = {
            "addressId": None,
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
            }],
            "isUpgrade": 0, # 是否升级单 0->否 1->是
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
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]
 
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
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_beforeSettlementProductList()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()    
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_wallet_getDetail()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    # 交付结算详情表
    orderPrice = None # 押货价
    
    @allure.step("商品版本列表:获取押货价")
    def step_mgmt_product_item_listVersion():

        nonlocal orderPrice
        data = {
        "versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        "pageNum": 1,
        "pageSize": 10,
        "serialNo": getOrderInfo["orderProductVOList"][0]["serialNo"], # 商品编码
        "title": None, # 商品名称
        "catalogId": None, # 类型id
        "saleCompanyId": None, # 销售主体id
        "orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
        "directSale": None, # 是否直销，1-是，0-否
        "orderWay": None, # 下单方式 1-自购,2-代购
        "deliverWay": None, # 交付方式 1-公司交付,2-门店交付
        "startTime": "", # 开始时间时间戳
        "endTime": "" # 结束时间时间戳
    }
        with _mgmt_product_item_listVersion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if d["serialNo"] == getOrderInfo["orderProductVOList"][0]["serialNo"]:
                        orderPrice = d["orderPrice"]
                        break

    @allure.step(" 交付结算列表: 转分订单流水检查")
    def step_mgmt_order_getOrderSettlementDetail():
            
        params = {
            "orderMonth": datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y%m"), # 上一个月，业绩月份202204
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "orderNo": getOrderInfo["orderNo"], # 订单编号/售后单号
            "orderType": 1, # 订单类型 1->商城报单 2->商城退单
            "isDifference": None, # 交付差额是否为负 0->否 1->是
            "tradingStartTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-01', # 上一个月第一天，交易开始时间2022-04-01
            "tradingEndTime": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 当天
            "pageNum": 1,
            "pageSize": 10
        }           
        with _mgmt_order_getOrderSettlementDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["orderNo"] == getOrderInfo["orderNo"]  # 订单号/售后单号
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 订单类型
            assert r.json()["data"]["list"][0]["orderTypeDesc"] == "商城报单" # 订单类型
            assert r.json()["data"]["list"][0]["retailPrice"] == getOrderInfo["orderAmount"] # 零售价金额
            assert r.json()["data"]["list"][0]["securityAmount"] == float(orderPrice) * int(getOrderInfo["orderProductVOList"][0]["quantity"]) # 押货价金额
            assert r.json()["data"]["list"][0]["retailPrice"] - r.json()["data"]["list"][0]["securityAmount"] == r.json()["data"]["list"][0]["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
            assert r.json()["data"]["list"][0]["orderAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secCouponAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["giftCouponAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["expressSubsidyAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionDiscount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["totalAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["orderAmount"] - r.json()["data"]["list"][0]["totalAmount"] == r.json()["data"]["list"][0]["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
            assert r.json()["data"]["list"][0]["receiveAmount"] - r.json()["data"]["list"][0]["payDifference"] == r.json()["data"]["list"][0]["difAmount"] # 店应收回款 - 店应补差额 = 交付差额
        
    step_mgmt_product_item_listVersion()
    step_mgmt_order_getOrderSettlementDetail()

    # 85折转分分公司流水
    @allure.step("分页列表-85折转分分公司流水")
    def step_mgmt_inventory_transferOrder_pageList():
                
        data = {
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号
            "customerCardNo": getOrderInfo["customerCard"], # 会员卡号
            "openOrderCardNo": getOrderInfo["creatorCard"], # 开单人卡号
            "storeCode": None, # 服务中心编号
            "openOrderManType": None, # 开单人类型 3->云商 4->微店
            "orderType": None, # 账款类型 1->报单 ，2->退单
            "month": time.strftime("%Y%m",time.localtime(time.time())), # 月份(yyyyMM)
            "pageNum": 1,
            "pageSize": 10,
            "verifyStartDay": "", # 审核开始时间(yyyy-MM-dd)
            "verifyEndDay": "" # 审核结束时间(yyyy-MM-dd)
        }            
        with _mgmt_inventory_transferOrder_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["list"][0]["storeCode"] == getOrderInfo["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == getOrderInfo["creatorCard"] # 开单人卡号           
            assert r.json()["data"]["list"][0]["openOrderManType"] == getOrderInfo["creatorType"] # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == getOrderInfo["creatorName"] # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == getOrderInfo["customerCard"] # 会员卡号
            assert r.json()["data"]["list"][0]["customerName"] == getOrderInfo["customerName"] # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == getOrderInfo["customerType"] # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ,2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 使用购物礼券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["verifyTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
            assert r.json()["data"]["list"][0]["storeName"] == getOrderInfo["storeName"] # 服务中心名称
    
    step_mgmt_inventory_transferOrder_pageList()
          
    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_dis_inventory_detail():
                
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 3, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y%m"), # 上个月份 202204月份，格式为：yyyyMM   
            "endMonth": (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y%m"), # 上个月份202204月份，格式为：yyyyMM
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 3 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -getOrderInfo["orderProductVOList"][0]["quantity"] # 交付数量
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    step_mgmt_dis_inventory_detail()

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
            assert r.json()["data"]["list"][0]["couponStatus"] == 1
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "待生效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderCompleteTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == None
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail()
    

@allure.title("85云商代购-转分结算前调整订单")
@allure.feature("mall_mobile_application")
@allure.story("/mobile/trade/orderCommit")
@pytest.mark.skipif(getBaseMonthlyReportData() != 3, reason="如果不在公开补报时间内,不执行")
def test_orderCommit_yunsh_2_85_BB(yunsh_login_ICBC_85, vip_login_2):
    "85折转分订单自购"
    
    before_by_cardNo = None # 用户信息
    productList = None # 商品详情
    getCurrentUserInfo = None # 个人用户信息
    getDetail = None # 获取钱包首页相关信息
    
    toSettlement = None # 选择商品去结算
    getFreightList = None # 运费补贴券
    getCouponList = None # 优惠券
    getSecondList = None # 秒返券
    getGiftList_2 = None # 电子礼券
    orderCommit = None # 订单信息
    getOrderInfo = None # 详细订单信息
    number = 10 # 购买商品数量

    token = os.environ["token_85"]
    access_token = os.environ["access_token_2"]
    user = vip_login_2["data"] # 给某个顾客下单的信息（非下单人）

    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("根据用户卡号查询是否可购买商品")
    def step_mobile_order_before_by_cardNo():
        
        nonlocal before_by_cardNo
        params = {
            "cardNo": user["cardNo"], # 顾客卡号
        } 
        with _mobile_order_before_by_cardNo(params, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            before_by_cardNo = r.json()["data"]
            
    @allure.step("查询85折转分商品--结算前销售调整")
    def step_mobile_product_discount_beforeSettlementProductList():
        
        nonlocal productList
        data = {
            "isDesc": 1, # 是否降序 1-是 0-否,默认为1
            "isProductNum": 1, # 只看有库存 1-是
            "isSelected": 1, # 只看已选 1-是(已选列表必传)
            "keyword": "", # 关键字
            "pageNum": 1,
            "pageSize": 10,
            "selectedList": [{ # 已选商品列表
                "serialNo": productCode_SecondCoupon, # 商品编码
                "selectNums": number # 数量
            }],
            "serialNo": None, # 商品编码
            "showId": "", # 分类id
            "sortBy": 0 # 0-库存，1-商品编码，2-单价与pv，3-数量(已选商品列表必传)，4-金额小计(已选商品列表必传),默认为0
        }                  
        with _mobile_product_discount_beforeSettlementProductList(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["serialNo"] == productCode_SecondCoupon:
                    productList = d
        
    @allure.step("选择商品去结算")
    def step_01_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
            "customerId":  user["userId"], # 给某个顾客下单的会员ID
            "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
            "productList": [{
                "serialNo": productList["serialNo"],
                "number": number,
                "retailPrice": productList["retailPrice"],
                "pv": productList["pv"],
                "imgUrl": productList["imgUrl"],
                "title": productList["title"]
            }],
            "sourceType": 9 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
        with _mobile_order_carts_toSettlement(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            toSettlement = r.json()["data"]
    
    @allure.step("获取运费补贴券列表")
    def step_mobile_order_carts_getFreightList():
        
        nonlocal getFreightList
        data = {
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "storeCode": toSettlement["checkoutVO"]["storeCode"], # 服务中心编码
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "sourceType": toSettlement["sourceType"], # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            "productList": [toSettlement["productList"][0]],
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
    def step_03_mobile_order_carts_toSettlement():
                    
        nonlocal toSettlement
        data = {
            "addressId": None,
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
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

    @allure.title("获取钱包首页相关信息")         
    def step_mobile_wallet_getDetail():
        
        nonlocal getDetail
        with _mobile_wallet_getDetail(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getDetail = r.json()["data"]

    @allure.step("提交订单")
    def step_mobile_trade_orderCommit():
                    
        nonlocal orderCommit
        data = {
            "addressId": None,
            "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
            "customerCard": toSettlement["customerCard"], # 给某个顾客下单的会员卡号
            "customerId":  toSettlement["customerMemberId"], # 给某个顾客下单的会员ID
            "expressType": toSettlement["expressType"], # 配送方式 1->服务中心自提 2->公司配送
            "orderAmount": toSettlement["price"]["productPrice"], # 商品金额,提交订单时必传(零售价*数量)
            "productList": [{
                "serialNo": toSettlement["productList"][0]["serialNo"],
                "number": toSettlement["productList"][0]["quantity"],
                "retailPrice": toSettlement["productList"][0]["retailPrice"],
                "pv": toSettlement["productList"][0]["pv"],
                "imgUrl": toSettlement["productList"][0]["picture"],
                "title": toSettlement["productList"][0]["title"]
            }],
            "isUpgrade": 0, # 是否升级单 0->否 1->是
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
        with _mobile_trade_orderCommit(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderCommit = r.json()["data"]
 
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
            
    step_mobile_personalInfo_getCurrentUserInfo()
    step_mobile_order_before_by_cardNo()
    step_mobile_product_discount_beforeSettlementProductList()
    step_01_mobile_order_carts_toSettlement()
    step_02_mobile_order_carts_toSettlement()    
    step_mobile_order_carts_getFreightList()
    step_mobile_order_carts_getCouponList()
    step_mobile_order_carts_getSecondList()
    step_mobile_order_carts_getGiftList_2()
    step_03_mobile_order_carts_toSettlement()
    step_mobile_wallet_getDetail()
    step_mobile_trade_orderCommit()
    step_mobile_orderInfo_getOrderInfo()
    
    # 交付结算详情表
    orderPrice = None # 押货价
    
    @allure.step("商品版本列表:获取押货价")
    def step_mgmt_product_item_listVersion():

        nonlocal orderPrice
        data = {
        "versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        "pageNum": 1,
        "pageSize": 10,
        "serialNo": getOrderInfo["orderProductVOList"][0]["serialNo"], # 商品编码
        "title": None, # 商品名称
        "catalogId": None, # 类型id
        "saleCompanyId": None, # 销售主体id
        "orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
        "directSale": None, # 是否直销，1-是，0-否
        "orderWay": None, # 下单方式 1-自购,2-代购
        "deliverWay": None, # 交付方式 1-公司交付,2-门店交付
        "startTime": "", # 开始时间时间戳
        "endTime": "" # 结束时间时间戳
    }
        with _mgmt_product_item_listVersion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if d["serialNo"] == getOrderInfo["orderProductVOList"][0]["serialNo"]:
                        orderPrice = d["orderPrice"]
                        break

    @allure.step(" 交付结算列表: 转分订单流水检查")
    def step_mgmt_order_getOrderSettlementDetail():
            
        params = {
            "orderMonth": datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y%m"), # 上一个月，业绩月份202204
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "orderNo": getOrderInfo["orderNo"], # 订单编号/售后单号
            "orderType": 1, # 订单类型 1->商城报单 2->商城退单
            "isDifference": None, # 交付差额是否为负 0->否 1->是
            "tradingStartTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-01', # 上一个月第一天，交易开始时间2022-04-01
            "tradingEndTime": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 当天
            "pageNum": 1,
            "pageSize": 10
        }           
        with _mgmt_order_getOrderSettlementDetail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["orderNo"] == getOrderInfo["orderNo"]  # 订单号/售后单号
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 订单类型
            assert r.json()["data"]["list"][0]["orderTypeDesc"] == "商城报单" # 订单类型
            assert r.json()["data"]["list"][0]["retailPrice"] == getOrderInfo["orderAmount"] # 零售价金额
            assert r.json()["data"]["list"][0]["securityAmount"] == float(orderPrice) * int(getOrderInfo["orderProductVOList"][0]["quantity"]) # 押货价金额
            assert r.json()["data"]["list"][0]["retailPrice"] - r.json()["data"]["list"][0]["securityAmount"] == r.json()["data"]["list"][0]["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
            assert r.json()["data"]["list"][0]["orderAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secCouponAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["giftCouponAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["expressSubsidyAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionDiscount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["totalAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["orderAmount"] - r.json()["data"]["list"][0]["totalAmount"] == r.json()["data"]["list"][0]["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
            assert r.json()["data"]["list"][0]["receiveAmount"] - r.json()["data"]["list"][0]["payDifference"] == r.json()["data"]["list"][0]["difAmount"] # 店应收回款 - 店应补差额 = 交付差额
        
    step_mgmt_product_item_listVersion()
    step_mgmt_order_getOrderSettlementDetail()

    # 85折转分分公司流水
    @allure.step("分页列表-85折转分分公司流水")
    def step_mgmt_inventory_transferOrder_pageList():
                
        data = {
            "companyCode": getOrderInfo["financeCompanyCode"], # 分公司编号
            "customerCardNo": getOrderInfo["customerCard"], # 会员卡号
            "openOrderCardNo": getOrderInfo["creatorCard"], # 开单人卡号
            "storeCode": None, # 服务中心编号
            "openOrderManType": None, # 开单人类型 3->云商 4->微店
            "orderType": None, # 账款类型 1->报单 ，2->退单
            "month": time.strftime("%Y%m",time.localtime(time.time())), # 月份(yyyyMM)
            "pageNum": 1,
            "pageSize": 10,
            "verifyStartDay": "", # 审核开始时间(yyyy-MM-dd)
            "verifyEndDay": "" # 审核结束时间(yyyy-MM-dd)
        }            
        with _mgmt_inventory_transferOrder_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == getOrderInfo["financeCompanyCode"] # 分公司编号
            assert r.json()["data"]["list"][0]["storeCode"] == getOrderInfo["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == getOrderInfo["creatorCard"] # 开单人卡号           
            assert r.json()["data"]["list"][0]["openOrderManType"] == getOrderInfo["creatorType"] # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == getOrderInfo["creatorName"] # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == getOrderInfo["customerCard"] # 会员卡号
            assert r.json()["data"]["list"][0]["customerName"] == getOrderInfo["customerName"] # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == getOrderInfo["customerType"] # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ,2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 使用购物礼券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["verifyTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 审核时间
            assert r.json()["data"]["list"][0]["storeName"] == getOrderInfo["storeName"] # 服务中心名称
    
    step_mgmt_inventory_transferOrder_pageList()
          
    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_mgmt_dis_inventory_detail():
                
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 3, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y%m"), # 上个月份 202204月份，格式为：yyyyMM   
            "endMonth": (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y%m"), # 上个月份202204月份，格式为：yyyyMM
            "storeCode": getOrderInfo["storeCode"], # 服务中心编号
            "productCode": getOrderInfo["orderProductVOList"][0]["serialNo"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 3 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -getOrderInfo["orderProductVOList"][0]["quantity"] # 交付数量
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    step_mgmt_dis_inventory_detail()

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
            assert r.json()["data"]["list"][0]["couponStatus"] == 1
            assert r.json()["data"]["list"][0]["couponStatusDesc"] == "待生效"
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["getTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getOrderInfo["orderCompleteTime"])/1000))
            assert r.json()["data"]["list"][0]["getType"] == 1
            assert r.json()["data"]["list"][0]["getTypeDesc"] == "购物获得"
            assert r.json()["data"]["list"][0]["memberType"] == getOrderInfo["customerType"]
            assert r.json()["data"]["list"][0]["realname"] == getOrderInfo["customerName"]
            assert r.json()["data"]["list"][0]["secondCouponAmount"] == getOrderInfo["returnCoupon"]
            assert r.json()["data"]["list"][0]["sourceOrderMonth"] == getOrderInfo["orderMonth"]
            assert r.json()["data"]["list"][0]["sourceOrderNo"] == getOrderInfo["orderNo"]
            assert r.json()["data"]["list"][0]["sourceStoreCode"] == getOrderInfo["storeCode"]
    
    step_mgmt_fin_voucher_getSecondCouponGetDetail() 




