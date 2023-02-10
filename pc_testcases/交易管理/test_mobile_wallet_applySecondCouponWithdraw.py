# coding:utf-8

from api.mall_mobile_application._mobile_wallet_getSecondCouponList import data, _mobile_wallet_getSecondCouponList
from api.mall_mobile_application._mobile_wallet_applySecondCouponWithdraw import data as data02, _mobile_wallet_applySecondCouponWithdraw
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/wallet/applySecondCouponWithdraw")
class TestClass:
    """
    秒返券申请提现
    /mobile/wallet/applySecondCouponWithdraw
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.token = os.environ["token"]
        self.vip_token = os.environ["vip_token"]

    @allure.severity(P1)
    @allure.title(" 秒返券申请提现-成功路径:  秒返券申请提现检查")
    def test_01_mobile_wallet_applySecondCouponWithdraw(self):

        secondCouponId = None
        
        @allure.step("秒返券列表,获取未使用秒返券Id")
        def step_mobile_wallet_getSecondCouponList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data)
            data["couponStatusList"] = [2] # 使用状态集合，商城使用，比如：未使用传[2]；占用中传[3]；已使用传[1]；已失效传[4,5]；已提现传[6,7]
            with _mobile_wallet_getSecondCouponList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
                
        @allure.step("秒返券申请提现")
        def step_mobile_wallet_applySecondCouponWithdraw():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"] = [secondCouponId]
            with _mobile_wallet_applySecondCouponWithdraw(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200  
        
        step_mobile_wallet_getSecondCouponList() 
        step_mobile_wallet_applySecondCouponWithdraw()         

    @allure.severity(P2)
    @allure.title(" 秒返券申请提现-失败路径:  秒返券重复申请提现检查")
    def test_02_mobile_wallet_applySecondCouponWithdraw(self):

        secondCouponId = None
        
        @allure.step("秒返券列表,获取未使用秒返券Id")
        def step_mobile_wallet_getSecondCouponList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data)
            data["couponStatusList"] = [2] # 使用状态集合，商城使用，比如：未使用传[2]；占用中传[3]；已使用传[1]；已失效传[4,5]；已提现传[6,7]
            with _mobile_wallet_getSecondCouponList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
                
        @allure.step("秒返券第一次申请提现")
        def step_01_mobile_wallet_applySecondCouponWithdraw():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"] = [secondCouponId]
            with _mobile_wallet_applySecondCouponWithdraw(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("秒返券第二次申请提现")
        def step_02_mobile_wallet_applySecondCouponWithdraw():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"] = [secondCouponId]
            with _mobile_wallet_applySecondCouponWithdraw(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 500
                assert r.json()["message"] == "存在非未使用状态的秒返券无法申请提现"  
        
        step_mobile_wallet_getSecondCouponList() 
        step_01_mobile_wallet_applySecondCouponWithdraw() 
        step_02_mobile_wallet_applySecondCouponWithdraw()        

    @allure.severity(P1)
    @allure.title(" 秒返券申请提现-成功路径:  10张秒返券申请提现检查")
    def test_03_mobile_wallet_applySecondCouponWithdraw(self):

        secondCouponId = []
        
        @allure.step("秒返券列表,获取10张未使用秒返券Id")
        def step_mobile_wallet_getSecondCouponList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data)
            data["couponStatusList"] = [2] # 使用状态集合，商城使用，比如：未使用传[2]；占用中传[3]；已使用传[1]；已失效传[4,5]；已提现传[6,7]
            with _mobile_wallet_getSecondCouponList(data, self.vip_token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    secondCouponId.append(d["secondCouponId"])
                
        @allure.step("秒返券申请提现")
        def step_mobile_wallet_applySecondCouponWithdraw():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"] = secondCouponId
            with _mobile_wallet_applySecondCouponWithdraw(data, self.vip_token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mobile_wallet_getSecondCouponList() 
        step_mobile_wallet_applySecondCouponWithdraw()       



