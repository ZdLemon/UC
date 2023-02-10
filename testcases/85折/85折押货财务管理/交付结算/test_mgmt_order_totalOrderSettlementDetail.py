# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getOrderSettlementDetail import params, _mgmt_order_getOrderSettlementDetail
from api.mall_mgmt_application._mgmt_order_totalOrderSettlementDetail import params as params02, _mgmt_order_totalOrderSettlementDetail

from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/totalOrderSettlementDetail")
class TestClass:
    """
    交付结算详情合计
    /mgmt/order/totalOrderSettlementDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P2)
    @allure.title(" 交付结算详情合计-成功路径: 查询交易日期默认本月合计检查")
    def test_01_mgmt_order_totalOrderSettlementDetail(self):
            
        retailPrice = 0
        securityAmount = 0
        payDifference = 0
        orderAmount = 0
        returnAmount = 0
        secCouponAmount = 0
        giftCouponAmount = 0
        couponAmount = 0
        expressSubsidyAmount = 0
        promotionDiscount = 0
        totalAmount = 0
        receiveAmount = 0
        difAmount = 0
        
        @allure.title("交付结算详情: 获取所有数据合计值")
        def step_mgmt_order_getOrderSettlementDetail():
            
            nonlocal retailPrice, securityAmount, payDifference, orderAmount, returnAmount, secCouponAmount, giftCouponAmount
            nonlocal couponAmount, expressSubsidyAmount, promotionDiscount, totalAmount, receiveAmount,  difAmount
            params = deepcopy(self.params)           
            with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                totalPage = r.json()["data"]["totalPage"]
            
            for Page in range(1, totalPage+1):
                params["pageNum"] = Page
                with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                    for d in r.json()["data"]["list"]:
                        retailPrice += d["retailPrice"]                     # 零售价金额
                        securityAmount += d["securityAmount"]               # 押货价金额
                        payDifference += d["payDifference"]                 # 店应补差额
                        orderAmount += d["orderAmount"]                     # 应付金额
                        returnAmount += d["returnAmount"]                   # 返还金额
                        secCouponAmount += d["secCouponAmount"]             # 秒返券
                        giftCouponAmount += d["giftCouponAmount"]           # 电子礼券
                        couponAmount += d["couponAmount"]                   # 优惠券
                        expressSubsidyAmount += d["expressSubsidyAmount"]   # 运费补贴券
                        promotionDiscount += d["promotionDiscount"]         # 活动优惠
                        totalAmount += d["totalAmount"]                     # 实付金额
                        receiveAmount += d["receiveAmount"]                 # 店应收回款
                        difAmount += d["difAmount"]                         # 交付差额
        
        @allure.title("交付结算详情合计")
        def step_mgmt_order_totalOrderSettlementDetail():
            
            params = deepcopy(self.params02)
            params["storeCode"] = store_85           
            with _mgmt_order_totalOrderSettlementDetail(params, self.access_token) as r:
                assert r.json()["data"]["retailPrice"] == retailPrice  # 零售价金额
                assert r.json()["data"]["securityAmount"] == securityAmount # 押货价金额
                assert r.json()["data"]["payDifference"] == payDifference # 店应补差额
                assert r.json()["data"]["orderAmount"] == orderAmount # 应付金额
                assert r.json()["data"]["returnAmount"] == returnAmount # 返还金额
                assert r.json()["data"]["secCouponAmount"] == secCouponAmount # 秒返券
                assert r.json()["data"]["giftCouponAmount"] == giftCouponAmount # 电子礼券
                assert r.json()["data"]["couponAmount"] == couponAmount # 优惠券
                assert r.json()["data"]["expressSubsidyAmount"] == expressSubsidyAmount # 运费补贴券
                assert r.json()["data"]["promotionDiscount"] == promotionDiscount # 活动优惠
                assert r.json()["data"]["totalAmount"] == totalAmount # 实付金额
                assert r.json()["data"]["receiveAmount"] == receiveAmount # 店应收回款
                assert r.json()["data"]["difAmount"] == difAmount # 交付差额
        
        step_mgmt_order_getOrderSettlementDetail()
        step_mgmt_order_totalOrderSettlementDetail()

    @allure.severity(P2)
    @allure.title(" 交付结算详情合计-成功路径: 查询订单类型合计检查")
    @pytest.mark.parametrize("orderType,ids", [(1, "商城报单"), (2, "商城退单")])
    def test_02_mgmt_order_totalOrderSettlementDetail(self, orderType, ids):
            
        retailPrice = 0
        securityAmount = 0
        payDifference = 0
        orderAmount = 0
        returnAmount = 0
        secCouponAmount = 0
        giftCouponAmount = 0
        couponAmount = 0
        expressSubsidyAmount = 0
        promotionDiscount = 0
        totalAmount = 0
        receiveAmount = 0
        difAmount = 0
        
        @allure.title("交付结算详情: 获取所有数据合计值")
        def step_mgmt_order_getOrderSettlementDetail():
            
            nonlocal retailPrice, securityAmount, payDifference, orderAmount, returnAmount, secCouponAmount, giftCouponAmount
            nonlocal couponAmount, expressSubsidyAmount, promotionDiscount, totalAmount, receiveAmount,  difAmount
            params = deepcopy(self.params)
            params["orderType"] = orderType           
            with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                totalPage = r.json()["data"]["totalPage"]
            
            for Page in range(1, totalPage+1):
                params["pageNum"] = Page
                with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                    for d in r.json()["data"]["list"]:
                        retailPrice += d["retailPrice"]                     # 零售价金额
                        securityAmount += d["securityAmount"]               # 押货价金额
                        payDifference += d["payDifference"]                 # 店应补差额
                        orderAmount += d["orderAmount"]                     # 应付金额
                        returnAmount += d["returnAmount"]                   # 返还金额
                        secCouponAmount += d["secCouponAmount"]             # 秒返券
                        giftCouponAmount += d["giftCouponAmount"]           # 电子礼券
                        couponAmount += d["couponAmount"]                   # 优惠券
                        expressSubsidyAmount += d["expressSubsidyAmount"]   # 运费补贴券
                        promotionDiscount += d["promotionDiscount"]         # 活动优惠
                        totalAmount += d["totalAmount"]                     # 实付金额
                        receiveAmount += d["receiveAmount"]                 # 店应收回款
                        difAmount += d["difAmount"]                         # 交付差额
        
        @allure.title("交付结算详情合计")
        def step_mgmt_order_totalOrderSettlementDetail():
            
            params = deepcopy(self.params02)
            params["orderType"] = orderType 
            params["storeCode"] = store_85          
            with _mgmt_order_totalOrderSettlementDetail(params, self.access_token) as r:
                assert r.json()["data"]["retailPrice"] == retailPrice  # 零售价金额
                assert r.json()["data"]["securityAmount"] == securityAmount # 押货价金额
                assert r.json()["data"]["payDifference"] == payDifference # 店应补差额
                assert r.json()["data"]["orderAmount"] == orderAmount # 应付金额
                assert r.json()["data"]["returnAmount"] == returnAmount # 返还金额
                assert r.json()["data"]["secCouponAmount"] == secCouponAmount # 秒返券
                assert r.json()["data"]["giftCouponAmount"] == giftCouponAmount # 电子礼券
                assert r.json()["data"]["couponAmount"] == couponAmount # 优惠券
                assert r.json()["data"]["expressSubsidyAmount"] == expressSubsidyAmount # 运费补贴券
                assert r.json()["data"]["promotionDiscount"] == promotionDiscount # 活动优惠
                assert r.json()["data"]["totalAmount"] == totalAmount # 实付金额
                assert r.json()["data"]["receiveAmount"] == receiveAmount # 店应收回款
                assert r.json()["data"]["difAmount"] == difAmount # 交付差额
        
        step_mgmt_order_getOrderSettlementDetail()
        step_mgmt_order_totalOrderSettlementDetail()

    @allure.severity(P2)
    @allure.title(" 交付结算详情合计-成功路径: 查询订单号&售后单号-售后号合计检查")
    @pytest.mark.parametrize("orderType,ids", [(1, "订单号"), (2, "售后单号")])
    def test_03_mgmt_order_totalOrderSettlementDetail(self, orderType,ids):
            
        retailPrice = 0
        securityAmount = 0
        payDifference = 0
        orderAmount = 0
        returnAmount = 0
        secCouponAmount = 0
        giftCouponAmount = 0
        couponAmount = 0
        expressSubsidyAmount = 0
        promotionDiscount = 0
        totalAmount = 0
        receiveAmount = 0
        difAmount = 0
        orderNo = None
        
        @allure.title("交付结算详情: 获取所有数据合计值")
        def step_mgmt_order_getOrderSettlementDetail():
            
            nonlocal retailPrice, securityAmount, payDifference, orderAmount, returnAmount, secCouponAmount, giftCouponAmount
            nonlocal couponAmount, expressSubsidyAmount, promotionDiscount, totalAmount, receiveAmount,  difAmount
            nonlocal orderNo
            
            params = deepcopy(self.params)
            params["orderType"] = orderType # 商城报单，退单                 
            with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                orderNo = r.json()["data"]["list"][0]["orderNo"]
                
            params["orderType"] = None # 商城报单，退单  
            params["orderNo"] = orderNo          
            with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    retailPrice += d["retailPrice"]                     # 零售价金额
                    securityAmount += d["securityAmount"]               # 押货价金额
                    payDifference += d["payDifference"]                 # 店应补差额
                    orderAmount += d["orderAmount"]                     # 应付金额
                    returnAmount += d["returnAmount"]                   # 返还金额
                    secCouponAmount += d["secCouponAmount"]             # 秒返券
                    giftCouponAmount += d["giftCouponAmount"]           # 电子礼券
                    couponAmount += d["couponAmount"]                   # 优惠券
                    expressSubsidyAmount += d["expressSubsidyAmount"]   # 运费补贴券
                    promotionDiscount += d["promotionDiscount"]         # 活动优惠
                    totalAmount += d["totalAmount"]                     # 实付金额
                    receiveAmount += d["receiveAmount"]                 # 店应收回款
                    difAmount += d["difAmount"]                         # 交付差额
        
        @allure.title("交付结算详情合计")
        def step_mgmt_order_totalOrderSettlementDetail():
            
            params = deepcopy(self.params02)
            params["orderNo"] = orderNo  
            params["storeCode"] = store_85         
            with _mgmt_order_totalOrderSettlementDetail(params, self.access_token) as r:
                assert r.json()["data"]["retailPrice"] == retailPrice  # 零售价金额
                assert r.json()["data"]["securityAmount"] == securityAmount # 押货价金额
                assert r.json()["data"]["payDifference"] == payDifference # 店应补差额
                assert r.json()["data"]["orderAmount"] == orderAmount # 应付金额
                assert r.json()["data"]["returnAmount"] == returnAmount # 返还金额
                assert r.json()["data"]["secCouponAmount"] == secCouponAmount # 秒返券
                assert r.json()["data"]["giftCouponAmount"] == giftCouponAmount # 电子礼券
                assert r.json()["data"]["couponAmount"] == couponAmount # 优惠券
                assert r.json()["data"]["expressSubsidyAmount"] == expressSubsidyAmount # 运费补贴券
                assert r.json()["data"]["promotionDiscount"] == promotionDiscount # 活动优惠
                assert r.json()["data"]["totalAmount"] == totalAmount # 实付金额
                assert r.json()["data"]["receiveAmount"] == receiveAmount # 店应收回款
                assert r.json()["data"]["difAmount"] == difAmount # 交付差额
        
        step_mgmt_order_getOrderSettlementDetail()
        step_mgmt_order_totalOrderSettlementDetail()

    @allure.severity(P2)
    @allure.title(" 交付结算详情合计-成功路径: 查询交付差额是否为负合计检查")
    @pytest.mark.parametrize("isDifference,ids", [(0, "否"), (1, "是")])
    def test_03_mgmt_order_totalOrderSettlementDetail(self, isDifference, ids):
            
        retailPrice = 0
        securityAmount = 0
        payDifference = 0
        orderAmount = 0
        returnAmount = 0
        secCouponAmount = 0
        giftCouponAmount = 0
        couponAmount = 0
        expressSubsidyAmount = 0
        promotionDiscount = 0
        totalAmount = 0
        receiveAmount = 0
        difAmount = 0
        
        @allure.title("交付结算详情: 获取所有数据合计值")
        def step_mgmt_order_getOrderSettlementDetail():
            
            nonlocal retailPrice, securityAmount, payDifference, orderAmount, returnAmount, secCouponAmount, giftCouponAmount
            nonlocal couponAmount, expressSubsidyAmount, promotionDiscount, totalAmount, receiveAmount,  difAmount
            params = deepcopy(self.params)
            params["isDifference"] = isDifference           
            with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                totalPage = r.json()["data"]["totalPage"]
            
            for Page in range(1, totalPage+1):
                params["pageNum"] = Page
                with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                    for d in r.json()["data"]["list"]:
                        retailPrice += d["retailPrice"]                     # 零售价金额
                        securityAmount += d["securityAmount"]               # 押货价金额
                        payDifference += d["payDifference"]                 # 店应补差额
                        orderAmount += d["orderAmount"]                     # 应付金额
                        returnAmount += d["returnAmount"]                   # 返还金额
                        secCouponAmount += d["secCouponAmount"]             # 秒返券
                        giftCouponAmount += d["giftCouponAmount"]           # 电子礼券
                        couponAmount += d["couponAmount"]                   # 优惠券
                        expressSubsidyAmount += d["expressSubsidyAmount"]   # 运费补贴券
                        promotionDiscount += d["promotionDiscount"]         # 活动优惠
                        totalAmount += d["totalAmount"]                     # 实付金额
                        receiveAmount += d["receiveAmount"]                 # 店应收回款
                        difAmount += d["difAmount"]                         # 交付差额
        
        @allure.title("交付结算详情合计")
        def step_mgmt_order_totalOrderSettlementDetail():
            
            params = deepcopy(self.params02)
            params["isDifference"] = isDifference   
            params["storeCode"] = store_85     
            with _mgmt_order_totalOrderSettlementDetail(params, self.access_token) as r:
                assert r.json()["data"]["retailPrice"] == retailPrice  # 零售价金额
                assert r.json()["data"]["securityAmount"] == securityAmount # 押货价金额
                assert r.json()["data"]["payDifference"] == payDifference # 店应补差额
                assert r.json()["data"]["orderAmount"] == orderAmount # 应付金额
                assert r.json()["data"]["returnAmount"] == returnAmount # 返还金额
                assert r.json()["data"]["secCouponAmount"] == secCouponAmount # 秒返券
                assert r.json()["data"]["giftCouponAmount"] == giftCouponAmount # 电子礼券
                assert r.json()["data"]["couponAmount"] == couponAmount # 优惠券
                assert r.json()["data"]["expressSubsidyAmount"] == expressSubsidyAmount # 运费补贴券
                assert r.json()["data"]["promotionDiscount"] == promotionDiscount # 活动优惠
                assert r.json()["data"]["totalAmount"] == totalAmount # 实付金额
                assert r.json()["data"]["receiveAmount"] == receiveAmount # 店应收回款
                assert r.json()["data"]["difAmount"] == difAmount # 交付差额
        
        step_mgmt_order_getOrderSettlementDetail()
        step_mgmt_order_totalOrderSettlementDetail()

