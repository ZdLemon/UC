# coding:utf-8

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
from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核

from setting import P1, P2, P3, username_85, store_85, name_85, productCode, store

from copy import deepcopy
import os
import allure
import uuid


@allure.feature("mall_store_application")
@allure.story("/appStore/purchase/commit")
class TestClass:
    """
    提交押货单
    /appStore/purchase/commit
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.store_token = os.environ["store_token"]
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("提交押货单-成功路径: 提交押货单检查")
    def test_appStore_purchase_commit(self):
        
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

        @allure.step("提交押货单页面的负库存押货商品列表")
        def step_appStore_purchaseOrder_negateProducts():
            
            nonlocal negateProducts
            with _appStore_purchaseOrder_negateProducts(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                negateProducts = r.json()["data"]
        
        @allure.step("提交押货单页面的押货商品搜索")
        def step_appStore_purchaseOrder_products():
            
            nonlocal products
            params = {
                "pageNum": 1,
                "pageSize": 40,
                "product": productCode
            }
            with _appStore_purchaseOrder_products(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        products = d
        
        @allure.step("押货金额")
        def step_appStore_purchase_balanceAmount():
            
            nonlocal availableAmount
            with _appStore_purchase_balanceAmount(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                availableAmount = r.json()["data"]["availableAmount"]
        
        @allure.step("提交押货单")
        def step_appStore_purchase_commit():
            
            nonlocal orderSn
            data = {
                "list": products_list,
                "transId": f"KEY_{store}_{uuid.uuid1()}" # 业务id KEY_902804_1f037473-cd4d-4996-8ff4-570becdd8ae0
            }
            with _appStore_purchase_commit(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"
                orderSn = r.json()["data"]

        @allure.step("按银行流水类型获取款项映射列表")
        def step_mgmt_inventory_remit_getSourceTypeByRemitType():
            
            nonlocal getSourceTypeByRemitType
            params = {
                "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
            }              
            with _mgmt_inventory_remit_getSourceTypeByRemitType(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getSourceTypeByRemitType = r.json()["data"]
                
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
                       
        @allure.step("查询分公司银行账号")
        def step_mgmt_sys_getAccountList():
            
            nonlocal getAccountList
            params = {
                "companyCode" : getStoreInfo["companyCode"],  # 公司编码
            }             
            with _mgmt_sys_getAccountList(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getAccountList = r.json()["data"] 

        @allure.step("根据storeCode查询押货余额主表数据")
        def step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore():
            
            nonlocal getMortgageAmountByStore
            params = {
                "storeCode": getStoreInfo["code"]
            }            
            with _mgmt_inventory_mortgageAmount_getMortgageAmountByStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getMortgageAmountByStore = r.json()["data"] 

        @allure.step("通过storeCode获取银行账户资料信息")
        def step_mgmt_store_getBankAccountList():
            
            nonlocal getBankAccountList
            params = {
                "storeCode": getStoreInfo["code"]
            }            
            with _mgmt_store_getBankAccountList(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200 
                getBankAccountList = r.json()["data"] 
 
        @allure.step("手工增押货款")
        def step_mgmt_inventory_remit_addManualInputRemit():
            
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
            with _mgmt_inventory_remit_addManualInputRemit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True

        @allure.step("手工录入流水分页搜索列表:获取待审核流水信息")
        def step_mgmt_inventory_remit_pageSearchList():
            
            nonlocal pageSearchList 
            data = deepcopy(self.data)
            data["storeCode"] = getStoreInfo["code"]
            data["sourceType"] = 8 # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
            data["verifyStatus"] = 0 # 审核状态 0 待审核 1 已审核          
            with _mgmt_inventory_remit_pageSearchList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                pageSearchList = r.json()["data"]["list"]

        @allure.step("手工录入流水审核")
        def step_mgmt_inventory_remit_verifyManualInputRemit():
            
            params = pageSearchList[0]
            params["verifyRemark"] = f"同意手工增押货款{sum([d['mortgagePrice'] * d['productNum'] for d in products_list]) - availableAmount + 10}元", # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, self.access_token) as r:
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




