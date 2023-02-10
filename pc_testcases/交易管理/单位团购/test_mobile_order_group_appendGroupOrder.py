# coding:utf-8

from api.mall_mobile_application._mobile_order_group_queryStoreGroupOrderByPage import params, _mobile_order_group_queryStoreGroupOrderByPage # 分页查询单位团购单
from api.mall_mobile_application._mobile_order_group_store_address import _mobile_order_group_store_address # 获取服务中心收货信息
from api.mall_mobile_application._mobile_personalInfo_getRegInfosByParentCode import _mobile_personalInfo_getRegInfosByParentCode # 通过传parentCode获得相应的区域信息
from api.mall_mobile_application._mobile_product_search import _mobile_product_search # 搜索商品
from api.basic_services._storage_upload import _storage_upload # 上传文件
from api.mall_mobile_application._mobile_order_group_appendGroupOrder import _mobile_order_group_appendGroupOrder #  新增单位团购单
from api.mall_mgmt_application._mgmt_inventory_group_order_audit import _mgmt_inventory_group_order_audit #  审核团购单

from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/order/group/appendGroupOrder")
class TestClass:
    """
    新增单位团购单
    /mobile/order/group/appendGroupOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.token = os.environ["token"]
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("新增单位团购单-成功路径: 新增单位团购单审核不通过检查")
    def test_mobile_order_group_appendGroupOrder(self):

        search = None # 产品信息
        store_address = None # 服务中心收货信息
        code = None # 广东省编码
        code_02 = None # 深圳市编码
        code_03 = None # 罗湖区编码
        code_04 = None # 桂园街道办事处编码
        file = None # 文件上传
        file_02 = None # 文件上传
        appendGroupOrder = None # 团购订单编号
        groupPrice = 400 # 团购价
        stock = 100 # 团购数量
        
               
        @allure.step("分页查询单位团购单")
        def step_mobile_order_group_queryStoreGroupOrderByPage():

            params = deepcopy(self.params)
            with _mobile_order_group_queryStoreGroupOrderByPage(params, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("获取服务中心收货信息")
        def step_mobile_order_group_store_address():
            nonlocal store_address
            with _mobile_order_group_store_address(self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                store_address = r.json()["data"]
        
        @allure.step("搜索商品")
        def step_mobile_product_search():

            nonlocal search
            data = {
                "keyword": productCode,
                "sortBy":1, # 排序字段(1-时间 2-销量 3-价格 4-最近修改时间)
                "isDesc":1, # 是否降序 0-否 1-是
                "isFilterCusProduct":1, # 是否过滤掉定制产品 0-否 1-是，默认为0
                "isActivateItem":0, # 是否升级商品 1-是 0-否
                "searchSource":1 # 搜索来源 1-单位团购
            }
            with _mobile_product_search(data, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                search = r.json()["data"]["list"][0]

        @allure.step("通过传parentCode获得相应的区域信息:获取广东省code")
        def step_01_mobile_personalInfo_getRegInfosByParentCode():
            
            nonlocal code
            params = {
                "parentCode": 0, # 省的parentCode默认为0
            }
            with _mobile_personalInfo_getRegInfosByParentCode(params, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["name"] == "广东省":
                        code = d["code"]
        
        @allure.step("通过传parentCode获得相应的区域信息:深圳市code")
        def step_02_mobile_personalInfo_getRegInfosByParentCode():

            nonlocal code_02
            params = {
                "parentCode": code, # 省的parentCode默认为0
            }
            with _mobile_personalInfo_getRegInfosByParentCode(params, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["name"] == "深圳市":
                        code_02 = d["code"]
        
        @allure.step("通过传parentCode获得相应的区域信息:罗湖区code")
        def step_03_mobile_personalInfo_getRegInfosByParentCode():

            nonlocal code_03
            params = {
                "parentCode": code_02, # 省的parentCode默认为0
            }
            with _mobile_personalInfo_getRegInfosByParentCode(params, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["name"] == "罗湖区":
                        code_03 = d["code"]
        
        @allure.step("通过传parentCode获得相应的区域信息:平湖街道办事处code")
        def step_04_mobile_personalInfo_getRegInfosByParentCode():

            nonlocal code_04
            params = {
                "parentCode": code_03, # 省的parentCode默认为0
            }
            with _mobile_personalInfo_getRegInfosByParentCode(params, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["name"] == "平湖街道办事处":
                        code_04 = d["code"]
                
        @allure.step("上传文件")
        def step_01_storage_upload():
            
            nonlocal file
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-finance", # str客户端Key(由管理员进行分配)
                "file": "data\团购单凭证01.jpg"
            }                 
            with _storage_upload(files, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                file = r.json()["datas"]
        
        @allure.step("上传文件")
        def step_02_storage_upload():
            
            nonlocal file_02
            files = {
                "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
                "clientKey": "mall-center-finance", # str客户端Key(由管理员进行分配)
                "file": "data\团购单凭证02.jpg"
            }                 
            with _storage_upload(files, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                file_02 = r.json()["datas"]

        @allure.step("新增单位团购单")
        def step_mobile_order_group_appendGroupOrder():
            nonlocal appendGroupOrder
            data = {
                "institution": "天下第一武道大会",
                "institutionAddr": {
                    "address": "武道一路1号",
                    "province": code,
                    "city": code_02,
                    "district": code_03,
                    "town": code_04
                },
                "receiveType": 2,
                "consigneeName": store_address["person"], # 收货人
                "consigneeMobile": store_address["phoneNum"], # 收货手机
                "consigneeAddr": {
                    "address": store_address["deliveryDetailAddress"], # 收货地址详细地址（门牌号）
                    "province": store_address["deliveryProvinceCode"], # 省份
                    "city": store_address["deliveryCityCode"], # 市
                    "district": store_address["deliveryAreaCode"], # 区
                    "town": store_address["deliveryStreetCode"] # 街道
                },
                "remitType": 2,
                "remittance": str(groupPrice * stock), # 团购总金额
                "remitCredentials": [{
                    "name": "团购单凭证01.jpg",
                    "url": file["fileUrlKey"]
                }],
                "needInvoice": 0,
                "invoiceType": 1,
                "contracts": None,
                "commitment": {
                    "name": "团购单凭证02.jpg",
                    "url": file_02["fileUrlKey"]
                },
                "remark": "",
                "bankAccount": "4000050909100468735", # 银行账号
                "bankName": " 深圳市龙岗区金泽泰健康服务中心", # 银行账户
                "invoice": None,
                "products": [{
                    "productId": search["productId"],
                    "serialNo": search["serialNo"],
                    "title": f"{search['serialNo']} {search['title']}",
                    "catalogTitle": search["catalogTitle"],
                    "catalogId": search["catalogId"],
                    "showList": search["showList"],
                    "retailPrice": search["retailPrice"],
                    "underlinedPrice": search["underlinedPrice"],
                    "groupPrice": groupPrice, # 团购价
                    "pv": search["pv"],
                    "securityPrice": search["securityPrice"],
                    "activityPrice": search["activityPrice"],
                    "preDepositPrice": search["preDepositPrice"],
                    "depositDiscountPrice": search["depositDiscountPrice"],
                    "imgUrl": search["imgUrl"],
                    "orderType": search["orderType"],
                    "isExchangeProduct": search["isExchangeProduct"],
                    "isPreProduct": search["isPreProduct"],
                    "productType": search["productType"],
                    "isActivateItem": search["isActivateItem"],
                    "purchaseLimitType": search["purchaseLimitType"],
                    "purchaseLimitNum": search["purchaseLimitNum"],
                    "isIdentityLimit": search["isIdentityLimit"],
                    "customerIdentityTypes": search["customerIdentityTypes"],
                    "customerCardTypes": search["customerCardTypes"],
                    "stock": stock, # 团购数量
                    "productCode": search["serialNo"],
                    "groupPricex": search["groupPrice"]
                }]
            }
            with _mobile_order_group_appendGroupOrder(data, self.token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200
                appendGroupOrder = r.json()["data"]

        @allure.step("审核团购单")
        def step_mgmt_inventory_group_order_audit():

            data = {
                "attachments":[], # 审核附件
                "auditResult": 0, # 审核结果：0、不通过 1、通过
                "auditView": f"我不同意团购单{appendGroupOrder}申请", # 审核意见
                "orderNo": appendGroupOrder # 订单编号
            }
            with _mgmt_inventory_group_order_audit(data, self.access_token) as r: 
                assert r.status_code == 200
                assert r.json()["code"] == 200         
               
        step_mobile_order_group_queryStoreGroupOrderByPage()
        step_mobile_order_group_store_address()
        step_mobile_product_search()
        step_01_mobile_personalInfo_getRegInfosByParentCode()
        step_02_mobile_personalInfo_getRegInfosByParentCode()
        step_03_mobile_personalInfo_getRegInfosByParentCode()
        step_04_mobile_personalInfo_getRegInfosByParentCode()
        step_01_storage_upload()  
        step_02_storage_upload()
        step_mobile_order_group_appendGroupOrder() 
        step_mgmt_inventory_group_order_audit()           


