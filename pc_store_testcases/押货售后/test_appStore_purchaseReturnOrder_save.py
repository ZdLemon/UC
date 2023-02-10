# coding:utf-8

from api.mall_store_application._appStore_purchaseReturnOrder_list import params, _appStore_purchaseReturnOrder_list # 押货退货单列表
from api.basic_services._auth_getUserInfo import _auth_getUserInfo # 获取当前用户登录缓存信息
from api.mall_store_application._appStore_common_getReason import _appStore_common_getReason # 获取各种退换货原因
from api.mall_store_application._appStore_purchaseReturnOrder_returnProducts import _appStore_purchaseReturnOrder_returnProducts # 提交退货单页面的押货退货商品搜索
from api.mall_store_application._appStore_purchaseReturnOrder_save import _appStore_purchaseReturnOrder_save # 提交退货单

from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 完美后台获取各种退换货原因
from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
from api.mall_mgmt_application._mgmt_inventory_returnOrder_addOpinion import _mgmt_inventory_returnOrder_addOpinion # 后台押货退货添加审批意见
from api.mall_mgmt_application. _mgmt_inventory_returnOrder_auditOrder import  _mgmt_inventory_returnOrder_auditOrder # 后台审批押货退货单


from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/purchaseReturnOrder/save")
class TestClass:
    """
    提交退货单
    /appStore/purchaseReturnOrder/save
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token"]
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("提交退货单-成功路径: 提交退货单检查")
    def test_appStore_purchaseReturnOrder_save(self):
        
        purchaseReturnOrder = None # 押货退货单列表信息
        getUserInfo = None # 获取当前用户登录缓存信息
        getReason = None # 获取各种退换货原因
        returnProducts = None # 提交退货单页面的押货退货商品搜索
        purchaseReturnOrder_save = None # 退货单信息
        productNum = 2 # 退货数量
        
        getReason_02 = None # 完美后台获取各种退换货原因
        getOrderDetail = None # 完美后台押货退货单详情
        addOpinion = None # 后台押货退货添加审批意见
        
        @allure.step("押货退货单列表")
        def step_appStore_purchaseReturnOrder_list():
            
            nonlocal purchaseReturnOrder
            params = deepcopy(self.params)
            with _appStore_purchaseReturnOrder_list(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                purchaseReturnOrder = r.json()["data"]["list"]
        
        @allure.step("获取当前用户登录缓存信息")
        def step_auth_getUserInfo():
            
            nonlocal getUserInfo
            with _auth_getUserInfo(self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getUserInfo = r.json()["data"] 

        @allure.step("获取各种退换货原因")
        def step_appStore_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 3, # 类型: 3退货 4换货
            }
            with _appStore_common_getReason(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("提交退货单页面的押货退货商品搜索")
        def step_appStore_purchaseReturnOrder_returnProducts():
            
            nonlocal returnProducts
            params = {
                "product": productCode, # 产品名称/产品编号
                "pageNum": 1,
                "pageSize": 20
            }
            with _appStore_purchaseReturnOrder_returnProducts(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["productCode"] == productCode:
                        returnProducts = d

        @allure.step("提交退货单")
        def step_appStore_purchaseReturnOrder_save():
            
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
            with _appStore_purchaseReturnOrder_save(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                purchaseReturnOrder_save = r.json()["data"]

        @allure.step("完美后台获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason_02
            params = {
                "type": 3, # 类型: 3退货 4换货
            }
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason_02 = r.json()["data"]

        @allure.step("完美后台押货退货添加审批意见")
        def step_mgmt_inventory_returnOrder_addOpinion():
            
            nonlocal addOpinion
            data = {
                "orderId": purchaseReturnOrder_save["orderId"], # 押货或售后单id
                "content": f"同意这个退货申请{purchaseReturnOrder_save['orderSn']}" # 意见内容
            }
            with _mgmt_inventory_returnOrder_addOpinion(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                addOpinion = r.json()["data"]

        @allure.step("完美后台押货退货单详情")
        def step_mgmt_inventory_returnOrder_getOrderDetail():
            
            nonlocal getOrderDetail
            params = {
                "orderId": purchaseReturnOrder_save["orderId"]
            }
            with _mgmt_inventory_returnOrder_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getOrderDetail = r.json()["data"]
                       
        @allure.step("完美后台审批押货退货单")
        def step_mgmt_inventory_returnOrder_auditOrder():
            
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
            with _mgmt_inventory_returnOrder_auditOrder(data, self.access_token) as r:
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
        step_mgmt_inventory_returnOrder_addOpinion()
        step_mgmt_inventory_returnOrder_auditOrder()



