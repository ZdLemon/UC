# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
from api.mall_mgmt_application._mgmt_inventory_common_isStoreInTrafficControl import _mgmt_inventory_common_isStoreInTrafficControl # 店铺是否处于交通管控
from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

from setting import P1, P2, P3, productCode_zh, productCode, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/addMortgageOrder")
class TestClass:
    """
    运营后台添加押货单
    /mgmt/inventory/order/addMortgageOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("运营后台添加押货单-成功路径: 添加押货单主路径检查")
    def test_01_mgmt_inventory_order_addMortgageOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 2 # 押货数量
        
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"]
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal getAvailableAmount
            params = {
                "storeCode": getStoreInfo["code"]
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAvailableAmount = r.json()["data"]

        @allure.step("店铺是否处于交通管控")
        def step_mgmt_inventory_common_isStoreInTrafficControl():  
            
            nonlocal isStoreInTrafficControl
            params = {
                "storeCode": getStoreInfo["code"]
            }
            with _mgmt_inventory_common_isStoreInTrafficControl(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]
                
        @allure.step("根据产品关键字搜索普通商品列表")
        def step_mgmt_inventory_order_searchProductsForAddPage():  
            
            nonlocal searchProductsForAddPage
            params = deepcopy(self.params)
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_inventory_order_searchProductsForAddPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductsForAddPage = r.json()["data"]["list"][0]
        
        @allure.step("运营后台添加押货单")
        def step_mgmt_inventory_order_addMortgageOrder():  
            
            nonlocal id
            data = {
                "invtMortgageOrderVO": {
                    "storeCode": getStoreInfo["code"],
                    "isDelivery": 1, # 0不需要发货 1需要发货
                    "remarks": "这个是客户急要的，仓库今天必须发出。" # 押货备注
                },
                "invtMortgageOrderProductVOList": [
                    {
                        "productCode": searchProductsForAddPage["productCode"], # 物品编号
                        "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
                    }
                ],
                "transId": f"KEY_{store}_{int(round(time.time() * 1000))}"
            }
            with _mgmt_inventory_order_addMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id =  r.json()["data"]

        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal getOrderDetail
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderDetail = r.json()["data"]
        
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_order_searchProductsForAddPage()
        step_mgmt_inventory_order_addMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()

    @allure.severity(P1)
    @allure.title("运营后台添加押货单-成功路径: 添加仅调账不发货押货单主路径检查")
    def test_02_mgmt_inventory_order_addMortgageOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 2 # 押货数量
        
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["code"] == store
                getStoreInfo = r.json()["data"]
        
        @allure.step("根据storeCode查询押货余额")
        def step_mgmt_inventory_mortgageAmount_getAvailableAmount():  
            
            nonlocal getAvailableAmount
            params = {
                "storeCode": getStoreInfo["code"]
            }
            with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAvailableAmount = r.json()["data"]

        @allure.step("店铺是否处于交通管控")
        def step_mgmt_inventory_common_isStoreInTrafficControl():  
            
            nonlocal isStoreInTrafficControl
            params = {
                "storeCode": getStoreInfo["code"]
            }
            with _mgmt_inventory_common_isStoreInTrafficControl(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]
                
        @allure.step("根据产品关键字搜索普通商品列表")
        def step_mgmt_inventory_order_searchProductsForAddPage():  
            
            nonlocal searchProductsForAddPage
            params = deepcopy(self.params)
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_inventory_order_searchProductsForAddPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductsForAddPage = r.json()["data"]["list"][0]
        
        @allure.step("运营后台添加押货单")
        def step_mgmt_inventory_order_addMortgageOrder():  
            
            nonlocal id
            data = {
                "invtMortgageOrderVO": {
                    "storeCode": getStoreInfo["code"],
                    "isDelivery": 0, # 0不需要发货 1需要发货
                    "remarks": "这个仅调账，不需要发货的，仓库不要发货哈" # 押货备注
                },
                "invtMortgageOrderProductVOList": [
                    {
                        "productCode": searchProductsForAddPage["productCode"], # 物品编号
                        "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
                    }
                ],
                "transId": f"KEY_{store}_{int(round(time.time() * 1000))}"
            }
            with _mgmt_inventory_order_addMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id =  r.json()["data"]

        @allure.step("后台获取押货单详情")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal getOrderDetail
            params = {
                "orderId": id
            }
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderDetail = r.json()["data"]
        
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_order_searchProductsForAddPage()
        step_mgmt_inventory_order_addMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()




