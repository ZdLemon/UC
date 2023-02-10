# coding:utf-8

from api.mall_mgmt_application._mgmt_store_contract_addStoreContractInvtBill import _mgmt_store_contract_addStoreContractInvtBill # 添加库存对账单电子合同批量任务
from api.mall_mgmt_application._mgmt_store_contract_getStoreContractInvtBillSettingInfo import _mgmt_store_contract_getStoreContractInvtBillSettingInfo # 获取公司签署人信息
from api.mall_mgmt_application._mgmt_store_contract_getStoreContractInvtBillList import params, _mgmt_store_contract_getStoreContractInvtBillList # 查询库存对账单合同列表
from api.mall_mgmt_application._mgmt_store_contract_dropStoreContractInvtBill import _mgmt_store_contract_dropStoreContractInvtBill # 作废对账单电子合同
from api.mall_mgmt_application._mgmt_store_contract_batchRedoStoreContractInvtBill import _mgmt_store_contract_batchRedoStoreContractInvtBill # 批量撤回对账单电子合同
from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_dis_inventory_bill_settled_store import params as params02, _mgmt_dis_inventory_bill_settled_store # 查询已月结服务中心
from api.settle_job._months_deposit_billCheck_page import data, _months_deposit_billCheck_page
from api.mall_mgmt_application._mgmt_inventory_bill_settled_store import params as params03, _mgmt_inventory_bill_settled_store # 查询已月结服务中心13
from util.stepreruns import stepreruns
from setting import P1, P2, P3, store_8502, store_02, USERNAME

