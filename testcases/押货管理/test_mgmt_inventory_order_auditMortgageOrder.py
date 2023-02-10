# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getAvailableAmount import _mgmt_inventory_mortgageAmount_getAvailableAmount # 根据storeCode查询押货余额
from api.mall_mgmt_application._mgmt_inventory_common_isStoreInTrafficControl import _mgmt_inventory_common_isStoreInTrafficControl # 店铺是否处于交通管控
from api.mall_mgmt_application._mgmt_inventory_order_searchProductsForAddPage import params, _mgmt_inventory_order_searchProductsForAddPage # 新增押货单页面:根据产品关键字搜索普通商品列表
from api.mall_mgmt_application._mgmt_inventory_order_addMortgageOrder import _mgmt_inventory_order_addMortgageOrder # 运营后台添加押货单
from api.mall_mgmt_application._mgmt_inventory_order_auditMortgageOrder import _mgmt_inventory_order_auditMortgageOrder # 运营后台审批押货单
from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import  _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情

from api.mall_mgmt_application._mgmt_inventory_order_getCusProductsForOpAddPage import params as params02, _mgmt_inventory_order_getCusProductsForOpAddPage # 运营后台提交定制品押货单页面的押货商品搜索列表
from api.mall_mgmt_application._mgmt_inventory_order_addCustomOrder import _mgmt_inventory_order_addCustomOrder # 添加定制品押货单

from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
from api.mall_mgmt_application._mgmt_inventory_remit_pageSearchList import data, _mgmt_inventory_remit_pageSearchList # 手工录入流水分页搜索列表
from api.mall_mgmt_application._mgmt_inventory_remit_verifyManualInputRemit import _mgmt_inventory_remit_verifyManualInputRemit # 手工录入流水审核

