# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_pageList import data, _mgmt_inventory_disInventoryTransfer_pageList # 押货转移管理列表
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_addTransferList import _mgmt_inventory_disInventoryTransfer_addTransferList # 库存列表
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_getPermissionAndAmount import _mgmt_inventory_disInventoryTransfer_getPermissionAndAmount # 根据storeCode查询权限和当前押货余额
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_inventoryTotalMsg import _mgmt_inventory_disInventoryTransfer_inventoryTotalMsg # 库存信息合计
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_getLastRecord import _mgmt_inventory_disInventoryTransfer_getLastRecord # 根据服务中心查询最新库存转移记录
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_getDeposit import _mgmt_inventory_disInventoryTransfer_getDeposit # 根据storeCode查询保证金
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_addTransfer import _mgmt_inventory_disInventoryTransfer_addTransfer # 新建库存转移
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_recordList import _mgmt_inventory_disInventoryTransfer_recordList # 库存转移记录列表
from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_cancelPay import _mgmt_inventory_disInventoryTransfer_cancelPay # 取消支付

from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disInventoryTransfer/addTransfer")
class TestClass:
    """
    新建库存转移
    /mgmt/inventory/disInventoryTransfer/addTransfer
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("新建库存转移-成功路径: 新建库存转移检查")
    def test_mgmt_inventory_disInventoryTransfer_addTransfer(self):
        
        addTransferList = None # 库存列表:大于0的库存
        recordList = None # 库存转移记录列表

        @allure.step("库存转移记录列表：查看是否存在待支付的转移记录")
        def step_01_mgmt_inventory_disInventoryTransfer_recordList():
            
            nonlocal recordList
            data = {
                "storeCode": store_85, # 服务中心编号
                "pageSize": 10, 
                "pageNum": 1,
            }                
            with _mgmt_inventory_disInventoryTransfer_recordList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["status"] == 2:
                        recordList = i

        @allure.step("取消支付")
        def step_mgmt_inventory_disInventoryTransfer_cancelPay():
            
            params = {
                "id": recordList["id"]
            }               
            with _mgmt_inventory_disInventoryTransfer_cancelPay(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("押货转移管理列表")
        def step_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = store_85
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeCode"] == store_85
        
        @allure.step("库存列表")
        def step_01_mgmt_inventory_disInventoryTransfer_addTransferList():
            
            data = {
                "storeCode": store_85, # 服务中心编号
                "pageSize": 10, 
                "pageNum": 1,
            }                
            with _mgmt_inventory_disInventoryTransfer_addTransferList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("根据storeCode查询权限和当前押货余额")
        def step_mgmt_inventory_disInventoryTransfer_getPermissionAndAmount():
            
            params = {
                "storeCode": store_85  # str服务中心编号
            }               
            with _mgmt_inventory_disInventoryTransfer_getPermissionAndAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("库存信息合计")
        def step_mgmt_inventory_disInventoryTransfer_inventoryTotalMsg():
            
            data = {
                "storeCode": store_85, # 服务中心编号
                "pageSize": 10, 
                "pageNum": 1,
            }                
            with _mgmt_inventory_disInventoryTransfer_inventoryTotalMsg(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("根据服务中心查询最新库存转移记录")
        def step_mgmt_inventory_disInventoryTransfer_getLastRecord():
            
            params = {
                "storeCode": store_85  # str服务中心编号
            }               
            with _mgmt_inventory_disInventoryTransfer_getLastRecord(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("根据storeCode查询保证金")
        def step_mgmt_inventory_disInventoryTransfer_getDeposit():
            
            params = {
                "storeCode": store_85  # str服务中心编号
            }               
            with _mgmt_inventory_disInventoryTransfer_getDeposit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("库存列表:大于0的库存")
        def step_02_mgmt_inventory_disInventoryTransfer_addTransferList():
            
            nonlocal addTransferList
            data = {
                "storeCode": store_85, # 服务中心编号
                "productNumQuery": 1, # 传1大于0;0等于0;-1小于0;2不为0;不传为查全部
                "pageSize": 100000, 
                "pageNum": 1,
            }                
            with _mgmt_inventory_disInventoryTransfer_addTransferList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addTransferList = r.json()["data"]["list"][0]

        @allure.step("新建库存转移")
        def step_mgmt_inventory_disInventoryTransfer_addTransfer():
            
            data = {
                "applyType": "2", # 提交途径 1门店提交 2后台提交
                "storeCode": store_85, # 服务中心编号
                "productList":[
                    {
                        "transferNum": 1, # 转移数量
                        "oneThreePrice": addTransferList["securityPrice"], # 1:3押货价
                        "eightFivePrice": addTransferList["orderPrice"], # 85折押货价
                        "productCode": addTransferList["serialNo"] # 产品编号
                    }
                ]
            }           
            with _mgmt_inventory_disInventoryTransfer_addTransfer(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("库存转移记录列表")
        def step_mgmt_inventory_disInventoryTransfer_recordList():
            
            nonlocal recordList
            data = {
                "storeCode": store_85, # 服务中心编号
                "pageSize": 10, 
                "pageNum": 1,
            }                
            with _mgmt_inventory_disInventoryTransfer_recordList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                recordList = r.json()["data"]["list"][0]

        step_01_mgmt_inventory_disInventoryTransfer_recordList()
        if recordList:
            step_mgmt_inventory_disInventoryTransfer_cancelPay()                 
        step_mgmt_inventory_disInventoryTransfer_pageList()
        step_01_mgmt_inventory_disInventoryTransfer_addTransferList()
        step_mgmt_inventory_disInventoryTransfer_getPermissionAndAmount()
        step_mgmt_inventory_disInventoryTransfer_inventoryTotalMsg()
        step_mgmt_inventory_disInventoryTransfer_getLastRecord()
        step_mgmt_inventory_disInventoryTransfer_getDeposit()
        step_02_mgmt_inventory_disInventoryTransfer_addTransferList()
        step_mgmt_inventory_disInventoryTransfer_addTransfer()
        step_mgmt_inventory_disInventoryTransfer_recordList()

