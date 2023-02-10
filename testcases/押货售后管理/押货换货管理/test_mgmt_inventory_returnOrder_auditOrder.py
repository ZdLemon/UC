# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getStoreSimpleInfo import _mgmt_inventory_common_getStoreSimpleInfo # 获取服务中心简单信息
from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 获取各种退换货原因
from api.basic_services._storage_upload import _storage_upload # 上传商品图片
from api.mall_mgmt_application._mgmt_inventory_common_getAllProductCodes import _mgmt_inventory_common_getAllProductCodes # 获取所有的商品编码列表
from api.mall_mgmt_application._mgmt_inventory_common_getProductByCode import _mgmt_inventory_common_getProductByCode # 根据一或二级编码精确商品信息
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_addMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder # 后台申请添加押货换货单
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_addOpinion import _mgmt_inventory_exchangeOrder_addOpinion # 后台押货换货添加审批意见
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_exchangeOrderDetail import _mgmt_inventory_exchangeOrder_exchangeOrderDetail # 后台押货换货单详情
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder # 后台审批押货换货单
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_processMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder # 后台押货换货单退回处理
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder # 后台押货换货单验货
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder # 后台押货换货单发货
from api.mall_mgmt_application._mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder import _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder # 后台押货换确认收货

from setting import P1, P2, P3, productCode_zh, productCode, store, AG

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/exchangeOrder/addMortgageExchangeOrder")
class TestClass:
    """
    后台申请添加押货换货单
    /mgmt/inventory/exchangeOrder/addMortgageExchangeOrder
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
            
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 只换不退主路径检查")
    def test_01_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(self):
            
        getStoreSimpleInfo = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        getAllProductCodes = None # 获取所有的商品编码列表
        getProductByCode = None # 根据一或二级编码精确商品信息
        getProductByCode02 = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        addMortgageExchangeOrder = None # 后台申请添加押货换货单
        addOpinion = None # 后台押货换货添加审批意见
        exchangeOrderDetail = None # 后台押货换货单详情

        @allure.step("获取服务中心简单信息")
        def step_mgmt_inventory_common_getStoreSimpleInfo():
            
            nonlocal getStoreSimpleInfo
            params = {
                "storeCode": store, # 服务中心编号
            }             
            with _mgmt_inventory_common_getStoreSimpleInfo(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreSimpleInfo = r.json()["data"]

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

        @allure.step("获取所有的商品编码列表")
        def step_mgmt_inventory_common_getAllProductCodes():
            
            nonlocal getAllProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getAllProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAllProductCodes = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_02_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode02
            params = {
                "productCode": AG, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode02 = r.json()["data"]

        @allure.step("后台申请添加押货换货单")
        def step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder():
            
            nonlocal addMortgageExchangeOrder
            data = {
                "storeCode": store,
                "exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "orderFileUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}", # 换货单附件，支持3个，用逗号隔开
                "productDisposalType": "", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemarks": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemarks": "我是二级原因的备注信息哦", # 二级原因备注
                "productVoList": [
                    {
                        "productCode": getProductByCode["productCode"], # 物品编号
                        "title": getProductByCode["productName"],
                        "packing": getProductByCode["productPacking"],
                        "meterUnit": getProductByCode["productUnit"],
                        "retailPrice": getProductByCode["retailPrice"], # 物品零售价
                        "productNum": productNum, # 物品换货数
                        "productProductionDate": "20220101", # 物品生产日期
                        "productBatch": "12345", # 批次号
                        "productSn": "", # 物品序列号/二维码
                        "productProblemDesc": "进水了", # 问题描述
                        "firstUseTime": "", # 第一次使用的时间
                        "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                        "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                        "securityPrice": 20,
                        "productDisposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    },
                    {
                        "productCode": getProductByCode02["productCode"], # 物品编号
                        "title": getProductByCode02["productName"],
                        "packing": getProductByCode02["productPacking"],
                        "meterUnit": getProductByCode02["productUnit"],
                        "retailPrice": getProductByCode02["retailPrice"], # 物品零售价
                        "productNum": productNum, # 物品换货数
                        "productProductionDate": "20220101", # 物品生产日期
                        "productBatch": "12345", # 批次号
                        "productSn": "", # 物品序列号/二维码
                        "productProblemDesc": "进水了", # 问题描述
                        "firstUseTime": "", # 第一次使用的时间
                        "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                        "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                        "securityPrice": 20,
                        "productDisposalType": 1 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                    },
                    ],
                "orderFileName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}" # 换货单附件名，支持3个，用逗号隔开
            }           
            with _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addMortgageExchangeOrder = r.json()["data"]

        @allure.step("后台押货换货添加审批意见")
        def step_mgmt_inventory_exchangeOrder_addOpinion():
            
            nonlocal addOpinion
            data = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
                "content": "业务部门同意押货只换不退" # 审批内容
            }           
            with _mgmt_inventory_exchangeOrder_addOpinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addOpinion = r.json()["data"]

        @allure.step("后台押货换货单详情")
        def step_mgmt_inventory_exchangeOrder_exchangeOrderDetail():
            
            nonlocal exchangeOrderDetail
            params = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
            }          
            with _mgmt_inventory_exchangeOrder_exchangeOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                exchangeOrderDetail = r.json()["data"]

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

        @allure.step("后台审批押货换货单")
        def step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"],
                "exchangeType": exchangeOrderDetail["orderVo"]["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemarks": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditStatus": "1", # 审批意见 0不通过 1通过
                "productDisposalType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": exchangeOrderDetail["orderVo"]["reasonFirst"], # 一级原因
                "reasonFirstRemarks": exchangeOrderDetail["orderVo"]["reasonFirstRemarks"], # 一级原因备注
                "reasonSecond": exchangeOrderDetail["orderVo"]["reasonSecond"], # 二级原因
                "reasonSecondRemarks": exchangeOrderDetail["orderVo"]["reasonSecondRemarks"], # 二级原因备注
                "productVoList": [{
                    "id": exchangeOrderDetail["productVos"][0]["id"], # 物品记录id
                    "productNum": exchangeOrderDetail["productVos"][0]["productNum"], # 物品换货数
                    "dailyUseType": exchangeOrderDetail["productVos"][0]["dailyUseType"],
                    "firstUseTime": exchangeOrderDetail["productVos"][0]["firstUseTime"],
                    "happenType": exchangeOrderDetail["productVos"][0]["happenType"],
                    "productBatch": exchangeOrderDetail["productVos"][0]["productBatch"], # 批次号
                    "productProblemDesc": exchangeOrderDetail["productVos"][0]["productProblemDesc"], # 问题描述
                    "productProductionDate": exchangeOrderDetail["productVos"][0]["productProductionDate"], # 物品生产日期
                    "productSn": exchangeOrderDetail["productVos"][0]["productSn"], # 物品序列号/二维码
                    "productDisposalType": exchangeOrderDetail["productVos"][0]["productDisposalType"] # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "returnInfo": exchangeOrderDetail["orderVo"]["returnAddress"] if exchangeOrderDetail["orderVo"]["returnAddress"] else "广州仓" # 退回信息
            }          
            with _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder(data, self.access_token) as r:
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

        @allure.step("后台押货换货单退回处理")
        def step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "expressAmount": 0, # 物流金额
                "expressCompany": "", # 快递公司
                "expressNo": "", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemarks": "这是我的报废图片", # 退回说明
                "returnType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }         
            with _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder(data, self.access_token) as r:
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

        @allure.step("后台押货换货单验货")
        def step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder():
            
            data = {
                "expressSubsidy": 0, # 运费补贴
                "inspectRemarks": "仓库验货部门验货没问题", # 验货备注
                "inspectStatus": "1", # 验货结果 0不通过 1通过
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "inspectProof": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']] # 验货凭证
            }         
            with _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换货单发货")
        def step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            }  
            with _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换确认收货")
        def step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            }  
            with _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_common_getStoreSimpleInfo()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_common_getAllProductCodes()
        step_mgmt_inventory_common_getProductByCode()
        step_02_mgmt_inventory_common_getProductByCode()
        step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder()
        # 待审批
        step_mgmt_inventory_exchangeOrder_addOpinion()
        step_mgmt_inventory_exchangeOrder_exchangeOrderDetail()
        step_04_storage_upload()
        step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder()
        # 待报废
        step_05_storage_upload()
        step_06_storage_upload()
        step_07_storage_upload()
        step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder()
        # 待验货
        step_08_storage_upload()
        step_09_storage_upload()
        step_10_storage_upload()
        step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder()
        # 待发货
        step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder()
        # 确认收货
        step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder()
        
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 先退后换主路径检查")
    def test_02_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(self):
            
        getStoreSimpleInfo = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        getAllProductCodes = None # 获取所有的商品编码列表
        getProductByCode = None # 根据一或二级编码精确商品信息
        getProductByCode02 = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        addMortgageExchangeOrder = None # 后台申请添加押货换货单
        addOpinion = None # 后台押货换货添加审批意见
        exchangeOrderDetail = None # 后台押货换货单详情

        @allure.step("获取服务中心简单信息")
        def step_mgmt_inventory_common_getStoreSimpleInfo():
            
            nonlocal getStoreSimpleInfo
            params = {
                "storeCode": store, # 服务中心编号
            }             
            with _mgmt_inventory_common_getStoreSimpleInfo(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreSimpleInfo = r.json()["data"]

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

        @allure.step("获取所有的商品编码列表")
        def step_mgmt_inventory_common_getAllProductCodes():
            
            nonlocal getAllProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getAllProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAllProductCodes = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_02_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode02
            params = {
                "productCode": AG, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode02 = r.json()["data"]

        @allure.step("后台申请添加押货换货单")
        def step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder():
            
            nonlocal addMortgageExchangeOrder
            data = {
                "storeCode": store,
                "exchangeType": 1, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "orderFileUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}", # 换货单附件，支持3个，用逗号隔开
                "productDisposalType": "", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemarks": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemarks": "我是二级原因的备注信息哦", # 二级原因备注
                "productVoList": [{
                    "productCode": getProductByCode["productCode"], # 物品编号
                    "title": getProductByCode["productName"],
                    "packing": getProductByCode["productPacking"],
                    "meterUnit": getProductByCode["productUnit"],
                    "retailPrice": getProductByCode["retailPrice"], # 物品零售价
                    "productNum": productNum, # 物品换货数
                    "productProductionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "productProblemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "securityPrice": 20,
                    "productDisposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "orderFileName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}" # 换货单附件名，支持3个，用逗号隔开
            }           
            with _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addMortgageExchangeOrder = r.json()["data"]

        @allure.step("后台押货换货添加审批意见")
        def step_mgmt_inventory_exchangeOrder_addOpinion():
            
            nonlocal addOpinion
            data = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
                "content": "业务部门同意押货先退后换" # 审批内容
            }           
            with _mgmt_inventory_exchangeOrder_addOpinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addOpinion = r.json()["data"]

        @allure.step("后台押货换货单详情")
        def step_mgmt_inventory_exchangeOrder_exchangeOrderDetail():
            
            nonlocal exchangeOrderDetail
            params = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
            }          
            with _mgmt_inventory_exchangeOrder_exchangeOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                exchangeOrderDetail = r.json()["data"]

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

        @allure.step("后台审批押货换货单")
        def step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"],
                "exchangeType": exchangeOrderDetail["orderVo"]["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemarks": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditStatus": "1", # 审批意见 0不通过 1通过
                "productDisposalType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": exchangeOrderDetail["orderVo"]["reasonFirst"], # 一级原因
                "reasonFirstRemarks": exchangeOrderDetail["orderVo"]["reasonFirstRemarks"], # 一级原因备注
                "reasonSecond": exchangeOrderDetail["orderVo"]["reasonSecond"], # 二级原因
                "reasonSecondRemarks": exchangeOrderDetail["orderVo"]["reasonSecondRemarks"], # 二级原因备注
                "productVoList": [{
                    "id": exchangeOrderDetail["productVos"][0]["id"], # 物品记录id
                    "productNum": exchangeOrderDetail["productVos"][0]["productNum"], # 物品换货数
                    "dailyUseType": exchangeOrderDetail["productVos"][0]["dailyUseType"],
                    "firstUseTime": exchangeOrderDetail["productVos"][0]["firstUseTime"],
                    "happenType": exchangeOrderDetail["productVos"][0]["happenType"],
                    "productBatch": exchangeOrderDetail["productVos"][0]["productBatch"], # 批次号
                    "productProblemDesc": exchangeOrderDetail["productVos"][0]["productProblemDesc"], # 问题描述
                    "productProductionDate": exchangeOrderDetail["productVos"][0]["productProductionDate"], # 物品生产日期
                    "productSn": exchangeOrderDetail["productVos"][0]["productSn"], # 物品序列号/二维码
                    "productDisposalType": exchangeOrderDetail["productVos"][0]["productDisposalType"] # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "returnInfo": exchangeOrderDetail["orderVo"]["returnAddress"] if exchangeOrderDetail["orderVo"]["returnAddress"] else "广州仓" # 退回信息
            }          
            with _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回快递单01.jpg"
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
                "file": "data/退回快递单02.jpg"
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
                "file": "data/退回快递单03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("后台押货换货单退回处理")
        def step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "expressAmount": 100, # 物流金额
                "expressCompany": "小河物流", # 快递公司
                "expressNo": "xh123456789", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemarks": "这是我的报废图片", # 退回说明
                "returnType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }         
            with _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder(data, self.access_token) as r:
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

        @allure.step("后台押货换货单验货")
        def step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder():
            
            data = {
                "expressSubsidy": 100, # 运费补贴
                "inspectRemarks": "仓库验货部门验货没问题", # 验货备注
                "inspectStatus": "1", # 验货结果 0不通过 1通过
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "inspectProof": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']] # 验货凭证
            }         
            with _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换货单发货")
        def step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            }  
            with _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换确认收货")
        def step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            }  
            with _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_common_getStoreSimpleInfo()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_common_getAllProductCodes()
        step_mgmt_inventory_common_getProductByCode()
        step_02_mgmt_inventory_common_getProductByCode()
        step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder()
        # 待审批
        step_mgmt_inventory_exchangeOrder_addOpinion()
        step_mgmt_inventory_exchangeOrder_exchangeOrderDetail()
        step_04_storage_upload()
        step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder()
        # 待退回
        step_05_storage_upload()
        step_06_storage_upload()
        step_07_storage_upload()
        step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder()
        # 待验货
        step_08_storage_upload()
        step_09_storage_upload()
        step_10_storage_upload()
        step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder()
        # 待发货
        step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder()
        # 确认收货
        step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder()
        
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 秒换主路径检查")
    def test_03_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(self):
            
        getStoreSimpleInfo = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        getAllProductCodes = None # 获取所有的商品编码列表
        getProductByCode = None # 根据一或二级编码精确商品信息
        getProductByCode02 = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        addMortgageExchangeOrder = None # 后台申请添加押货换货单
        addOpinion = None # 后台押货换货添加审批意见
        exchangeOrderDetail = None # 后台押货换货单详情

        @allure.step("获取服务中心简单信息")
        def step_mgmt_inventory_common_getStoreSimpleInfo():
            
            nonlocal getStoreSimpleInfo
            params = {
                "storeCode": store, # 服务中心编号
            }             
            with _mgmt_inventory_common_getStoreSimpleInfo(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreSimpleInfo = r.json()["data"]

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

        @allure.step("获取所有的商品编码列表")
        def step_mgmt_inventory_common_getAllProductCodes():
            
            nonlocal getAllProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getAllProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAllProductCodes = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_02_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode02
            params = {
                "productCode": AG, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode02 = r.json()["data"]

        @allure.step("后台申请添加押货换货单")
        def step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder():
            
            nonlocal addMortgageExchangeOrder
            data = {
                "storeCode": store,
                "exchangeType": 2, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "orderFileUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}", # 换货单附件，支持3个，用逗号隔开
                "productDisposalType": "", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemarks": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemarks": "我是二级原因的备注信息哦", # 二级原因备注
                "productVoList": [{
                    "productCode": getProductByCode["productCode"], # 物品编号
                    "title": getProductByCode["productName"],
                    "packing": getProductByCode["productPacking"],
                    "meterUnit": getProductByCode["productUnit"],
                    "retailPrice": getProductByCode["retailPrice"], # 物品零售价
                    "productNum": productNum, # 物品换货数
                    "productProductionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "productProblemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "securityPrice": 20,
                    "productDisposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "orderFileName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}" # 换货单附件名，支持3个，用逗号隔开
            }           
            with _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addMortgageExchangeOrder = r.json()["data"]

        @allure.step("后台押货换货添加审批意见")
        def step_mgmt_inventory_exchangeOrder_addOpinion():
            
            nonlocal addOpinion
            data = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
                "content": "业务部门同意押货先退后换" # 审批内容
            }           
            with _mgmt_inventory_exchangeOrder_addOpinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addOpinion = r.json()["data"]

        @allure.step("后台押货换货单详情")
        def step_mgmt_inventory_exchangeOrder_exchangeOrderDetail():
            
            nonlocal exchangeOrderDetail
            params = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
            }          
            with _mgmt_inventory_exchangeOrder_exchangeOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                exchangeOrderDetail = r.json()["data"]

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

        @allure.step("后台审批押货换货单")
        def step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"],
                "exchangeType": exchangeOrderDetail["orderVo"]["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemarks": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditStatus": "1", # 审批意见 0不通过 1通过
                "productDisposalType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": exchangeOrderDetail["orderVo"]["reasonFirst"], # 一级原因
                "reasonFirstRemarks": exchangeOrderDetail["orderVo"]["reasonFirstRemarks"], # 一级原因备注
                "reasonSecond": exchangeOrderDetail["orderVo"]["reasonSecond"], # 二级原因
                "reasonSecondRemarks": exchangeOrderDetail["orderVo"]["reasonSecondRemarks"], # 二级原因备注
                "productVoList": [{
                    "id": exchangeOrderDetail["productVos"][0]["id"], # 物品记录id
                    "productNum": exchangeOrderDetail["productVos"][0]["productNum"], # 物品换货数
                    "dailyUseType": exchangeOrderDetail["productVos"][0]["dailyUseType"],
                    "firstUseTime": exchangeOrderDetail["productVos"][0]["firstUseTime"],
                    "happenType": exchangeOrderDetail["productVos"][0]["happenType"],
                    "productBatch": exchangeOrderDetail["productVos"][0]["productBatch"], # 批次号
                    "productProblemDesc": exchangeOrderDetail["productVos"][0]["productProblemDesc"], # 问题描述
                    "productProductionDate": exchangeOrderDetail["productVos"][0]["productProductionDate"], # 物品生产日期
                    "productSn": exchangeOrderDetail["productVos"][0]["productSn"], # 物品序列号/二维码
                    "productDisposalType": exchangeOrderDetail["productVos"][0]["productDisposalType"] # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "returnInfo": exchangeOrderDetail["orderVo"]["returnAddress"] if exchangeOrderDetail["orderVo"]["returnAddress"] else "广州仓" # 退回信息
            }          
            with _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回快递单01.jpg"
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
                "file": "data/退回快递单02.jpg"
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
                "file": "data/退回快递单03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("后台押货换货单退回处理")
        def step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "expressAmount": 100, # 物流金额
                "expressCompany": "小河物流", # 快递公司
                "expressNo": "xh123456789", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemarks": "这是我的报废图片", # 退回说明
                "returnType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }         
            with _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder(data, self.access_token) as r:
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

        @allure.step("后台押货换货单验货")
        def step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder():
            
            data = {
                "expressSubsidy": 100, # 运费补贴
                "inspectRemarks": "仓库验货部门验货没问题", # 验货备注
                "inspectStatus": "1", # 验货结果 0不通过 1通过
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "inspectProof": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']] # 验货凭证
            }         
            with _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换货单发货")
        def step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            }  
            with _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换确认收货")
        def step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            }  
            with _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_common_getStoreSimpleInfo()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_common_getAllProductCodes()
        step_mgmt_inventory_common_getProductByCode()
        step_02_mgmt_inventory_common_getProductByCode()
        step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder()
        # 待审批
        step_mgmt_inventory_exchangeOrder_addOpinion()
        step_mgmt_inventory_exchangeOrder_exchangeOrderDetail()
        step_04_storage_upload()
        step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder()
        # 待退回
        step_05_storage_upload()
        step_06_storage_upload()
        step_07_storage_upload()
        step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder()
        # 待发货
        step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder()
        # 待验货
        step_08_storage_upload()
        step_09_storage_upload()
        step_10_storage_upload()
        step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder()
        # 确认收货
        step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder()
        
    @allure.severity(P1)
    @allure.title("后台申请添加押货换货单-成功路径: 先换后退主路径检查")
    def test_04_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(self):
            
        getStoreSimpleInfo = None # 获取服务中心简单信息
        getReason = None # 获取各种退换货原因
        uploads = [] # 上传商品图片
        getAllProductCodes = None # 获取所有的商品编码列表
        getProductByCode = None # 根据一或二级编码精确商品信息
        getProductByCode02 = None # 根据一或二级编码精确商品信息
        productNum = 2 # 押货退货数量
        addMortgageExchangeOrder = None # 后台申请添加押货换货单
        addOpinion = None # 后台押货换货添加审批意见
        exchangeOrderDetail = None # 后台押货换货单详情

        @allure.step("获取服务中心简单信息")
        def step_mgmt_inventory_common_getStoreSimpleInfo():
            
            nonlocal getStoreSimpleInfo
            params = {
                "storeCode": store, # 服务中心编号
            }             
            with _mgmt_inventory_common_getStoreSimpleInfo(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getStoreSimpleInfo = r.json()["data"]

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

        @allure.step("获取所有的商品编码列表")
        def step_mgmt_inventory_common_getAllProductCodes():
            
            nonlocal getAllProductCodes
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getAllProductCodes(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAllProductCodes = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode
            params = {
                "productCode": productCode, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode = r.json()["data"]

        @allure.step("根据一或二级编码精确商品信息")
        def step_02_mgmt_inventory_common_getProductByCode():
            
            nonlocal getProductByCode02
            params = {
                "productCode": AG, # 商品编码
            }              
            with _mgmt_inventory_common_getProductByCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProductByCode02 = r.json()["data"]

        @allure.step("后台申请添加押货换货单")
        def step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder():
            
            nonlocal addMortgageExchangeOrder
            data = {
                "storeCode": store,
                "exchangeType": 4, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "orderFileUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}", # 换货单附件，支持3个，用逗号隔开
                "productDisposalType": "", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": getReason[13]["returnReason"], # 一级原因
                "reasonFirstRemarks": "我是一级原因的备注信息哦", # 一级原因备注
                "reasonSecond": getReason[13]["reasonList"][2]["returnReason"], # 二级原因
                "reasonSecondRemarks": "我是二级原因的备注信息哦", # 二级原因备注
                "productVoList": [{
                    "productCode": getProductByCode["productCode"], # 物品编号
                    "title": getProductByCode["productName"],
                    "packing": getProductByCode["productPacking"],
                    "meterUnit": getProductByCode["productUnit"],
                    "retailPrice": getProductByCode["retailPrice"], # 物品零售价
                    "productNum": productNum, # 物品换货数
                    "productProductionDate": "20220101", # 物品生产日期
                    "productBatch": "12345", # 批次号
                    "productSn": "", # 物品序列号/二维码
                    "productProblemDesc": "进水了", # 问题描述
                    "firstUseTime": "", # 第一次使用的时间
                    "dailyUseType": "", # 日常使用时间 1早上 2中午 3晚上
                    "happenType": "", # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
                    "securityPrice": 20,
                    "productDisposalType": 2 # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "orderFileName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}" # 换货单附件名，支持3个，用逗号隔开
            }           
            with _mgmt_inventory_exchangeOrder_addMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addMortgageExchangeOrder = r.json()["data"]

        @allure.step("后台押货换货添加审批意见")
        def step_mgmt_inventory_exchangeOrder_addOpinion():
            
            nonlocal addOpinion
            data = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
                "content": "业务部门同意押货先退后换" # 审批内容
            }           
            with _mgmt_inventory_exchangeOrder_addOpinion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addOpinion = r.json()["data"]

        @allure.step("后台押货换货单详情")
        def step_mgmt_inventory_exchangeOrder_exchangeOrderDetail():
            
            nonlocal exchangeOrderDetail
            params = {
                "orderId": addMortgageExchangeOrder, # 押货或售后单id
            }          
            with _mgmt_inventory_exchangeOrder_exchangeOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                exchangeOrderDetail = r.json()["data"]

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

        @allure.step("后台审批押货换货单")
        def step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"],
                "exchangeType": exchangeOrderDetail["orderVo"]["exchangeType"], # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
                "auditFileUrl": f"{uploads[0]['fileUrlKey']}", # 审批附件
                "auditFileName": uploads[0]['relativePath'].split('/')[-1], # 审批附件名称
                "auditRemarks": "服务中心部门同意押货只换不退申请哦", # 审批备注
                "auditStatus": "1", # 审批意见 0不通过 1通过
                "productDisposalType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                "reasonFirst": exchangeOrderDetail["orderVo"]["reasonFirst"], # 一级原因
                "reasonFirstRemarks": exchangeOrderDetail["orderVo"]["reasonFirstRemarks"], # 一级原因备注
                "reasonSecond": exchangeOrderDetail["orderVo"]["reasonSecond"], # 二级原因
                "reasonSecondRemarks": exchangeOrderDetail["orderVo"]["reasonSecondRemarks"], # 二级原因备注
                "productVoList": [{
                    "id": exchangeOrderDetail["productVos"][0]["id"], # 物品记录id
                    "productNum": exchangeOrderDetail["productVos"][0]["productNum"], # 物品换货数
                    "dailyUseType": exchangeOrderDetail["productVos"][0]["dailyUseType"],
                    "firstUseTime": exchangeOrderDetail["productVos"][0]["firstUseTime"],
                    "happenType": exchangeOrderDetail["productVos"][0]["happenType"],
                    "productBatch": exchangeOrderDetail["productVos"][0]["productBatch"], # 批次号
                    "productProblemDesc": exchangeOrderDetail["productVos"][0]["productProblemDesc"], # 问题描述
                    "productProductionDate": exchangeOrderDetail["productVos"][0]["productProductionDate"], # 物品生产日期
                    "productSn": exchangeOrderDetail["productVos"][0]["productSn"], # 物品序列号/二维码
                    "productDisposalType": exchangeOrderDetail["productVos"][0]["productDisposalType"] # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
                }],
                "returnInfo": exchangeOrderDetail["orderVo"]["returnAddress"] if exchangeOrderDetail["orderVo"]["returnAddress"] else "广州仓" # 退回信息
            }          
            with _mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("上传商品图片")
        def step_05_storage_upload():
            
            nonlocal uploads
            uploads = []
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-inventory", # str客户端Key(由管理员进行分配)
                "file": "data/退回快递单01.jpg"
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
                "file": "data/退回快递单02.jpg"
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
                "file": "data/退回快递单03.jpg"
            }  
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                uploads.append(r.json()["datas"])

        @allure.step("后台押货换货单退回处理")
        def step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "expressAmount": 100, # 物流金额
                "expressCompany": "小河物流", # 快递公司
                "expressNo": "xh123456789", # 快递单号
                "expressProofUrl": "", # 快递凭证url
                "expressProofName": "", # 快递凭证名称
                "processRemarks": "这是我的报废图片", # 退回说明
                "returnType": exchangeOrderDetail["exchangeOrderReturnTypePairs"][0]["type"], # 退回方式 1服务中心报废 2自带 3邮寄
                "disposalProofName": f"{uploads[0]['relativePath'].split('/')[-1]},{uploads[1]['relativePath'].split('/')[-1]},{uploads[2]['relativePath'].split('/')[-1]}", # 报废凭证名称,最多9个，逗号隔开
                "disposalProofUrl": f"{uploads[0]['fileUrlKey']},{uploads[1]['fileUrlKey']},{uploads[2]['fileUrlKey']}" # 报废凭证,最多9个，逗号隔开
            }         
            with _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder(data, self.access_token) as r:
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

        @allure.step("后台押货换货单验货")
        def step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder():
            
            data = {
                "expressSubsidy": 100, # 运费补贴
                "inspectRemarks": "仓库验货部门验货没问题", # 验货备注
                "inspectStatus": "1", # 验货结果 0不通过 1通过
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "inspectProof": [uploads[0]['fileUrlKey'], uploads[1]['fileUrlKey'], uploads[2]['fileUrlKey']] # 验货凭证
            }         
            with _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换货单发货")
        def step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder():
            
            data = {
                "orderId": exchangeOrderDetail["orderVo"]["id"], # 换货单id
                "deliverTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), # 发货时间
                "deliverType": 2, # 发货方式 1顾客自提 2邮寄
                "expressCompany": "小河物流", # 新品配送物流公司
                "expressNo": "xh123456" # 物流单号
            }  
            with _mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("后台押货换确认收货")
        def step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder():
            
            data = {
                "id": exchangeOrderDetail["orderVo"]["id"], # 换货单id
            }  
            with _mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                                       
        # 新建
        step_mgmt_inventory_common_getStoreSimpleInfo()
        step_mgmt_inventory_common_getReason()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_inventory_common_getAllProductCodes()
        step_mgmt_inventory_common_getProductByCode()
        step_02_mgmt_inventory_common_getProductByCode()
        step_mgmt_inventory_exchangeOrder_addMortgageExchangeOrder()
        # 待审批
        step_mgmt_inventory_exchangeOrder_addOpinion()
        step_mgmt_inventory_exchangeOrder_exchangeOrderDetail()
        step_04_storage_upload()
        step_mgmt_inventory_exchangeOrder_auditMortgageExchangeOrder()
        # 待发货
        step_mgmt_inventory_exchangeOrder_deliverMortgageExchangeOrder()
        # 待退回
        step_05_storage_upload()
        step_06_storage_upload()
        step_07_storage_upload()
        step_mgmt_inventory_exchangeOrder_processMortgageExchangeOrder()
        # 待验货
        step_08_storage_upload()
        step_09_storage_upload()
        step_10_storage_upload()
        step_mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder()
        # 确认收货
        step_mgmt_inventory_exchangeOrder_confirmMortgageExchangeOrder()
        





