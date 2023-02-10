# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryDiffList import data, _mgmt_fin_voucher_second_coupon_queryDiffList

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryList import data as data02, _mgmt_fin_voucher_second_coupon_queryList
from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay
from api.mall_mobile_application._mobile_product_getProductDetail import params, _mobile_product_getProductDetail
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit
from api.mall_mobile_application._mobile_order_return_applyReturn import data as data06, _mobile_order_return_applyReturn
from api.mall_mobile_application._mobile_wallet_applySecondCouponWithdraw import data as data03, _mobile_wallet_applySecondCouponWithdraw
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data as data04, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_acceptWithdraw import _mgmt_fin_voucher_second_coupon_acceptWithdraw

from util.stepreruns import stepreruns
from setting import P1, P2, P3, username, store, name

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryDiffList")
class TestClass:
    """
    秒返券调差列表
    /mgmt/fin/voucher/second/coupon/queryDiffList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("秒返券调差列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username, username[:-2]])
    def test_01_mgmt_fin_voucher_second_coupon_queryDiffList(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo        
        with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                        assert i == cardNo
            else:
                r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券调差列表-成功路径: 仅支持精确查询来源订单号检查")
    def test_02_mgmt_fin_voucher_second_coupon_queryDiffList(self):
        
        data = deepcopy(self.data)      
        with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
            sourceOrderNo =  r.json()["data"]["list"][0]["sourceOrderNo"]
        
        @allure.step("秒返券调差列表-成功路径: 查询来源订单号检查")       
        def step_01_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            nonlocal sourceOrderNo
            data = deepcopy(self.data)
            data["sourceOrderNo"] = sourceOrderNo        
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                for i in set(d["sourceOrderNo"] for d in r.json()["data"]["list"]):
                        assert i == sourceOrderNo  
        
        @allure.step("秒返券调差列表-失败路径: 模糊查询来源订单号检查")       
        def step_02_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            nonlocal sourceOrderNo
            data = deepcopy(self.data)
            data["sourceOrderNo"] = sourceOrderNo[:-2]     
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_fin_voucher_second_coupon_queryDiffList()
        step_02_mgmt_fin_voucher_second_coupon_queryDiffList()

    @allure.severity(P2)
    @allure.title("秒返券调差列表-成功路径: 查询处理方案检查")
    @pytest.mark.parametrize("diffWay,diffWayname", [(1, "扣减相应金额"), (2, "补回相应金额")])
    def test_03_mgmt_fin_voucher_second_coupon_queryDiffList(self, diffWay, diffWayname):
        
        data = deepcopy(self.data)
        data["diffWay"] = diffWay
        with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
            for i in set(d["diffWay"] for d in r.json()["data"]["list"]):
                    assert i == diffWay


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryDiffList")
class TestClass02:
    """
    秒返券调差列表
    /mgmt/fin/voucher/second/coupon/queryDiffList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.data04 = deepcopy(data04)
        self.data06 = deepcopy(data06)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token_2"]
        self.token = os.environ["token"]

    @allure.severity(P1)
    @allure.title("秒返券调差列表: 秒返券已使用，来源订单退货检查")
    def test_01_mgmt_fin_voucher_second_coupon_queryDiffList(self, yunsh_Second_1_diff):
        
        queryList = yunsh_Second_1_diff
        
        @allure.step("秒返券列表:已使用且来源订单已退货信息")
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data02)
            data["sourceOrderNo"] =  queryList["sourceOrderNo"]  
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["couponStatus"] == 1
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已使用"
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["useOrderNo"] == queryList["useOrderNo"]

        @allure.step("秒返券调差列表:已使用且来源订单已退货检查")
        def step_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = queryList["sourceOrderNo"]
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["cardNo"] == queryList["cardNo"]
                assert r.json()["data"]["list"][0]["realname"] == queryList["realname"]
                assert r.json()["data"]["list"][0]["secondCouponAmount"] == queryList["secondCouponAmount"]
                assert r.json()["data"]["list"][0]["sourceOrderNo"] == queryList["sourceOrderNo"]
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["couponStatus"] == 1
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已使用"
                assert r.json()["data"]["list"][0]["uoReturnFlag"] == False
                assert r.json()["data"]["list"][0]["uoReturnFlagDesc"] == "否"
                assert r.json()["data"]["list"][0]["secondCouponCode"] == queryList["secondCouponCode"]
                assert r.json()["data"]["list"][0]["diffWay"] == 1
                assert r.json()["data"]["list"][0]["diffWayDesc"] == "扣减相应金额"
                         
        step_mgmt_fin_voucher_second_coupon_queryList()
        step_mgmt_fin_voucher_second_coupon_queryDiffList()
            
    @allure.severity(P1)
    @allure.title("秒返券调差列表: 秒返券已使用，来源订单退货,使用订单退货检查")
    def test_02_mgmt_fin_voucher_second_coupon_queryDiffList(self, yunsh_Second_1_diff_2):
        
        queryList = yunsh_Second_1_diff_2
        
        @allure.step("秒返券列表:已使用，且来源订单已退货,且使用订单已退货信息")
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data02)
            data["sourceOrderNo"] =  queryList["sourceOrderNo"]    
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["couponStatus"] == 1
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已使用"
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["useOrderNo"] == queryList["useOrderNo"]

        @allure.step("秒返券调差列表:已使用，且来源订单已退货检查")
        def step_01_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = queryList["sourceOrderNo"]
            data["diffWay"] = 1
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["cardNo"] == queryList["cardNo"]
                assert r.json()["data"]["list"][0]["realname"] == queryList["realname"]
                assert r.json()["data"]["list"][0]["secondCouponAmount"] == queryList["secondCouponAmount"]
                assert r.json()["data"]["list"][0]["sourceOrderNo"] == queryList["sourceOrderNo"]
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["couponStatus"] == 1
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已使用"
                assert r.json()["data"]["list"][0]["useOrderNo"] == queryList["useOrderNo"]
                assert r.json()["data"]["list"][0]["uoReturnFlag"] == False
                assert r.json()["data"]["list"][0]["uoReturnFlagDesc"] == "否"
                assert r.json()["data"]["list"][0]["secondCouponCode"] == queryList["secondCouponCode"]
                assert r.json()["data"]["list"][0]["diffWay"] == 1
                assert r.json()["data"]["list"][0]["diffWayDesc"] == "扣减相应金额"
               
        @allure.step("秒返券调差列表:已使用，使用订单已退货检查")
        def step_02_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = queryList["sourceOrderNo"]
            data["diffWay"] = 2
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["cardNo"] == queryList["cardNo"]
                assert r.json()["data"]["list"][0]["realname"] == queryList["realname"]
                assert r.json()["data"]["list"][0]["secondCouponAmount"] == queryList["secondCouponAmount"]
                assert r.json()["data"]["list"][0]["sourceOrderNo"] == queryList["sourceOrderNo"]
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["couponStatus"] == 1
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已使用"
                assert r.json()["data"]["list"][0]["useOrderNo"] == queryList["useOrderNo"]
                assert r.json()["data"]["list"][0]["uoReturnFlag"] == True
                assert r.json()["data"]["list"][0]["uoReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["secondCouponCode"] == queryList["secondCouponCode"]
                assert r.json()["data"]["list"][0]["diffWay"] == 2
                assert r.json()["data"]["list"][0]["diffWayDesc"] == "补回相应金额"
                         
        step_mgmt_fin_voucher_second_coupon_queryList()
        step_01_mgmt_fin_voucher_second_coupon_queryDiffList()
        step_02_mgmt_fin_voucher_second_coupon_queryDiffList()

    @allure.severity(P1)
    @allure.title("秒返券调差列表: 秒返券已提现，来源订单退货检查")
    def test_03_mgmt_fin_voucher_second_coupon_queryDiffList(self, yunsh_Second_6_diff):
        
        queryList = yunsh_Second_6_diff
        
        @allure.step("秒返券列表:已提现，且来源订单已退货信息")
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data02)
            data["sourceOrderNo"] =  queryList["sourceOrderNo"]    
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["couponStatus"] == 6
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已提现"
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["useOrderNo"] == None

        @allure.step("秒返券调差列表:已提现检查")
        def step_01_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = queryList["sourceOrderNo"]
            data["diffWay"] = 1
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["cardNo"] == queryList["cardNo"]
                assert r.json()["data"]["list"][0]["realname"] == queryList["realname"]
                assert r.json()["data"]["list"][0]["secondCouponAmount"] == queryList["secondCouponAmount"]
                assert r.json()["data"]["list"][0]["sourceOrderNo"] == queryList["sourceOrderNo"]
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["couponStatus"] == 6
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已提现"
                assert r.json()["data"]["list"][0]["useOrderNo"] == None
                assert r.json()["data"]["list"][0]["uoReturnFlag"] == False
                assert r.json()["data"]["list"][0]["uoReturnFlagDesc"] == "否"
                assert r.json()["data"]["list"][0]["secondCouponCode"] == queryList["secondCouponCode"]
                assert r.json()["data"]["list"][0]["diffWay"] == 1
                assert r.json()["data"]["list"][0]["diffWayDesc"] == "扣减相应金额"

        @allure.step("秒返券调差列表:已提现，且来源订单已退货检查")
        def step_02_mgmt_fin_voucher_second_coupon_queryDiffList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = queryList["sourceOrderNo"]
            data["diffWay"] = 1
            with _mgmt_fin_voucher_second_coupon_queryDiffList(data, self.access_token) as r:
                assert r.json()["data"]["list"][0]["cardNo"] == queryList["cardNo"]
                assert r.json()["data"]["list"][0]["realname"] == queryList["realname"]
                assert r.json()["data"]["list"][0]["secondCouponAmount"] == queryList["secondCouponAmount"]
                assert r.json()["data"]["list"][0]["sourceOrderNo"] == queryList["sourceOrderNo"]
                assert r.json()["data"]["list"][0]["soReturnFlag"] == True
                assert r.json()["data"]["list"][0]["soReturnFlagDesc"] == "是"
                assert r.json()["data"]["list"][0]["couponStatus"] == 6
                assert r.json()["data"]["list"][0]["couponStatusDesc"] == "已提现"
                assert r.json()["data"]["list"][0]["useOrderNo"] == None
                assert r.json()["data"]["list"][0]["uoReturnFlag"] == False
                assert r.json()["data"]["list"][0]["uoReturnFlagDesc"] == "否"
                assert r.json()["data"]["list"][0]["secondCouponCode"] == queryList["secondCouponCode"]
                assert r.json()["data"]["list"][0]["diffWay"] == 1
                assert r.json()["data"]["list"][0]["diffWayDesc"] == "扣减相应金额"          
        
        step_mgmt_fin_voucher_second_coupon_queryList()
        step_01_mgmt_fin_voucher_second_coupon_queryDiffList()
        step_02_mgmt_fin_voucher_second_coupon_queryDiffList()
  



