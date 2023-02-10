# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单

from setting import P1, P2, P3, productCode_zh, productCode, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/updateMortgageOrder")
class TestClass:
    """
    修改押货单
    /mgmt/inventory/order/updateMortgageOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
        

    @allure.severity(P1)
    @allure.title("修改押货单-成功路径: 修改押货单检查")
    def test_01_mgmt_inventory_order_updateMortgageOrder(self, purchase_commit):
            
        orderSn = purchase_commit
        id = None
        produc = None # 押货单详情待修改产品信息
        availableAmount = None # 根据storeCode查询押货余额
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params = deepcopy(self.params) 
            params["orderSn"] = orderSn
            params["customFlag"] = 0 # 是否有为定制品押货单 0不是 1是
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal produc
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["productVoList"]:
                    if d["productNum"] > 1:
                            produc = d
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal availableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]
        
        @allure.step("店铺库存校验接口")
        def step_mgmt_inventory_order_checkProductInventory():  
            
            data = {
                "productDtoList":[ # 需要修改的商品
                    {
                        "productCode": produc["productCode"], # 商品一级编码
                        "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                        "productNum":1 # 需要减少的商品数量(绝对值)
                    }
                ],
                "storeCode": store # 店铺中心编号
            }
            with _mgmt_inventory_order_checkProductInventory(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == []
 
        @allure.step("改押货单")
        def step_mgmt_inventory_order_updateMortgageOrder():  
            
            data = {
                "updateInvtMortgageOrderVO": {
                    "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
                    "id": id # 押货单id
                },
                "invtMortgageProductVOList": [
                    {
                        "productCode": produc["productCode"], # 物品编码
                        "id": produc["id"], # 物品id
                        "productNum": 1, # 物品数量
                        "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                    }
                ],
                "isBatchCancel": 0 # 批量取消标志
            }
            with _mgmt_inventory_order_updateMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == None
                assert r.json()["message"] == "操作成功"
                 
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_checkProductInventory()
        step_mgmt_inventory_order_updateMortgageOrder()

    @allure.severity(P1)
    @allure.title("修改押货单-成功路径: 修改定制产品押货单检查")
    def test_02_mgmt_inventory_order_updateMortgageOrder(self, purchase_commitCusOrder):
            
        orderSn = purchase_commitCusOrder
        id = None
        produc = None # 押货单详情待修改产品信息
        availableAmount = None # 根据storeCode查询押货余额
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params = deepcopy(self.params) 
            params["orderSn"] = orderSn
            params["customFlag"] = 1 # 是否有为定制品押货单 0不是 1是
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal produc
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["productVoList"]:
                    if d["productNum"] > 1:
                            produc = d
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal availableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]
        
        @allure.step("店铺库存校验接口")
        def step_mgmt_inventory_order_checkProductInventory():  
            
            data = {
                "productDtoList":[ # 需要修改的商品
                    {
                        "productCode": produc["productCode"], # 商品一级编码
                        "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                        "productNum":1 # 需要减少的商品数量(绝对值)
                    }
                ],
                "storeCode": store # 店铺中心编号
            }
            with _mgmt_inventory_order_checkProductInventory(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == []
 
        @allure.step("改押货单")
        def step_mgmt_inventory_order_updateMortgageOrder():  
            
            data = {
                "updateInvtMortgageOrderVO": {
                    "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
                    "id": id # 押货单id
                },
                "invtMortgageProductVOList": [
                    {
                        "productCode": produc["productCode"], # 物品编码
                        "id": produc["id"], # 物品id
                        "productNum": 1, # 物品数量
                        "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                    }
                ],
                "isBatchCancel": 0 # 批量取消标志
            }
            with _mgmt_inventory_order_updateMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == None
                assert r.json()["message"] == "操作成功"
                 
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_checkProductInventory()
        step_mgmt_inventory_order_updateMortgageOrder()

    @allure.severity(P1)
    @allure.title("修改押货单-成功路径: 批量取消或欠货停发检查")
    def test_03_mgmt_inventory_order_updateMortgageOrder(self, purchase_commit):
            
        orderSn = purchase_commit
        id = None
        produc = None # 押货单详情待修改产品信息
        availableAmount = None # 根据storeCode查询押货余额
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params = deepcopy(self.params) 
            params["orderSn"] = orderSn
            params["customFlag"] = 0 # 是否有为定制品押货单 0不是 1是
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal produc
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["productVoList"]:
                    if d["productNum"] > 1:
                            produc = d
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal availableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]
        
        @allure.step("店铺库存校验接口")
        def step_mgmt_inventory_order_checkProductInventory():  
            
            data = {
                "productDtoList":[ # 需要修改的商品
                    {
                        "productCode": produc["productCode"], # 商品一级编码
                        "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                        "productNum": produc["productNum"] # 需要减少的商品数量(绝对值)
                    }
                ],
                "storeCode": store # 店铺中心编号
            }
            with _mgmt_inventory_order_checkProductInventory(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == []
 
        @allure.step("改押货单")
        def step_mgmt_inventory_order_updateMortgageOrder():  
            
            data = {
                "updateInvtMortgageOrderVO": {
                    "orderRemarks": "没钱了，让公司欠货停发或批量取消押货单", # 押货单备注
                    "id": id # 押货单id
                },
                "invtMortgageProductVOList": [
                    {
                        "productCode": produc["productCode"], # 物品编码
                        "id": produc["id"], # 物品id
                        "productNum": 0, # 物品数量
                        "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                    }
                ],
                "isBatchCancel": 1 # 批量取消标志
            }
            with _mgmt_inventory_order_updateMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == None
                assert r.json()["message"] == "操作成功"
                 
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_checkProductInventory()
        step_mgmt_inventory_order_updateMortgageOrder()

    @allure.severity(P1)
    @allure.title("修改押货单-成功路径: 修改定制产品押货单检查")
    def test_04_mgmt_inventory_order_updateMortgageOrder(self, purchase_commitCusOrder):
            
        orderSn = purchase_commitCusOrder
        id = None
        produc = None # 押货单详情待修改产品信息
        availableAmount = None # 根据storeCode查询押货余额
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params = deepcopy(self.params) 
            params["orderSn"] = orderSn
            params["customFlag"] = 1 # 是否有为定制品押货单 0不是 1是
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal produc
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["productVoList"]:
                    if d["productNum"] > 1:
                            produc = d
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal availableAmount
            params = {
                "storeCode": store
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]
        
        @allure.step("店铺库存校验接口")
        def step_mgmt_inventory_order_checkProductInventory():  
            
            data = {
                "productDtoList":[ # 需要修改的商品
                    {
                        "productCode": produc["productCode"], # 商品一级编码
                        "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                        "productNum":produc["productNum"] # 需要减少的商品数量(绝对值)
                    }
                ],
                "storeCode": store # 店铺中心编号
            }
            with _mgmt_inventory_order_checkProductInventory(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == []
 
        @allure.step("改押货单")
        def step_mgmt_inventory_order_updateMortgageOrder():  
            
            data = {
                "updateInvtMortgageOrderVO": {
                    "orderRemarks": "没钱了，让公司欠货停发或批量取消押货单", # 押货单备注
                    "id": id # 押货单id
                },
                "invtMortgageProductVOList": [
                    {
                        "productCode": produc["productCode"], # 物品编码
                        "id": produc["id"], # 物品id
                        "productNum": 0, # 物品数量
                        "productMortgagePrice": produc["productMortgagePrice"] # 物品押货价
                    }
                ],
                "isBatchCancel": 1 # 批量取消标志
            }
            with _mgmt_inventory_order_updateMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == None
                assert r.json()["message"] == "操作成功"
                 
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_order_checkProductInventory()
        step_mgmt_inventory_order_updateMortgageOrder()
  