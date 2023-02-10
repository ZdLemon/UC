# coding:utf-8

from api.mall_mgmt_application._mgmt_order_getValetOrderList import params ,_mgmt_order_getValetOrderList

from setting import P1, P2, P3, username

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/getValetOrderList")
class TestClass:
    """
    代客售后列表
    /mgmt/order/getValetOrderList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("代客售后列表-成功路径: 查询默认本月检查")
    def test_01_mgmt_order_getValetOrderList(self):
            
        params = deepcopy(self.params)             
        with _mgmt_order_getValetOrderList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set([d["commitTimeDesc"][:7] for d in r.json()["data"]["list"]]):
                assert i == time.strftime("%Y-%m",time.localtime(time.time()))
            
    @allure.severity(P2)
    @allure.title("代客售后列表-成功路径: 查询会员卡号检查")
    def test_02_mgmt_order_getValetOrderList(self):
            
        params = deepcopy(self.params)  
        params["customerCard"] = username          
        with _mgmt_order_getValetOrderList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set([d["creatorCard"] for d in r.json()["data"]["list"]]):
                assert i == username

    @allure.severity(P2)
    @allure.title("代客售后列表-成功路径: 查询订单编号检查")
    def test_03_mgmt_order_getValetOrderList(self):
        
        orderNo = None
        
        @allure.step("代客售后列表：获取订单编号")
        def step_01_mgmt_order_getValetOrderList():
                
            nonlocal orderNo
            params = deepcopy(self.params)             
            with _mgmt_order_getValetOrderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderNo = r.json()["data"]["list"][0]["orderNo"]
        
        @allure.step("代客售后列表：获取订单编号")
        def step_02_mgmt_order_getValetOrderList(): 
               
            params = deepcopy(self.params)  
            params["orderNo"] = orderNo        
            with _mgmt_order_getValetOrderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["orderNo"]
        
        step_01_mgmt_order_getValetOrderList()
        step_02_mgmt_order_getValetOrderList()


