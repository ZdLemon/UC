# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getReason import params, _mgmt_inventory_common_getReason # 退换货原因
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import params as params02, _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchProduct import params as params03, _mgmt_inventory_dis_mortgage_returnOrder_searchProduct # 获取商品信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn import _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn # 新建押货退货单
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params as params04, _mgmt_inventory_dis_mortgage_returnOrder_listPage # 押货退货列表
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import params as params05, _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo # 展示审批保存信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_opinion import data, _mgmt_inventory_dis_mortgage_returnOrder_opinion # 添加审批意见
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_audit import data as data02, _mgmt_inventory_dis_mortgage_returnOrder_audit # 审批
from api.basic_services._storage_upload import files, _storage_upload # 退回时上传附件
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_process import data as data03, _mgmt_inventory_dis_mortgage_returnOrder_process # 退回处理
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_inspect import data as data04, _mgmt_inventory_dis_mortgage_returnOrder_inspect # 验货

from util.stepreruns import stepreruns
from setting import P1, P2, P3, store_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/returnOrder/inspect")
class TestClass:
    """
    验货
    /mgmt/inventory/dis/mortgage/returnOrder/inspect
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.params05 = deepcopy(params05)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.data04 = deepcopy(data04)
        self.files = deepcopy(files)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("审批-成功路径: 押货退货审批通过检查")
    def test_mgmt_inventory_dis_mortgage_returnOrder_inspect(self):
        
        getReason = None # 退换货原因
        searchStore = None # 店铺信息
        searchProduct = None # 商品信息
        id = None # 押货退货单id
        listPage = None # 押货退货列表信息
        searchAuditInfo = None # 展示审批保存信息
        storage_upload = None # 退回时上传附件信息
        
        @allure.step("获取各种退换货原因")
        def test_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = deepcopy(self.params)
            params["type:"] = 3 # 退货原因              
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]
        
        @allure.step("查询店铺信息")
        def test_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = deepcopy(self.params02)
            params["storeCode"] = store_85                   
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]
        
        @allure.step("商品编码搜索退货商品信息")
        def step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct():
            
            nonlocal searchProduct
            params = deepcopy(self.params03) 
            params["storeCode"] = store_85
            params["productCode"] = productCode           
            with _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchProduct = r.json()["data"]
        
        @allure.step("新建85折押货退货单")
        def step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn():
            
            nonlocal id
            data = {
                "productList": [{
                    "productCode": searchProduct["productCode"], # 商品编号
                    "productName": searchProduct["productName"], # 商品名称
                    "packing": searchProduct["packing"],
                    "unit": searchProduct["unit"],
                    "pieceBoxNorm": None,
                    "pieceBoxPrice": None,
                    "mortgagePrice": searchProduct["mortgagePrice"], # 85折押货价
                    "retailPrice": searchProduct["retailPrice"], # 零售价
                    "inventoryNum": searchProduct["inventoryNum"], # 库存数量
                    "returnNum": 2, # 退货数量
                    "remark": ""
                }],
                "orderMark": 0,
                "reasonFirst": getReason[1]["returnReason"],
                "reasonFirstRemark": "",
                "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
                "reasonSecondRemark": "",
                "storeCode": searchStore["storeCode"]
            }               
            with _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                id = r.json()["data"]

        @allure.step("押货退货分页列表:获取id")
        @stepreruns()
        def step_mgmt_inventory_dis_mortgage_returnOrder_listPage():
            
            nonlocal listPage
            params = deepcopy(self.params04) 
            params["storeCode"] = store_85               
            with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["id"] == id:
                        listPage = d
                        break

        @allure.step("押货退货单详情")
        def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
            
            params = deepcopy(self.params05) 
            params["id"] = id              
            with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["id"] == id
                assert r.json()["data"]["orderSn"] == listPage["orderSn"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo       
            with _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_returnOrder_opinion():
            
            data = deepcopy(self.data) 
            data["orderId"] = id
            data["content"] = f"同意{listPage['orderSn']}押货退货单申请"        
            with _mgmt_inventory_dis_mortgage_returnOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_returnOrder_audit():
            
            data = deepcopy(self.data02)
            data["id"] = id
            data["auditRemark"] = f"同意审批通过押货退货单{listPage['orderSn']}"
            data["auditResult"] = "1"
            data["reasonFirst"] = getReason[1]["returnReason"]
            data["reasonSecond"] = getReason[1]["reasonList"][1]["returnReason"]
            if searchAuditInfo:
                data["returnInfo"] = searchAuditInfo
                data["returnAddress"] = searchAuditInfo
            else:
                data["returnInfo"] = "我是退回地址"
                data["returnAddress"] = "我是退回地址"
            with _mgmt_inventory_dis_mortgage_returnOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传文件：退回时上传附件")
        def step_storage_upload():
            
            nonlocal storage_upload
            files = deepcopy(self.files) 
            files["clientKey"] = "mall-center-inventory" 
            files["file"] = "data/顺丰快递单.jpg"                
            with _storage_upload(files, self.access_token) as r:            
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                storage_upload = r.json()["datas"]

        @allure.step("退回处理")
        def step_mgmt_inventory_dis_mortgage_returnOrder_process():
            
            data = deepcopy(self.data03)
            data["orderId"] = id
            data["returnType"] = 2 # 退回类型 1自带 2邮寄
            data["expressProofUrl"] = storage_upload["fileUrlKey"]
            data["expressProofName"] = storage_upload["relativePath"][24:]
            with _mgmt_inventory_dis_mortgage_returnOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_returnOrder_inspect():
            
            data = deepcopy(self.data04)
            data["orderId"] = id
            data["inspectResult"] = "1" # 验货意见 0不通过 1通过
            data["inspectRemark"] = f"押货退货单{listPage['orderSn']}验货没问题"
            data["orderReturnRealAmount"] = str(listPage['returnAmount'])
            data["productList"] = [{"returnRealNum": 2, "productCode": searchProduct["productCode"]}]
            data["returnRealAmount"] = str(listPage['returnAmount'])
            with _mgmt_inventory_dis_mortgage_returnOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        test_mgmt_inventory_common_getReason()
        test_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct()
        step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn()
        step_mgmt_inventory_dis_mortgage_returnOrder_listPage()
        step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
        step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo()
        step_mgmt_inventory_dis_mortgage_returnOrder_opinion()
        step_mgmt_inventory_dis_mortgage_returnOrder_audit()
        step_storage_upload()
        step_mgmt_inventory_dis_mortgage_returnOrder_process()
        step_mgmt_inventory_dis_mortgage_returnOrder_inspect()
