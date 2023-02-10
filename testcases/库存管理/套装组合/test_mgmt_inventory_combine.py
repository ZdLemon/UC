# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_combine_page import params, _mgmt_inventory_combine_page # 分页查询套装组合列表
from api.mall_mgmt_application._mgmt_inventory_combine_show import _mgmt_inventory_combine_show # 套装组合展示
from api.mall_mgmt_application._mgmt_inventory_combine import _mgmt_inventory_combine # 套装组合
from api.mall_mgmt_application._mgmt_inventory_combine_detail import _mgmt_inventory_combine_detail # 查询套装组合明细

from setting import P1, P2, P3, store, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/combine")
class TestClass:
    """
    套装组合
    /mgmt/inventory/combine
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("套装组合-成功路径: 套装组合检查")
    def test_mgmt_inventory_combine(self, onSaleVersion, returnOrder_auditOrder_zh):
            
        combine_page = None # 分页查询套装组合列表
        combine_show = None # 套装组合展示
        productNum = 10 # 押货数量
        combineNum = 2 # 套装组合数量 
        combine_detail = None # 查询套装组合明细
        
        @allure.step("分页查询套装组合列表") 
        def  step_mgmt_inventory_combine_page(): 
        
            nonlocal combine_page
            params = deepcopy(self.params)
            params["combineState"] = 1 # 组合状态：1未组合、2已组合
            params["storeCode"] = store
            params["productCode"] = productCode_zh
            with _mgmt_inventory_combine_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    combine_page = r.json()["data"]["list"][0]

        @allure.step("套装组合展示") 
        def  step_mgmt_inventory_combine_show(): 
        
            nonlocal combine_show
            params = {
                "id" : combine_page["id"]
            }
            with _mgmt_inventory_combine_show(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                combine_show = r.json()["data"]           

        @allure.step("套装组合") 
        def  step_mgmt_inventory_combine(): 
        
            data = {
                "combineId": combine_page["id"], # 套装组合id
                "combineNum": combineNum # 套装组合数量
            }
            with _mgmt_inventory_combine(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询套装组合明细") 
        def  step_mgmt_inventory_combine_detail(): 
        
            nonlocal combine_detail
            params = {
                "id" : combine_page["id"]
            }
            with _mgmt_inventory_combine_detail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                combine_detail = r.json()["data"]           
       
        @allure.step("完美运营后台押货")
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

        step_mgmt_inventory_combine_page()
        step_mgmt_inventory_combine_show()
        if combine_show["before"][0]["productNum"] < 10:
            productNum = 10 - combine_show["before"][0]["productNum"]
            auditMortgageOrder()
        if combine_show["after"]["productNum"] > -combineNum:
            combineNum = -combine_show["after"]["productNum"]
        step_mgmt_inventory_combine()
        step_mgmt_inventory_combine_detail()
        
