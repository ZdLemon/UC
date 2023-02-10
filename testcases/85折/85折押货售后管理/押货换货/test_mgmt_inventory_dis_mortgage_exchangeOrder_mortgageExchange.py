# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
from api.basic_services._storage_upload import _storage_upload # 上传商品图片
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes import _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes # 获取所有匹配的商品编码列表
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchProductByCode import _mgmt_inventory_dis_mortgage_common_searchProductByCode # 按商品编码精确查询商品
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange import _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange # 押货换货下单
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_opinion import _mgmt_inventory_dis_mortgage_exchangeOrder_opinion # 添加审批意见
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_detail_id import _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id # 详情
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo # 展示审批保存信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_audit import _mgmt_inventory_dis_mortgage_exchangeOrder_audit # 审批
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_process import _mgmt_inventory_dis_mortgage_exchangeOrder_process # 退回
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_inspect import _mgmt_inventory_dis_mortgage_exchangeOrder_inspect # 验货
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_deliver import _mgmt_inventory_dis_mortgage_exchangeOrder_deliver # 发货
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_exchangeOrder_confirm import _mgmt_inventory_dis_mortgage_exchangeOrder_confirm # 确认收货

from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange")
class TestClass:
    """
    押货换货下单
    /mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
            
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 先换后退检查")
    def test_01_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(self):
            
        searchStore = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        searchMatchedProductCodes = None # 获取所有的商品编码列表
        searchProductByCode = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        mortgageExchange = None # 后台申请添加押货换货单
        opinion = None # 后台押货换货添加审批意见
        detail_id = None # 后台押货换货单详情
        searchAuditInfo = None # 展示审批保存信息

        @allure.step("查询店铺信息")
        def step_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = {
                "storeCode": store_85, # 服务中心编号
            }             
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]

        @allure.step("获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 4, 
            }             
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_03_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("获取所有匹配的商品编码列表")
        def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
            
            nonlocal searchMatchedProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchMatchedProductCodes = r.json()["data"]

        @allure.step("按商品编码精确查询商品")
        def step_mgmt_inventory_dis_mortgage_common_searchProductByCode():
            
            nonlocal searchProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductByCode = r.json()["data"]

        @allure.step("押货换货下单")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
            
            nonlocal mortgageExchange
            data = {
                "storeCode": store_85,
                "exchangeType": 1, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemark": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemark": "我是二级原因的备注信息哦", # 二级原因备注
                "productList": [
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 4 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    }],
                "files": [ 
                    {
                        "fileUrl": uploads[0]["fileUrlKey"],
                        "fileName": uploads[0]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[1]["fileUrlKey"],
                        "fileName": uploads[1]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[2]["fileUrlKey"],
                        "fileName": uploads[2]['relativePath'].split('/')[-1]
                    }
                ] # 换货单附件，支持3个
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                mortgageExchange = r.json()["data"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
            
            nonlocal opinion
            data = {
                "orderId": mortgageExchange, # 押货或售后单id
                "content": "业务部门同意押货只换不退" # 审批内容
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                opinion = r.json()["data"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo        
            with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("详情")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
            
            nonlocal detail_id
            params = {
                "id": mortgageExchange, # 押货或售后单id
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                detail_id = r.json()["data"]

        @allure.step("上传商品图片")
        def step_04_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/审批01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
            
            data = {
                "id": detail_id["id"],
                "exchangeType": detail_id["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemark": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditResult": "1", # 审批意见 0不通过 1通过
                "disposalType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": detail_id["reasonFirst"], # 一级原因
                "reasonFirstRemark": detail_id["reasonFirstRemark"], # 一级原因备注
                "reasonSecond": detail_id["reasonSecond"], # 二级原因
                "reasonSecondRemark": detail_id["reasonSecondRemark"], # 二级原因备注
                "productList": [{
                    "id": detail_id["products"][0]["id"],
                    "exchangeNum": detail_id["products"][0]["exchangeNum"], # 数量
                    "dailyUseType": detail_id["products"][0]["dailyUseType"], # 日常使用时间 1早上 2中午 3晚上
                    "firstUseTime": detail_id["products"][0]["firstUseTime"], # 第一次使用的时间
                    "happenType": detail_id["products"][0]["happenType"], # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "productBatch": detail_id["products"][0]["productBatch"], # 批次号
                    "problemDesc": detail_id["products"][0]["problemDesc"], # 问题描述
                    "productionDate": detail_id["products"][0]["productionDate"], # 物品生产日期
                    "productSn": detail_id["products"][0]["productSn"], # 物品序列号/二维码
                    "disposalType": detail_id["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    "productCode": detail_id["products"][0]["productCode"] # 商品编号
                }],
                "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_06_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_07_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("退回")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "expressAmount": 0, # 物流金额
                "expressCompany": "", # 快递公司
                "expressNo": "", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemark": "这是我的报废凭证，请过目", # 退回说明
                "returnType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }      
            with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
 
        @allure.step("上传商品图片")
        def step_08_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_09_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_10_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
            
            data = {
                "expressSubsidy": 0, # 运费补贴
                "inspectRemark": "仓库验货部门验货没问题", # 验货备注
                "inspectResult": "1", # 验货结果 0不通过 1通过
                "orderId": detail_id["id"],
                "inspectProofUrl": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']]
            }       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("发货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            } 
            with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("确认收货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
            }  
            with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_common_searchProductByCode()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
        # 待审批
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion()
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo()
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id()
        # step_04_storage_upload()
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_audit()
        # # 待上传凭证
        # step_05_storage_upload()
        # step_06_storage_upload()
        # step_07_storage_upload()
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_process()
        # # 待验货
        # step_08_storage_upload()
        # step_09_storage_upload()
        # step_10_storage_upload()
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect()
        # # 待发货
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver()
        # # 确认收货
        # step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm()

       

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange")
class TestClass02:
    """
    押货换货下单
    /mgmt/inventory/dis/mortgage/exchangeOrder/mortgageExchange
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
            
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 先换后退检查")
    def test_01_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(self):
            
        searchStore = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        searchMatchedProductCodes = None # 获取所有的商品编码列表
        searchProductByCode = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        mortgageExchange = None # 后台申请添加押货换货单
        opinion = None # 后台押货换货添加审批意见
        detail_id = None # 后台押货换货单详情
        searchAuditInfo = None # 展示审批保存信息

        @allure.step("查询店铺信息")
        def step_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = {
                "storeCode": store_85, # 服务中心编号
            }             
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]

        @allure.step("获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 4, 
            }             
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_03_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("获取所有匹配的商品编码列表")
        def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
            
            nonlocal searchMatchedProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchMatchedProductCodes = r.json()["data"]

        @allure.step("按商品编码精确查询商品")
        def step_mgmt_inventory_dis_mortgage_common_searchProductByCode():
            
            nonlocal searchProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductByCode = r.json()["data"]

        @allure.step("押货换货下单")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
            
            nonlocal mortgageExchange
            data = {
                "storeCode": store_85,
                "exchangeType": 1, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemark": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemark": "我是二级原因的备注信息哦", # 二级原因备注
                "productList": [
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12346", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "过期了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12347", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "破损了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 3 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12348", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "发霉了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 4 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    ],
                "files": [ 
                    {
                        "fileUrl": uploads[0]["fileUrlKey"],
                        "fileName": uploads[0]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[1]["fileUrlKey"],
                        "fileName": uploads[1]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[2]["fileUrlKey"],
                        "fileName": uploads[2]['relativePath'].split('/')[-1]
                    }
                ] # 换货单附件，支持3个
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                mortgageExchange = r.json()["data"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
            
            nonlocal opinion
            data = {
                "orderId": mortgageExchange, # 押货或售后单id
                "content": "业务部门同意押货只换不退" # 审批内容
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                opinion = r.json()["data"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo        
            with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("详情")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
            
            nonlocal detail_id
            params = {
                "id": mortgageExchange, # 押货或售后单id
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                detail_id = r.json()["data"]

        @allure.step("上传商品图片")
        def step_04_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/审批01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
            
            data = {
                "id": detail_id["id"],
                "exchangeType": detail_id["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemark": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditResult": "1", # 审批意见 0不通过 1通过
                "disposalType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": detail_id["reasonFirst"], # 一级原因
                "reasonFirstRemark": detail_id["reasonFirstRemark"], # 一级原因备注
                "reasonSecond": detail_id["reasonSecond"], # 二级原因
                "reasonSecondRemark": detail_id["reasonSecondRemark"], # 二级原因备注
                "productList": [{
                    "id": detail_id["products"][0]["id"],
                    "exchangeNum": detail_id["products"][0]["exchangeNum"], # 数量
                    "dailyUseType": detail_id["products"][0]["dailyUseType"], # 日常使用时间 1早上 2中午 3晚上
                    "firstUseTime": detail_id["products"][0]["firstUseTime"], # 第一次使用的时间
                    "happenType": detail_id["products"][0]["happenType"], # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "productBatch": detail_id["products"][0]["productBatch"], # 批次号
                    "problemDesc": detail_id["products"][0]["problemDesc"], # 问题描述
                    "productionDate": detail_id["products"][0]["productionDate"], # 物品生产日期
                    "productSn": detail_id["products"][0]["productSn"], # 物品序列号/二维码
                    "disposalType": detail_id["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    "productCode": detail_id["products"][0]["productCode"] # 商品编号
                }],
                "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_06_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_07_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("退回")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "expressAmount": 0, # 物流金额
                "expressCompany": "", # 快递公司
                "expressNo": "", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemark": "这是我的报废凭证，请过目", # 退回说明
                "returnType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }      
            with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
 
        @allure.step("上传商品图片")
        def step_08_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_09_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_10_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
            
            data = {
                "expressSubsidy": 0, # 运费补贴
                "inspectRemark": "仓库验货部门验货没问题", # 验货备注
                "inspectResult": "1", # 验货结果 0不通过 1通过
                "orderId": detail_id["id"],
                "inspectProofUrl": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']]
            }       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("发货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            } 
            with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("确认收货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
            }  
            with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_common_searchProductByCode()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
       
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 秒换检查")
    def test_02_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(self):
            
        searchStore = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        searchMatchedProductCodes = None # 获取所有的商品编码列表
        searchProductByCode = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        mortgageExchange = None # 后台申请添加押货换货单
        opinion = None # 后台押货换货添加审批意见
        detail_id = None # 后台押货换货单详情
        searchAuditInfo = None # 展示审批保存信息

        @allure.step("查询店铺信息")
        def step_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = {
                "storeCode": store_85, # 服务中心编号
            }             
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]

        @allure.step("获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 4, 
            }             
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_03_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("获取所有匹配的商品编码列表")
        def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
            
            nonlocal searchMatchedProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchMatchedProductCodes = r.json()["data"]

        @allure.step("按商品编码精确查询商品")
        def step_mgmt_inventory_dis_mortgage_common_searchProductByCode():
            
            nonlocal searchProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductByCode = r.json()["data"]

        @allure.step("押货换货下单")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
            
            nonlocal mortgageExchange
            data = {
                "storeCode": store_85,
                "exchangeType": 2, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemark": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemark": "我是二级原因的备注信息哦", # 二级原因备注
                "productList": [
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12346", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "过期了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12347", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "破损了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 3 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12348", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "发霉了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 4 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    ],
                "files": [ 
                    {
                        "fileUrl": uploads[0]["fileUrlKey"],
                        "fileName": uploads[0]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[1]["fileUrlKey"],
                        "fileName": uploads[1]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[2]["fileUrlKey"],
                        "fileName": uploads[2]['relativePath'].split('/')[-1]
                    }
                ] # 换货单附件，支持3个
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                mortgageExchange = r.json()["data"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
            
            nonlocal opinion
            data = {
                "orderId": mortgageExchange, # 押货或售后单id
                "content": "业务部门同意押货只换不退" # 审批内容
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                opinion = r.json()["data"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo        
            with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("详情")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
            
            nonlocal detail_id
            params = {
                "id": mortgageExchange, # 押货或售后单id
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                detail_id = r.json()["data"]

        @allure.step("上传商品图片")
        def step_04_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/审批01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
            
            data = {
                "id": detail_id["id"],
                "exchangeType": detail_id["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemark": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditResult": "1", # 审批意见 0不通过 1通过
                "disposalType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": detail_id["reasonFirst"], # 一级原因
                "reasonFirstRemark": detail_id["reasonFirstRemark"], # 一级原因备注
                "reasonSecond": detail_id["reasonSecond"], # 二级原因
                "reasonSecondRemark": detail_id["reasonSecondRemark"], # 二级原因备注
                "productList": [{
                    "id": detail_id["products"][0]["id"],
                    "exchangeNum": detail_id["products"][0]["exchangeNum"], # 数量
                    "dailyUseType": detail_id["products"][0]["dailyUseType"], # 日常使用时间 1早上 2中午 3晚上
                    "firstUseTime": detail_id["products"][0]["firstUseTime"], # 第一次使用的时间
                    "happenType": detail_id["products"][0]["happenType"], # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "productBatch": detail_id["products"][0]["productBatch"], # 批次号
                    "problemDesc": detail_id["products"][0]["problemDesc"], # 问题描述
                    "productionDate": detail_id["products"][0]["productionDate"], # 物品生产日期
                    "productSn": detail_id["products"][0]["productSn"], # 物品序列号/二维码
                    "disposalType": detail_id["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    "productCode": detail_id["products"][0]["productCode"] # 商品编号
                }],
                "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_06_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_07_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("退回")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "expressAmount": 0, # 物流金额
                "expressCompany": "", # 快递公司
                "expressNo": "", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemark": "这是我的报废凭证，请过目", # 退回说明
                "returnType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }      
            with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
 
        @allure.step("上传商品图片")
        def step_08_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_09_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_10_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
            
            data = {
                "expressSubsidy": 0, # 运费补贴
                "inspectRemark": "仓库验货部门验货没问题", # 验货备注
                "inspectResult": "1", # 验货结果 0不通过 1通过
                "orderId": detail_id["id"],
                "inspectProofUrl": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']]
            }       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("发货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            } 
            with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("确认收货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
            }  
            with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_common_searchProductByCode()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
           
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 只换不退检查")
    def test_03_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(self):
            
        searchStore = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        searchMatchedProductCodes = None # 获取所有的商品编码列表
        searchProductByCode = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        mortgageExchange = None # 后台申请添加押货换货单
        opinion = None # 后台押货换货添加审批意见
        detail_id = None # 后台押货换货单详情
        searchAuditInfo = None # 展示审批保存信息

        @allure.step("查询店铺信息")
        def step_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = {
                "storeCode": store_85, # 服务中心编号
            }             
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]

        @allure.step("获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 4, 
            }             
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_03_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("获取所有匹配的商品编码列表")
        def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
            
            nonlocal searchMatchedProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchMatchedProductCodes = r.json()["data"]

        @allure.step("按商品编码精确查询商品")
        def step_mgmt_inventory_dis_mortgage_common_searchProductByCode():
            
            nonlocal searchProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductByCode = r.json()["data"]

        @allure.step("押货换货下单")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
            
            nonlocal mortgageExchange
            data = {
                "storeCode": store_85,
                "exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemark": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemark": "我是二级原因的备注信息哦", # 二级原因备注
                "productList": [
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12346", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "过期了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12347", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "破损了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12348", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "发霉了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    ],
                "files": [ 
                    {
                        "fileUrl": uploads[0]["fileUrlKey"],
                        "fileName": uploads[0]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[1]["fileUrlKey"],
                        "fileName": uploads[1]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[2]["fileUrlKey"],
                        "fileName": uploads[2]['relativePath'].split('/')[-1]
                    }
                ] # 换货单附件，支持3个
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                mortgageExchange = r.json()["data"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
            
            nonlocal opinion
            data = {
                "orderId": mortgageExchange, # 押货或售后单id
                "content": "业务部门同意押货只换不退" # 审批内容
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                opinion = r.json()["data"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo        
            with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("详情")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
            
            nonlocal detail_id
            params = {
                "id": mortgageExchange, # 押货或售后单id
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                detail_id = r.json()["data"]

        @allure.step("上传商品图片")
        def step_04_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/审批01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
            
            data = {
                "id": detail_id["id"],
                "exchangeType": detail_id["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemark": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditResult": "1", # 审批意见 0不通过 1通过
                "disposalType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": detail_id["reasonFirst"], # 一级原因
                "reasonFirstRemark": detail_id["reasonFirstRemark"], # 一级原因备注
                "reasonSecond": detail_id["reasonSecond"], # 二级原因
                "reasonSecondRemark": detail_id["reasonSecondRemark"], # 二级原因备注
                "productList": [{
                    "id": detail_id["products"][0]["id"],
                    "exchangeNum": detail_id["products"][0]["exchangeNum"], # 数量
                    "dailyUseType": detail_id["products"][0]["dailyUseType"], # 日常使用时间 1早上 2中午 3晚上
                    "firstUseTime": detail_id["products"][0]["firstUseTime"], # 第一次使用的时间
                    "happenType": detail_id["products"][0]["happenType"], # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "productBatch": detail_id["products"][0]["productBatch"], # 批次号
                    "problemDesc": detail_id["products"][0]["problemDesc"], # 问题描述
                    "productionDate": detail_id["products"][0]["productionDate"], # 物品生产日期
                    "productSn": detail_id["products"][0]["productSn"], # 物品序列号/二维码
                    "disposalType": detail_id["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    "productCode": detail_id["products"][0]["productCode"] # 商品编号
                }],
                "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_06_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_07_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("退回")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "expressAmount": 0, # 物流金额
                "expressCompany": "", # 快递公司
                "expressNo": "", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemark": "这是我的报废凭证，请过目", # 退回说明
                "returnType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }      
            with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
 
        @allure.step("上传商品图片")
        def step_08_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_09_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_10_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
            
            data = {
                "expressSubsidy": 0, # 运费补贴
                "inspectRemark": "仓库验货部门验货没问题", # 验货备注
                "inspectResult": "1", # 验货结果 0不通过 1通过
                "orderId": detail_id["id"],
                "inspectProofUrl": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']]
            }       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("发货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            } 
            with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("确认收货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
            }  
            with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_common_searchProductByCode()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
        
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 先换后退检查")
    def test_04_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(self):
            
        searchStore = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        searchMatchedProductCodes = None # 获取所有的商品编码列表
        searchProductByCode = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        mortgageExchange = None # 后台申请添加押货换货单
        opinion = None # 后台押货换货添加审批意见
        detail_id = None # 后台押货换货单详情
        searchAuditInfo = None # 展示审批保存信息

        @allure.step("查询店铺信息")
        def step_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = {
                "storeCode": store_85, # 服务中心编号
            }             
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]

        @allure.step("获取各种退换货原因")
        def step_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = {
                "type": 4, 
            }             
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReason = r.json()["data"]

        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_03_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/货物03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("获取所有匹配的商品编码列表")
        def step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes():
            
            nonlocal searchMatchedProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchMatchedProductCodes = r.json()["data"]

        @allure.step("按商品编码精确查询商品")
        def step_mgmt_inventory_dis_mortgage_common_searchProductByCode():
            
            nonlocal searchProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_dis_mortgage_common_searchProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchProductByCode = r.json()["data"]

        @allure.step("押货换货下单")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange():
            
            nonlocal mortgageExchange
            data = {
                "storeCode": store_85,
                "exchangeType": 4, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemark": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemark": "我是二级原因的备注信息哦", # 二级原因备注
                "productList": [
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12346", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "过期了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12347", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "破损了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 3 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    {
                    "productCode": searchProductByCode["productCode"], # 商品编号
                    "productName": searchProductByCode["productName"],
                    "packing": searchProductByCode["retailPrice"],
                    "unit": searchProductByCode["unit"],
                    "retailPrice": searchProductByCode["retailPrice"], # 零售价
                    "exchangeNum": productNum, # 数量
                    "productionDate": "20220101", # 物品生产日期
                    "productBatch": "12348", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "problemDesc": "发霉了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "mortgagePrice": searchProductByCode["mortgagePrice"], # 85折押货价
                    "disposalType": 4 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓 4分公司自行处理
                    },
                    ],
                "files": [ 
                    {
                        "fileUrl": uploads[0]["fileUrlKey"],
                        "fileName": uploads[0]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[1]["fileUrlKey"],
                        "fileName": uploads[1]['relativePath'].split('/')[-1]
                    },
                    {
                        "fileUrl": uploads[2]["fileUrlKey"],
                        "fileName": uploads[2]['relativePath'].split('/')[-1]
                    }
                ] # 换货单附件，支持3个
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                mortgageExchange = r.json()["data"]

        @allure.step("添加审批意见")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_opinion():
            
            nonlocal opinion
            data = {
                "orderId": mortgageExchange, # 押货或售后单id
                "content": "业务部门同意押货只换不退" # 审批内容
            }           
            with _mgmt_inventory_dis_mortgage_exchangeOrder_opinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                opinion = r.json()["data"]

        @allure.step("展示审批保存信息")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo():
            
            nonlocal searchAuditInfo        
            with _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                searchAuditInfo = r.json()["data"]["returnAddress"]

        @allure.step("详情")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_detail_id():
            
            nonlocal detail_id
            params = {
                "id": mortgageExchange, # 押货或售后单id
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                detail_id = r.json()["data"]

        @allure.step("上传商品图片")
        def step_04_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/审批01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("审批")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_audit():
            
            data = {
                "id": detail_id["id"],
                "exchangeType": detail_id["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemark": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditResult": "1", # 审批意见 0不通过 1通过
                "disposalType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": detail_id["reasonFirst"], # 一级原因
                "reasonFirstRemark": detail_id["reasonFirstRemark"], # 一级原因备注
                "reasonSecond": detail_id["reasonSecond"], # 二级原因
                "reasonSecondRemark": detail_id["reasonSecondRemark"], # 二级原因备注
                "productList": [{
                    "id": detail_id["products"][0]["id"],
                    "exchangeNum": detail_id["products"][0]["exchangeNum"], # 数量
                    "dailyUseType": detail_id["products"][0]["dailyUseType"], # 日常使用时间 1早上 2中午 3晚上
                    "firstUseTime": detail_id["products"][0]["firstUseTime"], # 第一次使用的时间
                    "happenType": detail_id["products"][0]["happenType"], # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "productBatch": detail_id["products"][0]["productBatch"], # 批次号
                    "problemDesc": detail_id["products"][0]["problemDesc"], # 问题描述
                    "productionDate": detail_id["products"][0]["productionDate"], # 物品生产日期
                    "productSn": detail_id["products"][0]["productSn"], # 物品序列号/二维码
                    "disposalType": detail_id["products"][0]["disposalType"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    "productCode": detail_id["products"][0]["productCode"] # 商品编号
                }],
                "returnAddress": searchAuditInfo if searchAuditInfo else "广州仓" # 退回地址信息
            }          
            with _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_06_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_07_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("退回")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_process():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "expressAmount": 0, # 物流金额
                "expressCompany": "", # 快递公司
                "expressNo": "", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemark": "这是我的报废凭证，请过目", # 退回说明
                "returnType": f'{detail_id["exchangeOrderReturnTypePairs"][0]["type"]}', # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }      
            with _mgmt_inventory_dis_mortgage_exchangeOrder_process(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
 
        @allure.step("上传商品图片")
        def step_08_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货01.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_09_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货02.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("上传商品图片")
        def step_10_storage_upload():
            
            nonlocal uploads
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/验货03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("验货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_inspect():
            
            data = {
                "expressSubsidy": 0, # 运费补贴
                "inspectRemark": "仓库验货部门验货没问题", # 验货备注
                "inspectResult": "1", # 验货结果 0不通过 1通过
                "orderId": detail_id["id"],
                "inspectProofUrl": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']]
            }       
            with _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("发货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_deliver():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            } 
            with _mgmt_inventory_dis_mortgage_exchangeOrder_deliver(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("确认收货")
        def step_mgmt_inventory_dis_mortgage_exchangeOrder_confirm():
            
            data = {
                "orderId": detail_id["id"], # 换货单id
            }  
            with _mgmt_inventory_dis_mortgage_exchangeOrder_confirm(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes()
        step_mgmt_inventory_dis_mortgage_common_searchProductByCode()
        step_mgmt_inventory_dis_mortgage_exchangeOrder_mortgageExchange()
        
     
    
    
    
    
    
    
    
    
    
    