from copy import deepcopy
import os
import allure
import pytest
import datetime
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/addStoreContractInvtBill")
class TestClass:
    """
    添加库存对账单电子合同批量任务:13对账单
    /mgmt/store/contract/addStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
   
    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 13实时对账单-待生效")
    def test_01_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_02
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 1,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType":1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 1, # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
                "currentOperatorName": currentOperatorName
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["data"]["total"] == 1
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
                    assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
                    assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
                    assert r.json()["data"]["list"][0]["billType"] == 1 # 对账单类型
                    assert r.json()["data"]["list"][0]["billTypeName"] == "实时" # 对账单类型
                    assert r.json()["data"]["list"][0]["billMonth"].endswith(time.strftime("%Y/%m",time.localtime(time.time()))) # 对账单月份
                    assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
                    assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
                    assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d") # 发起签署日期
                    assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
                    assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
                    assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
                    assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
                    assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
                    assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
                    assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
                else:
                    assert r.json()["data"]["total"] == 0
      
        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            for getStoreContractInvtBill in getStoreContractInvtBillList:
                step_mgmt_store_contract_dropStoreContractInvtBill()
        # 如有待店铺签署，则撤回
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
        # 是否有待公司签署
        step_03_mgmt_store_contract_getStoreContractInvtBillList()
        step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
        step_mgmt_store_contract_addStoreContractInvtBill()
        step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 13实时对账单-立即生效")
    def test_02_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_02
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 1,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType": 1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 1, # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
                "currentOperatorName": currentOperatorName
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["data"]["total"] == 1
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
                    assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
                    assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
                    assert r.json()["data"]["list"][0]["billType"] == 1 # 对账单类型
                    assert r.json()["data"]["list"][0]["billTypeName"] == "实时" # 对账单类型
                    assert r.json()["data"]["list"][0]["billMonth"].endswith(time.strftime("%Y/%m",time.localtime(time.time()))) # 对账单月份
                    assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
                    assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
                    assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
                    assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
                    assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
                    assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
                    assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
                    assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
                    assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
                    assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
                else:
                    assert r.json()["data"]["total"] == 0
      
        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            for getStoreContractInvtBill in getStoreContractInvtBillList:
                step_mgmt_store_contract_dropStoreContractInvtBill()
        # 如有待店铺签署，则撤回
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
        # 是否有待公司签署
        step_03_mgmt_store_contract_getStoreContractInvtBillList()
        step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
        step_mgmt_store_contract_addStoreContractInvtBill()
        step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 已有待提交的13对账单")
    def test_03_mgmt_store_contract_addStoreContractInvtBill(self, login, addStoreContractInvtBill_13_1):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_02
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
       
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                     
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 1,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType":1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 1, # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
                "currentOperatorName": currentOperatorName
            }   
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，才继续执行
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 已有待店铺签署的13对账单")
    def test_04_mgmt_store_contract_addStoreContractInvtBill(self, login, addStoreContractInvtBill_13_2):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_02
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                      
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 1,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType": 1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 1, # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
                "currentOperatorName": currentOperatorName
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            for getStoreContractInvtBill in getStoreContractInvtBillList:
                step_mgmt_store_contract_dropStoreContractInvtBill()
        # 如有待店铺签署，才继续执行
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 13月结对账单-服务中心-立即生效")
    def test_05_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]
        settled_store = None # 查询已月结服务中心

        @allure.step("查询已月结服务中心: 获取服务中心编号")
        def step_01_mgmt_inventory_bill_settled_store():
            
            nonlocal settled_store
            params = deepcopy(self.params03)
            with _mgmt_inventory_bill_settled_store(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyCode"] and i["storeCode"]:
                            settled_store = i
                            break
                                               
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": settled_store["storeCode"]
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 1,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "billStartMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "billEndMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "companyCode": None,
                "currentOperatorName": currentOperatorName,
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 今天
                "billType": 2, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        # @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        # @stepreruns()
        # def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
        #     params = deepcopy(self.params)
        #     params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        #     params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        #     params["storeCode"] = getStoreInfo["code"]
        #     with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
        #         assert r.status_code == 200
        #         assert r.json()["code"] == 200
        #         if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
        #             assert r.json()["data"]["total"] == 1
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
        #             assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
        #             assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
        #             assert r.json()["data"]["list"][0]["billType"] == 2 # 对账单类型
        #             assert r.json()["data"]["list"][0]["billTypeName"] == "月结" # 对账单类型
        #             assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
        #             assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
        #             assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
        #             assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
        #             assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
        #             assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
        #             assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
        #             assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
        #             assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
        #             assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
        #             assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
        #         else:
        #             assert r.json()["data"]["total"] == 0
      
        step_01_mgmt_inventory_bill_settled_store()
        if settled_store:
            step_mgmt_inventory_common_getStoreInfo()
            # 如有待提交，则作废
            step_01_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                for getStoreContractInvtBill in getStoreContractInvtBillList:
                    step_mgmt_store_contract_dropStoreContractInvtBill()
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            # 是否有待公司签署
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()
            # step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 13月结对账单-分公司-立即生效")
    def test_06_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]
        settled_store = None # 查询已月结服务中心

        @allure.step("查询已月结服务中心: 获取分公司编号")
        def step_01_mgmt_inventory_bill_settled_store():
            
            nonlocal settled_store
            params = deepcopy(self.params03)
            with _mgmt_inventory_bill_settled_store(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyCode"] and i["storeCode"]:
                            settled_store = i
                            break
                                               
        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 1,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "billStartMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "billEndMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "companyCode": settled_store["companyCode"],
                "currentOperatorName": currentOperatorName,
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 今天
                "billType": 2, # 对账单类型，1/实时，2/月结
                "storeCode": "",
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 1 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        # @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        # @stepreruns()
        # def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
        #     params = deepcopy(self.params)
        #     params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        #     params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        #     params["storeCode"] = getStoreInfo["code"]
        #     with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
        #         assert r.status_code == 200
        #         assert r.json()["code"] == 200
        #         if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
        #             assert r.json()["data"]["total"] == 1
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
        #             assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
        #             assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
        #             assert r.json()["data"]["list"][0]["billType"] == 2 # 对账单类型
        #             assert r.json()["data"]["list"][0]["billTypeName"] == "月结" # 对账单类型
        #             assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
        #             assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
        #             assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
        #             assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
        #             assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
        #             assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
        #             assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
        #             assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
        #             assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
        #             assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
        #             assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
        #         else:
        #             assert r.json()["data"]["total"] == 0
      
        step_01_mgmt_inventory_bill_settled_store()
        if settled_store:
            # 如有待提交，则作废
            step_01_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                for getStoreContractInvtBill in getStoreContractInvtBillList:
                    step_mgmt_store_contract_dropStoreContractInvtBill()
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            # 是否有待公司签署
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()
            # step_04_mgmt_store_contract_getStoreContractInvtBillList()
   

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/addStoreContractInvtBill")
class TestClass02:
    """
    添加库存对账单电子合同批量任务：85折库存对账单
    /mgmt/store/contract/addStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
   
    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 85实时库存对账单-待生效")
    def test_01_mgmt_store_contract_addStoreContractInvtBill(self):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_8502
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType":1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["data"]["total"] == 1
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
                    assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
                    assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
                    assert r.json()["data"]["list"][0]["billType"] == 1 # 对账单类型
                    assert r.json()["data"]["list"][0]["billTypeName"] == "实时" # 对账单类型
                    assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
                    assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
                    assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
                    assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d") # 发起签署日期
                    assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
                    assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
                    assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
                    assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
                    assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
                    assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
                    assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
                else:
                    assert r.json()["data"]["total"] == 0
      
        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            for getStoreContractInvtBill in getStoreContractInvtBillList:
                step_mgmt_store_contract_dropStoreContractInvtBill()
        # 如有待店铺签署，则撤回
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
        # 是否有待公司签署
        step_03_mgmt_store_contract_getStoreContractInvtBillList()
        step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
        step_mgmt_store_contract_addStoreContractInvtBill()
        step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 85实时库存对账单-立即生效")
    def test_02_mgmt_store_contract_addStoreContractInvtBill(self):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_8502
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType":1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        @stepreruns()
        def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["data"]["total"] == 1
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
                    assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
                    assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
                    assert r.json()["data"]["list"][0]["billType"] == 1 # 对账单类型
                    assert r.json()["data"]["list"][0]["billTypeName"] == "实时" # 对账单类型
                    assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
                    assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
                    assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
                    assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
                    assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
                    assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
                    assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
                    assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
                    assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
                    assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
                    assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
                    assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
                else:
                    assert r.json()["data"]["total"] == 0
      
        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            for getStoreContractInvtBill in getStoreContractInvtBillList:
                step_mgmt_store_contract_dropStoreContractInvtBill()
        # 如有待店铺签署，则撤回
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_batchRedoStoreContractInvtBill()
        # 是否有待公司签署
        step_03_mgmt_store_contract_getStoreContractInvtBillList()
        step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
        step_mgmt_store_contract_addStoreContractInvtBill()
        step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 已有待提交的85折实时库存对账单")
    def test_03_mgmt_store_contract_addStoreContractInvtBill(self, addStoreContractInvtBill_85_1):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_8502
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
       
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                     
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType":1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，才继续执行
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 已有待店铺签署的85折实时库存对账单")
    def test_04_mgmt_store_contract_addStoreContractInvtBill(self, addStoreContractInvtBill_85_2):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": store_8502
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                      
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
                "billType":1, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        step_mgmt_inventory_common_getStoreInfo()
        # 如有待提交，则作废
        step_01_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            for getStoreContractInvtBill in getStoreContractInvtBillList:
                step_mgmt_store_contract_dropStoreContractInvtBill()
        # 如有待店铺签署，才继续执行
        step_02_mgmt_store_contract_getStoreContractInvtBillList()
        if getStoreContractInvtBillList:
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 85月结库存对账单-服务中心-立即生效")
    def test_05_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]
        settled_store = None # 查询已月结服务中心

        @allure.step("查询已月结服务中心: 获取服务中心编号")
        def step_01_mgmt_dis_inventory_bill_settled_store():
            
            nonlocal settled_store
            params = deepcopy(self.params02)
            with _mgmt_dis_inventory_bill_settled_store(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyCode"] and i["storeCode"]:
                            settled_store = i
                            break
                                               
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": settled_store["storeCode"]
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "billStartMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "billEndMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "companyCode": None,
                "currentOperatorName": currentOperatorName,
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 今天
                "billType": 2, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        # @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        # @stepreruns()
        # def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
        #     params = deepcopy(self.params)
        #     params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        #     params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        #     params["storeCode"] = getStoreInfo["code"]
        #     with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
        #         assert r.status_code == 200
        #         assert r.json()["code"] == 200
        #         if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
        #             assert r.json()["data"]["total"] == 1
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
        #             assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
        #             assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
        #             assert r.json()["data"]["list"][0]["billType"] == 2 # 对账单类型
        #             assert r.json()["data"]["list"][0]["billTypeName"] == "月结" # 对账单类型
        #             assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
        #             assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
        #             assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
        #             assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
        #             assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
        #             assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
        #             assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
        #             assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
        #             assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
        #             assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
        #             assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
        #         else:
        #             assert r.json()["data"]["total"] == 0
      
        step_01_mgmt_dis_inventory_bill_settled_store()
        if settled_store:
            step_mgmt_inventory_common_getStoreInfo()
            # 如有待提交，则作废
            step_01_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                for getStoreContractInvtBill in getStoreContractInvtBillList:
                    step_mgmt_store_contract_dropStoreContractInvtBill()
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            # 是否有待公司签署
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()
            # step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 85月结库存对账单-分公司-立即生效")
    def test_06_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]
        settled_store = None # 查询已月结服务中心

        @allure.step("查询已月结服务中心: 获取分公司编号")
        def step_01_mgmt_dis_inventory_bill_settled_store():
            
            nonlocal settled_store
            params = deepcopy(self.params02)
            with _mgmt_dis_inventory_bill_settled_store(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyCode"] and i["storeCode"]:
                            settled_store = i
                            break
                                               
        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "billStartMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "billEndMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "companyCode": settled_store["companyCode"],
                "currentOperatorName": currentOperatorName,
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 今天
                "billType": 2, # 对账单类型，1/实时，2/月结
                "storeCode": "",
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        # @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        # @stepreruns()
        # def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
        #     params = deepcopy(self.params)
        #     params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        #     params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        #     params["storeCode"] = getStoreInfo["code"]
        #     with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
        #         assert r.status_code == 200
        #         assert r.json()["code"] == 200
        #         if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
        #             assert r.json()["data"]["total"] == 1
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
        #             assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
        #             assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
        #             assert r.json()["data"]["list"][0]["billType"] == 2 # 对账单类型
        #             assert r.json()["data"]["list"][0]["billTypeName"] == "月结" # 对账单类型
        #             assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
        #             assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
        #             assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
        #             assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
        #             assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
        #             assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
        #             assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
        #             assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
        #             assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
        #             assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
        #             assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
        #         else:
        #             assert r.json()["data"]["total"] == 0
      
        step_01_mgmt_dis_inventory_bill_settled_store()
        if settled_store:
            # 如有待提交，则作废
            step_01_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                for getStoreContractInvtBill in getStoreContractInvtBillList:
                    step_mgmt_store_contract_dropStoreContractInvtBill()
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            # 是否有待公司签署
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()
            # step_04_mgmt_store_contract_getStoreContractInvtBillList()
   

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/contract/addStoreContractInvtBill")
# @pytest.mark.skip()
class TestClass03:
    """
    添加库存对账单电子合同批量任务：85折账款对账单
    /mgmt/store/contract/addStoreContractInvtBill
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.data = deepcopy(data)
   
    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 85月结账款对账单-服务中心-立即生效")
    def test_05_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]
        settled_store = None # 查询已月结服务中心

        @allure.step("查询已月结服务中心: 获取服务中心编号")
        def step_months_deposit_billCheck_page():
            
            nonlocal settled_store
            data = deepcopy(self.data)
            with _months_deposit_billCheck_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyCode"] and i["storeCode"]:
                            settled_store = i
                            break
                                               
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo 
            params = {
                "storeCode": settled_store["storeCode"]
            }
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"] 

        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 3,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "billStartMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "billEndMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "companyCode": None,
                "currentOperatorName": currentOperatorName,
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 今天
                "billType": 2, # 对账单类型，1/实时，2/月结
                "storeCode": getStoreInfo["code"],
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        # @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        # @stepreruns()
        # def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
        #     params = deepcopy(self.params)
        #     params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        #     params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        #     params["storeCode"] = getStoreInfo["code"]
        #     with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
        #         assert r.status_code == 200
        #         assert r.json()["code"] == 200
        #         if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
        #             assert r.json()["data"]["total"] == 1
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
        #             assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
        #             assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
        #             assert r.json()["data"]["list"][0]["billType"] == 2 # 对账单类型
        #             assert r.json()["data"]["list"][0]["billTypeName"] == "月结" # 对账单类型
        #             assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
        #             assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
        #             assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
        #             assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
        #             assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
        #             assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
        #             assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
        #             assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
        #             assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
        #             assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
        #             assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
        #         else:
        #             assert r.json()["data"]["total"] == 0
      
        step_months_deposit_billCheck_page()
        if settled_store:
            step_mgmt_inventory_common_getStoreInfo()
            # 如有待提交，则作废
            step_01_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                for getStoreContractInvtBill in getStoreContractInvtBillList:
                    step_mgmt_store_contract_dropStoreContractInvtBill()
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            # 是否有待公司签署
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()
            # step_04_mgmt_store_contract_getStoreContractInvtBillList()

    @allure.severity(P1)
    @allure.title("添加库存对账单电子合同批量任务: 85月结账款对账单-分公司-立即生效")
    def test_06_mgmt_store_contract_addStoreContractInvtBill(self, login):
        
        getStoreContractInvtBillSettingInfo = {} # 获取公司签署人信息
        getStoreContractInvtBillList = [] # 查询库存对账单合同列表
        getStoreInfo = None # 获取服务中心信息
        currentOperatorName = login["data"]["username"]
        settled_store = None # 查询已月结服务中心

        @allure.step("查询已月结服务中心: 获取分公司编号")
        def step_months_deposit_billCheck_page():
            
            nonlocal settled_store
            data = deepcopy(self.data)
            with _months_deposit_billCheck_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["companyCode"] and i["storeCode"]:
                            settled_store = i
                            break
                                               
        @allure.step("查询库存对账单合同列表: 获取待提交的合同")
        def step_01_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            params = deepcopy(self.params)
            params["signStatus"] = 1 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("作废对账单电子合同")
        def step_mgmt_store_contract_dropStoreContractInvtBill():
            
            data = {
                "docNo": getStoreContractInvtBill
            }
            with _mgmt_store_contract_dropStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询库存对账单合同列表: 获取待店铺签署的合同")
        def step_02_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])

        @allure.step("批量撤回对账单电子合同")
        def step_mgmt_store_contract_batchRedoStoreContractInvtBill():
            
            data = {
                "docNos": getStoreContractInvtBillList
            }
            with _mgmt_store_contract_batchRedoStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询库存对账单合同列表: 获取待公司签署的合同")
        def step_03_mgmt_store_contract_getStoreContractInvtBillList():        
                
            nonlocal getStoreContractInvtBillList
            getStoreContractInvtBillList = []
            params = deepcopy(self.params)
            params["signStatus"] = 3 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
            params["signType"] = 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            params["companyCode"] = settled_store["companyCode"]
            with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getStoreContractInvtBillList.append(i["docNo"])
                                                
        @allure.step("获取公司签署人信息")
        def step_mgmt_store_contract_getStoreContractInvtBillSettingInfo():
            
            nonlocal getStoreContractInvtBillSettingInfo
            params = {
                "signType" : 3,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            } 
            with _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreContractInvtBillSettingInfo = r.json()["data"]
        
        @allure.step("添加库存对账单电子合同批量任务")
        def step_mgmt_store_contract_addStoreContractInvtBill():
            
            data = {
                "billStartMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "billEndMonth": f'{int(time.strftime("%Y")) - 1}12' if time.strftime("%Y%m").endswith("01") else str(int(time.strftime("%Y%m")) - 1),
                "companyCode": settled_store["companyCode"],
                "currentOperatorName": currentOperatorName,
                "signStartDate": datetime.datetime.now().strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 今天
                "billType": 2, # 对账单类型，1/实时，2/月结
                "storeCode": "",
                "companyCustomerId": getStoreContractInvtBillSettingInfo["fddCustomerId"], # 公司签署人法大大客户编号(必填)
                "companySignPerson": getStoreContractInvtBillSettingInfo["oaNo"], # 公司签署人OA工号(必填)
                "signType": 3 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
            }  
            with _mgmt_store_contract_addStoreContractInvtBill(data, self.access_token) as r:
                assert r.status_code == 200
                if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
                    assert r.json()["code"] == 200
                else:
                    assert r.json()["code"] == 0 and r.json()["message"] == "该服务中心已存在此时间范围的对账单，请撤销后重新提交"

        # @allure.step("查询库存对账单合同列表: 确认85实时库存对账单-待生效")
        # @stepreruns()
        # def step_04_mgmt_store_contract_getStoreContractInvtBillList():        
                
        #     params = deepcopy(self.params)
        #     params["signStatus"] = 2 # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
        #     params["signType"] = 2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
        #     params["storeCode"] = getStoreInfo["code"]
        #     with _mgmt_store_contract_getStoreContractInvtBillList(params, self.access_token) as r:
        #         assert r.status_code == 200
        #         assert r.json()["code"] == 200
        #         if getStoreContractInvtBillList == []: # 是否有待公司签署，不同断言
        #             assert r.json()["data"]["total"] == 1
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["generateTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 对账单生成时间
        #             assert r.json()["data"]["list"][0]["companyCode"] == getStoreInfo["companyCode"] # 所属分公司
        #             assert r.json()["data"]["list"][0]["storeCode"] == getStoreInfo["code"] # 服务中心编号
        #             assert r.json()["data"]["list"][0]["billType"] == 2 # 对账单类型
        #             assert r.json()["data"]["list"][0]["billTypeName"] == "月结" # 对账单类型
        #             assert r.json()["data"]["list"][0]["billMonth"] == time.strftime("%Y/%m",time.localtime(time.time())) # 对账单月份
        #             assert r.json()["data"]["list"][0]["leaderName"] == getStoreInfo["leaderName"] # 负责人
        #             assert r.json()["data"]["list"][0]["companySignPerson"] == getStoreContractInvtBillSettingInfo["oaNo"] # 公司签署人
        #             assert r.json()["data"]["list"][0]["isSignOffline"] == 0 # 是否已线下签署，0/否，1/是
        #             assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["signStartDate"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 发起签署日期
        #             assert r.json()["data"]["list"][0]["signEndDate"] is None # 签署截止日期
        #             assert r.json()["data"]["list"][0]["storeSignTime"] is None # 店铺签署时间
        #             assert r.json()["data"]["list"][0]["rejectionReason"] is None # 拒签理由
        #             assert r.json()["data"]["list"][0]["companySignTime"] is None # 公司签署时间
        #             assert r.json()["data"]["list"][0]["redoTime"] is None # 撤回时间
        #             assert r.json()["data"]["list"][0]["redoOperator"] is None # 撤回人
        #             assert r.json()["data"]["list"][0]["redoReason"] is None # 撤回理由
        #         else:
        #             assert r.json()["data"]["total"] == 0
      
        step_months_deposit_billCheck_page()
        if settled_store:
            # 如有待提交，则作废
            step_01_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                for getStoreContractInvtBill in getStoreContractInvtBillList:
                    step_mgmt_store_contract_dropStoreContractInvtBill()
            # 如有待店铺签署，则撤回
            step_02_mgmt_store_contract_getStoreContractInvtBillList()
            if getStoreContractInvtBillList:
                step_mgmt_store_contract_batchRedoStoreContractInvtBill()
            # 是否有待公司签署
            step_03_mgmt_store_contract_getStoreContractInvtBillList()
            step_mgmt_store_contract_getStoreContractInvtBillSettingInfo()
            step_mgmt_store_contract_addStoreContractInvtBill()
            # step_04_mgmt_store_contract_getStoreContractInvtBillList()
