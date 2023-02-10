# coding:utf-8

from api.mall_mgmt_application._mgmt_product_stock_list import data, _mgmt_product_stock_list

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store, username
from util.stepreruns import stepreruns
from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import uuid
import calendar
import datetime



@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/list")
class TestClass:
    """
    库存列表-全部tab列表检查
    /mgmt/product/stock/list
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("库存列表-成功路径: 支持模糊查询产品编号检查")
    def test_01_mgmt_product_stock_list(self):

        serialNo = None
        
        @allure.step("库存列表-获取产品编号")
        def step_01_mgmt_product_stock_list():
            
            nonlocal serialNo
            data = deepcopy(self.data)
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                serialNo = r.json()["data"]["list"][0]["serialNo"]
        
        @allure.step("精确查询产品编号")
        def step_02_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["serialNo"] = serialNo
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["serialNo"] == serialNo    

        @allure.step("模糊查询产品编号")
        def step_03_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["serialNo"] = serialNo[:-1]
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert serialNo[:-1] in i["serialNo"]
        
        step_01_mgmt_product_stock_list() 
        step_02_mgmt_product_stock_list() 

                    
    @allure.severity(P2)
    @allure.title("库存列表-成功路径: 支持模糊查询产品名称检查")
    def test_02_mgmt_product_stock_list(self):

        productTitle = None
        
        @allure.step("库存列表-获取产品名称")
        def step_01_mgmt_product_stock_list():
            
            nonlocal productTitle
            data = deepcopy(self.data)
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productTitle = r.json()["data"]["list"][0]["productTitle"]
        
        @allure.step("精确查询产品名称")
        def step_02_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["productTitle"] = productTitle
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert productTitle == i["productTitle"]      

        @allure.step("模糊查询产品名称")
        def step_03_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["productTitle"] = productTitle[:-1]
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert productTitle[:-1] == i["productTitle"]
        
        step_01_mgmt_product_stock_list() 
        step_02_mgmt_product_stock_list() 
        # step_03_mgmt_product_stock_list() 
                    

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/list")
class TestClass02:
    """
    库存列表-限量tab列表检查
    /mgmt/product/stock/list
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("库存列表-限量tab列表-成功路径: 支持模糊查询产品编号检查")
    def test_01_mgmt_product_stock_list(self):

        serialNo = None
        
        @allure.step("库存列表-获取产品编号")
        def step_01_mgmt_product_stock_list():
            
            nonlocal serialNo
            data = deepcopy(self.data)
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                serialNo = r.json()["data"]["list"][0]["serialNo"]
        
        @allure.step("精确查询产品编号")
        def step_02_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["serialNo"] = serialNo
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert serialNo in i["serialNo"]      

        @allure.step("模糊查询产品编号")
        def step_03_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["serialNo"] = serialNo[:-1]
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert serialNo[:-1] in i["serialNo"]
        
        step_01_mgmt_product_stock_list() 
        step_02_mgmt_product_stock_list() 
        # step_03_mgmt_product_stock_list() 
                    
    @allure.severity(P2)
    @allure.title("库存列表-限量tab列表-成功路径: 仅支持精确查询产品名称检查")
    def test_02_mgmt_product_stock_list(self):

        productTitle = None
        
        @allure.step("库存列表-获取产品名称")
        def step_01_mgmt_product_stock_list():
            
            nonlocal productTitle
            data = deepcopy(self.data)
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productTitle = r.json()["data"]["list"][0]["productTitle"]
        
        @allure.step("精确查询产品名称")
        def step_02_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["productTitle"] = productTitle
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert productTitle == i["productTitle"]      

        @allure.step("模糊查询产品名称")
        def step_03_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["productTitle"] = productTitle[:-1]
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert productTitle[:-1] == i["productTitle"]
        
        step_01_mgmt_product_stock_list() 
        step_02_mgmt_product_stock_list() 
        # step_03_mgmt_product_stock_list() 
                    
  
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/list")
class TestClass03:
    """
    库存列表-非限量tab列表检查
    /mgmt/product/stock/list
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("库存列表-非限量tab列表-成功路径: 支持模糊查询产品编号检查")
    def test_01_mgmt_product_stock_list(self):

        serialNo = None
        
        @allure.step("库存列表-获取产品编号")
        def step_01_mgmt_product_stock_list():
            
            nonlocal serialNo
            data = deepcopy(self.data)
            data["stockType"] = "2"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                serialNo = r.json()["data"]["list"][0]["serialNo"]
        
        @allure.step("精确查询产品编号")
        def step_02_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["serialNo"] = serialNo
            data["stockType"] = "2"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert serialNo in i["serialNo"]      

        @allure.step("模糊查询产品编号")
        def step_03_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["serialNo"] = serialNo[:-1]
            data["stockType"] = "2"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert serialNo[:-1] in i["serialNo"]
        
        step_01_mgmt_product_stock_list() 
        step_02_mgmt_product_stock_list() 
        # step_03_mgmt_product_stock_list() 
                    
    @allure.severity(P2)
    @allure.title("库存列表-非限量tab列表-成功路径: 仅支持精确查询产品名称检查")
    def test_02_mgmt_product_stock_list(self):

        productTitle = None
        
        @allure.step("库存列表-获取产品名称")
        def step_01_mgmt_product_stock_list():
            
            nonlocal productTitle
            data = deepcopy(self.data)
            data["stockType"] = "2"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productTitle = r.json()["data"]["list"][0]["productTitle"]
        
        @allure.step("精确查询产品名称")
        def step_02_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["productTitle"] = productTitle
            data["stockType"] = "2"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert productTitle == i["productTitle"]      

        @allure.step("模糊查询产品名称")
        def step_03_mgmt_product_stock_list():
            
            data = deepcopy(self.data)
            data["productTitle"] = productTitle[:-1]
            data["stockType"] = "2"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert productTitle[:-1] == i["productTitle"]
        
        step_01_mgmt_product_stock_list() 
        step_02_mgmt_product_stock_list() 
        # step_03_mgmt_product_stock_list() 
                    
  
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/list")
class TestClass04:
    """
    库存列表-限量tab列表:店铺系统数据操作检查
    /mgmt/product/stock/list
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 店铺押货数据检查")
    def test_01_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None
        
        @allure.step("店铺后台押货")
        def purchase_commit():
            "店铺后台押货"
            
            from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
            from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
            from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
            from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            negateProducts = None # 负库存产品
            products = None # 产品信息
            availableAmount = None # 可用余额
            products_list = [] # 押货产品
            productNum = 2 # 押货产品数量
            orderSn = None # 押货单号
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息

            def step_appStore_purchaseOrder_negateProducts():
                "提交押货单页面的负库存押货商品列表"
                
                nonlocal negateProducts
                with _appStore_purchaseOrder_negateProducts(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    negateProducts = r.json()["data"]
            
            def step_appStore_purchaseOrder_products():
                "提交押货单页面的押货商品搜索"
                
                nonlocal products
                params = {
                    "pageNum": 1,
                    "pageSize": 40,
                    "product": productCode
                }
                with _appStore_purchaseOrder_products(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:
                            products = d
            
            def step_appStore_purchase_balanceAmount():
                "押货金额"
                
                nonlocal availableAmount
                with _appStore_purchase_balanceAmount(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]["availableAmount"]
            
            def step_appStore_purchase_commit():
                "提交押货单"
                
                nonlocal orderSn
                data = {
                    "list": products_list,
                    "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
                }
                with _appStore_purchase_commit(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["message"] == "操作成功"
                    orderSn = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 
        
            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            step_appStore_purchaseOrder_negateProducts()
            step_appStore_purchaseOrder_products()
            
            if negateProducts != []:
                for d in negateProducts:
                    products_list.append({
                        "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                        "productCode": d["productCode"], # 押货商品编码
                        "productNum": -d["currentStock"] # 押货商品数量
                    })
            else:
                products_list.append({
                        "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                        "productCode": products["productCode"], # 押货商品编码
                        "productNum": productNum # 押货商品数量
                    })
            
            step_appStore_purchase_balanceAmount()
            
            if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_appStore_purchase_commit()
            
            return orderSn
        
        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        purchase_commit() 
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 店铺押货退货数据检查")
    def test_02_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None
        
        @allure.step("店铺后台押货")
        def purchase_commit():
            "店铺后台押货"
            
            from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
            from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
            from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
            from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            negateProducts = None # 负库存产品
            products = None # 产品信息
            availableAmount = None # 可用余额
            products_list = [] # 押货产品
            productNum = 2 # 押货产品数量
            orderSn = None # 押货单号
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息

            def step_appStore_purchaseOrder_negateProducts():
                "提交押货单页面的负库存押货商品列表"
                
                nonlocal negateProducts
                with _appStore_purchaseOrder_negateProducts(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    negateProducts = r.json()["data"]
            
            def step_appStore_purchaseOrder_products():
                "提交押货单页面的押货商品搜索"
                
                nonlocal products
                params = {
                    "pageNum": 1,
                    "pageSize": 40,
                    "product": productCode
                }
                with _appStore_purchaseOrder_products(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:
                            products = d
            
            def step_appStore_purchase_balanceAmount():
                "押货金额"
                
                nonlocal availableAmount
                with _appStore_purchase_balanceAmount(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]["availableAmount"]
            
            def step_appStore_purchase_commit():
                "提交押货单"
                
                nonlocal orderSn
                data = {
                    "list": products_list,
                    "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
                }
                with _appStore_purchase_commit(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["message"] == "操作成功"
                    orderSn = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 
        
            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            step_appStore_purchaseOrder_negateProducts()
            step_appStore_purchaseOrder_products()
            
            if negateProducts != []:
                for d in negateProducts:
                    products_list.append({
                        "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                        "productCode": d["productCode"], # 押货商品编码
                        "productNum": -d["currentStock"] # 押货商品数量
                    })
            else:
                products_list.append({
                        "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                        "productCode": products["productCode"], # 押货商品编码
                        "productNum": productNum # 押货商品数量
                    })
            
            step_appStore_purchase_balanceAmount()
            
            if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_appStore_purchase_commit()
            
            return orderSn
               
        @allure.step("店铺后台押货退货")
        def purchaseReturnOrder():
            "店铺后台押货退货"
            
            from api.mall_store_application._appStore_purchaseReturnOrder_list import params as params01, _appStore_purchaseReturnOrder_list # 押货退货单列表
            from api.basic_services._auth_getUserInfo import _auth_getUserInfo # 获取当前用户登录缓存信息
            from api.mall_store_application._appStore_common_getReason import _appStore_common_getReason # 获取各种退换货原因
            from api.mall_store_application._appStore_purchaseReturnOrder_returnProducts import _appStore_purchaseReturnOrder_returnProducts # 提交退货单页面的押货退货商品搜索
            from api.mall_store_application._appStore_purchaseReturnOrder_save import _appStore_purchaseReturnOrder_save # 提交退货单
            from api.mall_store_application._appStore_purchaseReturnOrder_returnInfo import _appStore_purchaseReturnOrder_returnInfo # 提交退回信息

            from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 完美后台获取各种退换货原因
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_addOpinion import _mgmt_inventory_returnOrder_addOpinion # 后台押货退货添加审批意见
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_auditOrder import  _mgmt_inventory_returnOrder_auditOrder # 后台审批押货退货单
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_inspectOrder import  _mgmt_inventory_returnOrder_inspectOrder # 后台押货退货验货

            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            
            purchaseReturnOrder = None # 押货退货单列表信息
            getUserInfo = None # 获取当前用户登录缓存信息
            getReason = None # 获取各种退换货原因
            returnProducts = None # 提交退货单页面的押货退货商品搜索
            purchaseReturnOrder_save = None # 退货单信息
            productNum = 2 # 退货数量
            
            getReason_02 = None # 完美后台获取各种退换货原因
            getOrderDetail = None # 完美后台押货退货单详情
            addOpinion = None # 后台押货退货添加审批意见
                       
            def step_appStore_purchaseReturnOrder_list():
                "押货退货单列表"
                
                nonlocal purchaseReturnOrder
                params = deepcopy(params01)
                with _appStore_purchaseReturnOrder_list(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    purchaseReturnOrder = r.json()["data"]["list"]
            
            def step_auth_getUserInfo():
                "获取当前用户登录缓存信息"
                
                nonlocal getUserInfo
                with _auth_getUserInfo(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    getUserInfo = r.json()["data"] 

            def step_appStore_common_getReason():
                "获取各种退换货原因"
                
                nonlocal getReason
                params = {
                    "type": 3, # 类型: 3退货 4换货
                }
                with _appStore_common_getReason(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    getReason = r.json()["data"]

            def step_appStore_purchaseReturnOrder_returnProducts():
                "提交退货单页面的押货退货商品搜索"
                
                nonlocal returnProducts
                params = {
                    "product": productCode, # 产品名称/产品编号
                    "pageNum": 1,
                    "pageSize": 20
                }
                with _appStore_purchaseReturnOrder_returnProducts(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]:
                        if d["productCode"] == productCode:
                            returnProducts = d

            def step_appStore_purchaseReturnOrder_save():
                "提交退货单"
                
                nonlocal purchaseReturnOrder_save
                data = {
                    "invtMortgageReturnOrderProductVOList": [{
                        "productCode": productCode, # 物品编号
                        "productNum": productNum # 退货数量
                    }],
                    "invtMortgageReturnOrderVO": {
                        "reasonFirst": getReason[1]["returnReason"], # 一级原因
                        "reasonFirstRemarks": "我就是想退货，你敢不同意吗" # 一级原因备注
                    }
                }
                with _appStore_purchaseReturnOrder_save(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    purchaseReturnOrder_save = r.json()["data"]

            def step_mgmt_inventory_common_getReason():
                "完美后台获取各种退换货原因"
                
                nonlocal getReason_02
                params = {
                    "type": 3, # 类型: 3退货 4换货
                }
                with _mgmt_inventory_common_getReason(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    getReason_02 = r.json()["data"]

            def step_mgmt_inventory_returnOrder_addOpinion():
                "完美后台押货退货添加审批意见"
                
                nonlocal addOpinion
                data = {
                    "orderId": purchaseReturnOrder_save["orderId"], # 押货或售后单id
                    "content": f"同意这个退货申请{purchaseReturnOrder_save['orderSn']}" # 意见内容
                }
                with _mgmt_inventory_returnOrder_addOpinion(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    addOpinion = r.json()["data"]

            def step_mgmt_inventory_returnOrder_getOrderDetail():
                "完美后台押货退货单详情"
                
                nonlocal getOrderDetail
                params = {
                    "orderId": purchaseReturnOrder_save["orderId"]
                }
                with _mgmt_inventory_returnOrder_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    getOrderDetail = r.json()["data"]
                            
            def step_mgmt_inventory_returnOrder_auditOrder():
                "完美后台审批押货退货单"
                
                data = {
                    "id": purchaseReturnOrder_save["orderId"], # 押货退货单id
                    "auditRemarks": f"我只能同意退货申请{purchaseReturnOrder_save['orderSn']}", # 审核备注
                    "auditFileName": "", # 审核附件名称
                    "auditStatus": 1, # 审核结果 0不通过 1通过
                    "auditFileUrl": "", # 审核附件url
                    "reasonFirst": getReason_02[1]["returnReason"], # 一级原因
                    "reasonFirstRemarks": "我就是想退货，你敢不同意吗", # 一级原因备注
                    "reasonSecond": getReason_02[1]["reasonList"][1]["returnReason"], # 二级原因
                    "reasonSecondRemarks": "算了，这次就允许你退货吧", # 二级原因备注
                    "returnInfo": "深圳仓", # 退回地址信息
                    "preAuditFileUrl": ""
                }
                with _mgmt_inventory_returnOrder_auditOrder(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            def step_appStore_purchaseReturnOrder_returnInfo():
                "提交退回信息"
                
                data = {
                    "returnType": 2, # 退回类型 1自带 2邮寄
                    "expressCompany": "小何物流", # 物流公司
                    "expressNo": str(round(time.time())), # 物流单号
                    "expressFreightProof": "", # 物流费用凭证url
                    "expressFreightProofName": "", # 物流费用凭证名称
                    "processRemarks": "退回产品都要说明吗", # 退回处理说明
                    "orderId": purchaseReturnOrder_save["orderId"] # 退货单id
                }
                with _appStore_purchaseReturnOrder_returnInfo(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            def step_mgmt_inventory_returnOrder_inspectOrder():
                "完美后台押货退货验货"
                
                data = {
                    "orderId": purchaseReturnOrder_save["orderId"], # 退货单id
                    "inspectStatus": 1, # 验货意见 0不通过 1通过
                    "expressSubsidy": 100, # 运费补贴
                    "inspectRemarks": "我验货通过了", # 验货备注
                    "orderReturnRealAmount": getOrderDetail["orderVo"]["orderReturnAmount"], # orderReturnRealAmount
                    "productList": [{
                        "id": getOrderDetail["productVoList"][0]["id"], # 物品id
                        "productRealNum": getOrderDetail["productVoList"][0]["productNum"], # 物品实退数量
                        "productRealAmount": getOrderDetail["productVoList"][0]["productMortgagePrice"] * getOrderDetail["productVoList"][0]["productNum"] # 退货单实退金额总额
                    }]
                }
                with _mgmt_inventory_returnOrder_inspectOrder(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            step_appStore_purchaseReturnOrder_list()
            step_auth_getUserInfo()
            step_appStore_common_getReason()
            step_appStore_purchaseReturnOrder_returnProducts()
            step_appStore_purchaseReturnOrder_save()
            step_mgmt_inventory_common_getReason()
            step_mgmt_inventory_returnOrder_getOrderDetail()
            step_mgmt_inventory_returnOrder_addOpinion()
            step_mgmt_inventory_returnOrder_auditOrder()
            step_appStore_purchaseReturnOrder_returnInfo()
            step_mgmt_inventory_returnOrder_inspectOrder()
            
            return purchaseReturnOrder_save["orderSn"]
  
        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) - 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        purchase_commit()
        step_01_mgmt_product_stock_list()
        purchaseReturnOrder() 
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 店铺套装组合数据检查")
    def test_03_mgmt_product_stock_list(self, onSaleVersion, returnOrder_auditOrder_zh, db_mall_center_inventory):
        
        stock_list = None
        combine_detail = None # 套装组合明细
        
        def combine_confirm():
            "套装组合"
            
            from api.mall_store_application._appStore_inventory_combine_page import params as params01, _appStore_inventory_combine_page # 套装组合列表
            from api.mall_store_application._appStore_inventory_combine_preview import _appStore_inventory_combine_preview # 套装组合预览
            from api.mall_store_application._appStore_inventory_combine_confirm import _appStore_inventory_combine_confirm # 确认套装组合
            from api.mall_store_application._appStore_inventory_combine_history_page import _appStore_inventory_combine_history_page # 套装组合记录列表
            from api.mall_store_application._appStore_inventory_combine_detail import _appStore_inventory_combine_detail # 套装组合明细
            
            store_token = os.environ["store_token"]
            combine_page = None # 套装组合
            history_page = None # 套装组合记录
            combine_detail = None # 套装组合明细
            
            def test_appStore_inventory_combine_page():
                "套装组合列表:获取套装组合"
                
                nonlocal combine_page
                params = deepcopy(params01)
                with _appStore_inventory_combine_page(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    combine_page = r.json()["data"]["list"][0]
            
            def test_appStore_inventory_combine_preview():
                "套装组合预览"
                
                params = {
                    "id": combine_page["id"], # 套装组合id
                    "combineNum": combine_page["maxCombine"], # 套装组合数量
                    "productCode": combine_page["productCode"]
                }
                with _appStore_inventory_combine_preview(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            def test_appStore_inventory_combine_confirm():
                "确认套装组合"
                
                data = {
                    "combineId": combine_page["id"], # 套装组合id
                    "combineNum": 1, #combine_page["maxCombine"], # 套装组合数量
                    "productCode": combine_page["productCode"]
                }
                with _appStore_inventory_combine_confirm(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            def test_appStore_inventory_combine_history_page():
                "套装组合记录列表"
                
                nonlocal history_page
                params = {
                    "pageNum": 1,
                    "pageSize": 20,
                    "beginTime": "", # 开始时间
                    "endTime": "" # 结束时间
                }
                with _appStore_inventory_combine_history_page(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    history_page = r.json()["data"]["list"][0]

            @stepreruns()
            def test_appStore_inventory_combine_detail():
                "套装组合明细"
                
                nonlocal combine_detail
                params = {
                    "id": history_page["id"], # 套装组合id
                }
                with _appStore_inventory_combine_detail(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is not None
                    combine_detail = r.json()["data"]

            test_appStore_inventory_combine_page()
            test_appStore_inventory_combine_preview()
            test_appStore_inventory_combine_confirm()
            test_appStore_inventory_combine_history_page()
            test_appStore_inventory_combine_detail()
            
            return combine_detail

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) - combine_detail["combineNum"] * 5) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis
        
        step_01_mgmt_product_stock_list()
        combine_detail = combine_confirm() # 套装组合明细
        step_02_mgmt_product_stock_list() 

                     
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/list")
class TestClass05:
    """
    库存列表-限量tab列表:完美运营后台数据操作检查
    /mgmt/product/stock/list
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美运营后台押货数据检查")
    def test_01_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None
        
        @allure.step("运营后台押货")
        def auditMortgageOrder():
            "运营后台押货"
            
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
            from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
            from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
            from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
            from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            access_token = os.environ["access_token"]
            
            getStoreInfo = None # 获取服务中心信息
            availableAmount = None # 根据storeCode查询押货余额
            searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
            products_list = [] # 押货产品
            id = None # 押货单id
            getOrderDetail = None # 押货单详情
            productNum = 2 # 押货数量
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息
            
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"]
            
            def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
                "根据storeCode查询押货余额"  
                
                nonlocal availableAmount
                params = {
                    "storeCode": store
                }
                with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]
            
            def step_mgmt_inventory_order_searchProductsForAddPage(): 
                "根据产品关键字搜索普通商品列表" 
                
                nonlocal searchProductsForAddPage
                params = deepcopy(params01)
                params["storeCode"] = store
                params["keyword"] = productCode
                with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:   
                            searchProductsForAddPage = d
            
            def step_mgmt_inventory_order_addMortgageOrder(): 
                "运营后台添加押货单" 
                
                nonlocal id
                data = {
                    "invtMortgageOrderVO": {
                        "storeCode": store,
                        "isDelivery": 1, # 0不需要发货 1需要发货
                        "remarks": "" # 押货备注
                    },
                    "invtMortgageOrderProductVOList": [
                        {
                            "productCode": productCode, # 物品编号
                            "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                            "productNum": productNum # 数量
                        }
                    ]
                }
                with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    id =  r.json()["data"]
            
            def step_mgmt_inventory_order_auditMortgageOrder():
                "运营后台审批押货单"
                
                data = {
                    "id": id, # 押货单id
                    "auditStatus": 1, # 审核结果 0不通过 1通过
                    "auditRemarks": f"同意提交押货单申请" # 审核备注
                }
                with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == 1
            
            def step_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情"
                
                nonlocal getOrderDetail
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getOrderDetail = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 

            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True
                
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_inventory_mortgageAmount_getAvailableAmount()
            step_mgmt_inventory_order_searchProductsForAddPage()
            
            products_list.append({
                            "productCode": productCode, # 物品编号
                            "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                            "productNum": productNum # 数量
            })
            
            if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_mgmt_inventory_order_addMortgageOrder()
            step_mgmt_inventory_order_auditMortgageOrder()
            step_mgmt_inventory_order_getOrderDetail()
            
            return getOrderDetail["orderVo"]["orderSn"]

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        auditMortgageOrder()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美运营后台仅调账不发货押货单数据检查")
    def test_02_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None
        
        @allure.step("运营后台仅调账不发货押货单")
        def auditMortgageOrder_isDelivery():
            "运营后台仅调账不发货押货单"
            
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
            from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params as params01, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
            from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
            from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
            from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            access_token = os.environ["access_token"]
            
            getStoreInfo = None # 获取服务中心信息
            availableAmount = None # 根据storeCode查询押货余额
            searchProductsForAddPage = None # 根据产品关键字搜索普通商品列表
            products_list = [] # 押货产品
            id = None # 押货单id
            getOrderDetail = None # 押货单详情
            productNum = 2 # 押货数量
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息
            
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"]
            
            def step_mgmt_inventory_mortgageAmount_getAvailableAmount():
                "根据storeCode查询押货余额"  
                
                nonlocal availableAmount
                params = {
                    "storeCode": store
                }
                with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]
            
            def step_mgmt_inventory_order_searchProductsForAddPage(): 
                "根据产品关键字搜索普通商品列表" 
                
                nonlocal searchProductsForAddPage
                params = deepcopy(params01)
                params["storeCode"] = store
                params["keyword"] = productCode
                with _mgmt_inventory_order_searchProductsForAddPage(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:   
                            searchProductsForAddPage = d
            
            def step_mgmt_inventory_order_addMortgageOrder(): 
                "运营后台添加押货单" 
                
                nonlocal id
                data = {
                    "invtMortgageOrderVO": {
                        "storeCode": store,
                        "isDelivery": 0, # 0不需要发货 1需要发货
                        "orderRemarks": "",
                        "remarks": "我要公司帮忙押货，因为店铺系统不会用" # 押货备注
                    },
                    "invtMortgageOrderProductVOList": [
                        {
                            "productCode": productCode, # 物品编号
                            "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                            "productNum": productNum # 数量
                        }
                    ]
                }
                with _mgmt_inventory_order_addMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    id =  r.json()["data"]
            
            def step_mgmt_inventory_order_auditMortgageOrder():
                "运营后台审批押货单"
                
                data = {
                    "id": id, # 押货单id
                    "auditStatus": 1, # 审核结果 0不通过 1通过
                    "auditRemarks": f"同意提交押货单申请" # 审核备注
                }
                with _mgmt_inventory_order_auditMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == 1
            
            def step_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情"
                
                nonlocal getOrderDetail
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getOrderDetail = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 

            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['productMortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True
                
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_inventory_mortgageAmount_getAvailableAmount()
            step_mgmt_inventory_order_searchProductsForAddPage()
            
            products_list.append({
                            "productCode": productCode, # 物品编号
                            "productMortgagePrice": searchProductsForAddPage["productMortgagePrice"], # 物品押货价
                            "productNum": productNum # 数量
            })
            
            if availableAmount < sum([d["productMortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_mgmt_inventory_order_addMortgageOrder()
            step_mgmt_inventory_order_auditMortgageOrder()
            step_mgmt_inventory_order_getOrderDetail()
            
            return getOrderDetail["orderVo"]["orderSn"]

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        auditMortgageOrder_isDelivery()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美运营后台普通押货单修改数据检查")
    def test_03_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None

        def purchase_commit():
            "店铺后台押货"
            
            from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
            from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
            from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
            from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            negateProducts = None # 负库存产品
            products = None # 产品信息
            availableAmount = None # 可用余额
            products_list = [] # 押货产品
            productNum = 2 # 押货产品数量
            orderSn = None # 押货单号
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息

            def step_appStore_purchaseOrder_negateProducts():
                "提交押货单页面的负库存押货商品列表"
                
                nonlocal negateProducts
                with _appStore_purchaseOrder_negateProducts(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    negateProducts = r.json()["data"]
            
            def step_appStore_purchaseOrder_products():
                "提交押货单页面的押货商品搜索"
                
                nonlocal products
                params = {
                    "pageNum": 1,
                    "pageSize": 40,
                    "product": productCode
                }
                with _appStore_purchaseOrder_products(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:
                            products = d
            
            def step_appStore_purchase_balanceAmount():
                "押货金额"
                
                nonlocal availableAmount
                with _appStore_purchase_balanceAmount(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]["availableAmount"]
            
            def step_appStore_purchase_commit():
                "提交押货单"
                
                nonlocal orderSn
                data = {
                    "list": products_list,
                    "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
                }
                with _appStore_purchase_commit(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["message"] == "操作成功"
                    orderSn = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 
        
            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            step_appStore_purchaseOrder_negateProducts()
            step_appStore_purchaseOrder_products()
            
            if negateProducts != []:
                for d in negateProducts:
                    products_list.append({
                        "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                        "productCode": d["productCode"], # 押货商品编码
                        "productNum": -d["currentStock"] # 押货商品数量
                    })
            else:
                products_list.append({
                        "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                        "productCode": products["productCode"], # 押货商品编码
                        "productNum": productNum # 押货商品数量
                    })
            
            step_appStore_purchase_balanceAmount()
            
            if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_appStore_purchase_commit()
            
            return orderSn
               
        @allure.step("普通押货单修改")
        def updateMortgageOrder():
            "普通押货单修改"
            
            from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
            from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
            from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
            from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
            
            access_token = os.environ["access_token"]        
            orderSn = purchase_commit()
            id = None
            produc = None # 押货单详情待修改产品信息
            availableAmount = None # 根据storeCode查询押货余额
            
            def step_mgmt_inventory_order_listMortgageOrder():
                "获取id"
                
                nonlocal id
                params = deepcopy(params01) 
                params["orderSn"] = orderSn
                with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    id = r.json()["data"]["list"][0]["id"]
            
            def step_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情"
                
                nonlocal produc
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["productVoList"]:
                        if d["productNum"] > 1:
                                produc = d
            
            def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
                "根据storeCode查询押货余额" 
                
                nonlocal availableAmount
                params = {
                    "storeCode": store
                }
                with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]
            
            def step_mgmt_inventory_order_checkProductInventory(): 
                "店铺库存校验接口" 
                
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
                with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == []

            def step_mgmt_inventory_order_updateMortgageOrder(): 
                "改押货单" 
                
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
                with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == None
                    assert r.json()["message"] == "操作成功"
                        
            step_mgmt_inventory_order_listMortgageOrder()
            step_mgmt_inventory_order_getOrderDetail()
            step_mgmt_inventory_mortgageAmount_getAvailableAmount()
            step_mgmt_inventory_order_checkProductInventory()
            step_mgmt_inventory_order_updateMortgageOrder()
            
            return orderSn

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 1) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        updateMortgageOrder()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美运营后台普通押货单批量修改数据检查")
    def test_04_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None

        def purchase_commit():
            "店铺后台押货"
            
            from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
            from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
            from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
            from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            negateProducts = None # 负库存产品
            products = None # 产品信息
            availableAmount = None # 可用余额
            products_list = [] # 押货产品
            productNum = 2 # 押货产品数量
            orderSn = None # 押货单号
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息

            def step_appStore_purchaseOrder_negateProducts():
                "提交押货单页面的负库存押货商品列表"
                
                nonlocal negateProducts
                with _appStore_purchaseOrder_negateProducts(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    negateProducts = r.json()["data"]
            
            def step_appStore_purchaseOrder_products():
                "提交押货单页面的押货商品搜索"
                
                nonlocal products
                params = {
                    "pageNum": 1,
                    "pageSize": 40,
                    "product": productCode
                }
                with _appStore_purchaseOrder_products(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:
                            products = d
            
            def step_appStore_purchase_balanceAmount():
                "押货金额"
                
                nonlocal availableAmount
                with _appStore_purchase_balanceAmount(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]["availableAmount"]
            
            def step_appStore_purchase_commit():
                "提交押货单"
                
                nonlocal orderSn
                data = {
                    "list": products_list,
                    "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
                }
                with _appStore_purchase_commit(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["message"] == "操作成功"
                    orderSn = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 
        
            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            step_appStore_purchaseOrder_negateProducts()
            step_appStore_purchaseOrder_products()
            
            if negateProducts != []:
                for d in negateProducts:
                    products_list.append({
                        "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                        "productCode": d["productCode"], # 押货商品编码
                        "productNum": -d["currentStock"] # 押货商品数量
                    })
            else:
                products_list.append({
                        "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                        "productCode": products["productCode"], # 押货商品编码
                        "productNum": productNum # 押货商品数量
                    })
            
            step_appStore_purchase_balanceAmount()
            
            if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_appStore_purchase_commit()
            
            return orderSn
               
        @allure.step("普通押货单批量修改")
        def updateMortgageOrder_0():
            "普通押货单批量修改"
            
            from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
            from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
            from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
            from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
                    
            access_token = os.environ["access_token"]
            orderSn = purchase_commit()
            id = None
            produc = None # 押货单详情待修改产品信息
            availableAmount = None # 根据storeCode查询押货余额
            
            def step_mgmt_inventory_order_listMortgageOrder():
                "获取id"
                
                nonlocal id
                params = deepcopy(params01) 
                params["orderSn"] = orderSn
                with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    id = r.json()["data"]["list"][0]["id"]
            
            def step_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情"
                
                nonlocal produc
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["productVoList"]:
                        if d["productNum"] > 1:
                                produc = d
            
            def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
                "根据storeCode查询押货余额" 
                
                nonlocal availableAmount
                params = {
                    "storeCode": store
                }
                with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]
            
            def step_mgmt_inventory_order_checkProductInventory(): 
                "店铺库存校验接口" 
                
                data = {
                    "productDtoList":[ # 需要修改的商品
                        {
                            "productCode": produc["productCode"], # 商品一级编码
                            "productSecCode": produc["productSecCode"], # 商品二级编码(非定制品不要传此字段)
                            "productNum": 2 # 需要减少的商品数量(绝对值)
                        }
                    ],
                    "storeCode": store # 店铺中心编号
                }
                with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == []

            def step_mgmt_inventory_order_updateMortgageOrder(): 
                "改押货单" 
                
                data = {
                    "updateInvtMortgageOrderVO": {
                        "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
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
                with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == None
                    assert r.json()["message"] == "操作成功"
                        
            step_mgmt_inventory_order_listMortgageOrder()
            step_mgmt_inventory_order_getOrderDetail()
            step_mgmt_inventory_mortgageAmount_getAvailableAmount()
            step_mgmt_inventory_order_checkProductInventory()
            step_mgmt_inventory_order_updateMortgageOrder()
            
            return orderSn

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 0) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        updateMortgageOrder_0()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美运营后台普通押货单欠货停发数据检查")
    def test_05_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None

        def purchase_commit():
            "店铺后台押货"
            
            from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
            from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
            from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
            from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            negateProducts = None # 负库存产品
            products = None # 产品信息
            availableAmount = None # 可用余额
            products_list = [] # 押货产品
            productNum = 2 # 押货产品数量
            orderSn = None # 押货单号
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息

            def step_appStore_purchaseOrder_negateProducts():
                "提交押货单页面的负库存押货商品列表"
                
                nonlocal negateProducts
                with _appStore_purchaseOrder_negateProducts(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    negateProducts = r.json()["data"]
            
            def step_appStore_purchaseOrder_products():
                "提交押货单页面的押货商品搜索"
                
                nonlocal products
                params = {
                    "pageNum": 1,
                    "pageSize": 40,
                    "product": productCode
                }
                with _appStore_purchaseOrder_products(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:
                            products = d
            
            def step_appStore_purchase_balanceAmount():
                "押货金额"
                
                nonlocal availableAmount
                with _appStore_purchase_balanceAmount(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]["availableAmount"]
            
            def step_appStore_purchase_commit():
                "提交押货单"
                
                nonlocal orderSn
                data = {
                    "list": products_list,
                    "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
                }
                with _appStore_purchase_commit(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["message"] == "操作成功"
                    orderSn = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 
        
            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            step_appStore_purchaseOrder_negateProducts()
            step_appStore_purchaseOrder_products()
            
            if negateProducts != []:
                for d in negateProducts:
                    products_list.append({
                        "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                        "productCode": d["productCode"], # 押货商品编码
                        "productNum": -d["currentStock"] # 押货商品数量
                    })
            else:
                products_list.append({
                        "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                        "productCode": products["productCode"], # 押货商品编码
                        "productNum": productNum # 押货商品数量
                    })
            
            step_appStore_purchase_balanceAmount()
            
            if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_appStore_purchase_commit()
            
            return orderSn
               
        def updateMortgageOrder():
            "普通押货单修改"
            
            from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
            from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
            from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
            from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
            
            access_token = os.environ["access_token"]        
            orderSn = purchase_commit()
            id = None
            produc = None # 押货单详情待修改产品信息
            availableAmount = None # 根据storeCode查询押货余额
            
            def step_mgmt_inventory_order_listMortgageOrder():
                "获取id"
                
                nonlocal id
                params = deepcopy(params01) 
                params["orderSn"] = orderSn
                with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    id = r.json()["data"]["list"][0]["id"]
            
            def step_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情"
                
                nonlocal produc
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["productVoList"]:
                        if d["productNum"] > 1:
                                produc = d
            
            def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
                "根据storeCode查询押货余额" 
                
                nonlocal availableAmount
                params = {
                    "storeCode": store
                }
                with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]
            
            def step_mgmt_inventory_order_checkProductInventory(): 
                "店铺库存校验接口" 
                
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
                with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == []

            def step_mgmt_inventory_order_updateMortgageOrder(): 
                "改押货单" 
                
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
                with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == None
                    assert r.json()["message"] == "操作成功"
                        
            step_mgmt_inventory_order_listMortgageOrder()
            step_mgmt_inventory_order_getOrderDetail()
            step_mgmt_inventory_mortgageAmount_getAvailableAmount()
            step_mgmt_inventory_order_checkProductInventory()
            step_mgmt_inventory_order_updateMortgageOrder()
            
            return orderSn

        @allure.step("普通押货单欠货停发")
        def updateMortgageOrder_1_0():
            "普通押货单欠货停发"
            
            from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params as params01, _mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
            from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
            from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
            from api.mall_mgmt_application._mgmt_inventory_order_updateMortgageOrder import _mgmt_inventory_order_updateMortgageOrder # 修改押货单
            
            access_token = os.environ["access_token"]        
            orderSn = updateMortgageOrder()
            returnOrderSn = None # 欠货停发后生产的退押货单
            id = None
            produc = None # 押货单详情待修改产品信息
            availableAmount = None # 根据storeCode查询押货余额
            
            def step_mgmt_inventory_order_listMortgageOrder():
                "获取id"
                
                nonlocal id
                params = deepcopy(params01) 
                params["orderSn"] = orderSn
                with _mgmt_inventory_order_listMortgageOrder(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    id = r.json()["data"]["list"][0]["id"]
            
            def step_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情"
                
                nonlocal produc
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    produc = r.json()["data"]["productVoList"][0]
            
            def step_mgmt_inventory_mortgageAmount_getAvailableAmount(): 
                "根据storeCode查询押货余额" 
                
                nonlocal availableAmount
                params = {
                    "storeCode": store
                }
                with _mgmt_inventory_mortgageAmount_getAvailableAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]
            
            def step_mgmt_inventory_order_checkProductInventory(): 
                "店铺库存校验接口" 
                
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
                with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == []

            def step_mgmt_inventory_order_updateMortgageOrder(): 
                "改押货单" 
                
                data = {
                    "updateInvtMortgageOrderVO": {
                        "orderRemarks": "没钱了，让公司修改下押货单", # 押货单备注
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
                with _mgmt_inventory_order_updateMortgageOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == None
                    assert r.json()["message"] == "操作成功"

            def step_02_mgmt_inventory_order_getOrderDetail():
                "后台获取押货单详情:退押货单号"
                
                nonlocal returnOrderSn
                params = {
                    "orderId": id
                }
                with _mgmt_inventory_order_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    returnOrderSn = r.json()["data"]["editLogList"][0]["returnOrderSn"]
                        
            step_mgmt_inventory_order_listMortgageOrder()
            step_mgmt_inventory_order_getOrderDetail()
            step_mgmt_inventory_mortgageAmount_getAvailableAmount()
            step_mgmt_inventory_order_checkProductInventory()
            step_mgmt_inventory_order_updateMortgageOrder()
            step_02_mgmt_inventory_order_getOrderDetail()
            
            return returnOrderSn

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 0) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        updateMortgageOrder_1_0()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美后台押货退货单数据检查")
    def test_06_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None
   
        @allure.step("完美后台押货退货单")
        def returnOrder_auditOrder():
            "完美后台押货退货单"
            
            from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_getProductForAddPage import _mgmt_inventory_returnOrder_getProductForAddPage # 添加退货单时的商品搜索
            from api.mall_mgmt_application._mgmt_inventory_order_checkProductInventory import _mgmt_inventory_order_checkProductInventory # 店铺库存校验接口
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_addMortgageReturnOrder import _mgmt_inventory_returnOrder_addMortgageReturnOrder # 店铺库存校验接口
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
            from api.mall_mgmt_application._mgmt_inventory_returnOrder_addOpinion import _mgmt_inventory_returnOrder_addOpinion # 后台押货退货添加审批意见
            from api.mall_mgmt_application. _mgmt_inventory_returnOrder_auditOrder import  _mgmt_inventory_returnOrder_auditOrder # 后台审批押货退货单

            from api.mall_store_application._appStore_purchaseReturnOrder_returnInfo import _appStore_purchaseReturnOrder_returnInfo # 提交退回信息

            from api.mall_mgmt_application._mgmt_inventory_returnOrder_inspectOrder import  _mgmt_inventory_returnOrder_inspectOrder # 后台押货退货验货
            
            access_token = os.environ["access_token"]
            store_token = os.environ["store_token"]    
            getReason = None # 获取各种退换货原因 
            getStoreInfo = None # 获取服务中心信息
            getProductForAddPage = None # 添加退货单时的商品搜索
            productNum = 2 # 押货退货数量
            addMortgageReturnOrder = None # 押货退货单Id

            getOrderDetail = None # 完美后台押货退货单详情
            addOpinion = None # 后台押货退货添加审批意见
            
            def step_mgmt_inventory_common_getReason():
                "获取各种退换货原因"
                
                nonlocal getReason
                params = {
                    "type": 3, 
                }              
                with _mgmt_inventory_common_getReason(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    getReason = r.json()["data"]

            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getStoreInfo = r.json()["data"]

            def step_mgmt_inventory_returnOrder_getProductForAddPage():
                "添加退货单时的商品搜索"
                
                nonlocal getProductForAddPage
                params = {
                    "storeCode": store, # 服务中心编号
                    "productCode": productCode, # 商品一级或二级编码
                }              
                with _mgmt_inventory_returnOrder_getProductForAddPage(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getProductForAddPage = r.json()["data"]

            def step_mgmt_inventory_order_checkProductInventory():
                "店铺库存校验接口"
                
                data = {
                    "productDtoList":[ # 需要修改的商品
                        {
                            "productCode": productCode, # 商品一级编码
                            "productSecCode":"", # 商品二级编码(非定制品不要传此字段)
                            "productNum": 2 # 需要减少的商品数量(绝对值)
                        }
                    ],
                    "storeCode": store # 店铺中心编号
                }              
                with _mgmt_inventory_order_checkProductInventory(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] == []

            def step_mgmt_inventory_returnOrder_addMortgageReturnOrder():
                "后台申请添加押货退货单"
                
                nonlocal addMortgageReturnOrder
                getProductForAddPage["productNum"] = productNum
                getProductForAddPage["productRemarks"] = "我是产品退货备注说明"
                data = {
                    "invtMortgageReturnOrderProductVOList": [getProductForAddPage],
                    "invtMortgageReturnOrderVO": {
                        "orderMark": 0,
                        "reasonFirst": getReason[1]["returnReason"],
                        "reasonFirstRemarks": "我是一级备注原因哦哦哦哦哦哦",
                        "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
                        "reasonSecondRemarks": "我是二级备注原因哦哦哦哦哦哦",
                        "storeCode": getStoreInfo["code"]
                    }
                }              
                with _mgmt_inventory_returnOrder_addMortgageReturnOrder(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    addMortgageReturnOrder = r.json()["data"]

            def step_mgmt_inventory_returnOrder_addOpinion():
                "后台押货退货添加审批意见"
                
                nonlocal addOpinion
                data = {
                    "orderId": addMortgageReturnOrder, # 押货或售后单id
                    "content": f"同意这个退货申请" # 意见内容
                }
                with _mgmt_inventory_returnOrder_addOpinion(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    addOpinion = r.json()["data"]

            def step_mgmt_inventory_returnOrder_getOrderDetail():
                "后台押货退货单详情"
                
                nonlocal getOrderDetail
                params = {
                    "orderId": addMortgageReturnOrder
                }
                with _mgmt_inventory_returnOrder_getOrderDetail(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    getOrderDetail = r.json()["data"]
                            
            def step_mgmt_inventory_returnOrder_auditOrder():
                "后台审批押货退货单"
                
                data = {
                    "id": addMortgageReturnOrder, # 押货退货单id
                    "auditRemarks": f"我只能同意退货申请", # 审核备注
                    "auditFileName": "", # 审核附件名称
                    "auditStatus": 1, # 审核结果 0不通过 1通过
                    "auditFileUrl": "", # 审核附件url
                    "reasonFirst": getReason[1]["returnReason"], # 一级原因
                    "reasonFirstRemarks": "我就是想退货，你敢不同意吗", # 一级原因备注
                    "reasonSecond": getReason[1]["reasonList"][1]["returnReason"], # 二级原因
                    "reasonSecondRemarks": "算了，这次就允许你退货吧", # 二级原因备注
                    "returnInfo": "深圳仓", # 退回地址信息
                    "preAuditFileUrl": ""
                }
                with _mgmt_inventory_returnOrder_auditOrder(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            def step_appStore_purchaseReturnOrder_returnInfo():
                "提交退回信息"
                
                data = {
                    "returnType": 2, # 退回类型 1自带 2邮寄
                    "expressCompany": "小何物流", # 物流公司
                    "expressNo": str(round(time.time())), # 物流单号
                    "expressFreightProof": "", # 物流费用凭证url
                    "expressFreightProofName": "", # 物流费用凭证名称
                    "processRemarks": "退回产品都要说明吗", # 退回处理说明
                    "orderId": addMortgageReturnOrder # 退货单id
                }
                with _appStore_purchaseReturnOrder_returnInfo(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200

            def step_mgmt_inventory_returnOrder_inspectOrder():
                "完美后台押货退货验货"
                
                data = {
                    "orderId": addMortgageReturnOrder, # 退货单id
                    "inspectStatus": 1, # 验货意见 0不通过 1通过
                    "expressSubsidy": 100, # 运费补贴
                    "inspectRemarks": "我验货通过了", # 验货备注
                    "orderReturnRealAmount": getOrderDetail["orderVo"]["orderReturnAmount"], # orderReturnRealAmount
                    "productList": [{
                        "id": getOrderDetail["productVoList"][0]["id"], # 物品id
                        "productRealNum": getOrderDetail["productVoList"][0]["productNum"], # 物品实退数量
                        "productRealAmount": getOrderDetail["productVoList"][0]["productMortgagePrice"] * getOrderDetail["productVoList"][0]["productNum"] # 退货单实退金额总额
                    }]
                }
                with _mgmt_inventory_returnOrder_inspectOrder(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    
            step_mgmt_inventory_common_getReason()
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_inventory_returnOrder_getProductForAddPage()
            step_mgmt_inventory_order_checkProductInventory()
            step_mgmt_inventory_returnOrder_addMortgageReturnOrder()
            step_mgmt_inventory_returnOrder_addOpinion()
            step_mgmt_inventory_returnOrder_getOrderDetail()
            step_mgmt_inventory_returnOrder_auditOrder()
            step_appStore_purchaseReturnOrder_returnInfo()
            step_mgmt_inventory_returnOrder_inspectOrder()
            
            return getOrderDetail["orderVo"]["orderSn"]

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) - 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        returnOrder_auditOrder()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美后台代客售后-押货库存数据检查")
    def test_07_mgmt_product_stock_list(self, walletPay_to_me, db_mall_center_inventory):
        
        stock_list = None

        @allure.step("店铺后台押货:确保库存>5")
        def purchase_commit():
            "店铺后台押货"
            
            from api.mall_store_application._appStore_purchaseOrder_negateProducts import _appStore_purchaseOrder_negateProducts # 提交押货单页面的负库存押货商品列表
            from api.mall_store_application._appStore_purchaseOrder_products import _appStore_purchaseOrder_products # 提交押货单页面的押货商品搜索
            from api.mall_store_application._appStore_purchase_balanceAmount import _appStore_purchase_balanceAmount # 押货金额
            from api.mall_store_application._appStore_purchase_commit import _appStore_purchase_commit # 提交押货单

            from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
            from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
            from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
            from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
            from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
            from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
            from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data as data01, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
            from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核
            
            store_token = os.environ["store_token"]
            access_token = os.environ["access_token"]
            negateProducts = None # 负库存产品
            products = None # 产品信息
            availableAmount = None # 可用余额
            products_list = [] # 押货产品
            productNum = 5 # 押货产品数量
            orderSn = None # 押货单号
            
            getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
            getStoreInfo = None # 获取服务中心信息
            getAccountList = None # 查询分公司银行账号
            getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
            getBankAccountList = None # 通过storeCode获取银行账户资料信息
            pageSearchList = None # 待审核流水信息

            def step_appStore_purchaseOrder_negateProducts():
                "提交押货单页面的负库存押货商品列表"
                
                nonlocal negateProducts
                with _appStore_purchaseOrder_negateProducts(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    negateProducts = r.json()["data"]
            
            def step_appStore_purchaseOrder_products():
                "提交押货单页面的押货商品搜索"
                
                nonlocal products
                params = {
                    "pageNum": 1,
                    "pageSize": 40,
                    "product": productCode
                }
                with _appStore_purchaseOrder_products(params, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]["list"]:
                        if d["productCode"] == productCode:
                            products = d
            
            def step_appStore_purchase_balanceAmount():
                "押货金额"
                
                nonlocal availableAmount
                with _appStore_purchase_balanceAmount(store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    availableAmount = r.json()["data"]["availableAmount"]
            
            def step_appStore_purchase_commit():
                "提交押货单"
                
                nonlocal orderSn
                data = {
                    "list": products_list,
                    "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
                }
                with _appStore_purchase_commit(data, store_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["message"] == "操作成功"
                    orderSn = r.json()["data"]

            def step_mgmt_inventory_remit_getSourceTypeByRemitType():
                "按银行流水类型获取款项映射列表"
                
                nonlocal getSourceTypeByRemitType
                params = {
                    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
                }              
                with _mgmt_inventory_remit_getSourceTypeByRemitType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getSourceTypeByRemitType = r.json()["data"]
                    
            def step_mgmt_inventory_common_getStoreInfo():
                "获取服务中心信息"
                
                nonlocal getStoreInfo
                params = {
                    "storeCode": store
                }              
                with _mgmt_inventory_common_getStoreInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["code"] == store
                    getStoreInfo = r.json()["data"] 
                            
            def step_mgmt_sys_getAccountList():
                "查询分公司银行账号"
                
                nonlocal getAccountList
                params = {
                    "companyCode" : getStoreInfo["companyCode"],  # 公司编码
                }             
                with _mgmt_sys_getAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getAccountList = r.json()["data"] 

            def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
                "根据storeCode查询押货余额主表数据"
                
                nonlocal getMortgageAmountByStore
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getMortgageAmountByStore = r.json()["data"] 

            def step_mgmt_store_getBankAccountList():
                "通过storeCode获取银行账户资料信息"
                
                nonlocal getBankAccountList
                params = {
                    "storeCode": getStoreInfo["code"]
                }            
                with _mgmt_store_getBankAccountList(params, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200 
                    getBankAccountList = r.json()["data"] 
        
            def step_mgmt_inventory_remit_addManualInputRemit():
                "手工增押货款"
                
                data = {
                    "storeCode": getStoreInfo["code"], # 店铺编号
                    "storeName": getStoreInfo["name"],
                    "leaderName": getStoreInfo["leaderName"],
                    "companyCode": getStoreInfo["companyCode"], # 分公司code
                    "sourceType": 8, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                    "changeReason": "汇押货款", # 调整原因
                    "remitMoney": sum([d["mortgagePrice"] * d["productNum"] for d in products_list]) - availableAmount + 10, # 汇款金额
                    "account": getBankAccountList[0]["account"], # 付款账号
                    "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                    "remark": f"录入手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 备注
                    "receiptAccount": getAccountList[0]["account"], # 收款账号
                    "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
                }           
                with _mgmt_inventory_remit_addManualInputRemit(data, access_token) as r:
                    assert r.status_code == 200            
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            def step_mgmt_inventory_remit_pageSearchList():
                "手工录入流水分页搜索列表:获取待审核流水信息"
                
                nonlocal pageSearchList 
                data = deepcopy(data01)
                data["storeCode"] = getStoreInfo["code"]
                data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
                data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
                with _mgmt_inventory_remit_pageSearchList(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    pageSearchList = r.json()["data"]["list"]

            def step_mgmt_inventory_remit_verifyManualInputRemit():
                "手工录入流水审核"
                
                params = pageSearchList[0]
                params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
                params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
                params["show"] = True
                params["type"] = 2               
                with _mgmt_inventory_remit_verifyManualInputRemit(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"] is True

            step_appStore_purchaseOrder_negateProducts()
            step_appStore_purchaseOrder_products()
            
            if negateProducts != []:
                for d in negateProducts:
                    if d["productCode"] == productCode:
                        products_list.append({
                            "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                            "productCode": d["productCode"], # 押货商品编码
                            "productNum": -d["currentStock"] + productNum # 押货商品数量
                        })
                        
                    products_list.append({
                        "mortgagePrice": d["productMortgagePrice"], # 商品押货价
                        "productCode": d["productCode"], # 押货商品编码
                        "productNum": -d["currentStock"] # 押货商品数量
                    })
            else:
                products_list.append({
                        "mortgagePrice": products["productMortgagePrice"], # 商品押货价
                        "productCode": products["productCode"], # 押货商品编码
                        "productNum": productNum # 押货商品数量
                    })
            
            step_appStore_purchase_balanceAmount()
            
            if availableAmount < sum([d["mortgagePrice"] * d["productNum"] for d in products_list]):
                step_mgmt_inventory_remit_getSourceTypeByRemitType()
                step_mgmt_inventory_common_getStoreInfo()
                step_mgmt_sys_getAccountList()
                step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
                step_mgmt_store_getBankAccountList()
                step_mgmt_inventory_remit_addManualInputRemit()
                step_mgmt_inventory_remit_pageSearchList()
                step_mgmt_inventory_remit_verifyManualInputRemit()
                
            step_appStore_purchase_commit()
            
            return orderSn
  
        @allure.step("代客售后-押货库存")
        def return_applyReturn():
            "代客售后-押货库存"
            
            from api.mall_mgmt_application._mgmt_order_return_getOrderReturnList import _mgmt_order_return_getOrderReturnList # 退货单列表
            from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表
            from api.mall_mgmt_application._mgmt_order_orderInfo import _mgmt_order_orderInfo # 订单信息
            from api.mall_mgmt_application._mgmt_order_return_calcRefundAmount import _mgmt_order_return_calcRefundAmount # 计算订单退款金额
            from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
            from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
            from api.mall_mgmt_application._mgmt_order_return_applyReturn import _mgmt_order_return_applyReturn # 申请退货
            from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情
            from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
            from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核
            
            access_token = os.environ["access_token"]
            
            orderNo = None # 订单编号
            calcRefundAmount = None # 计算订单退款金额
            upgradeOrderVerify = None # 升级单校验
            getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
            applyReturn = None # 退货单
            getOrderReturnDetails = None # 退货详情
            
            def step_mgmt_order_return_getOrderReturnList():
                "退货单列表：是否有待审核的退货单"
                    
                nonlocal orderNo, applyReturn
                params = {
                    "returnType": 1, # 退货类型 1->当月退货 2->隔月退货
                    "expressType": None, # 发货方式 1->服务中心自提 2->公司交付
                    "applySource": None, # 申请来源 0->总公司代客售后 1->顾客申请 2->公司申请 3->商城1.0
                    "companyCode": "", # 分公司编号
                    "financeCompanyCode": "", # 财务分公司编号
                    "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
                    "storeCode": "", # 服务中心编号
                    "customerCard": "", # 顾客卡号
                    "creatorCard": username, # 开单人卡号
                    "returnNo": "", # 退货单号
                    "orderNo": "", # 订单号
                    "isDeliver": None, # 是否发货 0->不发货 1->发货
                    "isUpgrade": None, # 是否升级单 0->否 1->是
                    "depositNo": "", # 对应定金订单号
                    "currentPage": 1, 
                    "pageSize": 10,
                    "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
                    "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
                    "returnStatus": 1, # 服务状态 1->待审核 2->待退回 3->待验货 98->已取消 99->已完成
                    "pageNum": 1,
                }           
                with _mgmt_order_return_getOrderReturnList(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]["list"]:
                        orderNo = r.json()["data"]["list"][0]["orderNo"]
                        applyReturn = r.json()["data"]["list"][0]["returnNo"] 
            
            def step_mgmt_order_orderList():
                "订单列表：获取订单编号"
                    
                nonlocal orderNo
                params = {
                    "pageNum": 1,
                    "pageSize": 10,
                    "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
                    "orderNo": "",
                    "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
                    "stockType": 2, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
                    "creatorCard": username, # 开单人卡号
                    "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
                    "isUpgrade": 0, # 是否升级单
                    "commitStartTime": f"{time.strftime('%Y-%m', time.localtime(time.time()))}-01", # 开单开始时间
                    "commitEndTime": time.strftime("%Y-%m-%d", time.localtime(time.time())), # 开单结束时间
                }           
                with _mgmt_order_orderList(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    orderNo = r.json()["data"]["list"][0]["orderNo"]   
            
            def step_mgmt_order_orderInfo():
                "订单信息"
                    
                params = {
                    "orderNo": orderNo, # 订单编号
                }      
                with _mgmt_order_orderInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mgmt_order_return_calcRefundAmount(): 
                "计算订单退款金额"
                
                nonlocal calcRefundAmount   
                params = {
                    "orderNo": orderNo, # 订单编号
                }      
                with _mgmt_order_return_calcRefundAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    calcRefundAmount = r.json()["data"]

            def step_mgmt_order_return_upgradeOrderVerify(): 
                "升级单校验"
                
                nonlocal upgradeOrderVerify   
                data = {
                    "orderNo": orderNo, 
                    "applySource": 0,
                }     
                with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
                    upgradeOrderVerify = r.json()["data"]["resultType"]
            
            def step_sys_api_getAllReturnReasonByType(): 
                "通过退换货类型获取 一级,二级层级原因"
                
                nonlocal getAllReturnReasonByType   
                params = {
                    "returnType": 1, # 退换货类型：1.商城退货，2.商城换货，3.服务中心押货退货，4.服务中心押货换货，5.展业包订货退货，6.展业包订货换货
                }   
                with _sys_api_getAllReturnReasonByType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getAllReturnReasonByType = r.json()["data"]

            def step_mgmt_order_return_applyReturn(): 
                "申请退货"
                
                nonlocal applyReturn 
                data = {
                    "orderNo": orderNo, # 订单编号
                    "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
                    "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
                    "reason1Remark": "我没钱了要退货", # 退货一级原因备注
                    "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
                    "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
                    "reason2Remark": "给你特批退货吧", # 退货二级原因备注
                    "applySource": 0 # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
                }   
                with _mgmt_order_return_applyReturn(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    applyReturn = r.json()["data"]

            def step_mgmt_order_return_getOrderReturnDetails(): 
                "退货详情"
                
                nonlocal getOrderReturnDetails
                params = {
                    "returnNo": applyReturn, # 退货单号
                }
                with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getOrderReturnDetails = r.json()["data"]

            def step_mgmt_order_return_saveComment():
                "新增或修改留言" 
                
                data = {
                    "serviceNo": applyReturn, # 退货/换货单号
                    "comment": "我同意这个代客售后申请", # 留言内容
                    "id": "" # 留言id
                }
                with _mgmt_order_return_saveComment(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_02_mgmt_order_return_upgradeOrderVerify(): 
                "升级单校验"
                
                nonlocal upgradeOrderVerify   
                data = {
                    "orderNo": orderNo, 
                }     
                with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
                    upgradeOrderVerify = r.json()["data"]["resultType"]
            
            def step_mgmt_order_return_auditOrderReturn(): 
                "分公司退货审核"
                
                data = {
                    "serviceNo": applyReturn, # 售后单号
                    "auditStatus": "1", # 审核状态 1->通过 2->不通过
                    "remarks": "同意退款" # 审核意见
                }
                with _mgmt_order_return_auditOrderReturn(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    
            step_mgmt_order_return_getOrderReturnList()
            if applyReturn: 
                step_mgmt_order_return_getOrderReturnDetails()
                step_mgmt_order_return_saveComment()
                step_02_mgmt_order_return_upgradeOrderVerify()
                step_mgmt_order_return_auditOrderReturn()        
            step_mgmt_order_orderList()
            step_mgmt_order_orderInfo()
            step_mgmt_order_return_calcRefundAmount()
            step_mgmt_order_return_upgradeOrderVerify()
            step_sys_api_getAllReturnReasonByType()
            step_mgmt_order_return_applyReturn()
            step_mgmt_order_return_getOrderReturnDetails()
            step_mgmt_order_return_saveComment()
            step_02_mgmt_order_return_upgradeOrderVerify()
            step_mgmt_order_return_auditOrderReturn()
            
            return getOrderReturnDetails

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + getOrderReturnDetails["orderReturnProducts"][0]["quantity"]) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        purchase_commit()
        step_01_mgmt_product_stock_list()
        getOrderReturnDetails = return_applyReturn()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 完美后台代客售后-押货库存-隔月退货数据检查")
    def test_08_mgmt_product_stock_list(self, db_mall_center_inventory):
        
        stock_list = None
   
        @allure.step("代客售后-押货库存-隔月退货")
        def return_applyReturn_2():
            "代客售后-押货库存-隔月退货"
            
            from api.mall_mgmt_application._mgmt_order_return_getOrderReturnList import _mgmt_order_return_getOrderReturnList # 退货单列表
            from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表
            from api.mall_mgmt_application._mgmt_order_orderInfo import _mgmt_order_orderInfo # 订单信息
            from api.mall_mgmt_application._mgmt_order_return_calcRefundAmount import _mgmt_order_return_calcRefundAmount # 计算订单退款金额
            from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
            from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
            from api.mall_mgmt_application._mgmt_order_return_applyReturn import _mgmt_order_return_applyReturn # 申请退货
            from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情
            from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
            from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核
            
            access_token = os.environ["access_token"]
            
            orderNo = None # 订单编号
            calcRefundAmount = None # 计算订单退款金额
            upgradeOrderVerify = None # 升级单校验
            getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
            applyReturn = None # 退货单
            
            def step_mgmt_order_return_getOrderReturnList():
                "退货单列表：是否有待审核的退货单"
                    
                nonlocal orderNo, applyReturn
                params = {
                    "returnType": 2, # 退货类型 1->当月退货 2->隔月退货
                    "expressType": None, # 发货方式 1->服务中心自提 2->公司交付
                    "applySource": None, # 申请来源 0->总公司代客售后 1->顾客申请 2->公司申请 3->商城1.0
                    "companyCode": "", # 分公司编号
                    "financeCompanyCode": "", # 财务分公司编号
                    "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
                    "storeCode": "", # 服务中心编号
                    "customerCard": "", # 顾客卡号
                    "creatorCard": username, # 开单人卡号
                    "returnNo": "", # 退货单号
                    "orderNo": "", # 订单号
                    "isDeliver": None, # 是否发货 0->不发货 1->发货
                    "isUpgrade": None, # 是否升级单 0->否 1->是
                    "depositNo": "", # 对应定金订单号
                    "currentPage": 1, 
                    "pageSize": 10,
                    "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
                    "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
                    "returnStatus": 1, # 服务状态 1->待审核 2->待退回 3->待验货 98->已取消 99->已完成
                    "pageNum": 1,
                }           
                with _mgmt_order_return_getOrderReturnList(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]["list"]:
                        orderNo = r.json()["data"]["list"][0]["orderNo"]
                        applyReturn = r.json()["data"]["list"][0]["returnNo"]   
            
            def step_mgmt_order_orderList():
                "订单列表：获取订单编号"
                    
                nonlocal orderNo
                params = {
                    "pageNum": 1,
                    "pageSize": 10,
                    "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
                    "orderNo": "",
                    "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
                    "stockType": 2, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
                    "creatorCard": username, # 开单人卡号
                    "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
                    "isUpgrade": 0, # 是否升级单
                    "commitStartTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-1', # 开单开始时间
                    "commitEndTime": f'{datetime.date.today().replace(month=datetime.date.today().month - 1).strftime("%Y-%m")}-28', # 开单结束时间
                }           
                with _mgmt_order_orderList(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    orderNo = r.json()["data"]["list"][0]["orderNo"]   
            
            def step_mgmt_order_orderInfo():
                "订单信息"
                    
                params = {
                    "orderNo": orderNo, # 订单编号
                }      
                with _mgmt_order_orderInfo(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mgmt_order_return_calcRefundAmount(): 
                "计算订单退款金额"
                
                nonlocal calcRefundAmount   
                params = {
                    "orderNo": orderNo, # 订单编号
                }      
                with _mgmt_order_return_calcRefundAmount(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    calcRefundAmount = r.json()["data"]

            def step_mgmt_order_return_upgradeOrderVerify(): 
                "升级单校验"
                
                nonlocal upgradeOrderVerify   
                data = {
                    "orderNo": orderNo, 
                    "applySource": 0,
                }     
                with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
                    upgradeOrderVerify = r.json()["data"]["resultType"]
            
            def step_sys_api_getAllReturnReasonByType(): 
                "通过退换货类型获取 一级,二级层级原因"
                
                nonlocal getAllReturnReasonByType   
                params = {
                    "returnType": 1, # 退换货类型：1.商城退货，2.商城换货，3.服务中心押货退货，4.服务中心押货换货，5.展业包订货退货，6.展业包订货换货
                }   
                with _sys_api_getAllReturnReasonByType(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getAllReturnReasonByType = r.json()["data"]

            def step_mgmt_order_return_applyReturn(): 
                "申请退货"
                
                nonlocal applyReturn 
                data = {
                    "orderNo": orderNo, # 订单编号
                    "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
                    "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
                    "reason1Remark": "我没钱了要退货", # 退货一级原因备注
                    "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
                    "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
                    "reason2Remark": "给你特批退货吧", # 退货二级原因备注
                    "applySource": 0 # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
                }   
                with _mgmt_order_return_applyReturn(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    applyReturn = r.json()["data"]

            def step_mgmt_order_return_getOrderReturnDetails(): 
                "退货详情"
                
                params = {
                    "returnNo": applyReturn, # 退货单号
                }
                with _mgmt_order_return_getOrderReturnDetails(params, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["orderReturn"]["returnType"] == 2 # 退货类型 1->当月退货 2->隔月退货
                    assert r.json()["data"]["orderReturn"]["returnTypeDesc"] == "隔月退货"

            def step_mgmt_order_return_saveComment():
                "新增或修改留言" 
                
                data = {
                    "serviceNo": applyReturn, # 退货/换货单号
                    "comment": "我同意这个代客售后申请", # 留言内容
                    "id": "" # 留言id
                }
                with _mgmt_order_return_saveComment(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_02_mgmt_order_return_upgradeOrderVerify(): 
                "升级单校验"
                
                nonlocal upgradeOrderVerify   
                data = {
                    "orderNo": orderNo, 
                }     
                with _mgmt_order_return_upgradeOrderVerify(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
                    upgradeOrderVerify = r.json()["data"]["resultType"]
            
            def step_mgmt_order_return_auditOrderReturn(): 
                "分公司退货审核"
                
                data = {
                    "serviceNo": applyReturn, # 售后单号
                    "auditStatus": "1", # 审核状态 1->通过 2->不通过
                    "remarks": "同意退款" # 审核意见
                }
                with _mgmt_order_return_auditOrderReturn(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    
            step_mgmt_order_return_getOrderReturnList()
            if applyReturn: 
                step_mgmt_order_return_getOrderReturnDetails()
                step_mgmt_order_return_saveComment()
                step_02_mgmt_order_return_upgradeOrderVerify()
                step_mgmt_order_return_auditOrderReturn()        
            step_mgmt_order_orderList()
            step_mgmt_order_orderInfo()
            step_mgmt_order_return_calcRefundAmount()
            step_mgmt_order_return_upgradeOrderVerify()
            step_sys_api_getAllReturnReasonByType()
            step_mgmt_order_return_applyReturn()
            step_mgmt_order_return_getOrderReturnDetails()
            step_mgmt_order_return_saveComment()
            step_02_mgmt_order_return_upgradeOrderVerify()
            step_mgmt_order_return_auditOrderReturn()
            
            return applyReturn

        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        return_applyReturn_2()
        step_02_mgmt_product_stock_list() 


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/stock/list")
class TestClass06:
    """
    库存列表-限量tab列表:商城前端数据操作检查
    /mgmt/product/stock/list
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 商城前端自提订单数据检查")
    def test_01_mgmt_product_stock_list(self, db_mall_center_inventory, login_oauth_token):
        
        stock_list = None
        
        @allure.step("给钱包加钱>=10000，以便钱包支付")
        def wallet_add_10000():
            "给钱包加钱>=10000，以便钱包支付"
            
            from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import _mgmt_fin_wallet_applyAdjust # 手工录入款项审核-提交
            from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
            from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import _mgmt_fin_wallet_getAdjustList # 手工录入款项审核-列表
            from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import _mgmt_fin_wallet_getAdjustDetail # 手工录入款项审核-详情
            from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust # 手工录入款项审核-审核
            from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 顾客信用额列表-列表
            from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
            from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
            
            wallet = None # 现有钱包信息（信用额，实际结余）
            walletAdjustId = None
            getAdjustDetail = None
            walletCreditApplyId = None
            access_token = os.environ["access_token"]
            
            def step_mgmt_fin_wallet_getList():
                "钱包手工录入列表:获取钱包信息"
                
                nonlocal wallet
                data = {
                    "storeCode": None,
                    "cardNo": username, # 会员卡号
                    "mobile": None, # 顾客手机号
                    "companyCode": None, # 	分公司编号
                    "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
                    "creditEnable": None, # 是否有信用额
                    "negativeEnable": None, # 钱包余额为负
                    "pageNum": 1,
                    "pageSize": 10
                }                   
                with _mgmt_fin_wallet_getList(data, access_token) as r:
                    wallet = r.json()["data"]["list"][0]
                    assert r.json()["data"]["list"][0]["cardNo"] == username
                    
            def step_mgmt_fin_wallet_applyAdjust():
                "手工录入流水-其他款"

                data = {
                    "walletId": wallet["walletId"] , # 钱包id
                    "companyCode": wallet["companyNo"], # 分公司
                    "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
                    "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
                    "adjustReason": f"其他款 {adjustAmount}元"
                }          
                with _mgmt_fin_wallet_applyAdjust(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
            
            def step_mgmt_fin_wallet_getAdjustList():
                "手工录入款项审核-列表"
                
                nonlocal walletAdjustId
                data = {
                    "adjustStatus": None, # 审批状态：1：待审核；2：已通过；3：已驳回，6：已撤回
                    "adjustMonth": None, # 录入月份
                    "mobile": None, # 普通过客手机号
                    "cardNo": username, # 会员卡号
                    "companyCode": None, # 分公司编号
                    "pageNum": 1,
                    "pageSize": 10
                }        
                with _mgmt_fin_wallet_getAdjustList(data, access_token) as r:
                    walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["list"][0]["adjustStatus"] == 1

            def step_mgmt_fin_wallet_getAdjustDetail():
                "手工录入款项审核-详情"
                
                nonlocal getAdjustDetail
                params = {
                    "id": walletAdjustId
                }       
                with _mgmt_fin_wallet_getAdjustDetail(params, access_token) as r:
                    getAdjustDetail = r.json()["data"]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mgmt_fin_wallet_auditAdjust():
                "手工录入款项审核-审核"
                
                data = getAdjustDetail
                data["status"] = "2"
                data["auditRemark"] = f"同意其他款 {adjustAmount}元"   
                data["walletAdjustId"] = walletAdjustId    
                with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            step_mgmt_fin_wallet_getList()
            if wallet["thisMonthActualBalanceAmt"] < 0:
                adjustAmount = 10000 - wallet["thisMonthActualBalanceAmt"] # 输入金额
            elif wallet["thisMonthActualBalanceAmt"] >= 0:
                adjustAmount = 10000 + wallet["thisMonthActualBalanceAmt"] # 输入金额
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
                   
        @allure.step("云商-钱包-自购订单")
        def walletPay_to_me():
            "云商-钱包-自购订单"
            
            from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search # 搜索商品
            from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
            from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
            from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
            from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
            from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
            from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
            from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
            from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
            from api.mall_mobile_application._mobile_payment_getPayMethod import _mobile_payment_getPayMethod #  获取支付方式
            from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay # 支付
            from api.mall_mobile_application._mobile_payment_queryWalletPayOrder import _mobile_payment_queryWalletPayOrder # 查询支付成功信息
            from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息
                    
            productList = None # 商品详情
            getFreightList = None # 运费补贴券
            getCouponList = None # 优惠券
            getSecondList = None # 秒返券
            getGiftList_2 = None # 电子礼券
            availableBalance = None # 钱包可用余额
            associationPay = None # 支付方式-邮政储蓄银行信息
            orderCommit = None # 订单信息
            payOrderNo = None # 支付流水号
            queryWalletPayOrder = None # 支付成功信息
            getOrderInfo = None # 详细订单信息
            number = 2 # 购买商品数量
            user = login_oauth_token["data"] # 给某个顾客下单的信息（非下单人）
            token = os.environ["token"]
            
            def step_mobile_product_search():
                "搜索商品"

                nonlocal productList
                data = deepcopy(data01)
                data["keyword"] = productCode
                with _mobile_product_search(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    productList = r.json()["data"]["list"][0]

            def step_mobile_order_carts_getFreightList():
                "获取运费补贴券列表"
                
                nonlocal getFreightList
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                }         
                with _mobile_order_carts_getFreightList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]:
                        getFreightList = r.json()["data"][0]

            def step_mobile_order_carts_getCouponList():
                "获取选中结算分组的可用和不可用优惠券列表"
                            
                nonlocal getCouponList
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "storeCode": user["storeCode"]
                }         
                with _mobile_order_carts_getCouponList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]["availableList"]:
                        getCouponList = r.json()["data"]["availableList"][0]

            def step_mobile_order_carts_getSecondList():
                "获取购物秒返券券列表"
                            
                nonlocal getSecondList
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "storeCode": user["storeCode"]
                }        
                with _mobile_order_carts_getSecondList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]:
                        for d in r.json()["data"]:
                            if d["isUsed"] == 1:
                                getSecondList = d["secondCouponId"]
            
            def step_mobile_order_carts_getGiftList_2():
                "获取电子礼券列表"
                
                nonlocal getGiftList_2
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                }        
                with _mobile_order_carts_getGiftList_2(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]:
                        getGiftList_2 = r.json()["data"][0]

            def step_mobile_order_carts_toSettlement():
                "选择商品去结算"
                            
                data = {
                    "addressId": None,
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "customerId":  user["userId"], # 给某个顾客下单的会员ID
                    "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                    "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "orderInvoice": None, # 发票信息
                    "couponList": [], # 使用的优惠卷
                    "giftList": [], # 使用的电子礼券
                    "freightList": [], # 使用的运费补贴礼券
                    "secondCouponList": [], # 使用的秒返券
                    "storeCode": user["storeCode"], # 服务中心编码
                    "ownerId": "", # 送货人ID
                    "pv": productList["pv"] * number,
                    "remarks": "", # 备注
                    "returnRate": 0.12, # 返还比例
                    "sharerId": None, # 分享人id
                    "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                }
                if getFreightList: # 运费补贴券
                    data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
                if getCouponList: # 优惠卷
                    data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
                if getSecondList: # 秒返券
                    data["secondCouponList"].append({"secondCouponId": getSecondList})
                if getGiftList_2: # 电子礼券
                    data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
                with _mobile_order_carts_toSettlement(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mobile_trade_orderCommit():
                "提交订单"
                            
                nonlocal orderCommit
                data = {
                    "addressId": None,
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "customerId": user["userId"], # 给某个顾客下单的会员ID
                    "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                    "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "orderInvoice": None, # # 发票信息
                    "couponList": [], # 使用的优惠卷
                    "giftList": [], # 使用的电子礼券
                    "freightList": [], # 使用的运费补贴礼券
                    "secondCouponList": [], # 使用的秒返券
                    "storeCode": user["storeCode"], # 服务中心编码
                    "ownerId": "", # 送货人ID
                    "pv": productList["pv"] * number,
                    "remarks": "", # 备注
                    "returnRate": 0.12, # 返还比例
                    "sharerId": None, # 分享人id
                    "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "isUpgrade": 0 # 是否升级单 0->否 1->是
                } 
                if getFreightList: # 运费补贴券
                    data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
                if getCouponList: # 优惠卷
                    data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
                if getSecondList: # 秒返券
                    data["secondCouponList"].append({"secondCouponId": getSecondList})
                if getGiftList_2: # 电子礼券
                    data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                   
                with _mobile_trade_orderCommit(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    orderCommit = r.json()["data"]

            def step_mobile_wallet_queryPasswordExist():
                "是否设置了支付密码"
                
                with _mobile_wallet_queryPasswordExist(token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
            def step_mobile_wallet_getDetail():
                "获取钱包首页相关信息"
                
                nonlocal  availableBalance
                with _mobile_wallet_getDetail(token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableBalance = r.json()["data"]["availableBalance"]
            
            def step_mobile_payment_getPayMethod():
                "获取支付方式"

                nonlocal associationPay
                data = {
                    "orderNoList":[orderCommit["orderNo"]], # 订单号集合
                    "payType":"PC", # 支付类型,H5、APP、PC、PROGRAM
                    "sourceType":1 # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
                }
                with _mobile_payment_getPayMethod(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]:
                        if d["bankName"] == "邮政储蓄银行":
                            associationPay = d

            def step_mobile_payment_associationPay():
                "支付"

                nonlocal payOrderNo
                data = {
                    "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
                    "channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
                    "orderNoList": [orderCommit["orderNo"]],
                    "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
                    "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
                    "feeRate": 0, # 手续费率
                    "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
                    "walletPassword": "", # 钱包充值密码,非免密必传字段
                    "orderNo": orderCommit["orderNo"]
                }
                with _mobile_payment_associationPay(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    payOrderNo = r.json()["data"]["payOrderNo"]

            def step_mobile_payment_queryWalletPayOrder():
                "查询支付成功信息"

                nonlocal queryWalletPayOrder
                params = {
                    "payNo": payOrderNo, # 订单编号(必填)
                }
                with _mobile_payment_queryWalletPayOrder(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    queryWalletPayOrder = r.json()["data"]

            def step_mobile_orderInfo_getOrderInfo():
                "通过订单号查询客户端订单信息"

                nonlocal getOrderInfo
                params = {
                    "orderNo": orderCommit["orderNo"] # 订单编号(必填)
                }
                with _mobile_orderInfo_getOrderInfo(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getOrderInfo = r.json()["data"]
                    
            step_mobile_product_search()
            step_mobile_order_carts_getFreightList()
            step_mobile_order_carts_getCouponList()
            step_mobile_order_carts_getSecondList()
            step_mobile_order_carts_getGiftList_2()
            step_mobile_order_carts_toSettlement()
            step_mobile_trade_orderCommit()
            step_mobile_wallet_queryPasswordExist()
            step_mobile_wallet_getDetail()
            step_mobile_payment_getPayMethod()
            step_mobile_payment_associationPay()
            step_mobile_payment_queryWalletPayOrder()
            step_mobile_orderInfo_getOrderInfo()
            
            return queryWalletPayOrder
    
        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) - 2) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        wallet_add_10000()
        walletPay_to_me()
        step_02_mgmt_product_stock_list() 

    @allure.severity(P1)
    @allure.title("库存列表-限量tab列表-成功路径: 商城前端自提订单退货数据检查")
    def test_02_mgmt_product_stock_list(self, db_mall_center_inventory, login_oauth_token):
        
        stock_list = None
        
        @allure.step("给钱包加钱>=10000，以便钱包支付")
        def wallet_add_10000():
            "给钱包加钱>=10000，以便钱包支付"
            
            from api.mall_mgmt_application._mgmt_fin_wallet_applyAdjust import _mgmt_fin_wallet_applyAdjust # 手工录入款项审核-提交
            from api.mall_mgmt_application._mgmt_fin_wallet_getList import _mgmt_fin_wallet_getList # 完美钱包管理-列表
            from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustList import _mgmt_fin_wallet_getAdjustList # 手工录入款项审核-列表
            from api.mall_mgmt_application._mgmt_fin_wallet_getAdjustDetail import _mgmt_fin_wallet_getAdjustDetail # 手工录入款项审核-详情
            from api.mall_mgmt_application._mgmt_fin_wallet_auditAdjust import _mgmt_fin_wallet_auditAdjust # 手工录入款项审核-审核
            from api.mall_mgmt_application._mgmt_fin_wallet_credit_getApplyList import _mgmt_fin_wallet_credit_getApplyList # 顾客信用额列表-列表
            from api.mall_mgmt_application._mgmt_fin_wallet_credit_addApply import _mgmt_fin_wallet_credit_addApply # 顾客信用额列表-新增
            from api.mall_mgmt_application._mgmt_fin_wallet_credit_auditApply import _mgmt_fin_wallet_credit_auditApply # 顾客信用额列表-审核
            
            wallet = None # 现有钱包信息（信用额，实际结余）
            walletAdjustId = None
            getAdjustDetail = None
            walletCreditApplyId = None
            access_token = os.environ["access_token"]
            
            def step_mgmt_fin_wallet_getList():
                "钱包手工录入列表:获取钱包信息"
                
                nonlocal wallet
                data = {
                    "storeCode": None,
                    "cardNo": username, # 会员卡号
                    "mobile": None, # 顾客手机号
                    "companyCode": None, # 	分公司编号
                    "cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
                    "creditEnable": None, # 是否有信用额
                    "negativeEnable": None, # 钱包余额为负
                    "pageNum": 1,
                    "pageSize": 10
                }                   
                with _mgmt_fin_wallet_getList(data, access_token) as r:
                    wallet = r.json()["data"]["list"][0]
                    assert r.json()["data"]["list"][0]["cardNo"] == username
                    
            def step_mgmt_fin_wallet_applyAdjust():
                "手工录入流水-其他款"

                data = {
                    "walletId": wallet["walletId"] , # 钱包id
                    "companyCode": wallet["companyNo"], # 分公司
                    "type": 5, # 款项类型 1:还欠款;2:补银行流水3:手工退款4:押货款与钱包互转5:其他
                    "adjustAmount": adjustAmount, # 输入金额，支持负数，当增加余额时传正数；减少余额时传负数
                    "adjustReason": f"其他款 {adjustAmount}元"
                }          
                with _mgmt_fin_wallet_applyAdjust(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
            
            def step_mgmt_fin_wallet_getAdjustList():
                "手工录入款项审核-列表"
                
                nonlocal walletAdjustId
                data = {
                    "adjustStatus": None, # 审批状态：1：待审核；2：已通过；3：已驳回，6：已撤回
                    "adjustMonth": None, # 录入月份
                    "mobile": None, # 普通过客手机号
                    "cardNo": username, # 会员卡号
                    "companyCode": None, # 分公司编号
                    "pageNum": 1,
                    "pageSize": 10
                }        
                with _mgmt_fin_wallet_getAdjustList(data, access_token) as r:
                    walletAdjustId = r.json()["data"]["list"][0]["walletAdjustId"]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["list"][0]["adjustStatus"] == 1

            def step_mgmt_fin_wallet_getAdjustDetail():
                "手工录入款项审核-详情"
                
                nonlocal getAdjustDetail
                params = {
                    "id": walletAdjustId
                }       
                with _mgmt_fin_wallet_getAdjustDetail(params, access_token) as r:
                    getAdjustDetail = r.json()["data"]
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mgmt_fin_wallet_auditAdjust():
                "手工录入款项审核-审核"
                
                data = getAdjustDetail
                data["status"] = "2"
                data["auditRemark"] = f"同意其他款 {adjustAmount}元"   
                data["walletAdjustId"] = walletAdjustId    
                with _mgmt_fin_wallet_auditAdjust(data, access_token) as r:
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            step_mgmt_fin_wallet_getList()
            if wallet["thisMonthActualBalanceAmt"] < 0:
                adjustAmount = 10000 - wallet["thisMonthActualBalanceAmt"] # 输入金额
            elif wallet["thisMonthActualBalanceAmt"] >= 0:
                adjustAmount = 10000 + wallet["thisMonthActualBalanceAmt"] # 输入金额
            step_mgmt_fin_wallet_applyAdjust()
            step_mgmt_fin_wallet_getAdjustList()
            step_mgmt_fin_wallet_getAdjustDetail()
            step_mgmt_fin_wallet_auditAdjust()
                   
        def walletPay_to_me():
            "云商-钱包-自购订单"
            
            from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search # 搜索商品
            from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
            from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
            from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
            from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
            from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
            from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
            from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
            from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
            from api.mall_mobile_application._mobile_payment_getPayMethod import _mobile_payment_getPayMethod #  获取支付方式
            from api.mall_mobile_application._mobile_payment_associationPay import _mobile_payment_associationPay # 支付
            from api.mall_mobile_application._mobile_payment_queryWalletPayOrder import _mobile_payment_queryWalletPayOrder # 查询支付成功信息
            from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息
                    
            productList = None # 商品详情
            getFreightList = None # 运费补贴券
            getCouponList = None # 优惠券
            getSecondList = None # 秒返券
            getGiftList_2 = None # 电子礼券
            availableBalance = None # 钱包可用余额
            associationPay = None # 支付方式-邮政储蓄银行信息
            orderCommit = None # 订单信息
            payOrderNo = None # 支付流水号
            queryWalletPayOrder = None # 支付成功信息
            getOrderInfo = None # 详细订单信息
            number = 2 # 购买商品数量
            user = login_oauth_token["data"] # 给某个顾客下单的信息（非下单人）
            token = os.environ["token"]
            
            def step_mobile_product_search():
                "搜索商品"

                nonlocal productList
                data = deepcopy(data01)
                data["keyword"] = productCode
                with _mobile_product_search(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    productList = r.json()["data"]["list"][0]

            def step_mobile_order_carts_getFreightList():
                "获取运费补贴券列表"
                
                nonlocal getFreightList
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                }         
                with _mobile_order_carts_getFreightList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]:
                        getFreightList = r.json()["data"][0]

            def step_mobile_order_carts_getCouponList():
                "获取选中结算分组的可用和不可用优惠券列表"
                            
                nonlocal getCouponList
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "storeCode": user["storeCode"]
                }         
                with _mobile_order_carts_getCouponList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]["availableList"]:
                        getCouponList = r.json()["data"]["availableList"][0]

            def step_mobile_order_carts_getSecondList():
                "获取购物秒返券券列表"
                            
                nonlocal getSecondList
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "storeCode": user["storeCode"]
                }        
                with _mobile_order_carts_getSecondList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]:
                        for d in r.json()["data"]:
                            if d["isUsed"] == 1:
                                getSecondList = d["secondCouponId"]
            
            def step_mobile_order_carts_getGiftList_2():
                "获取电子礼券列表"
                
                nonlocal getGiftList_2
                data = {
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                }        
                with _mobile_order_carts_getGiftList_2(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    if r.json()["data"]:
                        getGiftList_2 = r.json()["data"][0]

            def step_mobile_order_carts_toSettlement():
                "选择商品去结算"
                            
                data = {
                    "addressId": None,
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "customerId":  user["userId"], # 给某个顾客下单的会员ID
                    "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                    "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "orderInvoice": None, # 发票信息
                    "couponList": [], # 使用的优惠卷
                    "giftList": [], # 使用的电子礼券
                    "freightList": [], # 使用的运费补贴礼券
                    "secondCouponList": [], # 使用的秒返券
                    "storeCode": user["storeCode"], # 服务中心编码
                    "ownerId": "", # 送货人ID
                    "pv": productList["pv"] * number,
                    "remarks": "", # 备注
                    "returnRate": 0.12, # 返还比例
                    "sharerId": None, # 分享人id
                    "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                }
                if getFreightList: # 运费补贴券
                    data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
                if getCouponList: # 优惠卷
                    data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
                if getSecondList: # 秒返券
                    data["secondCouponList"].append({"secondCouponId": getSecondList})
                if getGiftList_2: # 电子礼券
                    data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
                with _mobile_order_carts_toSettlement(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mobile_trade_orderCommit():
                "提交订单"
                            
                nonlocal orderCommit
                data = {
                    "addressId": None,
                    "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                    "customerId": user["userId"], # 给某个顾客下单的会员ID
                    "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                    "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                    "productList": [{
                        "serialNo": productList["serialNo"],
                        "number": number,
                        "retailPrice": productList["retailPrice"],
                        "pv": productList["pv"],
                        "imgUrl": productList["imgUrl"],
                        "title": productList["title"]
                    }],
                    "orderInvoice": None, # # 发票信息
                    "couponList": [], # 使用的优惠卷
                    "giftList": [], # 使用的电子礼券
                    "freightList": [], # 使用的运费补贴礼券
                    "secondCouponList": [], # 使用的秒返券
                    "storeCode": user["storeCode"], # 服务中心编码
                    "ownerId": "", # 送货人ID
                    "pv": productList["pv"] * number,
                    "remarks": "", # 备注
                    "returnRate": 0.12, # 返还比例
                    "sharerId": None, # 分享人id
                    "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                    "isUpgrade": 0 # 是否升级单 0->否 1->是
                } 
                if getFreightList: # 运费补贴券
                    data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
                if getCouponList: # 优惠卷
                    data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
                if getSecondList: # 秒返券
                    data["secondCouponList"].append({"secondCouponId": getSecondList})
                if getGiftList_2: # 电子礼券
                    data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                   
                with _mobile_trade_orderCommit(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    orderCommit = r.json()["data"]

            def step_mobile_wallet_queryPasswordExist():
                "是否设置了支付密码"
                
                with _mobile_wallet_queryPasswordExist(token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                
            def step_mobile_wallet_getDetail():
                "获取钱包首页相关信息"
                
                nonlocal  availableBalance
                with _mobile_wallet_getDetail(token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    availableBalance = r.json()["data"]["availableBalance"]
            
            def step_mobile_payment_getPayMethod():
                "获取支付方式"

                nonlocal associationPay
                data = {
                    "orderNoList":[orderCommit["orderNo"]], # 订单号集合
                    "payType":"PC", # 支付类型,H5、APP、PC、PROGRAM
                    "sourceType":1 # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
                }
                with _mobile_payment_getPayMethod(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    for d in r.json()["data"]:
                        if d["bankName"] == "邮政储蓄银行":
                            associationPay = d

            def step_mobile_payment_associationPay():
                "支付"

                nonlocal payOrderNo
                data = {
                    "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
                    "channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
                    "orderNoList": [orderCommit["orderNo"]],
                    "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
                    "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
                    "feeRate": 0, # 手续费率
                    "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
                    "walletPassword": "", # 钱包充值密码,非免密必传字段
                    "orderNo": orderCommit["orderNo"]
                }
                with _mobile_payment_associationPay(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    payOrderNo = r.json()["data"]["payOrderNo"]

            def step_mobile_payment_queryWalletPayOrder():
                "查询支付成功信息"

                nonlocal queryWalletPayOrder
                params = {
                    "payNo": payOrderNo, # 订单编号(必填)
                }
                with _mobile_payment_queryWalletPayOrder(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    queryWalletPayOrder = r.json()["data"]

            def step_mobile_orderInfo_getOrderInfo():
                "通过订单号查询客户端订单信息"

                nonlocal getOrderInfo
                params = {
                    "orderNo": orderCommit["orderNo"] # 订单编号(必填)
                }
                with _mobile_orderInfo_getOrderInfo(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getOrderInfo = r.json()["data"]
                    
            step_mobile_product_search()
            step_mobile_order_carts_getFreightList()
            step_mobile_order_carts_getCouponList()
            step_mobile_order_carts_getSecondList()
            step_mobile_order_carts_getGiftList_2()
            step_mobile_order_carts_toSettlement()
            step_mobile_trade_orderCommit()
            step_mobile_wallet_queryPasswordExist()
            step_mobile_wallet_getDetail()
            step_mobile_payment_getPayMethod()
            step_mobile_payment_associationPay()
            step_mobile_payment_queryWalletPayOrder()
            step_mobile_orderInfo_getOrderInfo()
            
            return queryWalletPayOrder

        @allure.step("云商-钱包-自购订单退货")
        def walletPay_to_me_applyReturn():
            "云商-钱包-自购订单退货"
            
            from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data as data01, _mobile_orderInfo_getClientOrderList # 客户端订单列表查询
            from api.mall_mobile_application._mobile_web_order_as_applyAfterSale import _mobile_web_order_as_applyAfterSale # 申请售后是否支持退货、换货、维修、返修
            from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import _mobile_web_order_as_returnMonthVerify # 隔月退货验证
            from api.mall_center_sys._mgmt_sys_getAllReNotice import _mgmt_sys_getAllReNotice # 获取退货须知集合
            from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息
            from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
            from api.mall_mobile_application._mobile_web_order_return_getReturnType import _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
            from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import _mobile_web_order_as_upgradeOrderVerify # 升级单校验
            from api.mall_mobile_application._mobile_order_return_applyReturn import _mobile_order_return_applyReturn # 申请退货/退款
            
            queryWalletPayOrder = walletPay_to_me() # 支付成功信息
            returnMonthVerify = "" # 隔月退货验证结果
            getReturnReasonByType = None # 退货/退款原因列表
            getReturnType = None # 获取退货类型：1：当月退 2：隔月退
            upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
            applyReturn = None # 退货单号
            token = os.environ["token"] # 云商
            
            @stepreruns()
            def step_mobile_orderInfo_getClientOrderList():
                "客户端订单列表查询"
                
                data = deepcopy(data01)
                data["orderNo"] = queryWalletPayOrder["orderNos"][0] # 订单号
                data["queryType"] = None # 查询类型(默认为null) null->原有订单(包含85折订单)查询 1->85折转分订单 2->85折转分补报订单 3->85折转分订单+85折转分补报订单
                data["orderStatus"] = [2] # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部        
                with _mobile_orderInfo_getClientOrderList(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200 
                    assert r.json()["data"]["list"][0]["orderNo"] == queryWalletPayOrder["orderNos"][0]
            
            def step_mobile_web_order_as_applyAfterSale():
                "申请售后是否支持退货、换货、维修、返修"

                params = {
                    "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
                }
                with _mobile_web_order_as_applyAfterSale(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    assert r.json()["data"]["expressType"] == 1 # 配送方式 1->服务中心自提 2->公司配送
                    assert r.json()["data"]["isExchange"] == 0 # 是否支持换货：1->是；0->否
                    assert r.json()["data"]["isRepair"] == 0 # 是否支持维修：1->是；0->否
                    assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
                    assert r.json()["data"]["isReturnRepair"] == 0 # 是否支持返修：1->是；0->否
                    assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
                    assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
                    assert r.json()["data"]["orderNo"] == queryWalletPayOrder["orderNos"][0]

            def step_mobile_web_order_as_returnMonthVerify():
                "隔月退货验证"
                    
                nonlocal returnMonthVerify
                params = {
                    "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
                }
                with _mobile_web_order_as_returnMonthVerify(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    returnMonthVerify = r.json()["data"]

            def step_mgmt_sys_getAllReNotice():
                "获取退货须知集合"
                    
                with _mgmt_sys_getAllReNotice(token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mobile_orderInfo_getOrderInfo():
                "通过订单号查询客户端订单信息"
                    
                params = {
                    "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
                }
                with _mobile_orderInfo_getOrderInfo(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200

            def step_mobile_order_return_getReturnReasonByType():
                "退货/退款原因列表"
                    
                nonlocal getReturnReasonByType
                with _mobile_order_return_getReturnReasonByType(token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getReturnReasonByType = r.json()["data"]

            def step_mobile_web_order_return_getReturnType():
                "获取退货类型：1：当月退 2：隔月退"
                    
                nonlocal getReturnType
                params = {
                    "orderMonth": time.strftime("%Y%m",time.localtime(time.time()))
                }
                with _mobile_web_order_return_getReturnType(params, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    getReturnType = r.json()["data"]

            def step_mobile_web_order_as_upgradeOrderVerify():
                "升级单校验"
                    
                nonlocal upgradeOrderVerify
                data = {
                    "orderNo": queryWalletPayOrder["orderNos"][0] # 订单号
                }
                with _mobile_web_order_as_upgradeOrderVerify(data, token) as r:            
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    upgradeOrderVerify = r.json()["data"]["resultType"]  

            def step_mobile_order_return_applyReturn():
                "申请退货/退款"
                
                nonlocal applyReturn
                data = {
                    "attachmentUrlList": [], # 退货凭证URL列表
                    "orderNo": queryWalletPayOrder["orderNos"][0], # 订单编号
                    "reason1": getReturnReasonByType[0]["returnReason"], # 退货一级原因
                    "reason1Id": getReturnReasonByType[0]["id"], # 退货一级原因id
                    "reason1Remark": "" # 退货一级原因备注
                }
                with _mobile_order_return_applyReturn(data, token) as r:  
                    assert r.status_code == 200
                    assert r.json()["code"] == 200
                    applyReturn = r.json()["data"]
            
            step_mobile_orderInfo_getClientOrderList()  
            step_mobile_web_order_as_applyAfterSale()
            step_mobile_web_order_as_returnMonthVerify()
            step_mgmt_sys_getAllReNotice()
            step_mobile_orderInfo_getOrderInfo()
            step_mobile_order_return_getReturnReasonByType()
            step_mobile_web_order_return_getReturnType()
            step_mobile_web_order_as_upgradeOrderVerify()              
            step_mobile_order_return_applyReturn()
            
            return queryWalletPayOrder, applyReturn
            
        @allure.step("库存列表-限量产品-初始数据")
        def step_01_mgmt_product_stock_list():
            
            nonlocal stock_list
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["serialNo"] == productCode:
                        stock_list = i
        
        @allure.step("库存列表-限量产品-期末数据")
        def step_02_mgmt_product_stock_list():
            
            "查询数据库数据"
            db = db_mall_center_inventory
            sql = f"SELECT SUM(product_num) FROM invt_inventory WHERE product_code = '{productCode}' AND product_num > 0 AND del = 0;"
            db.execute(sql)
            datasum =  db.fetchall()[0][0]
            
            data = deepcopy(self.data)
            data["serialNo"] = productCode
            data["stockType"] = "1"
            with _mgmt_product_stock_list(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeSaleQuota"] == str(int(stock_list["storeSaleQuota"]) + 0) # 服务中心可销售库存
                assert int(r.json()["data"]["list"][0]["storeSaleQuota"]) == datasum # mysql = redis

        step_01_mgmt_product_stock_list()
        wallet_add_10000()
        walletPay_to_me_applyReturn()
        step_02_mgmt_product_stock_list() 

