# coding:utf-8

from api.mall_mgmt_application._mgmt_store_contract_getStoreContractInvtBillList import params, _mgmt_store_contract_getStoreContractInvtBillList # 查询库存对账单合同列表
from api.mall_mgmt_application._mgmt_store_contract_batchRedoStoreContractInvtBill import _mgmt_store_contract_batchRedoStoreContractInvtBill # 批量撤回对账单电子合同
from util.stepreruns import stepreruns
from setting import P1, P2, P3, store_8502, USERNAME

from copy import deepcopy
import os
import allure
import pytest
import datetime
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/batchRedoStoreContractInvtBill")
class TestClass:
    """
    批量撤回对账单电子合同:13对账单
    /mgmt/store/contract/batchRedoStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
   
    @allure.severity(P2)
    @allure.title("撤回13对账单: 主路径检查")
    def test_01_mgmt_store_contract_batchRedoStoreContractInvtBill(self, addStoreContractInvtBill_13_2):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillList["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 7
                getStoreContractInvtBillList["signStatusName"] = "已撤回"
                getStoreContractInvtBillList["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        getStoreContractInvtBillList["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillList
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待店铺签署，则撤回
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("批量撤回13对账单: 主路径检查")
    def test_02_mgmt_store_contract_batchRedoStoreContractInvtBill(self, addStoreContractInvtBill_13_2, addStoreContractInvtBill_13_2_2):
        
        getStoreContractInvtBillLists = [] # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"] and r.json()["data"]["total"] >= 2:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][1])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillLists[0]["docNo"], getStoreContractInvtBillLists[1]["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 7
                getStoreContractInvtBillList["signStatusName"] = "已撤回"
                getStoreContractInvtBillList["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        getStoreContractInvtBillList["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillList
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待店铺签署，则撤回
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillLists:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            for getStoreContractInvtBillList in getStoreContractInvtBillLists:
                step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("批量撤回13对账单: 待店铺签署+其他状态检查")
    @pytest.mark.parametrize("signStatus", [1, 3, 4, 6, 7, 8, 9], ids=["待提交", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_03_mgmt_store_contract_batchRedoStoreContractInvtBill(self, signStatus, addStoreContractInvtBill_13_2):
        
        getStoreContractInvtBillLists = [] # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])

        @allure.step("查询库存对账单合同列表: 获取非待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillLists[0]["docNo"], getStoreContractInvtBillLists[1]["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态是待店铺签署才能进行撤回操作"

        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillLists[0]["signStatus"] = 7
                getStoreContractInvtBillLists[0]["signStatusName"] = "已撤回"
                getStoreContractInvtBillLists[0]["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillLists[0]["docNo"]:
                        getStoreContractInvtBillLists[0]["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillLists[0]
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillLists[0]["docNo"] in docNos
             
        @allure.step("查询库存对账单合同列表: 确认非待店铺签署的合同撤回无效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillLists[1]["docNo"]:
                        assert i == getStoreContractInvtBillLists[1]
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillLists[1]["docNo"] in docNos
     
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if len(getStoreContractInvtBillLists) == 2:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("撤回13对账单: 仅能撤回待店铺签署的13对账单检查")
    @pytest.mark.parametrize("signStatus", [1, 3, 4, 6, 7, 8, 9], ids=["待提交", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_04_mgmt_store_contract_batchRedoStoreContractInvtBill(self, signStatus):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取非待店铺签署的合同")
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

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillList["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态是待店铺签署才能进行撤回操作"
        
        @allure.step("查询库存对账单合同列表: 确认撤回无效")
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
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/batchRedoStoreContractInvtBill")
class TestClass02:
    """
    批量撤回对账单电子合同:85折库存对账单
    /mgmt/store/contract/batchRedoStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
   
    @allure.severity(P2)
    @allure.title("撤回85折库存对账单: 主路径检查")
    def test_01_mgmt_store_contract_batchRedoStoreContractInvtBill(self, addStoreContractInvtBill_85_2):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillList["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 7
                getStoreContractInvtBillList["signStatusName"] = "已撤回"
                getStoreContractInvtBillList["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        getStoreContractInvtBillList["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillList
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待店铺签署，则撤回
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("批量撤回85折库存对账单: 主路径检查")
    def test_02_mgmt_store_contract_batchRedoStoreContractInvtBill(self, addStoreContractInvtBill_85_2, addStoreContractInvtBill_85_2_2):
        
        getStoreContractInvtBillLists = [] # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"] and r.json()["data"]["total"] >= 2:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][1])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillLists[0]["docNo"], getStoreContractInvtBillLists[1]["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 7
                getStoreContractInvtBillList["signStatusName"] = "已撤回"
                getStoreContractInvtBillList["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        getStoreContractInvtBillList["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillList
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待店铺签署，则撤回
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillLists:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            for getStoreContractInvtBillList in getStoreContractInvtBillLists:
                step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("批量撤回85折库存对账单: 待店铺签署+其他状态检查")
    @pytest.mark.parametrize("signStatus", [1, 3, 4, 6, 7, 8, 9], ids=["待提交", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_03_mgmt_store_contract_batchRedoStoreContractInvtBill(self, signStatus, addStoreContractInvtBill_85_2):
        
        getStoreContractInvtBillLists = [] # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])

        @allure.step("查询库存对账单合同列表: 获取非待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillLists[0]["docNo"], getStoreContractInvtBillLists[1]["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态是待店铺签署才能进行撤回操作"

        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillLists[0]["signStatus"] = 7
                getStoreContractInvtBillLists[0]["signStatusName"] = "已撤回"
                getStoreContractInvtBillLists[0]["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillLists[0]["docNo"]:
                        getStoreContractInvtBillLists[0]["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillLists[0]
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillLists[0]["docNo"] in docNos
             
        @allure.step("查询库存对账单合同列表: 确认非待店铺签署的合同撤回无效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillLists[1]["docNo"]:
                        assert i == getStoreContractInvtBillLists[1]
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillLists[1]["docNo"] in docNos
     
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if len(getStoreContractInvtBillLists) == 2:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("撤回85折库存对账单: 仅能撤回待店铺签署的85折库存对账单检查")
    @pytest.mark.parametrize("signStatus", [1, 3, 4, 6, 7, 8, 9], ids=["待提交", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_04_mgmt_store_contract_batchRedoStoreContractInvtBill(self, signStatus):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取非待店铺签署的合同")
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

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillList["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态是待店铺签署才能进行撤回操作"
        
        @allure.step("查询库存对账单合同列表: 确认撤回无效")
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
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/batchRedoStoreContractInvtBill")
class TestClass03:
    """
    批量撤回对账单电子合同:85折账款对账单
    /mgmt/store/contract/batchRedoStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
   
    @allure.severity(P2)
    @allure.title("撤回85折账款对账单: 主路径检查")
    def test_01_mgmt_store_contract_batchRedoStoreContractInvtBill(self, addStoreContractInvtBill_85_2):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillList = r.json()["data"]["list"][0]

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillList["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 7
                getStoreContractInvtBillList["signStatusName"] = "已撤回"
                getStoreContractInvtBillList["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        getStoreContractInvtBillList["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillList
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待店铺签署，则撤回
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P2)
    @allure.title("批量撤回85折账款对账单: 主路径检查")
    def test_02_mgmt_store_contract_batchRedoStoreContractInvtBill(self, addStoreContractInvtBill_85_2, addStoreContractInvtBill_85_2_2):
        
        getStoreContractInvtBillLists = [] # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"] and r.json()["data"]["total"] >= 2:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][1])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillLists[0]["docNo"], getStoreContractInvtBillLists[1]["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillList["signStatus"] = 7
                getStoreContractInvtBillList["signStatusName"] = "已撤回"
                getStoreContractInvtBillList["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillList["docNo"]:
                        getStoreContractInvtBillList["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillList
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillList["docNo"] in docNos
     
        # 如有待店铺签署，则撤回
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillLists:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            for getStoreContractInvtBillList in getStoreContractInvtBillLists:
                step_02_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("批量撤回85折账款对账单: 待店铺签署+其他状态检查")
    @pytest.mark.parametrize("signStatus", [1, 3, 4, 6, 7, 8, 9], ids=["待提交", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_03_mgmt_store_contract_batchRedoStoreContractInvtBill(self, signStatus, addStoreContractInvtBill_85_2):
        
        getStoreContractInvtBillLists = [] # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])

        @allure.step("查询库存对账单合同列表: 获取非待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillLists
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreContractInvtBillLists.append(r.json()["data"]["list"][0])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillLists[0]["docNo"], getStoreContractInvtBillLists[1]["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态是待店铺签署才能进行撤回操作"

        @allure.step("查询库存对账单合同列表: 确认已撤回")
        @stepreruns()
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 7 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillLists[0]["signStatus"] = 7
                getStoreContractInvtBillLists[0]["signStatusName"] = "已撤回"
                getStoreContractInvtBillLists[0]["redoOperator"] = USERNAME # 撤回人
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillLists[0]["docNo"]:
                        getStoreContractInvtBillLists[0]["redoTime"] = i["redoTime"] # 撤回时间
                        assert i == getStoreContractInvtBillLists[0]
                        assert time.strftime("%Y-%m-%d", time.localtime(int(i["redoTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 撤回时间
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillLists[0]["docNo"] in docNos
             
        @allure.step("查询库存对账单合同列表: 确认非待店铺签署的合同撤回无效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = signStatus # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                docNos = []
                for i in r.json()["data"]["list"]:
                    if i["docNo"] == getStoreContractInvtBillLists[1]["docNo"]:
                        assert i == getStoreContractInvtBillLists[1]
                    docNos.append(i["docNo"])
                assert getStoreContractInvtBillLists[1]["docNo"] in docNos
     
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if len(getStoreContractInvtBillLists) == 2:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P3)
    @allure.title("撤回85折账款对账单: 仅能撤回待店铺签署的85折账款对账单检查")
    @pytest.mark.parametrize("signStatus", [1, 3, 4, 6, 7, 8, 9], ids=["待提交", "待公司签署", "签署完成", "拒签", "已撤回", "已作废", "生成失败"])
    def test_04_mgmt_store_contract_batchRedoStoreContractInvtBill(self, signStatus):
        
        getStoreContractInvtBillList = None # 查询库存对账单合同列表

        @allure.step("查询库存对账单合同列表: 获取非待店铺签署的合同")
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

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": [getStoreContractInvtBillList["docNo"]]
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0
                assert r.json()["message"] == "合同状态是待店铺签署才能进行撤回操作"
        
        @allure.step("查询库存对账单合同列表: 确认撤回无效")
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
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
