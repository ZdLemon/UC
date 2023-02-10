# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawList import data, _mgmt_fin_voucher_second_coupon_queryWithdrawList
from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/queryWithdrawList")
class TestClass:
    """
    秒返券提现列表
    /mgmt/fin/voucher/second/coupon/queryWithdrawList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("秒返券提现列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username, username[:-1]], ids=["完整的会员卡号", "会员卡号的一部分"])
    def test_01_mgmt_fin_voucher_second_coupon_queryWithdrawList(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo         
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                        assert i == username  
            else:
                assert r.json()["data"]["list"] == []  

    @allure.severity(P2)
    @allure.title("秒返券提现列表: 仅支持精确查询会员手机号检查")
    def test_02_mgmt_fin_voucher_second_coupon_queryWithdrawList(self, login_oauth_token):
        
        data = deepcopy(self.data)
        data["mobile"] = login_oauth_token["data"]["mobile"]          
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == data["mobile"]  
        
        data["mobile"] = login_oauth_token["data"]["mobile"][:-1]     
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            assert r.json()["data"]["list"] == []  

    @allure.severity(P2)
    @allure.title("秒返券提现列表-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_second_coupon_queryWithdrawList(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType        
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                        assert i == memberType 
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券提现列表-成功路径: 查询批次号检查")
    def test_04_mgmt_fin_voucher_second_coupon_queryWithdrawList(self):
        
        data = deepcopy(self.data)
        data["withdrawBatch"] = f'{time.strftime("%Y%m",time.localtime(time.time()))}001' 
        data["withdrawStatus"] = 2  # 提现状态，1：待受理；2：已受理；3：已撤销
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["withdrawBatch"] for d in r.json()["data"]["list"]):
                        assert i == data["withdrawBatch"] 
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("秒返券提现列表-成功路径: 查询提现时间检查")
    def test_05_mgmt_fin_voucher_second_coupon_queryWithdrawList(self):
        
        data = deepcopy(self.data) 
        data["withdrawEndTimeStr"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        data["withdrawStartTimeStr"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        data["withdrawStatus"] = 2  # 提现状态，1：待受理；2：已受理；3：已撤销  
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            for i in set(d["withdrawTimeDesc"][0:10] for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m-%d",time.localtime(time.time()))

    @allure.severity(P2)
    @allure.title("秒返券提现列表-成功路径: 查询提现状态检查")
    @pytest.mark.parametrize("withdrawStatus,ids", [(1, "待受理"), (2, "已受理"), (3, "已撤销")])
    def test_06_mgmt_fin_voucher_second_coupon_queryWithdrawList(self, withdrawStatus, ids):
                
        data = deepcopy(self.data) 
        data["withdrawStatus"] = withdrawStatus  # 提现状态，1：待受理；2：已受理；3：已撤销  
        with _mgmt_fin_voucher_second_coupon_queryWithdrawList(data, self.access_token) as r:
            for i in set(d["withdrawStatus"] for d in r.json()["data"]["list"]):
                    assert i == withdrawStatus