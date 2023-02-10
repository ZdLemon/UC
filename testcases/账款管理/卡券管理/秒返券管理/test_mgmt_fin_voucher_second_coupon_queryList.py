# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryList import data as data, _mgmt_fin_voucher_second_coupon_queryList

from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay
from api.mall_mobile_application._mobile_product_getProductDetail import params, _mobile_product_getProductDetail
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit

from api.mall_mobile_application._mobile_order_return_applyReturn import data as data06, _mobile_order_return_applyReturn

from api.mall_mobile_application._mobile_wallet_getSecondCouponList import data as data03, _mobile_wallet_getSecondCouponList
from api.mall_mobile_application._mobile_wallet_applySecondCouponWithdraw import data as data02, _mobile_wallet_applySecondCouponWithdraw

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data as data04, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_acceptWithdraw import _mgmt_fin_voucher_second_coupon_acceptWithdraw

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data as data05, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_revokeWithdraw import _mgmt_fin_voucher_second_coupon_revokeWithdraw
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawdtlList import params as params02, _mgmt_fin_voucher_second_coupon_queryWithdrawdtlList

from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawList import _mobile_wallet_querySecondCouponWithdrawList
from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawdtlList import params as params03, _mobile_wallet_querySecondCouponWithdrawdtlList
from setting import P1, P2, P3, username, store, username_vip, store_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryList")
class TestClass:
    """
    秒返券列表：搜索功能检查
    /mgmt/fin/voucher/second/coupon/queryList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    
    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询订单业绩月份检查")
    def test_01_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceOrderEndMonth"] = time.strftime("%Y%m",time.localtime(time.time()))
        data["sourceOrderStartMonth"] = time.strftime("%Y%m",time.localtime(time.time()))                  
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["sourceOrderMonth"] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y%m",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询会员卡号检查")
    def test_02_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["cardNo"] = username          
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == data["cardNo"]    

    @allure.severity(P3)
    @allure.title("秒返券列表-失败路径: 仅支持精确查询会员卡号检查")
    def test_021_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["cardNo"] = username[:-2]          
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []  

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询会员手机号检查")
    def test_03_mgmt_fin_voucher_second_coupon_queryList(self, login_oauth_token):
        
        data = deepcopy(self.data)
        data["mobile"] = login_oauth_token["data"]["mobile"]          
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == data["mobile"]  

    @allure.severity(P3)
    @allure.title("秒返券列表-失败路径: 仅支持精确查询会员手机号检查")
    def test_031_mgmt_fin_voucher_second_coupon_queryList(self, login_oauth_token):
        
        data = deepcopy(self.data)
        data["mobile"] = login_oauth_token["data"]["mobile"][:-2]        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP顾客", "云商", "微店"])
    def test_04_mgmt_fin_voucher_second_coupon_queryList(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                    assert i == memberType 

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询来源订单号检查")
    def test_05_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            sourceOrderNo =  r.json()["data"]["list"][0]["sourceOrderNo"]
               
        data = deepcopy(self.data)
        data["sourceOrderNo"] = sourceOrderNo        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["sourceOrderNo"] for d in r.json()["data"]["list"]):
                    assert i == sourceOrderNo  

    @allure.severity(P3)
    @allure.title("秒返券列表-失败路径: 仅支持精确查询来源订单号检查")
    def test_051_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            sourceOrderNo =  r.json()["data"]["list"][0]["sourceOrderNo"]
        
        
        data = deepcopy(self.data)
        data["sourceOrderNo"] = sourceOrderNo[:-2]
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询提现批次号检查")
    def test_06_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["withdrawBatch"] = f'{time.strftime("%Y%m",time.localtime(time.time()))}001'        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["withdrawBatch"] for d in r.json()["data"]["list"]):
                    assert i == data["withdrawBatch"] 

    @allure.severity(P3)
    @allure.title("秒返券列表-失败路径: 仅支持精确查询提现批次号检查")
    def test_061_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["withdrawBatch"] = f'{time.strftime("%Y%m",time.localtime(time.time()))}00'        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询服务中心编号检查")
    def test_07_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["sourceStoreCode"] for d in r.json()["data"]["list"]):
                    assert i == data["sourceStoreCode"] 

    @allure.severity(P3)
    @allure.title("秒返券列表-失败路径: 仅支持精确查询服务中心编号检查")
    def test_071_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store[:-2]        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询发放时间检查")
    def test_08_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)   
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["effectTimeDesc"][0:7] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 单选查询使用状态检查")
    @pytest.mark.parametrize("couponStatus", list(range(1, 9)), ids=["已使用", "未使用", "占用中", "已失效", "退货失效", "已提现", "提现中", "已锁定"])
    def test_09_mgmt_fin_voucher_second_coupon_queryList(self, couponStatus):
        
        data = deepcopy(self.data)
        data["couponStatusList"] = [couponStatus]
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["couponStatus"] for d in r.json()["data"]["list"]):
                    assert i == couponStatus

    @allure.severity(P3)
    @allure.title("秒返券列表-成功路径: 3项多选查询使用状态检查")
    @pytest.mark.parametrize("couponStatus", list(combinations("12345678", 3)))
    def test_091_mgmt_fin_voucher_second_coupon_queryList(self, couponStatus):
        
        data = deepcopy(self.data)
        data["couponStatusList"] = list(couponStatus)
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert str(d["couponStatus"]) in list(couponStatus)

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 查询是否已退货检查")
    @pytest.mark.parametrize("soReturnFlag,ids", [(True, "是"), (False,  "否")])
    def test_10_mgmt_fin_voucher_second_coupon_queryList(self, soReturnFlag, ids):
        
        data = deepcopy(self.data)
        data["soReturnFlag"] = soReturnFlag
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["soReturnFlagDesc"] for d in r.json()["data"]["list"]):
                    assert i == ids


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryList")
class TestClass02:
    """
    秒返券列表：状态流转
    /mgmt/fin/voucher/second/coupon/queryList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.data04 = deepcopy(data04)
        self.data05 = deepcopy(data05)
        self.data06 = deepcopy(data06)
        
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)

        self.access_token = os.environ["access_token_2"]
        self.token = os.environ["token"] # 云商
        self.token_85 = os.environ["token_85"] # 云商85

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: VIP顾客-未使用->占用中检查(订单待支付)")
    def test_01_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_3):
            
        getSecondList = vip_Second_2_3

                 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"]    
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 3

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: VIP顾客-未使用->已使用检查(订单待支付)")
    def test_02_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_1):
            
        getSecondList = vip_Second_2_1

                 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 1

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: 云商-未使用->退货失效检查(订单退货)")
    def test_03_mgmt_fin_voucher_second_coupon_queryList(self, yunsh_Second_2_5):
            
        getSecondList = yunsh_Second_2_5

                 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 5

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: 云商-未使用->已锁定检查(订单退货待审核)")
    def test_03_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_8):
            
        getSecondList = vip_Second_2_8

                 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 8

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: VIP顾客-未使用->提现中检查(秒返券提现待审核)")
    def test_04_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_7):
            
        getSecondList = vip_Second_2_7
 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 7

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: VIP顾客-未使用->已提现检查(秒返券提现)")
    def test_05_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_6):
            
        getSecondList = vip_Second_2_6
 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 6

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: VIP顾客-未使用->未使用检查(完美运营后台-秒返券提现撤销)")
    def test_06_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_7_2_houtai):
            
        getSecondList = vip_Second_7_2_houtai
 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 2

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券列表-成功路径: VIP顾客-未使用->未使用检查(商城前端-秒返券提现撤销)")
    def test_07_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_7_2_qiantai):
            
        getSecondList = vip_Second_7_2_qiantai
 
        @allure.step("秒返券列表")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondList["sourceOrderNo"] 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["couponStatus"] == 2

        if getSecondList:
            step_mgmt_fin_voucher_second_coupon_queryList()
