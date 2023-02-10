# coding:utf-8

from api.mall_mgmt_application._mgmt_store_contract_getStoreContractInvtBillList import params, _mgmt_store_contract_getStoreContractInvtBillList # 查询库存对账单合同列表
from api.mall_mgmt_application._mgmt_store_contract_dropStoreContractInvtBill import _mgmt_store_contract_dropStoreContractInvtBill # 作废对账单电子合同
from util.stepreruns import stepreruns
from setting import P1, P2, P3, store_8502

from copy import deepcopy
import os
import allure
import pytest
import datetime
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/dropStoreContractInvtBill")
class TestClass:
    """
    作废对账单电子合同:13对账单
    /mgmt/store/contract/dropStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
   
    @allure.severity(P2)
    @allure.title("作废13对账单: 主路径检查")
    def test_01_mgmt_store_contract_dropStoreContractInvtBill(self, addStoreContractInvtBill_13_1):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBillList["docNo"]
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已作废")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 8 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 8
                getStoreContractInvtBillList["signStatusName"] = "已作废"
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        assert i == getStoreContractInvtBillList
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_dropStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("作废13对账单: 仅能作废待提交的13对账单检查")
    @pytest.mark.parametrize("signStatus", [2, 3, 4, 6, 7, 8, 9], ids=["待店铺签署", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_02_mgmt_store_contract_dropStoreContractInvtBill(self, signStatus):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取非待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBillList["docNo"]
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态必须为待提交状态"
        
        @allure.step("查询库存对账单合同列表: 确认作废无效")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        assert i == getStoreContractInvtBillList
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_dropStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/dropStoreContractInvtBill")
class TestClass02:
    """
    作废对账单电子合同:85折库存对账单
    /mgmt/store/contract/dropStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
   
    @allure.severity(P2)
    @allure.title("作废85折库存对账单: 主路径检查")
    def test_01_mgmt_store_contract_dropStoreContractInvtBill(self, addStoreContractInvtBill_85_1):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBillList["docNo"]
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已作废")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 8 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 8
                getStoreContractInvtBillList["signStatusName"] = "已作废"
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        assert i == getStoreContractInvtBillList
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_dropStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("作废对85折库存对账单: 仅能作废待提交的85折库存对账单检查")
    @pytest.mark.parametrize("signStatus", [2, 3, 4, 6, 7, 8, 9], ids=["待店铺签署", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_02_mgmt_store_contract_dropStoreContractInvtBill(self, signStatus):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取非待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBillList["docNo"]
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态必须为待提交状态"
        
        @allure.step("查询库存对账单合同列表: 确认作废无效")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        assert i == getStoreContractInvtBillList
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_dropStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/dropStoreContractInvtBill")
class TestClass03:
    """
    作废对账单电子合同:85折账款对账单
    /mgmt/store/contract/dropStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
   
    @allure.severity(P2)
    @allure.title("作废85折账款对账单: 主路径检查")
    def test_01_mgmt_store_contract_dropStoreContractInvtBill(self):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBillList["docNo"]
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已作废")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 8 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 8
                getStoreContractInvtBillList["signStatusName"] = "已作废"
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        assert i == getStoreContractInvtBillList
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_dropStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("作废85折账款对账单: 仅能作废待提交的85折账款对账单检查")
    @pytest.mark.parametrize("signStatus", [2, 3, 4, 6, 7, 8, 9], ids=["待店铺签署", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_02_mgmt_store_contract_dropStoreContractInvtBill(self, signStatus):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取非待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBillList["docNo"]
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态必须为待提交状态"
        
        @allure.step("查询库存对账单合同列表: 确认作废无效")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        assert i == getStoreContractInvtBillList
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_dropStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()











