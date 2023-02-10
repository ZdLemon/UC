# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo import data, _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo

from setting import P1, P2, P3, username, store, username_vip, store_85, username_85, mobile
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/freight/subsidy/queryFreightSubsidyManagerInfo")
class TestClass:
    """
    运费补贴券管理查询
    /mgmt/fin/voucher/freight/subsidy/queryFreightSubsidyManagerInfo
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]

    
    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 查询发放时间默认当月检查")
    def test_01_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self):
        
        data = deepcopy(self.data)                
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(time.strftime("%Y-%m", time.localtime(int(d["createTime"])/1000)) for d in r.json()["data"]["list"]):
                    assert i == time.strftime("%Y-%m",time.localtime(time.time()))

    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("cardNo", [username_85, username_85[:-1]], ids=["正确的负责人卡号", "负责人卡号的一部分"])
    def test_02_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self, cardNo):
        
        data = deepcopy(self.data)
        data["cardNo"] = cardNo        
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == cardNo
            else:
                assert r.json()["data"]["list"] == [] 

    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 支持模糊查询会员手机号检查")
    @pytest.mark.parametrize("mobile", [mobile, mobile[:-1]], ids=["正确的会员手机号", "会员手机号的一部分"])
    def test_03_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self, mobile):
        
        data = deepcopy(self.data)
        data["mobile"] = mobile          
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert mobile in i
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 查询会员身份检查")
    @pytest.mark.parametrize("memberType", [1, 2, 3, 4], ids=["普通顾客", "优惠顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self, memberType):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType          
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["memberType"] for d in r.json()["data"]["list"]):
                    assert i == memberType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("shopCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_04_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self, shopCode):
        
        data = deepcopy(self.data)
        data["shopCode"] = shopCode         
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["shopCode"] for d in r.json()["data"]["list"]):
                    assert  i == shopCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 查询补贴原因检查")
    @pytest.mark.parametrize("subsidyReason", [1, 2, 3, 4, 5, 6, 7], ids=["押货退货", "押货换货", "展业包订购单退货", "展业包订购单换货", "顾客订单退货", "顾客订单换货", "货损货差 "])
    def test_05_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self, subsidyReason):
        
        data = deepcopy(self.data)
        data["subsidyReason"] = subsidyReason # 运费补贴原因 1:押货退货 2:押货换货 3:展业包订购单退货 4:展业包订购单换货 5:顾客订单退货 6:顾客订单换货 7货损货差        
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["subsidyReason"] for d in r.json()["data"]["list"]):
                    assert i == subsidyReason
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("运费补贴券管理查询-成功路径: 查询使用状态检查")
    @pytest.mark.parametrize("freightCouponStatus", [1, 2, 3, 4], ids=["已使用", "未使用", "占用中", "已失效 "])
    def test_06_mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(self, freightCouponStatus):
        
        data = deepcopy(self.data)
        data["freightCouponStatus"] = freightCouponStatus # 运费补贴券状态 1:已使用 2:未使用 3:占用中 4:已失效          
        with _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyManagerInfo(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["freightCouponStatus"] for d in r.json()["data"]["list"]):
                    assert i == freightCouponStatus
            else:
                assert r.json()["data"]["list"] == []
