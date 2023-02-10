# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_revokeWithdraw import _mgmt_fin_voucher_second_coupon_revokeWithdraw
from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/revokeWithdraw")
class TestClass:
    """
    秒返券提现撤销
    /mgmt/fin/voucher/second/coupon/revokeWithdraw
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("秒返券提现撤销-成功路径: 撤销检查")
    def test_01_mgmt_fin_voucher_second_coupon_revokeWithdraw(self):
        
        queryWithdrawList = None
        
        @allure.title("秒返券提现列表,获取Id")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 1 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryWithdrawList = r.json()["data"]["list"][0]

        @allure.title("秒返券提现撤销")
        def step_mgmt_fin_voucher_second_coupon_revokeWithdraw():
            
            data = {
                "id":queryWithdrawList["id"] # 主键id
            }   
            with _mgmt_fin_voucher_second_coupon_revokeWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if queryWithdrawList:
            step_mgmt_fin_voucher_second_coupon_revokeWithdraw()


    @allure.severity(P2)
    @allure.title("秒返券提现撤销-成功路径: 重复撤销检查")
    def test_02_mgmt_fin_voucher_second_coupon_revokeWithdraw(self):
        
        queryWithdrawList = None
        
        @allure.title("秒返券提现列表,获取Id")
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 1 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryWithdrawList = r.json()["data"]["list"][0]

        @allure.title("秒返券提现撤销")
        def step_mgmt_fin_voucher_second_coupon_revokeWithdraw():
            
            data = {
                "id":queryWithdrawList["id"] # 主键id
            }   
            with _mgmt_fin_voucher_second_coupon_revokeWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.title("秒返券提现第二次撤销")
        def step_02_mgmt_fin_voucher_second_coupon_revokeWithdraw():
            
            data = {
                "id":queryWithdrawList["id"] # 主键id
            }   
            with _mgmt_fin_voucher_second_coupon_revokeWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 500
                assert r.json()["message"] == "该记录非待受理状态不能撤销，请刷新后查看"

        
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if queryWithdrawList:
            step_mgmt_fin_voucher_second_coupon_revokeWithdraw()
            step_02_mgmt_fin_voucher_second_coupon_revokeWithdraw()