from setting import P1, P2, P3, productCode, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/auditMortgageOrder")
class TestClass:
    """
    运营后台审批押货单
    /mgmt/inventory/order/auditMortgageOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("运营后台审批押货单-成功路径: 审批押货单主路径检查")
    def test_01_mgmt_inventory_order_auditMortgageOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        searchProductsForAddPage = [] # 根据产品关键字搜索普通商品列表
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 2 # 押货数量
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        pageSearchList = None # 待审核流水信息
        
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
                searchProductsForAddPage.append(r.json()["data"]["list"][0])
        
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
                        "productCode": searchProductsForAddPage[0]["productCode"], # 物品编号
                        "productMortgagePrice": searchProductsForAddPage[0]["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
                    }
                ],
                "transId": f"KEY_{store}_{int(round(time.time() * 1000))}"
            }
            with _mgmt_inventory_order_addMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id =  r.json()["data"]
      
        @allure.step("运营后台审批押货单")
        def step_mgmt_inventory_order_auditMortgageOrder():
            
            data = {
                "id": id, # 押货单id
                "auditStatus": 1, # 审核结果 0不通过 1通过
                "auditRemarks": f"同意提交押货单申请" # 审核备注
            }
            with _mgmt_inventory_order_auditMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == 1
       
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

        # 手工录入款
        
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
                "remitMoney": searchProductsForAddPage[0]["productMortgagePrice"] * productNum - getAvailableAmount, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f'录入手工增押货款{searchProductsForAddPage[0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 备注
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
            params["verifyRemark"] = f'同意手工增押货款{searchProductsForAddPage[0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
         
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_order_searchProductsForAddPage()
        
        if getAvailableAmount < searchProductsForAddPage[0]["productMortgagePrice"] * productNum: # 如果押货款余额不够，则手工录入款
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

    @allure.severity(P1)
    @allure.title("运营后台审批押货单-成功路径: 审批仅调账不发货押货单主路径检查")
    def test_02_mgmt_inventory_order_auditMortgageOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        searchProductsForAddPage = [] # 根据产品关键字搜索普通商品列表
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 2 # 押货数量
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        pageSearchList = None # 待审核流水信息
        
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
                searchProductsForAddPage.append(r.json()["data"]["list"][0])
        
        @allure.step("运营后台添加押货单")
        def step_mgmt_inventory_order_addMortgageOrder():  
            
            nonlocal id
            data = {
                "invtMortgageOrderVO": {
                    "storeCode": getStoreInfo["code"],
                    "isDelivery": 0, # 0不需要发货 1需要发货
                    "remarks": "这个是仅调账的押货单，仓库不需要发货。" # 押货备注
                },
                "invtMortgageOrderProductVOList": [
                    {
                        "productCode": searchProductsForAddPage[0]["productCode"], # 物品编号
                        "productMortgagePrice": searchProductsForAddPage[0]["productMortgagePrice"], # 物品押货价
                        "productNum": productNum # 数量
                    }
                ],
                "transId": f"KEY_{store}_{int(round(time.time() * 1000))}"
            }
            with _mgmt_inventory_order_addMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id =  r.json()["data"]
      
        @allure.step("运营后台审批押货单")
        def step_mgmt_inventory_order_auditMortgageOrder():
            
            data = {
                "id": id, # 押货单id
                "auditStatus": 1, # 审核结果 0不通过 1通过
                "auditRemarks": f"同意提交押货单申请" # 审核备注
            }
            with _mgmt_inventory_order_auditMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == 1
       
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

        # 手工录入款
        
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
                "remitMoney": searchProductsForAddPage[0]["productMortgagePrice"] * productNum - getAvailableAmount, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f'录入手工增押货款{searchProductsForAddPage[0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 备注
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
            params["verifyRemark"] = f'同意手工增押货款{searchProductsForAddPage[0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
         
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_order_searchProductsForAddPage()
        
        if getAvailableAmount < searchProductsForAddPage[0]["productMortgagePrice"] * productNum: # 如果押货款余额不够，则手工录入款
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

    @allure.severity(P1)
    @allure.title("运营后台审批押货单-成功路径: 审批定制品押货单主路径检查")
    def test_03_mgmt_inventory_order_auditMortgageOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        getCusProductsForOpAddPage = None # 根据产品关键字搜索普通商品列表
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 2 # 押货数量
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        pageSearchList = None # 待审核流水信息
        
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
            params = deepcopy(self.params02)
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

        @allure.step("运营后台审批押货单")
        def step_mgmt_inventory_order_auditMortgageOrder():
            
            data = {
                "id": id, # 押货单id
                "auditStatus": 1, # 审核结果 0不通过 1通过
                "auditRemarks": f"同意提交押货单申请" # 审核备注
            }
            with _mgmt_inventory_order_auditMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == 1
       
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
        
        # 手工录入款
        
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
                "remitMoney": getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum - getAvailableAmount, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f'录入手工增押货款{getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 备注
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
            params["verifyRemark"] = f'同意手工增押货款{getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
         
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_order_getCusProductsForOpAddPage()
        
        if getAvailableAmount < getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum: # 如果押货款余额不够，则手工录入款
            step_mgmt_inventory_remit_getSourceTypeByRemitType()
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_sys_getAccountList()
            step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
            step_mgmt_store_getBankAccountList()
            step_mgmt_inventory_remit_addManualInputRemit()
            step_mgmt_inventory_remit_pageSearchList()
            step_mgmt_inventory_remit_verifyManualInputRemit()
            
        step_mgmt_inventory_order_addCustomOrder()
        step_mgmt_inventory_order_auditMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()

    @allure.severity(P1)
    @allure.title("运营后台审批押货单-成功路径: 审批仅调账不发货定制品押货单主路径检查")
    def test_04_mgmt_inventory_order_auditMortgageOrder(self):
        
        getStoreInfo = None # 获取服务中心信息
        getAvailableAmount = None # 根据storeCode查询押货余额
        isStoreInTrafficControl = None # 店铺是否处于交通管控
        getCusProductsForOpAddPage = None # 根据产品关键字搜索普通商品列表
        id = None # 押货单id
        getOrderDetail = None # 押货单详情
        productNum = 2 # 押货数量
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        pageSearchList = None # 待审核流水信息
        
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
            params = deepcopy(self.params02)
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
                "orderRemarks": "这个是仅调账不发货单，仓库不需要发货。", # 备注 店铺中心无需填写
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

        @allure.step("运营后台审批押货单")
        def step_mgmt_inventory_order_auditMortgageOrder():
            
            data = {
                "id": id, # 押货单id
                "auditStatus": 1, # 审核结果 0不通过 1通过
                "auditRemarks": f"同意提交押货单申请" # 审核备注
            }
            with _mgmt_inventory_order_auditMortgageOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == 1
       
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
        
        # 手工录入款
        
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
                "remitMoney": getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum - getAvailableAmount, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f'录入手工增押货款{getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 备注
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
            params["verifyRemark"] = f'同意手工增押货款{getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum - getAvailableAmount}元', # 审核备注
            params["verifyResult"] = 1 # 审核结果 1通过，2拒绝
            params["show"] = True
            params["type"] = 2               
            with _mgmt_inventory_remit_verifyManualInputRemit(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
         
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_inventory_mortgageAmount_getAvailableAmount()
        step_mgmt_inventory_common_isStoreInTrafficControl()
        step_mgmt_inventory_order_getCusProductsForOpAddPage()
        
        if getAvailableAmount < getCusProductsForOpAddPage["subProductList"][0]["productMortgagePrice"] * productNum: # 如果押货款余额不够，则手工录入款
            step_mgmt_inventory_remit_getSourceTypeByRemitType()
            step_mgmt_inventory_common_getStoreInfo()
            step_mgmt_sys_getAccountList()
            step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
            step_mgmt_store_getBankAccountList()
            step_mgmt_inventory_remit_addManualInputRemit()
            step_mgmt_inventory_remit_pageSearchList()
            step_mgmt_inventory_remit_verifyManualInputRemit()
            
        step_mgmt_inventory_order_addCustomOrder()
        step_mgmt_inventory_order_auditMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()

