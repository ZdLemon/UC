# coding:utf-8

from api.mall_center_member._member_mgmt_getBusinessList import params, _member_mgmt_getBusinessList

from util.stepreruns import stepreruns
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/member/mgmt/getBusinessList")
class TestClass:
    """
    获取云商微店列表
    /member/mgmt/getBusinessList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询开卡方式检查")
    @pytest.mark.parametrize("companyNo", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_01_member_mgmt_getBusinessList(self, companyNo):
        
        params = deepcopy(self.params)
        params["companyNo"] = companyNo  
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["rdcCompanyNo"] for d in r.json()["data"]["list"]):
                    assert i == companyNo 

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询会员卡号检查")
    def test_02_member_mgmt_getBusinessList(self):

        getSecondCouponGetDetail = None
        
        @allure.step("获取云商微店列表: 获取会员卡号")
        def step_01_member_mgmt_getBusinessList():
            
            nonlocal getSecondCouponGetDetail
            params = deepcopy(self.params)
            params["pageSize"] = 100     
            with _member_mgmt_getBusinessList(params, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["cardNo"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("获取云商微店列表")
        def step_02_member_mgmt_getBusinessList():
            
            params = deepcopy(self.params)
            params["cardNo"] = getSecondCouponGetDetail["cardNo"] 
            params["openCardTime"] = None      
            with _member_mgmt_getBusinessList(params, self.access_token) as r:
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == getSecondCouponGetDetail["cardNo"] 
        
        step_01_member_mgmt_getBusinessList()
        if getSecondCouponGetDetail:
            step_02_member_mgmt_getBusinessList() 

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询顾客类型检查")
    @pytest.mark.parametrize("businessType", [1, 2], ids=["云商", "微店"])
    def test_03_member_mgmt_getBusinessList(self, businessType):
        
        params = deepcopy(self.params)
        params["businessType"] = businessType  # 顾客类型：1->云商；2->微店（云+）    
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["businessType"] for d in r.json()["data"]["list"]):
                    assert i == businessType  

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询注册手机号检查")
    def test_04_member_mgmt_getBusinessList(self):

        getSecondCouponGetDetail = None
        
        @allure.step("获取云商微店列表: 获取注册手机号")
        def step_01_member_mgmt_getBusinessList():
            
            nonlocal getSecondCouponGetDetail
            params = deepcopy(self.params)
            params["pageSize"] = 100        
            with _member_mgmt_getBusinessList(params, self.access_token) as r:
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["mobile"]:
                            getSecondCouponGetDetail = i
                            
        @allure.title("获取云商微店列表")
        def step_02_member_mgmt_getBusinessList():
            
            params = deepcopy(self.params)
            params["mobile"] = getSecondCouponGetDetail["mobile"]
            params["openCardTime"] = None        
            with _member_mgmt_getBusinessList(params, self.access_token) as r:
                for i in set(d["mobile"] for d in r.json()["data"]["list"]):
                    assert i == getSecondCouponGetDetail["mobile"] 
        
        step_01_member_mgmt_getBusinessList()
        if getSecondCouponGetDetail:
            step_02_member_mgmt_getBusinessList()  

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询账号状态检查")
    @pytest.mark.parametrize("status", [0, 1, 2, -1], ids=["启用", "禁用", "冻结", "已注销"])
    def test_05_member_mgmt_getBusinessList(self, status):
        
        params = deepcopy(self.params)
        params["status"] = status  # 状态：0 启用, 1 禁用, 2 冻结, -1 已注销  
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["status"] for d in r.json()["data"]["list"]):
                    if status == -1:
                        assert i == 2
                    else:
                        assert i == 0

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询新卡升级方式检查")
    @pytest.mark.parametrize("promotionType", [1, 2], ids=["产品升级", "pv升级"])
    def test_06_member_mgmt_getBusinessList(self, promotionType):
        
        params = deepcopy(self.params)
        params["promotionType"] = promotionType  # 新卡升级方式 1：产品升级 2：pv升级
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["promotionType"] for d in r.json()["data"]["list"]):
                    assert i == promotionType 

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询注册方式检查")
    @pytest.mark.parametrize("registerMode", ["SHARE_PRODUCT", "SHARE_MATERIAL", "SHARE_DOCUMENT", "INVITE_REGISTER", "FULL_AGENT", "OFFLINE_AGENT", "SELF_REGISTER"], ids=["分享产品", "分享素材", "分享文档", "邀请注册", "全程代办", "线下注册", "自主注册"])
    def test_07_member_mgmt_getBusinessList(self, registerMode):
        
        params = deepcopy(self.params)
        params["registerMode"] = registerMode  # 注册方式 分享产品：SHARE_PRODUCT，分享素材：SHARE_MATERIAL，分享文档：SHARE_DOCUMENT，邀请注册：INVITE_REGISTER，全程代办：FULL_AGENT，线下注册：OFFLINE_AGENT，自主注册：SELF_REGISTER
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["registerMode"] for d in r.json()["data"]["list"]):
                    assert i == registerMode 

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询开卡方式检查")
    @pytest.mark.parametrize("openCardMode", ["SHARE_PRODUCT", "SHARE_MATERIAL", "SHARE_DOCUMENT", "INVITE_REGISTER", "FULL_AGENT", "OFFLINE_AGENT", "SELF_REGISTER"], ids=["分享产品", "分享素材", "分享文档", "邀请开卡", "全程代办", "线下开卡", "自主开卡"])
    def test_08_member_mgmt_getBusinessList(self, openCardMode):
        
        params = deepcopy(self.params)
        params["openCardMode"] = openCardMode  # 开卡方式 分享产品：SHARE_PRODUCT，分享素材：SHARE_MATERIAL，分享文档：SHARE_DOCUMENT，邀请注册：INVITE_REGISTER，全程代办：FULL_AGENT，线下开卡：OFFLINE_AGENT，自主开卡：SELF_REGISTER
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["openCardMode"] for d in r.json()["data"]["list"]):
                    assert i == openCardMode 

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询本人身份证验证状态检查")
    @pytest.mark.parametrize("selfIdCardVaildStatus", [0, 1], ids=["未验证", "已验证"])
    def test_09_member_mgmt_getBusinessList(self, selfIdCardVaildStatus):
        
        params = deepcopy(self.params)
        params["selfIdCardVaildStatus"] = selfIdCardVaildStatus  # 本人身份证认证状态 0：未验证; 1：已验证       
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["validationOneselfIdcardStatus"] for d in r.json()["data"]["list"]):
                    assert i == selfIdCardVaildStatus  

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询配偶身份证验证状态检查")
    @pytest.mark.parametrize("spouseIdCardVaildStatus", [0, 1], ids=["未验证", "已验证"])
    def test_10_member_mgmt_getBusinessList(self, spouseIdCardVaildStatus):
        
        params = deepcopy(self.params)
        params["spouseIdCardVaildStatus"] = spouseIdCardVaildStatus  # 配偶身份证认证状态 0：未验证; 1：已验证   
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["validationSpouseIdcardStatus"] for d in r.json()["data"]["list"]):
                    assert i == spouseIdCardVaildStatus  

    @allure.severity(P2)
    @allure.title("获取云商微店列表-成功路径: 查询手机号验证状态检查")
    @pytest.mark.parametrize("mobileVaildStatus", [0, 1], ids=["未验证", "已验证"])
    def test_11_member_mgmt_getBusinessList(self, mobileVaildStatus):
        
        params = deepcopy(self.params)
        params["mobileVaildStatus"] = mobileVaildStatus  # 手机认证状态 0：未验证; 1：已验证      
        with _member_mgmt_getBusinessList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["validationOneselfMobileStatus"] for d in r.json()["data"]["list"]):
                    assert i == mobileVaildStatus  

