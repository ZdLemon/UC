# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 退换货原因
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes import _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes # 获取所有匹配的商品编码列表
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange import _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange # 押货换货下单
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_detail_id import _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id # 详情
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo # 展示审批保存信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_opinion import _mgmt_inventory_dis_mortgage_exchangeOrder_opinion # 添加审批意见
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_audit import _mgmt_inventory_dis_mortgage_exchangeOrder_audit # 审批
from api.basic_services._storage_upload import files, _storage_upload # 退回时上传附件
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_process import _mgmt_inventory_dis_mortgage_exchangeOrder_process # 退回处理
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_inspect import _mgmt_inventory_dis_mortgage_exchangeOrder_inspect # 验货
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_deliver import _mgmt_inventory_dis_mortgage_exchangeOrder_deliver # 发货
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_confirm import _mgmt_inventory_dis_mortgage_exchangeOrder_confirm # 确认收货

from util.stepreruns import stepreruns
from setting import P1, P2, P3, store_85, productCode

from copy import deepcopy
import os
import allure
import time
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange")
class TestClass:
    """
    押货换货下单
    /mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange
    """
    def setup_class(self):
        self.files = deepcopy(files)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("押货换货下单-成功路径: 先退后换检查")
    def test_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(self):
        
        getReason = None # 退换货原因
        searchStore = None # 店铺信息
        searchMatchedProductCodes = None # 商品信息
        id = None # 押货退货单id
        listPage = None # 押货退货列表信息
        returnOrder_detail = None # 押货退货单详情
        searchAuditInfo = None # 展示审批保存信息
        storage_upload = None # 退回时上传附件信息
        returnNum = 2 # 换货数量
               
        @allure.step("获取各种退换货原因")
        def test_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 4, 
            }             
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]
        
        @allure.step("查询店铺信息")
        def test_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = {
                "storeCode" : store_85,  # 服务中心编号
            }                   
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]
        
        @allure.step("获取所有匹配的商品编码列表")
        def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
            
            nonlocal searchMatchedProductCodes
            params = {
                "productCode": productCode # 产品编号
            }           
            with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchMatchedProductCodes = r.json()["data"]
        
        @allure.step("押货换货下单")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
            
            nonlocal id
            data = {
                "productList": [{
                    "productCode": searchMatchedProductCodes["productCode"], # 商品编号
                    "productName": searchMatchedProductCodes["productName"], # 商品名称
                    "packing": searchMatchedProductCodes["packing"],
                    "unit": searchMatchedProductCodes["unit"],
                    "pieceBoxNorm": None,
                    "pieceBoxPrice": None,
                    "mortgagePrice": searchMatchedProductCodes["mortgagePrice"], # 85折押货价
                    "retailPrice": searchMatchedProductCodes["retailPrice"], # 零售价
                    "inventoryNum": searchMatchedProductCodes["inventoryNum"], # 库存数量
                    "returnNum": returnNum, # 退货数量
                    "remark": ""
                }],
                "orderMark": 0,
                "reasonFirst": getReason[1]["returnReason"],
                "reasonFirstRemark": "",
                "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
                "reasonSecondRemark": "",
                "storeCode": searchStore["storeCode"]
            }               
            with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                id = r.json()["data"]

        @allure.step("详情")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
            
            nonlocal returnOrder_detail
            params = {
                "id": id
            }              
            with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                returnOrder_detail = r.json()["data"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
            
            data = {
                "orderId": id, # 押货或售后单id
                "content": f"同意{returnOrder_detail['orderSn']}押货换货单申请" # 审批内容
            }       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
            
            data = {
                "id": id, # 押货换货单id
                "exchangeType": returnOrder_detail["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": "", # 审批附件
                "auditFileName": "", # 审批附件名称
                "auditRemark": f"同意审批通过押货换货单{returnOrder_detail['orderSn']}", # 审核备注
                "auditResult": "1", # 审批意见 0不通过 1通过
                "disposalType": returnOrder_detail["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                "reasonFirst": returnOrder_detail["reasonFirst"], # 一级原因
                "reasonFirstRemark": returnOrder_detail["reasonFirstRemark"], # 一级原因备注
                "reasonSecond": returnOrder_detail["reasonSecond"], # 二级原因
                "reasonSecondRemark": returnOrder_detail["reasonSecondRemark"], # 二级原因备注
                "productList": [{
                    "id": returnOrder_detail["products"][0]["id"],
                    "exchangeNum": returnOrder_detail["products"][0]["exchangeNum"],
                    "dailyUseType": returnOrder_detail["products"][0]["dailyUseType"],
                    "firstUseTime": returnOrder_detail["products"][0]["firstUseTime"],
                    "happenType": returnOrder_detail["products"][0]["happenType"],
                    "productBatch": returnOrder_detail["products"][0]["productBatch"],
                    "problemDesc": returnOrder_detail["products"][0]["problemDesc"],
                    "productionDate": returnOrder_detail["products"][0]["productionDate"],
                    "productSn": returnOrder_detail["products"][0]["productSn"],
                    "disposalType": returnOrder_detail["products"][0]["disposalType"],
                    "productCode": returnOrder_detail["products"][0]["productCode"]
                }],
                "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
            }
            with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("退回处理")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
            
            data = deepcopy(self.data03)
            data["orderId"] = id
            data["returnType"] = 2 # 退回类型 1自带 2邮寄
            data["expressProofUrl"] = storage_upload["fileUrlKey"]
            data["expressProofName"] = storage_upload["relativePath"][24:]
            data = {
                "orderId": id, # id
                "returnType": "3", # 退回类型 1自带 2邮寄
                "expressNo": "xhl123456", # 物流单号
                "expressCompany": "完美物流", # 物流公司
                "expressProofUrl": "",
                "expressProofName": "", # 快递凭证名称
                "processRemark": "这是我的退回凭证，请验收" # 退回处理说明
            }
            with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
            
            data = {
                "expressSubsidy":15,
                "inspectRemark": f"押货换货单{returnOrder_detail['orderSn']}验货没问题",
                "inspectResult": "1", # 验货意见 0不通过 1通过
                "orderId": id,
                "inspectProofUrl":[]
            }
            with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("发货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
            
            data = {
                "orderId":"336", # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType":2, # 发货方式 1顾客自提 2邮寄
                "expressCompany":"小河物流", # 新品配送物流公司
                "expressNo":"xh123456789" # 物流单号
            }
            with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("确认收货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
            
            data = {
                "orderId": id, 
            }
            with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        test_mgmt_inventory_common_getReason()
        test_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_audit()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_process()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id()
