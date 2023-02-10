# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_getSecondCouponGetDetail import data, _mgmt_fin_voucher_getSecondCouponGetDetail

from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay
from api.mall_mobile_application._mobile_product_getProductDetail import params, _mobile_product_getProductDetail
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit

from api.mall_mobile_application._mobile_order_return_applyReturn import data as data06, _mobile_order_return_applyReturn

from api.basic_services._jobinfo_trigger import _jobinfo_trigger
from api.basic_services._xxl_job_admin_login import xxl_job_admin_login
from util.stepreruns import stepreruns
from setting import P1, P2, P3, username, store, name, username_vip, name_vip

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/getSecondCouponGetDetail")
class TestClass:
    """
    秒返券获券明细:搜索检查
    /mgmt/fin/voucher/getSecondCouponGetDetail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 查询默认条件检查")
    def test_01_mgmt_fin_voucher_getSecondCouponGetDetail(self):
        
        data = deepcopy(self.data)
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 仅支持精确查询会员卡号检查")
    def test_02_mgmt_fin_voucher_getSecondCouponGetDetail(self):

        getSecondCouponGetDetail = None
        
        @allure.step("秒返券获券明细: 获取会员卡号")
        def step_01_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            nonlocal getSecondCouponGetDetail
            data = deepcopy(self.data)
            data["pageSize"] = 100        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["cardNo"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("秒返券获券明细")
        def step_02_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            data = deepcopy(self.data)
            data["cardNo"] = getSecondCouponGetDetail["cardNo"]        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                        assert i == getSecondCouponGetDetail["cardNo"] 
        
        step_01_mgmt_fin_voucher_getSecondCouponGetDetail()
        if getSecondCouponGetDetail:
            step_02_mgmt_fin_voucher_getSecondCouponGetDetail()  

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["vip顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_getSecondCouponGetDetail(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType         
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                    assert i == data["memberType"]  

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 仅支持精确查询来源订单检查")
    def test_04_mgmt_fin_voucher_getSecondCouponGetDetail(self):
        
        getSecondCouponGetDetail = None
        
        @allure.step("秒返券获券明细: 获取来源订单")
        def step_01_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            nonlocal getSecondCouponGetDetail
            data = deepcopy(self.data)
            data["pageSize"] = 100        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["sourceOrderNo"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("秒返券获券明细")
        def step_02_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            data = deepcopy(self.data)
            data["sourceOrderNo"] = getSecondCouponGetDetail["sourceOrderNo"]        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                for i in set(d["sourceOrderNo"] for d in r.json()["data"]["list"]):
                        assert i == getSecondCouponGetDetail["sourceOrderNo"] 
        
        step_01_mgmt_fin_voucher_getSecondCouponGetDetail()
        if getSecondCouponGetDetail:
            step_02_mgmt_fin_voucher_getSecondCouponGetDetail()  

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 单选查询交易类型检查")
    @pytest.mark.parametrize("getType", [1, 2], ids=["购物获得", "月结更新"])
    def test_05_mgmt_fin_voucher_getSecondCouponGetDetail(self, getType):
        
        data = deepcopy(self.data)
        data["getType"] = getType       
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["getType"] for d in r.json()["data"]["list"]):
                    assert i == getType 

    @allure.severity(P2)
    @allure.title("秒返券获券明细: 仅支持精确查询服务中心编号检查")
    def test_06_mgmt_fin_voucher_getSecondCouponGetDetail(self):
        
        getSecondCouponGetDetail = None
        
        @allure.step("秒返券获券明细: 获取服务中心编号")
        def step_01_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            nonlocal getSecondCouponGetDetail
            data = deepcopy(self.data)
            data["pageSize"] = 100        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["sourceStoreCode"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("秒返券获券明细")
        def step_02_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            data = deepcopy(self.data)
            data["sourceStoreCode"] = getSecondCouponGetDetail["sourceStoreCode"]        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                for i in set(d["sourceStoreCode"] for d in r.json()["data"]["list"]):
                    assert i == getSecondCouponGetDetail["sourceStoreCode"] 
        
        step_01_mgmt_fin_voucher_getSecondCouponGetDetail()
        if getSecondCouponGetDetail:
            step_02_mgmt_fin_voucher_getSecondCouponGetDetail()  

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 查询券状态检查")
    @pytest.mark.parametrize("couponStatus", [1, 2, 3, 4], ids=["待生效", "已生效", "退货失效", "月结失效"])
    def test_07_mgmt_fin_voucher_getSecondCouponGetDetail(self, couponStatus):
        
        data = deepcopy(self.data)
        data["couponStatus"] = couponStatus       
        with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:            
                for i in set(d["couponStatus"] for d in r.json()["data"]["list"]):
                    assert i == couponStatus

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 查询生成时间检查")
    def test_08_mgmt_fin_voucher_getSecondCouponGetDetail(self):

        getSecondCouponGetDetail = None
        
        @allure.step("秒返券获券明细: 获取生成时间")
        def step_01_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            nonlocal getSecondCouponGetDetail
            data = deepcopy(self.data)
            data["pageSize"] = 100        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["getTimeDesc"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("秒返券获券明细")
        def step_02_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            data = deepcopy(self.data)
            data["getStartTime"] = f'{getSecondCouponGetDetail["getTimeDesc"][:10]} 00:00:00' #"2022-03-25 00:00:00"
            data["getEndTime"] = f'{getSecondCouponGetDetail["getTimeDesc"][:10]} 23:59:59' #"2022-03-25 23:59:59"        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                for i in set(d["getTimeDesc"][:10] for d in r.json()["data"]["list"]):
                    assert i == getSecondCouponGetDetail["getTimeDesc"][:10]
        
        step_01_mgmt_fin_voucher_getSecondCouponGetDetail()
        if getSecondCouponGetDetail:
            step_02_mgmt_fin_voucher_getSecondCouponGetDetail()

    @allure.severity(P2)
    @allure.title("秒返券获券明细-成功路径: 查询业绩月份检查")
    def test_09_mgmt_fin_voucher_getSecondCouponGetDetail(self):
        
        getSecondCouponGetDetail = None
        
        @allure.step("秒返券获券明细: 获取业绩月份")
        def step_01_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            nonlocal getSecondCouponGetDetail
            data = deepcopy(self.data)
            data["pageSize"] = 100        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["sourceOrderMonth"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("秒返券获券明细")
        def step_02_mgmt_fin_voucher_getSecondCouponGetDetail():
            
            data = deepcopy(self.data)
            data["transMonthEnd"] = getSecondCouponGetDetail["sourceOrderMonth"]
            data["transMonthStart"] = getSecondCouponGetDetail["sourceOrderMonth"]        
            with _mgmt_fin_voucher_getSecondCouponGetDetail(data, self.access_token) as r:
                for i in set(d["sourceOrderMonth"] for d in r.json()["data"]["list"]):
                    assert i == getSecondCouponGetDetail["sourceOrderMonth"] 
        
        step_01_mgmt_fin_voucher_getSecondCouponGetDetail()
        if getSecondCouponGetDetail:
            step_02_mgmt_fin_voucher_getSecondCouponGetDetail()  


