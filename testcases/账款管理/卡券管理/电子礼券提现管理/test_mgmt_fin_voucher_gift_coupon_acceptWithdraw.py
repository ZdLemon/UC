# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_gift_coupon_queryPendingWithdrawList import data, _mgmt_fin_voucher_gift_coupon_queryPendingWithdrawList # 电子礼券提现列表
from api.mall_mgmt_application._mgmt_fin_voucher_gift_coupon_queryWithdrawdtlList import _mgmt_fin_voucher_gift_coupon_queryWithdrawdtlList # 电子礼券提现详情查询
from api.mall_mgmt_application._mgmt_fin_voucher_gift_coupon_acceptWithdraw import _mgmt_fin_voucher_gift_coupon_acceptWithdraw # 电子礼券提现受理

from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/gift/coupon/acceptWithdraw")
class TestClass:
    """
    电子礼券提现受理
    /mgmt/fin/voucher/gift/coupon/acceptWithdraw
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("电子礼券提现受理-成功路径: 主路径检查")
    def test_01_mgmt_fin_voucher_gift_coupon_acceptWithdraw(self):
        
        queryPendingWithdrawList = {}
        
        @allure.step("电子礼券提现列表：获取待受理的withdrawId")
        def step_mgmt_fin_voucher_gift_coupon_queryPendingWithdrawList():
            
            nonlocal queryPendingWithdrawList
            data = deepcopy(self.data)       
            with _mgmt_fin_voucher_gift_coupon_queryPendingWithdrawList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    queryPendingWithdrawList = r.json()["data"][0] 
                
        @allure.step("电子礼券提现受理")
        def step_mgmt_fin_voucher_gift_coupon_acceptWithdraw():
            
            data = {
                "remark": f"我同意您提现了:{queryPendingWithdrawList['withdrawNo']}", # 备注
                "idList": [queryPendingWithdrawList["id"]] # 主键id集合
            }      
            with _mgmt_fin_voucher_gift_coupon_acceptWithdraw(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"        
        
        @allure.step("电子礼券提现详情查询:确认受理成功")
        def step_mgmt_fin_voucher_gift_coupon_queryWithdrawdtlList():
            
            params = {
                "withdrawId": queryPendingWithdrawList["id"]
            }    
            with _mgmt_fin_voucher_gift_coupon_queryWithdrawdtlList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["withdrawStatus"] == 2 # 状态
                assert r.json()["data"]["withdrawStatusDesc"] == "已受理" # 状态
                assert r.json()["data"]["withdrawAmount"] == queryPendingWithdrawList["withdrawAmount"] # 金额
                assert r.json()["data"]["giftCouponNum"] == queryPendingWithdrawList["giftCouponNum"] # 数量
                assert r.json()["data"]["withdrawTimeDesc"] == queryPendingWithdrawList["withdrawTimeDesc"] # 提现时间
                withdrawAmount = 0
                for i in r.json()["data"]["withdrawdtlDtoList"]:
                    withdrawAmount += i["giftCouponAmount"]
                assert r.json()["data"]["withdrawAmount"] == withdrawAmount
                assert r.json()["data"]["withdrawNo"] == queryPendingWithdrawList["withdrawNo"] # 提现批次号
                assert r.json()["data"]["receiveTimeDesc"][:10] == time.strftime("%Y-%m-%d",time.localtime(time.time()))
       
        step_mgmt_fin_voucher_gift_coupon_queryPendingWithdrawList()
        if queryPendingWithdrawList:
            step_mgmt_fin_voucher_gift_coupon_acceptWithdraw()
            step_mgmt_fin_voucher_gift_coupon_queryWithdrawdtlList()
        



