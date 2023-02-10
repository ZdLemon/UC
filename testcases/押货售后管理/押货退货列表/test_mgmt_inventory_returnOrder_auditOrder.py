# coding:utf-8

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

from setting import P1, P2, P3, productCode_zh, productCode, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/returnOrder/auditOrder")
class TestClass:
    """
    后台审批押货退货单
    /mgmt/inventory/returnOrder/auditOrder
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
        self.store_token = os.environ["store_token"]
            
    @allure.severity(P1)
    @allure.title("后台审批押货退货单-成功路径: 后台审批押货退货单检查")
    def test_mgmt_inventory_returnOrder_auditOrder(self):
            
        getReason = None # 获取各种退换货原因 
        getStoreInfo = None # 获取服务中心信息
        getProductForAddPage = None # 添加退货单时的商品搜索
        productNum = 2 # 押货退货数量
        addMortgageReturnOrder = None # 押货退货单Id

        getOrderDetail = None # 完美后台押货退货单详情
        addOpinion = None # 后台押货退货添加审批意见
        
        @allure.step("获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 3, 
            }              
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("获取服务中心信息")
        def step_mgmt_inventory_common_getStoreInfo():
            
            nonlocal getStoreInfo
            params = {
                "storeCode": store
            }              
            with _mgmt_inventory_common_getStoreInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStoreInfo = r.json()["data"]

        @allure.step("添加退货单时的商品搜索")
        def step_mgmt_inventory_returnOrder_getProductForAddPage():
            
            nonlocal getProductForAddPage
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productCode, # 商品一级或二级编码
            }              
            with _mgmt_inventory_returnOrder_getProductForAddPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductForAddPage = r.json()["data"]

        @allure.step("店铺库存校验接口")
        def step_mgmt_inventory_order_checkProductInventory():
            
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
            with _mgmt_inventory_order_checkProductInventory(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == []

        @allure.step("后台申请添加押货退货单")
        def step_mgmt_inventory_returnOrder_addMortgageReturnOrder():
            
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
            with _mgmt_inventory_returnOrder_addMortgageReturnOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addMortgageReturnOrder = r.json()["data"]

        @allure.step("后台押货退货添加审批意见")
        def step_mgmt_inventory_returnOrder_addOpinion():
            
            nonlocal addOpinion
            data = {
                "orderId": addMortgageReturnOrder, # 押货或售后单id
                "content": f"同意这个退货申请" # 意见内容
            }
            with _mgmt_inventory_returnOrder_addOpinion(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                addOpinion = r.json()["data"]

        @allure.step("后台押货退货单详情")
        def step_mgmt_inventory_returnOrder_getOrderDetail():
            
            nonlocal getOrderDetail
            params = {
                "orderId": addMortgageReturnOrder
            }
            with _mgmt_inventory_returnOrder_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getOrderDetail = r.json()["data"]
                       
        @allure.step("后台审批押货退货单")
        def step_mgmt_inventory_returnOrder_auditOrder():
            
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
            with _mgmt_inventory_returnOrder_auditOrder(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("提交退回信息")
        def step_appStore_purchaseReturnOrder_returnInfo():
            
            data = {
                "returnType": 2, # 退回类型 1自带 2邮寄
                "expressCompany": "小何物流", # 物流公司
                "expressNo": str(round(time.time())), # 物流单号
                "expressFreightProof": "", # 物流费用凭证url
                "expressFreightProofName": "", # 物流费用凭证名称
                "processRemarks": "退回产品都要说明吗", # 退回处理说明
                "orderId": addMortgageReturnOrder # 退货单id
            }
            with _appStore_purchaseReturnOrder_returnInfo(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
 
        @allure.step("完美后台押货退货验货")
        def step_mgmt_inventory_returnOrder_inspectOrder():
            
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
            with _mgmt_inventory_returnOrder_inspectOrder(data, self.access_token) as r:
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
        





