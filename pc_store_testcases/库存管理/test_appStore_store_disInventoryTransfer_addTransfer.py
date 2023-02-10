# coding:utf-8

from api.mall_store_application._appStore_store_disInventoryTransfer_totalMsg import _appStore_store_disInventoryTransfer_totalMsg # 转移的合计信息
from api.mall_store_application._appStore_store_disInventoryTransfer_recordList import _appStore_store_disInventoryTransfer_recordList # 库存转移记录列表
from api.mall_store_application._appStore_store_disInventoryTransfer_addTransferList import _appStore_store_disInventoryTransfer_addTransferList # 库存列表

from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import time


@allure.feature("mall_store_application")
@allure.story("/appStore/store/disInventoryTransfer/addTransfer")
class TestClass:
    """
    新建库存转移记录
    /appStore/store/disInventoryTransfer/addTransfer
    """
    def setup_class(self):
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P1)
    @allure.title("新建库存转移记录-成功路径:新建库存转移记录检查")
    def test_appStore_store_disInventoryTransfer_addTransfer(self):
        
        addTransferList = None # 库存列表
        recordList = None # 库存转移记录列表
        
        @allure.step("转移的合计信息")
        def step_appStore_store_disInventoryTransfer_totalMsg():
            
            data = {
                "storeCode": store_85,
                "pageNum":1,
                "pageSize":20
            }
            with _appStore_store_disInventoryTransfer_totalMsg(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("库存转移记录列表")
        def step_01_appStore_store_disInventoryTransfer_recordList():
            
            data = {
                "storeCode": store_85,
                "pageNum":1,
                "pageSize":20
            }
            with _appStore_store_disInventoryTransfer_recordList(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                
        @allure.step("库存列表")
        def step_appStore_store_disInventoryTransfer_addTransferList():
            
            nonlocal addTransferList
            data = {
                "storeCode": store_85, # 服务中心编号
                "query": "", # 搜索条件
                "pageNum": 1,
                "pageSize": 10000,
                "productNumQuery": 2 # 传1大于0;0等于0;-1小于0;2不为0;不传为查全部
            }
            with _appStore_store_disInventoryTransfer_addTransferList(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                addTransferList = r.json()["data"]["list"][0]
                
        @allure.step("新建库存转移记录")
        def step_appStore_store_disInventoryTransfer_addTransfer():
            
            data = {
                "applyType": 1, # 提交途径 1门店提交 2后台提交
                "productList":[
                    {
                        "eightFivePrice": addTransferList["orderPrice"], # 85折押货价
                        "oneThreePrice": addTransferList["securityPrice"], # 1:3押货价
                        "productCode": addTransferList["serialNo"], # 产品编号
                        "transferNum": 1 # 转移数量
                    }
                ],
                "storeCode": store_85 # 服务中心编号
            }
            with _appStore_store_disInventoryTransfer_addTransfer(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("库存转移记录列表")
        def step_02_appStore_store_disInventoryTransfer_recordList():
            
            nonlocal recordList
            data = {
                "storeCode": store_85,
                "status": "1", # 状态 1已完成 2待支付 3已取消
                "pageNum":1,
                "pageSize":20
            }
            with _appStore_store_disInventoryTransfer_recordList(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
                recordList = r.json()["data"]["list"][0]
                                            
        step_appStore_store_disInventoryTransfer_totalMsg()
        step_01_appStore_store_disInventoryTransfer_recordList()
        step_appStore_store_disInventoryTransfer_addTransferList()
        step_appStore_store_disInventoryTransfer_addTransfer()
        step_02_appStore_store_disInventoryTransfer_recordList()



