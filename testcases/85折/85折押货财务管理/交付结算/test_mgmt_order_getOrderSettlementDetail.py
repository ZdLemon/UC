# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getOrderSettlementDetail import params, _mgmt_order_getOrderSettlementDetail
from api.mall_mgmt_application._mgmt_product_item_listVersion import data, _mgmt_product_item_listVersion # 产品版本列表

from util.getBaseMonthlyReportData import getBaseMonthlyReportData
from setting import P1, P2, P3, username_85, store_85, name_85, productCode
from util.stepreruns import stepreruns
from copy import deepcopy
import os
import allure
import pytest
import time
import calendar
import datetime
from datetime import date, timedelta


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSettlementDetail")
class TestClass:
    """
    交付结算详情:搜索检查
    /mgmt/order/getOrderSettlementDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title(" 交付结算列表-成功路径: 查询交易日期默认本月检查")
    def test_01_mgmt_order_getOrderSettlementDetail(self):
        
        params = deepcopy(self.params)           
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["tradingHoursDesc"][:7] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m",time.localtime(time.time()))
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title(" 交付结算列表: 下拉选项查询订单类型检查")
    @pytest.mark.parametrize("orderType,ids", [(1, "商城报单"), (2, "商城退单")])
    def test_02_mgmt_order_getOrderSettlementDetail(self, orderType, ids):
        
        params = deepcopy(self.params)
        params["orderType"] = orderType                     
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert d["orderType"] == orderType
                assert d["orderTypeDesc"] == ids
                if orderType == 1:
                    assert d["orderNo"].startswith("GH")
                elif orderType == 2:
                    assert d["orderNo"].startswith("TGH")

    @allure.severity(P2)
    @allure.title(" 交付结算列表: 查询订单号/售后单号-订单号检查")
    def test_031_mgmt_order_getOrderSettlementDetail(self):
        
        params = deepcopy(self.params)
        params["orderType"] = 1 # 商城报单                    
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            orderNo = r.json()["data"]["list"][0]["orderNo"]
            
        params = deepcopy(self.params)
        params["orderNo"] = orderNo             
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            assert r.json()["data"]["list"][0]["orderNo"] == orderNo

    @allure.severity(P2)
    @allure.title(" 交付结算列表: 查询订单号/售后单号-售后单号检查")
    def test_032_mgmt_order_getOrderSettlementDetail(self):
        
        params = deepcopy(self.params)
        params["orderType"] = 2 # 商城退单                  
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            orderNo = r.json()["data"]["list"][0]["orderNo"]
            
        params = deepcopy(self.params)
        params["orderNo"] = orderNo             
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            assert r.json()["data"]["list"][0]["orderNo"] == orderNo
                     
    @allure.severity(P2)
    @allure.title(" 交付结算列表: 下拉选项查询交付差额是否为负检查")
    @pytest.mark.parametrize("isDifference,ids", [(0, "否"), (1, "是")])
    def test_04_mgmt_order_getOrderSettlementDetail(self, isDifference, ids):
        
        params = deepcopy(self.params)
        params["isDifference"] = isDifference                    
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                for i in r.json()["data"]["list"]:
                    if isDifference:
                        assert i["difAmount"] < 0
                    else:
                        assert i["difAmount"] >= 0
                    

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSettlementDetail")
class TestClass02:
    """
    交付结算详情:各字段关系检查
    /mgmt/order/getOrderSettlementDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("交付结算详情-成功路径: 各字段逻辑关系检查")
    def test_01_mgmt_order_getOrderSettlementDetail(self):
        
        params = deepcopy(self.params)           
        with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
            for d in r.json()["data"]["list"]:
                assert d["retailPrice"] - d["securityAmount"] == d["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
                assert d["orderAmount"] - d["totalAmount"] == d["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
                assert d["receiveAmount"] - d["payDifference"] == d["difAmount"] # 店应收回款 - 店应补差额 = 交付差额



@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getOrderSettlementDetail")
@pytest.mark.skipif(time.localtime(time.time()).tm_mday > 8, reason="如果超过8日,前端不允许退货上个月的85折订单")
class TestClass05:
    """
    交付结算详情:补报截止日期前，退货上个月的订单流水算上个月业绩检查
    /mgmt/order/getOrderSettlementDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
        self.token_85 = os.environ["token_85"]
   
    @allure.severity(P1)
    @allure.title("交付结算详情-成功路径: 8日前,退货上个月的订单流水检查")
    def test_01_mgmt_order_getOrderSettlementDetail(self, FGY_applyReturn_85):
        
        applyReturn, getOrderInfo = FGY_applyReturn_85
        orderPrice = None # 押货价
        
        @allure.step("商品版本列表:获取押货价")
        def step_mgmt_product_item_listVersion():

            nonlocal orderPrice
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            with _mgmt_product_item_listVersion(data, self.access_token) as r:
                orderPrice = r.json()["data"]["list"][0]["orderPrice"]
        
        @allure.step(" 交付结算列表: 退货上个月的订单流水检查")
        @stepreruns()
        def step_mgmt_order_getOrderSettlementDetail():
                
            params = deepcopy(self.params)
            params["orderMonth"] = datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y%m") # 上一个月，业绩月份202204
            params["tradingStartTime"] = f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-01' # 上一个月第一天，交易开始时间2022-04-01
            params["tradingEndTime"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当天
            params["orderNo"] = applyReturn           
            with _mgmt_order_getOrderSettlementDetail(params, self.access_token) as r:
                assert r.json()["data"]["list"][0]["orderNo"] == applyReturn  # 订单号/售后单号
                assert r.json()["data"]["list"][0]["orderType"] == 2 # 订单类型
                assert r.json()["data"]["list"][0]["orderTypeDesc"] == "商城退单" # 订单类型
                assert r.json()["data"]["list"][0]["retailPrice"] == -getOrderInfo["orderAmount"] # 零售价金额
                assert r.json()["data"]["list"][0]["securityAmount"] == -float(orderPrice) * int(getOrderInfo["orderProductVOList"][0]["quantity"]) # 押货价金额
                assert r.json()["data"]["list"][0]["retailPrice"] - r.json()["data"]["list"][0]["securityAmount"] == r.json()["data"]["list"][0]["payDifference"] # 零售价金额 - 押货价金额 = 店应补差额
                assert r.json()["data"]["list"][0]["orderAmount"] == -getOrderInfo["orderAmount"] or 0 # 应付金额
                assert r.json()["data"]["list"][0]["returnAmount"] == -getOrderInfo["returnAmount"] or 0 # 返还金额
                assert r.json()["data"]["list"][0]["secCouponAmount"] == -getOrderInfo["secCouponAmount"] or 0 # 秒返券
                assert r.json()["data"]["list"][0]["giftCouponAmount"] == -getOrderInfo["giftCouponAmount"] or 0 # 电子礼券
                assert r.json()["data"]["list"][0]["couponAmount"] == -getOrderInfo["couponAmount"] or 0 # 优惠券
                assert r.json()["data"]["list"][0]["expressSubsidyAmount"] == -getOrderInfo["expressSubsidyAmount"] or 0 # 运费补贴券
                assert r.json()["data"]["list"][0]["promotionDiscount"] == -getOrderInfo["promotionDiscount"] or 0 # 活动优惠
                assert r.json()["data"]["list"][0]["totalAmount"] == -getOrderInfo["totalAmount"] # 实付金额
                assert r.json()["data"]["list"][0]["orderAmount"] - r.json()["data"]["list"][0]["totalAmount"] == r.json()["data"]["list"][0]["receiveAmount"] # 应付金额 - 实付金额 = 店应收回款
                assert r.json()["data"]["list"][0]["receiveAmount"] - r.json()["data"]["list"][0]["payDifference"] == r.json()["data"]["list"][0]["difAmount"] # 店应收回款 - 店应补差额 = 交付差额
           
        step_mgmt_product_item_listVersion()
        step_mgmt_order_getOrderSettlementDetail()
