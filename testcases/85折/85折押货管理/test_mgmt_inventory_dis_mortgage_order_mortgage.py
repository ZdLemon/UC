# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_getMortgageAmount import _mgmt_inventory_dis_mortgage_order_getMortgageAmount # 查询店铺押货余额与限额
from api.mall_mgmt_application._mgmt_inventory_common_isStoreInTrafficControl import _mgmt_inventory_common_isStoreInTrafficControl # 店铺是否处于交通管控
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import params, _mgmt_inventory_dis_mortgage_order_searchProductPage # 关键字搜索可押货商品分页
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_fetchFreightTemplate import _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate # 获取最新的运费计算模板
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import _mgmt_inventory_dis_mortgage_order_mortgage # 押货下单

from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import time
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
class TestClass:
    """
    押货下单
    /mgmt/inventory/dis/mortgage/order/mortgage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("押货下单-成功路径: 85折押货下单检查")
    @pytest.mark.skip()
    def test_01_mgmt_inventory_dis_mortgage_order_mortgage(self):
        
        getStoreInfo = None # 获取服务中心信息
        getMortgageAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        searchProductPage = None # 新增押货单页面:根据产品关键字搜索普通商品列表
        fetchFreightTemplate = None # 获取最新的运费计算模板
        mortgageNum = 2 # 押货数量
        mortgage = None # 押货下单
        
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store_85
            }               
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"]

        @allure.step("查询店铺押货余额与限额")
        def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
            
            nonlocal getMortgageAmount
            params = {
                "storeCode": getStoreInfo["code"]
            }               
            with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getMortgageAmount = r.json()["data"]

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
         
        @allure.step("关键字搜索可押货商品分页")
        def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params)
            params["storeCode"] = getStoreInfo["code"]
            params["keyword"] = productCode        
            with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["productCode"] == productCode:
                            searchProductPage = i
 
        @allure.step("获取最新的运费计算模板")
        def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
            
            nonlocal fetchFreightTemplate             
            with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                fetchFreightTemplate = r.json()["data"]
                                  
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal mortgage
            data = {
                "storeCode": getStoreInfo["code"], 
                "isDelivery": 1, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": mortgageNum # 押货商品数量
                }],
                "transId": f"{getStoreInfo['code']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
            }            
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                mortgage = r.json()["data"]

        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_dis_mortgage_order_searchProductPage()
        step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
        step_mgmt_inventory_dis_mortgage_order_mortgage()

    @allure.severity(P2)
    @allure.title("押货下单-失败路径: 85折押货下单重复transId检查")
    def test_02_mgmt_inventory_dis_mortgage_order_mortgage(self):

        getStoreInfo = None # 获取服务中心信息
        getMortgageAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        searchProductPage = None # 新增押货单页面:根据产品关键字搜索普通商品列表
        fetchFreightTemplate = None # 获取最新的运费计算模板
        mortgageNum = 2 # 押货数量
        mortgage = None # 押货下单
        
        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store_85
            }               
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"]

        @allure.step("查询店铺押货余额与限额")
        def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
            
            nonlocal getMortgageAmount
            params = {
                "storeCode": getStoreInfo["code"]
            }               
            with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getMortgageAmount = r.json()["data"]

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
         
        @allure.step("关键字搜索可押货商品分页")
        def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params)
            params["storeCode"] = getStoreInfo["code"]
            params["keyword"] = productCode        
            with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        if i["productCode"] == productCode:
                            searchProductPage = i
 
        @allure.step("获取最新的运费计算模板")
        def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
            
            nonlocal fetchFreightTemplate             
            with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                fetchFreightTemplate = r.json()["data"]
                                  
        @allure.step("押货下单")
        def step_01_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal mortgage
            data = {
                "storeCode": getStoreInfo["code"], 
                "isDelivery": 1, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": mortgageNum # 押货商品数量
                }],
                "transId": transId # 业务id 902208_1649053566676
            }            
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                mortgage = r.json()["data"]

        @allure.step("押货下单")
        def step_02_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal mortgage
            data = {
                "storeCode": getStoreInfo["code"], 
                "isDelivery": 0, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": mortgageNum * 2 # 押货商品数量
                }],
                "transId": transId # 业务id 902208_1649053566676
            }            
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                mortgage = r.json()["data"]

        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_dis_mortgage_order_searchProductPage()
        step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
        transId = f"KEY_{getStoreInfo['code']}_{int(round(time.time() * 1000))}"
        step_01_mgmt_inventory_dis_mortgage_order_mortgage()
        step_02_mgmt_inventory_dis_mortgage_order_mortgage()