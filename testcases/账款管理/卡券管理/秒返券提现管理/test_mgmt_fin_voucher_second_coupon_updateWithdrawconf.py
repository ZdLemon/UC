# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_updateWithdrawconf import data, _mgmt_fin_voucher_second_coupon_updateWithdrawconf

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryWithdrawconfLog import _mgmt_fin_voucher_second_coupon_queryWithdrawconfLog
from setting import P1, P2, P3, username, store, username_vip
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/updateWithdrawconf")
class TestClass:
    """
    秒返券提现配置修改
    /mgmt/fin/voucher/second/coupon/updateWithdrawconf
    """
    
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P1)
    @allure.title("秒返券提现配置修改-成功路径: 配置修改检查")
    def test_mgmt_fin_voucher_second_coupon_updateWithdrawconf(self, login_2):
        
        @allure.step("秒返券提现配置修改")
        def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
            
            data = deepcopy(self.data) 
            data["maxNum"] = 200
            data["minAmount"] = 20
            data["remark"] = """
            
            1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
            2. 来源订单提交售后后：
                a、此订单关联的未使用购物秒返券需锁定
                b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
            
            3.1.0需求：
            拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
            1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
            2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
            """
            
            with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("秒返券提现配置修改记录,确认是否修改成功")
        @stepreruns()
        def step_mgmt_fin_voucher_second_coupon_queryWithdrawconfLog():
    
            with _mgmt_fin_voucher_second_coupon_queryWithdrawconfLog(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["updateNum"] == 200
                assert r.json()["data"][0]["updateAmount"] == 20
                assert r.json()["data"][0]["operatorTimeDesc"][:10] == time.strftime("%Y-%m-%d",time.localtime(time.time()))
                assert r.json()["data"][0]["operatorName"] == login_2["data"]["username"]
    
        step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()
        step_mgmt_fin_voucher_second_coupon_queryWithdrawconfLog()
        


