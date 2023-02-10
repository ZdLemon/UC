# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawdtlList import params, _mgmt_fin_voucher_second_coupon_queryWithdrawdtlList
from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryWithdrawdtlList")
class TestClass:
    """
    秒返券提现详情查询
    /mgmt/fin/voucher/second/coupon/queryWithdrawdtlList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("秒返券提现详情查询-成功路径: 待处理秒返券详情检查")
    def test_01_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList(self):
        
        queryWithdrawList = None
        
        @allure.step("秒返券提现列表,获取Id")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 1 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryWithdrawList = r.json()["data"]["list"][0]

        @allure.step("秒返券提现详情查询")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList():
            
            params = {
                "withdrawId":queryWithdrawList["id"] # 主键id
            }   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawdtlList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["secondCouponNum"] == queryWithdrawList["secondCouponNum"]
                assert r.json()["data"]["withdrawAmount"] == queryWithdrawList["withdrawAmount"]
                assert r.json()["data"]["withdrawNo"] == queryWithdrawList["withdrawNo"]
                assert r.json()["data"]["withdrawStatus"] == queryWithdrawList["withdrawStatus"]
                assert r.json()["data"]["withdrawStatusDesc"] == queryWithdrawList["withdrawStatusDesc"]
                assert r.json()["data"]["withdrawTimeDesc"] == queryWithdrawList["withdrawTimeDesc"]
       
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if queryWithdrawList:
            step_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList()
        
    @allure.severity(P2)
    @allure.title("秒返券提现详情查询-成功路径: 已处理秒返券详情检查")
    def test_02_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList(self):
        
        queryWithdrawList = None
        
        @allure.step("秒返券提现列表,获取Id")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryWithdrawList = r.json()["data"]["list"][0]

        @allure.step("秒返券提现详情查询")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList():
            
            params = {
                "withdrawId":queryWithdrawList["id"] # 主键id
            }   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawdtlList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["secondCouponNum"] == queryWithdrawList["secondCouponNum"]
                assert r.json()["data"]["withdrawAmount"] == queryWithdrawList["withdrawAmount"]
                assert r.json()["data"]["withdrawNo"] == queryWithdrawList["withdrawNo"]
                assert r.json()["data"]["withdrawStatus"] == queryWithdrawList["withdrawStatus"]
                assert r.json()["data"]["withdrawStatusDesc"] == queryWithdrawList["withdrawStatusDesc"]
                assert r.json()["data"]["withdrawTimeDesc"] == queryWithdrawList["withdrawTimeDesc"]
       
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if queryWithdrawList:
            step_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList()
        
    @allure.severity(P2)
    @allure.title("秒返券提现详情查询-成功路径: 已撤销秒返券详情检查")
    def test_03_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList(self):
        
        queryWithdrawList = None
        
        @allure.step("秒返券提现列表,获取Id")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryWithdrawList = r.json()["data"]["list"][0]

        @allure.step("秒返券提现详情查询")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList():
            
            params = {
                "withdrawId":queryWithdrawList["id"] # 主键id
            }   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawdtlList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["secondCouponNum"] == queryWithdrawList["secondCouponNum"]
                assert r.json()["data"]["withdrawAmount"] == queryWithdrawList["withdrawAmount"]
                assert r.json()["data"]["withdrawNo"] == queryWithdrawList["withdrawNo"]
                assert r.json()["data"]["withdrawStatus"] == queryWithdrawList["withdrawStatus"]
                assert r.json()["data"]["withdrawStatusDesc"] == queryWithdrawList["withdrawStatusDesc"]
                assert r.json()["data"]["withdrawTimeDesc"] == queryWithdrawList["withdrawTimeDesc"]
       
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if queryWithdrawList:
            step_mgmt_fin_voucher_second_coupon_queryWithdrawdtlList()
        

