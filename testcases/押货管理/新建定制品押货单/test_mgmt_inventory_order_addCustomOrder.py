# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
from api.mall_mgmt_application._mgmt_inventory_common_isStoreInTrafficControl import _mgmt_inventory_common_isStoreInTrafficControl # 店铺是否处于交通管控
from api.mall_mgmt_application._mgmt_inventory_order_getCusProductsForOpAddPage import params, _mgmt_inventory_order_getCusProductsForOpAddPage # 运营后台提交定制品押货单页面的押货商品搜索列表
from api.mall_mgmt_application._mgmt_inventory_order_addCustomOrder import _mgmt_inventory_order_addCustomOrder # 添加定制品押货单
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
@allure.story("/mgmt/inventory/order/addCustomOrder")
class TestClass:
    """
    添加定制品押货单
    /mgmt/inventory/order/addCustomOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("运营后台添加定制品押货单-成功路径: 添加定制品押货单主路径检查")
    def test_01_mgmt_inventory_order_addCustomOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        getCusProductsForOpAddPage = None # 根据产品关键字搜索普通商品列表
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
                
        @allure.step("运营后台提交定制品押货单页面的押货商品搜索列表")
        def step_mgmt_inventory_order_getCusProductsForOpAddPage():  
            
            nonlocal getCusProductsForOpAddPage
            params = deepcopy(self.params)
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_inventory_order_getCusProductsForOpAddPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCusProductsForOpAddPage = r.json()["data"][0]
        
        @allure.step("运营后台添加押货单")
        def step_mgmt_inventory_order_addCustomOrder():  
            
            nonlocal id
            data = {
                "transId": f"KEY_{store}_{int(round(time.time() * 1000))}", # 业务id
                "isDelivery": 1, # 店铺中心无需填写 0不需要发货 1需要发货
                "storeCode": getStoreInfo["code"],
                "orderRemarks": "这个是客户急要的定制品，仓库今天必须发出。", # 备注 店铺中心无需填写
                "productList": [{
                    "productCode": getCusProductsForOpAddPage["productCode"], # 押货商品编码
                    "productSecondCode": getCusProductsForOpAddPage["subProductList"][0]["productSecCode"], # 押货商品二级编码
                    "productMortgagePrice": getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"], # 商品押货价
                    "productNum": productNum # 押货商品数量
                }]
            }
            with _mgmt_inventory_order_addCustomOrder(data, self.access_token) as r:
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
        step_mgmt_inventory_order_getCusProductsForOpAddPage()
        step_mgmt_inventory_order_addCustomOrder()
        step_mgmt_inventory_order_getOrderDetail()

    @allure.severity(P1)
    @allure.title("运营后台添加定制品押货单-成功路径: 添加定制品仅调账不发货押货单主路径检查")
    def test_02_mgmt_inventory_order_addCustomOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        getCusProductsForOpAddPage = None # 根据产品关键字搜索普通商品列表
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
                
        @allure.step("运营后台提交定制品押货单页面的押货商品搜索列表")
        def step_mgmt_inventory_order_getCusProductsForOpAddPage():  
            
            nonlocal getCusProductsForOpAddPage
            params = deepcopy(self.params)
            params["storeCode"] = getStoreInfo["code"]
            with _mgmt_inventory_order_getCusProductsForOpAddPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCusProductsForOpAddPage = r.json()["data"][0]
        
        @allure.step("运营后台添加押货单")
        def step_mgmt_inventory_order_addCustomOrder():  
            
            nonlocal id
            data = {
                "transId": f"KEY_{store}_{int(round(time.time() * 1000))}", # 业务id
                "isDelivery": 0, # 店铺中心无需填写 0不需要发货 1需要发货
                "storeCode": getStoreInfo["code"],
                "orderRemarks": "这个是仅调账押货单，仓库不需要发货。", # 备注 店铺中心无需填写
                "productList": [{
                    "productCode": getCusProductsForOpAddPage["productCode"], # 押货商品编码
                    "productSecondCode": getCusProductsForOpAddPage["subProductList"][0]["productSecCode"], # 押货商品二级编码
                    "productMortgagePrice": getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"], # 商品押货价
                    "productNum": productNum # 押货商品数量
                }]
            }
            with _mgmt_inventory_order_addCustomOrder(data, self.access_token) as r:
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
        step_mgmt_inventory_order_getCusProductsForOpAddPage()
        step_mgmt_inventory_order_addCustomOrder()
        step_mgmt_inventory_order_getOrderDetail()


