# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_wallet_getTransDetail import data, _mgmt_fin_wallet_getTransDetail # 完美钱包管理-交易详情
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest
from operator import itemgetter

from util.stepreruns import stepreruns
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/wallet/getTransDetail")
class TestClass:
    """
    完美钱包管理-交易详情
    /mgmt/fin/wallet/getTransDetail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
        
    @allure.severity(P2)
    @allure.title("钱包交易详情-成功路径: 查询报表字段检查")
    @pytest.mark.parametrize("reportField", [1, 2, 3], ids=["本期汇款", "本期使用", "本期提现"])
    def test_01_mgmt_fin_wallet_getTransDetail(self, reportField, login_oauth_token):
        
        data = deepcopy(self.data) 
        data["walletId"] = login_oauth_token["data"]["userId"]  
        data["reportField"] = reportField                    
        with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
            if r.json()["data"]["page"]:
                for i in set(d["backstageTransType"] for d in r.json()["data"]["page"]["list"]):
                    if data["reportField"] == 1:
                        assert i in [1, 2, 7, 9, 10, 11, 12, 13, 16]
                    elif data["reportField"] == 2:
                        assert i in [3, 8, 16, 17, 18]
                    elif data["reportField"] == 3:
                        assert i in [6]
            else:
                assert r.json()["data"]["page"] is None

    @allure.severity(P2)
    @allure.title("钱包交易详情-成功路径: 查询前端交易类型检查")
    @pytest.mark.parametrize("receptionTransType", list(range(1, 11)), ids=["汇入", "退货", "购货", "提现", "退款", "信用额", "转款", "其他", "预售定金", "定金返还"])
    def test_02_mgmt_fin_wallet_getTransDetail(self, receptionTransType, login_oauth_token):
        
        data = deepcopy(self.data) 
        data["walletId"] = login_oauth_token["data"]["userId"]    
        data["receptionTransType"] = receptionTransType                   
        with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
            if r.json()["data"]["page"]:
                for i in set(d["receptionTransType"] for d in r.json()["data"]["page"]["list"]):
                    if data["receptionTransType"] == 1:
                        assert i in [1, 2, 9, 10, 16]
                    elif data["receptionTransType"] == 2:
                        assert i in [3]
                    elif data["receptionTransType"] == 3:
                        assert i in [8]
                    elif data["receptionTransType"] == 4:
                        assert i in [6]
                    elif data["receptionTransType"] == 5:
                        assert i in [7, 11]
                    elif data["receptionTransType"] == 6:
                        assert i in [14, 15]
                    elif data["receptionTransType"] == 7:
                        assert i in [12]
                    elif data["receptionTransType"] == 8:
                        assert i in [13]
                    elif data["receptionTransType"] == 9:
                        assert i in [17]
                    elif data["receptionTransType"] == 10:
                        assert i in [18]
            else:
                assert r.json()["data"]["page"] is None

    @allure.severity(P2)
    @allure.title("钱包交易详情-成功路径: 查询后台交易类型检查")
    @pytest.mark.parametrize("backstageTransType", list(range(1, 17)), ids=["充值", "购货转入", "退货转入", "购货支付", "提现", "原路退款", "信用额增加", "信用额扣减", "还欠款", "补银行流水", "手工退款", "押货款与钱包互转", "其他", "定金转入", "预售定金", "定金返还"])
    def test_03_mgmt_fin_wallet_getTransDetail(self, backstageTransType,  login_oauth_token):
        
        data = deepcopy(self.data) 
        data["walletId"] = login_oauth_token["data"]["userId"]  
        data["backstageTransType"] = backstageTransType                   
        with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
            if r.json()["data"]["page"]:
                for i in set(d["backstageTransType"] for d in r.json()["data"]["page"]["list"]):
                    if data["backstageTransType"] == 1:
                        assert i == 1
                    elif data["backstageTransType"] == 2:
                        assert i == 2
                    elif data["backstageTransType"] == 3:
                        assert i == 3    
                    elif data["backstageTransType"] == 4:
                        assert i == 8
                    elif data["backstageTransType"] == 5:
                        assert i == 6
                    elif data["backstageTransType"] == 6:
                        assert i == 7
                    elif data["backstageTransType"] == 7:
                        assert i == 14
                    elif data["backstageTransType"] == 8:
                        assert i == 15
                    elif data["backstageTransType"] == 9:
                        assert i == 9
                    elif data["backstageTransType"] == 10:
                        assert i == 10
                    elif data["backstageTransType"] == 11:
                        assert i == 11
                    elif data["backstageTransType"] == 12:
                        assert i == 12
                    elif data["backstageTransType"] == 13:
                        assert i == 13
                    elif data["backstageTransType"] == 14:
                        assert i == 16
                    elif data["backstageTransType"] == 15:
                        assert i == 17
                    elif data["backstageTransType"] == 16:
                        assert i == 18 
            else:
                assert r.json()["data"]["page"] is None                 

    @allure.severity(P2)
    @allure.title("钱包交易详情-成功路径: 查询订单编号检查")
    @stepreruns(counts=2)
    def test_04_mgmt_fin_wallet_getTransDetail(self, login_oauth_token):
        
        orderNo = None
        
        @allure.step("获取订单编号")
        def step_01_mgmt_fin_wallet_getTransDetail():
            
            nonlocal orderNo
            data = deepcopy(self.data) 
            data["walletId"] = login_oauth_token["data"]["userId"]  
            data["backstageTransType"] = 4               
            with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderNo = r.json()["data"]["page"]["list"][0]["orderNo"]

        @allure.step("查询订单编号")
        def step_02_mgmt_fin_wallet_getTransDetail():
            
            data = deepcopy(self.data) 
            data["walletId"] = login_oauth_token["data"]["userId"]
            data["orderNo"] = orderNo 
            data["backstageTransType"] = None             
            with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
                for i in set(d["orderNo"] for d in r.json()["data"]["page"]["list"]):
                    assert i == orderNo
                    
        step_01_mgmt_fin_wallet_getTransDetail()
        step_02_mgmt_fin_wallet_getTransDetail()
        
    @allure.severity(P2)
    @allure.title("钱包交易详情-失败路径: 仅支持精确查询订单编号检查")
    def test_041_mgmt_fin_wallet_getTransDetail(self, login_oauth_token):
        
        data = deepcopy(self.data) 
        data["walletId"] = login_oauth_token["data"]["userId"]  
        data["backstageTransType"] = 4                
        with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            orderNo = r.json()["data"]["page"]["list"][0]["orderNo"]

        data["backstageTransType"] = None   
        data["orderNo"] = orderNo[:-1]      
        with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
            assert r.json()["data"]["page"] is None

    @allure.severity(P2)
    @allure.title("钱包交易详情-成功路径: 查询是否有信用额检查")
    @pytest.mark.parametrize("creditEnable", [True, False], ids=["是", "否"])
    def test_05_mgmt_fin_wallet_getTransDetail(self, creditEnable, login_oauth_token):
        
        data = deepcopy(self.data) 
        data["walletId"] = login_oauth_token["data"]["userId"]   
        data["creditEnable"] = creditEnable                    
        with _mgmt_fin_wallet_getTransDetail(data, self.access_token) as r:
            if r.json()["data"]["page"]:
                for i in set(d["backstageTransType"] for d in r.json()["data"]["page"]["list"]):
                    if data["creditEnable"]:
                        assert i in [14, 15]
                    else:
                        assert i in [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18]
            else:
                assert r.json()["data"]["page"] is None










