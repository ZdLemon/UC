# coding:utf-8

from api.mall_mgmt_application._mgmt_order_return_getOrderRefundList import data, _mgmt_order_return_getOrderRefundList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/getOrderRefundList")
class TestClass:
    """
    管理后台-顾客订单退款失败记录查询
    /mgmt/order/return/getOrderRefundList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("顾客订单退款失败记录查询-成功路径: 查询订单编号检查")
    def test_01_mgmt_order_return_getOrderRefundList(self):
        
        data = deepcopy(self.data)
        data["orderNo"] = "SG031000220317000008"                             
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                assert data["orderNo"] == d["orderNo"]

    @allure.severity(P3)
    @allure.title("顾客订单退款失败记录查询-失败路径: 仅支持精确查询订单编号检查")
    def test_02_mgmt_order_return_getOrderRefundList(self):
        
        data = deepcopy(self.data)
        data["orderNo"] = "SG03100022031700000"                             
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("顾客订单退款失败记录查询-成功路径: 查询申请退款时间检查")
    def test_03_mgmt_order_return_getOrderRefundList(self):
        
        data = deepcopy(self.data)
        data["applyBeginTime"] = "2022-03-17" 
        data["applyEndTime"] = "2022-03-17"                           
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert len(r.json()["data"]["list"]) == 1

    @allure.severity(P3)
    @allure.title("顾客订单退款失败记录查询-成功路径: 查询付款方式检查")
    @pytest.mark.parametrize("payType", [101, 102, 103, 201, 202, 203, 204, 205, 800, 801, 802, 803, 804, 805, 806, 807, 808])
    def test_04_mgmt_order_return_getOrderRefundList(self, payType):
        
        data = deepcopy(self.data)
        data["payType"] = payType                            
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            for i in set(d["payType"] for d in r.json()["data"]["list"]):
                assert data["payType"] == i

    @allure.severity(P2)
    @allure.title("顾客订单退款失败记录查询-成功路径: 查询开单人卡号检查")
    def test_05_mgmt_order_return_getOrderRefundList(self):
        
        data = deepcopy(self.data)
        data["creatorCard"] = "3000003482"                            
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            for i in set(d["customerCard"] for d in r.json()["data"]["list"]):
                assert data["creatorCard"] == i

    @allure.severity(P3)
    @allure.title("顾客订单退款失败记录查询-失败路径: 仅支持精确查询开单人卡号检查")
    def test_06_mgmt_order_return_getOrderRefundList(self):
        
        data = deepcopy(self.data)
        data["creatorCard"] = "300000348"                            
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("顾客订单退款失败记录查询-失败路径: 查询退款进度检查")
    @pytest.mark.parametrize("refundStatus", [2, 4, 5], ids=["退款中", "待对账校验", "成功退款到钱包"])
    def test_07_mgmt_order_return_getOrderRefundList(self, refundStatus):
        
        data = deepcopy(self.data)
        data["refundStatus"] = refundStatus                           
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            for i in set(d["refundStatus"] for d in r.json()["data"]["list"]):
                assert data["refundStatus"] == i

    @allure.severity(P3)
    @allure.title("顾客订单退款失败记录查询-失败路径: 查询退款分公司检查")
    @pytest.mark.parametrize("financeCompanyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_08_mgmt_order_return_getOrderRefundList(self, financeCompanyCode):
        
        data = deepcopy(self.data)
        data["financeCompanyCode"] = financeCompanyCode                          
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            for i in set(d["financeCompanyCode"] for d in r.json()["data"]["list"]):
                assert data["financeCompanyCode"] == i

    @allure.severity(P2)
    @allure.title("顾客订单退款失败记录查询-成功路径: 查询首次发起退款时间检查")
    def test_09_mgmt_order_return_getOrderRefundList(self):
        
        data = deepcopy(self.data)
        data["refundBeginTime"] = "2022-04-12" 
        data["refundEndTime"] = "2022-04-12"                           
        with _mgmt_order_return_getOrderRefundList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(d["refundApplyTime"])/1000)) == "2022-04-12"

















