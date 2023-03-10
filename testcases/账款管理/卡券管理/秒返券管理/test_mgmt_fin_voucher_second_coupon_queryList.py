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
    ????????????????????????????????????
    /mgmt/fin/voucher/second/coupon/queryList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    
    @allure.severity(P2)
    @allure.title("???????????????-????????????: ??????????????????????????????")
    def test_01_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceOrderEndMonth"] = time.strftime("%Y%m",time.localtime(time.time()))
        data["sourceOrderStartMonth"] = time.strftime("%Y%m",time.localtime(time.time()))                  
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["sourceOrderMonth"] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y%m",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ????????????????????????")
    def test_02_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["cardNo"] = username          
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == data["cardNo"]    

    @allure.severity(P3)
    @allure.title("???????????????-????????????: ???????????????????????????????????????")
    def test_021_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["cardNo"] = username[:-2]          
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []  

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ???????????????????????????")
    def test_03_mgmt_fin_voucher_second_coupon_queryList(self, login_oauth_token):
        
        data = deepcopy(self.data)
        data["mobile"] = login_oauth_token["data"]["mobile"]          
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == data["mobile"]  

    @allure.severity(P3)
    @allure.title("???????????????-????????????: ??????????????????????????????????????????")
    def test_031_mgmt_fin_voucher_second_coupon_queryList(self, login_oauth_token):
        
        data = deepcopy(self.data)
        data["mobile"] = login_oauth_token["data"]["mobile"][:-2]        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ??????????????????????????????")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP??????", "??????", "??????"])
    def test_04_mgmt_fin_voucher_second_coupon_queryList(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                    assert i == memberType 

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ???????????????????????????")
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
    @allure.title("???????????????-????????????: ??????????????????????????????????????????")
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
    @allure.title("???????????????-????????????: ???????????????????????????")
    def test_06_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["withdrawBatch"] = f'{time.strftime("%Y%m",time.localtime(time.time()))}001'        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["withdrawBatch"] for d in r.json()["data"]["list"]):
                    assert i == data["withdrawBatch"] 

    @allure.severity(P3)
    @allure.title("???????????????-????????????: ??????????????????????????????????????????")
    def test_061_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["withdrawBatch"] = f'{time.strftime("%Y%m",time.localtime(time.time()))}00'        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ??????????????????????????????")
    def test_07_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["sourceStoreCode"] for d in r.json()["data"]["list"]):
                    assert i == data["sourceStoreCode"] 

    @allure.severity(P3)
    @allure.title("???????????????-????????????: ?????????????????????????????????????????????")
    def test_071_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store[:-2]        
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ????????????????????????")
    def test_08_mgmt_fin_voucher_second_coupon_queryList(self):
        
        data = deepcopy(self.data)   
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["effectTimeDesc"][0:7] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ??????????????????????????????")
    @pytest.mark.parametrize("couponStatus", list(range(1, 9)), ids=["?????????", "?????????", "?????????", "?????????", "????????????", "?????????", "?????????", "?????????"])
    def test_09_mgmt_fin_voucher_second_coupon_queryList(self, couponStatus):
        
        data = deepcopy(self.data)
        data["couponStatusList"] = [couponStatus]
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            for i in set(d["couponStatus"] for d in r.json()["data"]["list"]):
                    assert i == couponStatus

    @allure.severity(P3)
    @allure.title("???????????????-????????????: 3?????????????????????????????????")
    @pytest.mark.parametrize("couponStatus", list(combinations("12345678", 3)))
    def test_091_mgmt_fin_voucher_second_coupon_queryList(self, couponStatus):
        
        data = deepcopy(self.data)
        data["couponStatusList"] = list(couponStatus)
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert str(d["couponStatus"]) in list(couponStatus)

    @allure.severity(P2)
    @allure.title("???????????????-????????????: ???????????????????????????")
    @pytest.mark.parametrize("soReturnFlag,ids", [(True, "???"), (False,  "???")])
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
    ??????????????????????????????
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
        self.token = os.environ["token"] # ??????
        self.token_85 = os.environ["token_85"] # ??????85

    @allure.severity(P1)
    @allure.title("???????????????-????????????: VIP??????-?????????->???????????????(???????????????)")
    def test_01_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_3):
            
        getSecondList = vip_Second_2_3

                 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: VIP??????-?????????->???????????????(???????????????)")
    def test_02_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_1):
            
        getSecondList = vip_Second_2_1

                 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: ??????-?????????->??????????????????(????????????)")
    def test_03_mgmt_fin_voucher_second_coupon_queryList(self, yunsh_Second_2_5):
            
        getSecondList = yunsh_Second_2_5

                 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: ??????-?????????->???????????????(?????????????????????)")
    def test_03_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_8):
            
        getSecondList = vip_Second_2_8

                 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: VIP??????-?????????->???????????????(????????????????????????)")
    def test_04_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_7):
            
        getSecondList = vip_Second_2_7
 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: VIP??????-?????????->???????????????(???????????????)")
    def test_05_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_2_6):
            
        getSecondList = vip_Second_2_6
 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: VIP??????-?????????->???????????????(??????????????????-?????????????????????)")
    def test_06_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_7_2_houtai):
            
        getSecondList = vip_Second_7_2_houtai
 
        @allure.step("???????????????")
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
    @allure.title("???????????????-????????????: VIP??????-?????????->???????????????(????????????-?????????????????????)")
    def test_07_mgmt_fin_voucher_second_coupon_queryList(self, vip_Second_7_2_qiantai):
            
        getSecondList = vip_Second_7_2_qiantai
 
        @allure.step("???????????????")
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
