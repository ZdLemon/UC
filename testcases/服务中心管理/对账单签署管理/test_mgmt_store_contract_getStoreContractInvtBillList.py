# coding:utf-8

from api.mall_mgmt_application._mgmt_store_contract_getStoreContractInvtBillList import params, _mgmt_store_contract_getStoreContractInvtBillList # 查询库存对账单合同列表

from setting import P1, P2, P3, store_8502

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/getStoreContractInvtBillList")
class TestClass:
    """
    查询库存对账单合同列表:13对账单签署管理
    /mgmt/store/contract/getStoreContractInvtBillList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询服务中心编号检查")
    def test_01_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 13对账单签署管理
        
        @allure.step("13对账单签署管理: 获取服务中心编号")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("13对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["storeCode"] = getStoreContractInvtBillList["storeCode"]
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == getStoreContractInvtBillList["storeCode"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询对账单月份检查")
    def test_02_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 13对账单签署管理
        
        @allure.step("13对账单签署管理:获取对账单月份")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("13对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minBillMonth"] = getStoreContractInvtBillList["billStartMonth"]
            params["maxBillMonth"] = getStoreContractInvtBillList["billEndMonth"]
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["billStartMonth"] == getStoreContractInvtBillList["billStartMonth"]
                    assert i["billEndMonth"] == getStoreContractInvtBillList["billEndMonth"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询所属分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_store_contract_getStoreContractInvtBillList(self, companyCode):        
        
        @allure.step("13对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["companyCode"] = companyCode
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        assert i["companyCode"] == companyCode
                else:
                    assert r.json()["data"]["list"] == []
       
        step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询发起签署日期检查")
    def test_04_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 13对账单签署管理
        
        @allure.step("13对账单签署管理:获取发起签署日期")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("13对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minSignStartDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
            params["maxSignStartDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询店铺签署时间检查")
    def test_05_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 13对账单签署管理
        
        @allure.step("13对账单签署管理:获取店铺签署时间")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("13对账单签署管理:获取店铺签署时间")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 4 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
                            
        @allure.step("13对账单签署管理")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minStoreSignDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
            params["maxStoreSignDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["storeSignTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList is None:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_03_mgmt_store_contract_getStoreContractInvtBillList()
        else:
            step_03_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询公司签署人检查")
    def test_06_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 13对账单签署管理
        
        @allure.step("13对账单签署管理:获取公司签署人")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("13对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["companySignPerson"] = getStoreContractInvtBillList["companySignPerson"]
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["companySignPerson"] == getStoreContractInvtBillList["companySignPerson"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询是否线下签署检查")
    @pytest.mark.parametrize("isSignOffline", [1, 0], ids=["是", "否"])
    def test_07_mgmt_store_contract_getStoreContractInvtBillList(self, isSignOffline):        
            
        params = deepcopy(self.params)
        params["isSignOffline"] = isSignOffline
        params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["isSignOffline"] == isSignOffline
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("13对账单签署管理-成功路径: 查询签署状态检查")
    @pytest.mark.parametrize("signStatus", [1, 2, 3, 4, 5, 6, 7, 8, 9], ids=["待提交", "待店铺签署", "待公司签署", "签署完成", "超时中止签署", "拒签", "已撤回", "已作废", "生成失败"])
    def test_08_mgmt_store_contract_getStoreContractInvtBillList(self, signStatus):        
            
        params = deepcopy(self.params)
        params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["signStatus"] == signStatus
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/getStoreContractInvtBillList")
class TestClass02:
    """
    查询库存对账单合同列表:85折库存对账单
    /mgmt/store/contract/getStoreContractInvtBillList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询服务中心编号检查")
    def test_01_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("查询库存对账单合同列表: 获取服务中心编号")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("查询库存对账单合同列表")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["storeCode"] = getStoreContractInvtBillList["storeCode"]
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == getStoreContractInvtBillList["storeCode"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询对账单月份检查")
    def test_02_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("查询库存对账单合同列表:获取对账单月份")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("查询库存对账单合同列表")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minBillMonth"] = getStoreContractInvtBillList["billStartMonth"]
            params["maxBillMonth"] = getStoreContractInvtBillList["billEndMonth"]
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["billStartMonth"] == getStoreContractInvtBillList["billStartMonth"]
                    assert i["billEndMonth"] == getStoreContractInvtBillList["billEndMonth"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询所属分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_store_contract_getStoreContractInvtBillList(self, companyCode):        
        
        @allure.step("查询库存对账单合同列表")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["companyCode"] = companyCode
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        assert i["companyCode"] == companyCode
                else:
                    assert r.json()["data"]["list"] == []
       
        step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询发起签署日期检查")
    def test_04_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("查询库存对账单合同列表:获取发起签署日期")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("查询库存对账单合同列表")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minSignStartDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
            params["maxSignStartDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询店铺签署时间检查")
    def test_05_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("查询库存对账单合同列表:获取店铺签署时间")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("查询库存对账单合同列表:获取店铺签署时间")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 4 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
                            
        @allure.step("查询库存对账单合同列表")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minStoreSignDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
            params["maxStoreSignDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["storeSignTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList is None:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_03_mgmt_store_contract_getStoreContractInvtBillList()
        else:
            step_03_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询公司签署人检查")
    def test_06_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("查询库存对账单合同列表:获取公司签署人")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("查询库存对账单合同列表")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["companySignPerson"] = getStoreContractInvtBillList["companySignPerson"]
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["companySignPerson"] == getStoreContractInvtBillList["companySignPerson"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询是否线下签署检查")
    @pytest.mark.parametrize("isSignOffline", [1, 0], ids=["是", "否"])
    def test_07_mgmt_store_contract_getStoreContractInvtBillList(self, isSignOffline):        
            
        params = deepcopy(self.params)
        params["isSignOffline"] = isSignOffline
        params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["isSignOffline"] == isSignOffline
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("查询库存对账单合同列表-成功路径: 查询签署状态检查")
    @pytest.mark.parametrize("signStatus", [1, 2, 3, 4, 6, 7, 8, 9], ids=["待提交", "待店铺签署", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_08_mgmt_store_contract_getStoreContractInvtBillList(self, signStatus):        
            
        params = deepcopy(self.params)
        params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["signStatus"] == signStatus
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/getStoreContractInvtBillList")
class TestClass03:
    """
    查询库存对账单合同列表：85折账款对账单
    /mgmt/store/contract/getStoreContractInvtBillList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询服务中心编号检查")
    def test_01_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("85折账款对账单签署管理:获取服务中心编号")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("85折账款对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["storeCode"] = getStoreContractInvtBillList["storeCode"]
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["storeCode"] == getStoreContractInvtBillList["storeCode"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询对账单月份检查")
    def test_02_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("85折账款对账单签署管理:获取对账单月份")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("85折账款对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minBillMonth"] = getStoreContractInvtBillList["billStartMonth"]
            params["maxBillMonth"] = getStoreContractInvtBillList["billEndMonth"]
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["billStartMonth"] == getStoreContractInvtBillList["billStartMonth"]
                    assert i["billEndMonth"] == getStoreContractInvtBillList["billEndMonth"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询所属分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_store_contract_getStoreContractInvtBillList(self, companyCode):        
        
        @allure.step("85折账款对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["companyCode"] = companyCode
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        assert i["companyCode"] == companyCode
                else:
                    assert r.json()["data"]["list"] == []
       
        step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询发起签署日期检查")
    def test_04_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("85折账款对账单签署管理:获取发起签署日期")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("85折账款对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minSignStartDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
            params["maxSignStartDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["signStartDate"])/1000))
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询店铺签署时间检查")
    def test_05_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("85折账款对账单签署管理:获取店铺签署时间")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("85折账款对账单签署管理:获取店铺签署时间")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 4 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
                            
        @allure.step("85折账款对账单签署管理")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["minStoreSignDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
            params["maxStoreSignDate"] = time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d", time.localtime(int(i["storeSignTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(int(getStoreContractInvtBillList["storeSignTime"])/1000))
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList is None:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_03_mgmt_store_contract_getStoreContractInvtBillList()
        else:
            step_03_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询公司签署人检查")
    def test_06_mgmt_store_contract_getStoreContractInvtBillList(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表
        
        @allure.step("85折账款对账单签署管理:获取公司签署人")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():
            
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]
        
        @allure.step("85折账款对账单签署管理")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():
            
            params = deepcopy(self.params)
            params["companySignPerson"] = getStoreContractInvtBillList["companySignPerson"]
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert i["companySignPerson"] == getStoreContractInvtBillList["companySignPerson"]
       
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询是否线下签署检查")
    @pytest.mark.parametrize("isSignOffline", [1, 0], ids=["是", "否"])
    def test_07_mgmt_store_contract_getStoreContractInvtBillList(self, isSignOffline):        
            
        params = deepcopy(self.params)
        params["isSignOffline"] = isSignOffline
        params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["isSignOffline"] == isSignOffline
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折账款对账单签署管理-成功路径: 查询签署状态检查")
    @pytest.mark.parametrize("signStatus", [1, 2, 3, 4, 6, 7, 8, 9], ids=["待提交", "待店铺签署", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_08_mgmt_store_contract_getStoreContractInvtBillList(self, signStatus):        
            
        params = deepcopy(self.params)
        params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert i["signStatus"] == signStatus
            else:
                assert r.json()["data"]["list"] == []





