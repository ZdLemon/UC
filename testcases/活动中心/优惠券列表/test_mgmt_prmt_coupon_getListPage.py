# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params ,_mgmt_prmt_coupon_getListPage

from setting import P1, P2, P3, couponName, couponNumber

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/coupon/getListPage")
class TestClass:
    """
    分页获取优惠券列表
    /mgmt/prmt/coupon/getListPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询默认条件检查")
    def test_01_mgmt_prmt_coupon_getListPage(self):
            
        params = deepcopy(self.params)             
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 支持模糊查询优惠券名称检查")
    @pytest.mark.parametrize("couponName", [couponName, couponName[:-1]], ids=["优惠券完整名称", "优惠券名称的一部分"])
    def test_02_mgmt_prmt_coupon_getListPage(self, couponName):
            
        params = deepcopy(self.params)
        params["couponName"] = couponName       
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert couponName in d["couponName"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 支持模糊查询优惠券编号检查")
    @pytest.mark.parametrize("couponNumber", [couponNumber, couponNumber[:-1]], ids=["优惠券完整编号", "优惠券编号的一部分"])
    def test_03_mgmt_prmt_coupon_getListPage(self, couponNumber):
            
        params = deepcopy(self.params)
        params["couponNumber"] = couponNumber       
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert couponNumber in d["couponNumber"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询创建时间检查")
    def test_04_mgmt_prmt_coupon_getListPage(self):
        
        createTime = None
        
        @allure.step("获取创建时间")
        def step_01_mgmt_prmt_coupon_getListPage():    
            
            nonlocal createTime
            params = deepcopy(self.params)      
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                createTime = r.json()["data"]["list"][0]["createTime"][:10]
        
        @allure.step("查询派发创建时间")
        def step_02_mgmt_prmt_coupon_getListPage():    
            
            params = deepcopy(self.params) 
            params["createTimeMin"] = f"{createTime} 00:00:00"
            params["createTimeMax"] = f"{createTime} 23:59:59"
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert d["createTime"][:10] == createTime
        
        step_01_mgmt_prmt_coupon_getListPage()
        step_02_mgmt_prmt_coupon_getListPage()

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询优惠券有效期检查")
    @pytest.mark.skip("这个搜索条件不实用，列表中都没有这个字段信息")
    def test_05_mgmt_prmt_coupon_getListPage(self):
        
        endTime = None
        
        @allure.step("获取优惠券有效期")
        def step_01_mgmt_prmt_coupon_getListPage():    
            
            nonlocal endTime
            params = deepcopy(self.params)      
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                endTime = r.json()["data"]["list"][0]["endTime"][:10]
        
        @allure.step("查询派发创建时间")
        def step_02_mgmt_prmt_coupon_getListPage():    
            
            params = deepcopy(self.params) 
            params["startTime"] = f"{endTime} 00:00:00"
            params["endTime"] = f"{endTime} 23:59:59"
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["endTime"] is None:
                        d["endTimeString"] == "不限制"
                    else:
                        assert d["endTime"][:10] == endTime
        
        step_01_mgmt_prmt_coupon_getListPage()
        step_02_mgmt_prmt_coupon_getListPage()

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询生成兑换码检查")
    @pytest.mark.parametrize("isGenerateCode", [0, 1], ids=["不生成", "生成"])
    def test_06_mgmt_prmt_coupon_getListPage(self, isGenerateCode):
            
        params = deepcopy(self.params)
        params["isGenerateCode"] = isGenerateCode # 是否生成优惠码0不生成1生成
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["isGenerateCode"] for d in r.json()["data"]["list"]):
                    assert i == isGenerateCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询使用限制检查")
    @pytest.mark.parametrize("limitStore", [0, 1, 2], ids=["自购/代购都不限制门店使用", "自购/代购都限制门店使用", "仅代购限制门店使用"])
    def test_07_mgmt_prmt_coupon_getListPage(self, limitStore):
            
        params = deepcopy(self.params)
        params["limitStore"] = limitStore # 是否限制门店0自购/代购都不限制门店使用1自购/代购都限制门店使用2仅代购限制门店使用
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["limitStore"] for d in r.json()["data"]["list"]):
                    assert i == limitStore
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 多选查询平台限制检查")
    @pytest.mark.parametrize("platforms,ids", [(1, "APP"), (2, "PC"), (4, "小程序"), ("1, 2", "APP、PC"), ("1, 2, 4", "APP、PC、小程序")])
    def test_08_mgmt_prmt_coupon_getListPage(self, platforms, ids):
            
        params = deepcopy(self.params)
        params["platforms"] = platforms
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["platform"] == ids
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询下单限制检查")
    @pytest.mark.parametrize("orderWayList", [1, 2], ids=["自购", "代购"])
    def test_09_mgmt_prmt_coupon_getListPage(self, orderWayList):
            
        params = deepcopy(self.params)
        params["orderWayList"] = orderWayList # 下单限制1自购2代购
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["orderWays"] for d in r.json()["data"]["list"]):
                    assert i == orderWayList
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("优惠券列表-成功路径: 查询优惠券状态检查")
    @pytest.mark.parametrize("couponState", [1, 2, 3, 4, 5, 6, 7], ids=["待审核", "待生效", "生效中", "已失效", "已禁用", "已驳回", "草稿"])
    def test_10_mgmt_prmt_coupon_getListPage(self, couponState):
            
        params = deepcopy(self.params)
        params["couponState"] = couponState # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
        with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["couponState"] for d in r.json()["data"]["list"]):
                    assert i == couponState
            else:
                assert r.json()["data"]["list"] == []












