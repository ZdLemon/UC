# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_acceptWithdraw import _mgmt_fin_voucher_second_coupon_acceptWithdraw
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawdtlList import params, _mgmt_fin_voucher_second_coupon_queryWithdrawdtlList
from setting import P1, P2, P3, username, store, username_vip
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/acceptWithdraw")
class TestClass:
    """
    秒返券提现受理接口
    /mgmt/fin/voucher/second/coupon/acceptWithdraw
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P1)
    @allure.title("秒返券提现受理-成功路径: 批量受理检查")
    def test_01_mgmt_fin_voucher_second_coupon_acceptWithdraw(self):
        
        queryWithdrawList = [] # 秒返券提现列表
        
        @allure.title("秒返券提现列表,获取Id")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 1 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        queryWithdrawList.append(i)

        @allure.title("秒返券提现受理")
        def step_mgmt_fin_voucher_second_coupon_acceptWithdraw():
            
            data = {
                "batchMonth": queryWithdrawList[0]["withdrawNo"][2:8], # 业绩月份YYYYMM
                "remark":"同意提现", # 备注
                "idList":[i["id"] for i in queryWithdrawList] # 主键id集合
            }   
            with _mgmt_fin_voucher_second_coupon_acceptWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if queryWithdrawList:
            step_mgmt_fin_voucher_second_coupon_acceptWithdraw()

    @allure.severity(P2)
    @allure.title("秒返券提现受理-失败路径: 已提现的不能再提现检查")
    def test_02_mgmt_fin_voucher_second_coupon_acceptWithdraw(self):
        
        queryWithdrawList = None # 秒返券提现列表
        
        @allure.title("秒返券提现列表,获取Id")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    queryWithdrawList = r.json()["data"]["list"][0]
        
        @allure.step("秒返券提现受理")
        def step_mgmt_fin_voucher_second_coupon_acceptWithdraw():
            
            data = {
                "batchMonth": queryWithdrawList["withdrawNo"][2:8], # 业绩月份YYYYMM
                "remark":"同意提现", # 备注
                "idList":[queryWithdrawList["id"]] # 主键id集合
            }   
            with _mgmt_fin_voucher_second_coupon_acceptWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 500
                assert r.json()["message"] == "选中的记录存在非待受理的，请刷新列表后重试"
        
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        step_mgmt_fin_voucher_second_coupon_acceptWithdraw()

    @allure.severity(P2)
    @allure.title("秒返券提现受理-失败路径: 已撤销的不能再受理检查")
    def test_03_mgmt_fin_voucher_second_coupon_acceptWithdraw(self):
        
        queryWithdrawList = None
        
        @allure.title("秒返券提现列表,获取Id")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal queryWithdrawList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 3 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
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
            with _mgmt_fin_voucher_second_coupon_acceptWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 500

        
        step_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        step_mgmt_fin_voucher_second_coupon_acceptWithdraw()

    @allure.severity(P2)
    @allure.title("秒返券提现受理-成功路径: 批量受理中有已受理的秒返券检查")
    def test_04_mgmt_fin_voucher_second_coupon_acceptWithdraw(self):
        
        batchMonth = None
        idList = []
        
        @allure.title("秒返券提现列表,获取待处理的Id")
        @stepreruns()
        def step_01_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal batchMonth, idList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 1 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    batchMonth = r.json()["data"]["list"][0]["withdrawNo"][2:8]
                    idList.append(r.json()["data"]["list"][0]["id"])
        
        @allure.title("秒返券提现列表,获取已处理的Id")
        def step_02_mgmt_fin_voucher_second_coupon_queryWithdrawList():
            
            nonlocal idList
            data = deepcopy(self.data)
            data["withdrawStatus"] = 2 # 提现状态，1：待受理；2：已受理；3：已撤销   
            with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    idList.append(r.json()["data"]["list"][0]["id"])

        @allure.title("秒返券提现")
        def step_mgmt_fin_voucher_second_coupon_acceptWithdraw():
            
            data = {
                "batchMonth": batchMonth, # 业绩月份YYYYMM
                "remark":"同意提现", # 备注
                "idList":idList # 主键id集合
            }   
            with _mgmt_fin_voucher_second_coupon_acceptWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_01_mgmt_fin_voucher_second_coupon_queryWithdrawList()
        if idList:
            step_02_mgmt_fin_voucher_second_coupon_queryWithdrawList()
            step_mgmt_fin_voucher_second_coupon_acceptWithdraw()



