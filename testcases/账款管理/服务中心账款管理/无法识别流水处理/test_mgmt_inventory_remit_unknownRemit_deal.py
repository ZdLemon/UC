# coding:utf-8

from api.basic_services._login import _login
from api.mall_center_pay._pay_notify_mockBankflow import data as data02, _pay_notify_mockBankflow
from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_pageList import data, _mgmt_inventory_remit_unknownRemit_pageList
from api.mall_mgmt_application._mgmt_store_getStoreByCode import params, _mgmt_store_getStoreByCode
from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_deal import _mgmt_inventory_remit_unknownRemit_deal
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/remit/unknownRemit/deal")
class TestClass:
    """
    未知款项流水处理
    /mgmt/inventory/remit/unknownRemit/deal
    """
    
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("未知款项流水处理-成功路径：无法识别款确认押货款检查") 
    def test_01_mgmt_inventory_remit_unknownRemit_pageList(self):
        
        pageList = None # 待处理的未识别流水
        getStoreByCode = None # 服务中心信息
        
        @allure.step("生成无法识别流水，方便测试")    
        def step_pay_notify_mockBankflow():
            
            data = deepcopy(self.data02)
            data[0]["accountName"] = "我是无法识别的银行账户"
            data[0]["accountNo"] = "622123456789951753"
            data[0]["bankName"] = "中国工商银行深圳华南城支行"
            with _pay_notify_mockBankflow(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.text == "SUCCESS"
        
        @allure.step("未知款项流水分页搜索列表")
        def step_mgmt_inventory_remit_unknownRemit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
            with _mgmt_inventory_remit_unknownRemit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]

        @allure.step("根据服务中心编号获取服务中心")    
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreByCode = r.json()["data"]
        
        @allure.step("无法识别款确认押货款")    
        def step_mgmt_inventory_remit_unknownRemit_deal():
            
            data = pageList
            data["businessMode"] = 2
            data["changeReason"] = "汇押货款"
            data["dealRemark"] = "我是处理备注信息"
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["show"] = True 
            data["sourceType"] = 5 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
            data["storeCode"] = getStoreByCode["store"]["code"]  
            data["storeCodeSearch"] = True  
            data["storeName"] = getStoreByCode["store"]["name"]
            data["type"] = 2  
            data["sourceTypeList"] = [
                {
                    "id": 5,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 5,
                    "name": "无法识别款确认押货款",
                    "changeReason": "汇押货款",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "id": 6,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 6,
                    "name": "无法识别款退款",
                    "changeReason": "无",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "type": 15,
                    "name": "无法识别款不处理（需有批示或批文时可选择）",
                    "changeReason": "无"
                }
            ]
            with _mgmt_inventory_remit_unknownRemit_deal(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
                assert r.json()["message"] == "操作成功"

        step_pay_notify_mockBankflow()
        step_mgmt_inventory_remit_unknownRemit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_inventory_remit_unknownRemit_deal()

    @allure.severity(P2)
    @allure.title("未知款项流水处理-成功路径：无法识别款退款检查") 
    def test_02_mgmt_inventory_remit_unknownRemit_pageList(self):
        
        pageList = None # 待处理的未识别流水
        getStoreByCode = None # 服务中心信息
        
        @allure.step("生成无法识别流水，方便测试")    
        def step_pay_notify_mockBankflow():
            
            data = deepcopy(self.data02)
            data[0]["accountName"] = "我是无法识别的银行账户"
            data[0]["accountNo"] = "622123456789951753"
            data[0]["bankName"] = "中国工商银行深圳华南城支行"
            with _pay_notify_mockBankflow(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.text == "SUCCESS"
                
        @allure.step("未知款项流水分页搜索列表")
        def step_mgmt_inventory_remit_unknownRemit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
            with _mgmt_inventory_remit_unknownRemit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]

        @allure.step("根据服务中心编号获取服务中心")    
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreByCode = r.json()["data"]
        
        @allure.step("无法识别款退款")    
        def step_mgmt_inventory_remit_unknownRemit_deal():
            
            data = pageList
            data["businessMode"] = 2
            data["changeReason"] = "无"
            data["dealRemark"] = "我是处理备注信息"
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["show"] = True 
            data["sourceType"] = 6 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
            data["storeCode"] = getStoreByCode["store"]["code"]  
            data["storeCodeSearch"] = True  
            data["storeName"] = getStoreByCode["store"]["name"]
            data["type"] = 2  
            data["sourceTypeList"] = [
                {
                    "id": 5,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 5,
                    "name": "无法识别款确认押货款",
                    "changeReason": "汇押货款",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "id": 6,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 6,
                    "name": "无法识别款退款",
                    "changeReason": "无",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "type": 15,
                    "name": "无法识别款不处理（需有批示或批文时可选择）",
                    "changeReason": "无"
                }
            ]
            with _mgmt_inventory_remit_unknownRemit_deal(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
                assert r.json()["message"] == "操作成功"

        step_pay_notify_mockBankflow()
        step_mgmt_inventory_remit_unknownRemit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_inventory_remit_unknownRemit_deal()

    @allure.severity(P2)
    @allure.title("未知款项流水处理-成功路径：无法识别款不处理检查") 
    def test_03_mgmt_inventory_remit_unknownRemit_pageList(self):
        
        pageList = None # 待处理的未识别流水
        getStoreByCode = None # 服务中心信息
        
        @allure.step("生成无法识别流水，方便测试")    
        def step_pay_notify_mockBankflow():
            
            data = deepcopy(self.data02)
            data[0]["accountName"] = "我是无法识别的银行账户"
            data[0]["accountNo"] = "622123456789951753"
            data[0]["bankName"] = "中国工商银行深圳华南城支行"
            with _pay_notify_mockBankflow(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.text == "SUCCESS"
        
        @allure.step("未知款项流水分页搜索列表")
        def step_mgmt_inventory_remit_unknownRemit_pageList():
            
            nonlocal pageList
            data = deepcopy(self.data)
            data["dealStatus"] = 0 # 处理状态 0 待处理 1 已处理 2 -> 不处理
            with _mgmt_inventory_remit_unknownRemit_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageList = r.json()["data"]["list"][0]

        @allure.step("根据服务中心编号获取服务中心")    
        def step_mgmt_store_getStoreByCode():
            
            nonlocal getStoreByCode
            params = deepcopy(self.params)
            params["code"] = store_85                 
            with _mgmt_store_getStoreByCode(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreByCode = r.json()["data"]
        
        @allure.step("无法识别款不处理")    
        def step_mgmt_inventory_remit_unknownRemit_deal():
            
            data = pageList
            data["businessMode"] = 2
            data["changeReason"] = "无"
            data["dealRemark"] = "我是处理备注信息"
            data["leaderName"] = getStoreByCode["user"]["realname"]
            data["show"] = True 
            data["sourceType"] = 15 # 款项类型 5、无法识别款确认押货款、6无法识别款退款、 15无法识别款不处理
            data["storeCode"] = getStoreByCode["store"]["code"]  
            data["storeCodeSearch"] = True  
            data["storeName"] = getStoreByCode["store"]["name"]
            data["type"] = 2  
            data["sourceTypeList"] = [
                {
                    "id": 5,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 5,
                    "name": "无法识别款确认押货款",
                    "changeReason": "汇押货款",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "id": 6,
                    "createTime": None,
                    "updateTime": None,
                    "del": 0,
                    "type": 6,
                    "name": "无法识别款退款",
                    "changeReason": "无",
                    "bizType": 1,
                    "bizName": "银行汇款",
                    "detailType": 2
                }, 
                {
                    "type": 15,
                    "name": "无法识别款不处理（需有批示或批文时可选择）",
                    "changeReason": "无"
                }
            ]
            with _mgmt_inventory_remit_unknownRemit_deal(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
                assert r.json()["message"] == "操作成功"

        step_pay_notify_mockBankflow()
        step_mgmt_inventory_remit_unknownRemit_pageList()
        step_mgmt_store_getStoreByCode()
        step_mgmt_inventory_remit_unknownRemit_deal()





