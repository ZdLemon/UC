# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getReason import _mgmt_inventory_common_getReason # 退换货原因
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchProduct import _mgmt_inventory_dis_mortgage_returnOrder_searchProduct # 获取商品信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn import _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn # 新建押货退货单
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo # 展示审批保存信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_opinion import _mgmt_inventory_dis_mortgage_returnOrder_opinion # 添加审批意见
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_audit import _mgmt_inventory_dis_mortgage_returnOrder_audit # 审批
from api.basic_services._storage_upload import files as files01, _storage_upload # 退回时上传附件
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_process import _mgmt_inventory_dis_mortgage_returnOrder_process # 退回处理
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_inspect import _mgmt_inventory_dis_mortgage_returnOrder_inspect # 验货

from api.mall_store_application._appStore_common_getReason import _appStore_common_getReason # 获取各种退换货原因
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_searchPositiveProducts import _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts # 获取服务中心正库存的商品信息
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_mortgageReturn import _appStore_store_dis_mortgage_returnOrder_mortgageReturn # 押货退货下单
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_process import _appStore_store_dis_mortgage_returnOrder_process # 退回处理

from api.mall_mgmt_application._mgmt_dis_inventory_combine_page import _mgmt_dis_inventory_combine_page # 分页查询套装组合列表
from api.mall_mgmt_application._mgmt_dis_inventory_combine_forward import _mgmt_dis_inventory_combine_forward # 套装组合展示
from api.mall_mgmt_application._mgmt_dis_inventory_combine import _mgmt_dis_inventory_combine # 套装组合
from api.mall_mgmt_application._mgmt_dis_inventory_combine_detail import _mgmt_dis_inventory_combine_detail # 分页查询套装组合明细

from api.mall_mgmt_application._mgmt_dis_inventory_split_page import _mgmt_dis_inventory_split_page # 查询套装拆分列表
from api.mall_mgmt_application._mgmt_dis_inventory_split_forward import _mgmt_dis_inventory_split_forward # 拆分单个套装确认页
from api.mall_mgmt_application._mgmt_dis_inventory_split import _mgmt_dis_inventory_split # 套装拆分
from api.mall_mgmt_application._mgmt_dis_inventory_split_record_page import _mgmt_dis_inventory_split_record_page # 查询套装拆分记录列表
from api.mall_mgmt_application._mgmt_dis_inventory_split_detail import _mgmt_dis_inventory_split_detail # 套装拆明细

from api.mall_store_application._appStore_dis_inventory_combine_page import _appStore_dis_inventory_combine_page # 套装组合列表
from api.mall_store_application._appStore_dis_inventory_combine_preview import _appStore_dis_inventory_combine_preview # 套装组合预览
from api.mall_store_application._appStore_dis_inventory_combine_confirm import _appStore_dis_inventory_combine_confirm # 套装组合
from api.mall_store_application._appStore_dis_inventory_combine_record_page import _appStore_dis_inventory_combine_record_page # 套装组合记录列表
from api.mall_store_application._appStore_dis_inventory_combine_detail import _appStore_dis_inventory_combine_detail # 套装组合明细

from api.mall_mgmt_application._mgmt_product_item_listVersion import _mgmt_product_item_listVersion # 商品版本列表
from api.mall_mgmt_application._mgmt_product_item_onSaleVersion import _mgmt_product_item_onSaleVersion # 上架
from api.mall_mgmt_application._mgmt_product_item_offSaleVersion import _mgmt_product_item_offSaleVersion # 下架
from api.mall_mgmt_application._mgmt_product_ctrl_listInfoAudit import _mgmt_product_ctrl_listInfoAudit # 产品信息审核列表
from api.mall_mgmt_application._mgmt_product_ctrl_infoAudit import _mgmt_product_ctrl_infoAudit # 审核

from api.mall_store_application._appStore_store_dis_mortgage_common_fetchFreightTemplate import _appStore_store_dis_mortgage_common_fetchFreightTemplate # 获取最新的运费计算模板
from api.mall_store_application._appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling import _appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling # 获取启用中的拼箱费上限
from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import _appStore_store_dis_mortgageOrder_searchProductPage # 关键字搜索可押货商品分页
from api.mall_store_application._appStore_store_dis_mortgageOrder_searchCartProducts import _appStore_store_dis_mortgageOrder_searchCartProducts # 获取购物车数据
from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import _appStore_store_dis_mortgageOrder_pushProductsToCart # 推送购物车数据
from api.mall_store_application._appStore_common_isStoreInTrafficControl import _appStore_common_isStoreInTrafficControl # 店铺是否处于交通管控
from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import _appStore_store_dis_mortgageOrder_mortgage # 押货下单
from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import _appStore_store_dis_mortgageOrder_detail_id # 押货单详情
from api.mall_store_application._appStore_store_dis_mortgageOrder_getMortgageAmount import _appStore_store_dis_mortgageOrder_getMortgageAmount # 查询店铺押货余额与限额
from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import _appStore_store_dis_mortgageOrder_prePayCheck # 押货单支付前的金额校验
from api.mall_store_application._appStore_store_deposit_msg import _appStore_store_deposit_msg # 获取服务中心可用押货保证金余额
from api.mall_store_application._appStore_store_getSignBankAccountList import _appStore_store_getSignBankAccountList # 获取签约银行列表
from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay # 支付
from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo # 押货单发货
 
from api.mall_mgmt_application._mgmt_inventory_deposit_storeDepositDetail import _mgmt_inventory_deposit_storeDepositDetail # 85折账款管理 -- 服务中心押货保证详情
from api.mall_mgmt_application._mgmt_dis_inventory_detail import _mgmt_dis_inventory_detail # 查询库存明细

from util.stepreruns import stepreruns
from setting import ACC, ACC05, store_85, AG, AG2
import os
import allure
import pytest
from copy import deepcopy
import time
import uuid
import calendar
import random, string

# 押货退货-（后台-押货退货，店铺-押货退货，后台-套装组合，后台-套装拆分，店铺-套装组合）

# 押货退货

@allure.title("85云商-完美运营后台-押货退货")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/returnOrder/mortgageReturn")
def test_mortgageReturn_85_DTYH(login_store_85):
    
    getReason = None # 退换货原因
    searchStore = None # 店铺信息
    searchProduct = None # 商品信息
    searchProduct02 = None # 商品信息
    returnNum = 2 # 退货数量
    expressSubsidy = "20" # 运费补贴
    id = None # 押货退货单id
    returnOrder_detail = None # 押货退货单详情
    searchAuditInfo = None # 展示审批保存信息
    storage_upload = None # 退回时上传附件信息
    access_token = os.environ["access_token_2"]

    @allure.step("获取各种退换货原因")    
    def step_mgmt_inventory_common_getReason():
        
        nonlocal getReason
        params = {
            "type": 3, # 退货原因
        }              
        with _mgmt_inventory_common_getReason(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]

    @allure.step("查询店铺信息")      
    def step_mgmt_inventory_dis_mortgage_common_searchStore():
        
        nonlocal searchStore
        params = {
            "storeCode" : login_store_85["data"]["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_common_searchStore(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchStore = r.json()["data"]

    @allure.step("商品编码搜索退货商品信息")      
    def step_01_mgmt_inventory_dis_mortgage_returnOrder_searchProduct():
        
        nonlocal searchProduct
        params = {
            "productCode": AG, # 商品编号
            "storeCode": searchStore["storeCode"]
        }          
        with _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchProduct = r.json()["data"]

    @allure.step("商品编码搜索退货商品信息")      
    def step_02_mgmt_inventory_dis_mortgage_returnOrder_searchProduct():
        
        nonlocal searchProduct02
        params = {
            "productCode": AG2, # 商品编号
            "storeCode": searchStore["storeCode"]
        }          
        with _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchProduct02 = r.json()["data"]

    @allure.step("新建85折押货退货单")      
    def step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn():
        
        nonlocal id
        data = {
            "productList": [
                {
                "productCode": searchProduct["productCode"], # 商品编号
                "productName": searchProduct["productName"], # 商品名称
                "packing": searchProduct["packing"], # 规格
                "unit": searchProduct["unit"], # 单位
                "pieceBoxNorm": searchProduct["pieceBoxNorm"], # 押货规格
                "pieceBoxPrice": searchProduct["pieceBoxPrice"], # 拼箱价
                "mortgagePrice": searchProduct["mortgagePrice"], # 85折押货价
                "retailPrice": searchProduct["retailPrice"], # 零售价
                "inventoryNum": searchProduct["inventoryNum"], # 当前库存
                "returnNum": returnNum, # 退货数量
                "remark": ""
                },
                {
                "productCode": searchProduct02["productCode"], # 商品编号
                "productName": searchProduct02["productName"], # 商品名称
                "packing": searchProduct02["packing"], # 规格
                "unit": searchProduct02["unit"], # 单位
                "pieceBoxNorm": searchProduct["pieceBoxNorm"], # 押货规格
                "pieceBoxPrice": searchProduct["pieceBoxPrice"], # 拼箱价
                "mortgagePrice": searchProduct02["mortgagePrice"], # 85折押货价
                "retailPrice": searchProduct02["retailPrice"], # 零售价
                "inventoryNum": searchProduct02["inventoryNum"], # 当前库存
                "returnNum": returnNum, # 退货数量
                "remark": ""
                }
                ],
            "orderMark": 0,
            "reasonFirst": getReason[1]["returnReason"],
            "reasonFirstRemark": "我是一级原因备注哦",
            "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
            "reasonSecondRemark": "我是二级原因备注呀",
            "storeCode": searchStore["storeCode"]
        }               
        with _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            id = r.json()["data"]

    @allure.step("押货退货单详情")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
        
        nonlocal returnOrder_detail
        params = {
            "id": id, 
        }              
        with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["id"] == id
            returnOrder_detail = r.json()["data"]

    @allure.step("展示审批保存信息")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo():
        
        nonlocal searchAuditInfo       
        with _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchAuditInfo = r.json()["data"]["returnAddress"]

    @allure.step("添加审批意见")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_opinion():
        
        data = {
            "orderId": returnOrder_detail["id"], # 押货或售后单id
            "content": f"同意{returnOrder_detail['orderSn']}押货退货单申请" # 审批内容
        }        
        with _mgmt_inventory_dis_mortgage_returnOrder_opinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("审批")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_audit():
        
        data = {
            "id": returnOrder_detail["id"], # id
            "auditRemark": f"同意审批通过押货退货单{returnOrder_detail['orderSn']}", # 审核备注
            "auditFileName": "", # 审核附件名称
            "auditResult": "1", # 审核结果 0不通过 1通过
            "auditFileUrl": "", # 审核附件url
            "reasonFirst": returnOrder_detail["reasonFirst"], # 一级原因
            "reasonFirstRemark": returnOrder_detail["reasonFirstRemark"], # 一级原因备注
            "reasonSecond": returnOrder_detail["reasonSecond"], # 二级原因
            "reasonSecondRemark": returnOrder_detail["reasonSecondRemark"], # 二级原因备注
            "returnInfo": "",
            "preAuditFileUrl": "",
            "returnAddress": ""
        }
        if searchAuditInfo:
            data["returnInfo"] = searchAuditInfo
            data["returnAddress"] = searchAuditInfo
        else:
            data["returnInfo"] = "我是退回地址"
            data["returnAddress"] = "我是退回地址"
        with _mgmt_inventory_dis_mortgage_returnOrder_audit(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("上传文件：退回时上传附件")  
    def step_storage_upload():
        
        nonlocal storage_upload
        files = deepcopy(files01) 
        files["clientKey"] = "mall-center-inventory" 
        files["file"] = "data/退回快递单01.jpg"                
        with _storage_upload(files, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["datas"]["msg"] == "文件上传成功"
            storage_upload = r.json()["datas"]

    @allure.step("退回处理")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_process():
        
        data = {
            "orderId": returnOrder_detail["id"], # id
            "returnType": "2", # 退回类型 1自带 2邮寄
            "expressNo": "wmwl123456", # 物流单号
            "expressCompany": "完美物流", # 物流公司
            "expressProofUrl": storage_upload["fileUrlKey"],
            "expressProofName": storage_upload["relativePath"][24:], # 快递凭证名称
            "processRemark": "" # 退回处理说明
        }
        with _mgmt_inventory_dis_mortgage_returnOrder_process(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("验货")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_inspect():
        
        data = {
            "orderId": returnOrder_detail["id"], # id
            "inspectResult": "1", # 验货意见 0不通过 1通过
            "expressSubsidy": expressSubsidy, # 运费补贴
            "inspectRemark": f"押货退货单{returnOrder_detail['orderSn']}验货没问题", # 验货备注
            "orderReturnRealAmount": str(returnOrder_detail['returnAmount']),
            "productList": [ # 商品列表
                {
                "returnRealNum": returnOrder_detail["productList"][0]["returnNum"],
                "productCode": returnOrder_detail["productList"][0]["productCode"]
                },
                {
                "returnRealNum": returnOrder_detail["productList"][1]["returnNum"],
                "productCode": returnOrder_detail["productList"][1]["productCode"]
                }
                ],
            "returnRealAmount": str(returnOrder_detail['returnAmount']) # 物品实退金额总额
        }
        with _mgmt_inventory_dis_mortgage_returnOrder_inspect(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mgmt_inventory_common_getReason()
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_01_mgmt_inventory_dis_mortgage_returnOrder_searchProduct()
    step_02_mgmt_inventory_dis_mortgage_returnOrder_searchProduct()
    step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo()
    step_mgmt_inventory_dis_mortgage_returnOrder_opinion()
    step_mgmt_inventory_dis_mortgage_returnOrder_audit()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_storage_upload()
    step_mgmt_inventory_dis_mortgage_returnOrder_process()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_inspect()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()

    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": returnOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": returnOrder_detail["orderSn"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
            for i in r.json()["data"]["list"]:                     
                assert i["dealTypeName"] == "押货退货"
                assert i["recordType"] == 5 # 款项类型
                assert i["recordTypeName"] == "无" # 款项类型名称
                assert i["diffMoney"] == returnOrder_detail["returnRealAmount"] # 交易金额 
                assert i["bankAccount"] == None # 银行账号
                assert i["payTypeName"] is None # 支付方式
                assert i["remark"] == None # 备注
                assert i["mortgageOrderNo"] == returnOrder_detail["orderSn"] # 关联单号
                assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 2, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": returnOrder_detail["storeCode"], # 服务中心编号
            "productCode": returnOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == returnOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -returnOrder_detail["productList"][0]["returnNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 2, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": returnOrder_detail["storeCode"], # 服务中心编号
            "productCode": returnOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == returnOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -returnOrder_detail["productList"][1]["returnNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-店铺运营后台-押货退货")
@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgage/returnOrder/mortgageReturn")
def test_mortgageReturn_85_TYH(login_store_85): 
    "店铺系统85折押货退货"
    
    returnNum = 1 # 退货数量
    expressSubsidy = "20" # 运费补贴
    getReason = None # 获取各种退换货原因
    searchPositiveProducts = [] # 正库存商品编号
    mortgageReturn = None # 押货退货单id
    returnOrder_detail = None # 押货退货单详情
    searchAuditInfo = None # 展示审批保存信息
    store_token_85 = os.environ["store_token_85"]
    access_token = os.environ["access_token_2"]

    @allure.step("获取各种退换货原因")    
    def step_appStore_common_getReason():
        
        nonlocal getReason
        params = {
            "type": 3, # 类型: 3退货 4换货
        }
        with _appStore_common_getReason(params, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getReason = r.json()["data"]

    @allure.step("获取服务中心正库存的商品信息")         
    def step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts():
        
        nonlocal searchPositiveProducts
        params = {
            "pageNum": 1,
            "pageSize": 20,
            "product": None # 商品
        }
        with _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts(params, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if len(searchPositiveProducts) < 2 and d["inventoryNum"] > 0:
                    searchPositiveProducts.append(d)
                if len(searchPositiveProducts) >= 2:
                    break
            
    @allure.step("押货退货下单")     
    def step_appStore_store_dis_mortgage_returnOrder_mortgageReturn():
               
        nonlocal mortgageReturn
        data = {
            "reasonFirst": getReason[1]["returnReason"], # 一级原因
            "reasonFirstRemark": "我是一级原因备注哦", # 一级原因备注
            "productList": [
                {
                "productCode": searchPositiveProducts[0]["productCode"], # 商品编码
                "productNum": returnNum,
                "productRemarks": "",
                "remark": "", # 商品备注
                "returnNum": returnNum # 商品退货数量
                },
                {
                "productCode": searchPositiveProducts[1]["productCode"], # 商品编码
                "productNum": returnNum,
                "productRemarks": "",
                "remark": "", # 商品备注
                "returnNum": returnNum # 商品退货数量
                }
                ], 
            "storeCode": login_store_85["data"]["storeCode"] # 服务中心编码
        }
        with _appStore_store_dis_mortgage_returnOrder_mortgageReturn(data, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            mortgageReturn = r.json()["data"]

    @allure.step("押货退货单详情") 
    def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
        
        nonlocal returnOrder_detail
        params = {
            "id": mortgageReturn, 
        }                    
        with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["id"] == mortgageReturn
            returnOrder_detail = r.json()["data"]

    @allure.step("展示审批保存信息")     
    def step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo():
        
        nonlocal searchAuditInfo       
        with _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            searchAuditInfo = r.json()["data"]["returnAddress"]

    @allure.step("添加审批意见")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_opinion():
        
        data = {
            "orderId": returnOrder_detail["id"], # 押货或售后单id
            "content": f"同意{returnOrder_detail['orderSn']}押货退货单申请" # 审批内容
        }        
        with _mgmt_inventory_dis_mortgage_returnOrder_opinion(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("审批")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_audit():
        
        data = {
            "id": returnOrder_detail["id"], # id
            "auditRemark": f"同意审批通过押货退货单{returnOrder_detail['orderSn']}", # 审核备注
            "auditFileName": "", # 审核附件名称
            "auditResult": "1", # 审核结果 0不通过 1通过
            "auditFileUrl": "", # 审核附件url
            "reasonFirst": returnOrder_detail["reasonFirst"], # 一级原因
            "reasonFirstRemark": "我是一级原因备注哦", # 一级原因备注
            "reasonSecond": getReason[1]["reasonList"][1]["returnReason"], # 二级原因
            "reasonSecondRemark": "我是二级原因备注哦", # 二级原因备注
            "returnInfo": "",
            "preAuditFileUrl": "",
            "returnAddress": ""
        }
        if searchAuditInfo:
            data["returnInfo"] = searchAuditInfo
            data["returnAddress"] = searchAuditInfo
        else:
            data["returnInfo"] = "我是退回地址"
            data["returnAddress"] = "我是退回地址"
        with _mgmt_inventory_dis_mortgage_returnOrder_audit(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("退回处理")     
    def step_appStore_store_dis_mortgage_returnOrder_process():
            
        data = {
            "returnType": "2", # 退回类型 1自带 2邮寄
            "expressCompany": "小何物流", # 物流公司
            "expressNo": f"xh{random.sample(string.digits, 8)}", # 物流单号
            "expressProofUrl": "", # 快递凭证url
            "expressProofName": "", # 快递凭证名称
            "processRemark": "", # 退回处理说明
            "orderId": returnOrder_detail["id"] # 退货单id
        }
        with _appStore_store_dis_mortgage_returnOrder_process(data, store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("验货")  
    def step_mgmt_inventory_dis_mortgage_returnOrder_inspect():
        
        data = {
            "orderId": returnOrder_detail["id"], # id
            "inspectResult": "1", # 验货意见 0不通过 1通过
            "expressSubsidy": expressSubsidy, # 运费补贴
            "inspectRemark": f"押货退货单{returnOrder_detail['orderSn']}验货没问题", # 验货备注
            "orderReturnRealAmount": str(returnOrder_detail['returnAmount']),
            "productList": [ # 商品列表
                {
                "returnRealNum": returnOrder_detail["productList"][0]["returnNum"],
                "productCode": returnOrder_detail["productList"][0]["productCode"]
                },
                {
                "returnRealNum": returnOrder_detail["productList"][1]["returnNum"],
                "productCode": returnOrder_detail["productList"][1]["productCode"]
                }
                ],
            "returnRealAmount": str(returnOrder_detail['returnAmount']) # 物品实退金额总额
        }
        with _mgmt_inventory_dis_mortgage_returnOrder_inspect(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
                   
    step_appStore_common_getReason()
    step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts()
    step_appStore_store_dis_mortgage_returnOrder_mortgageReturn()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo()
    step_mgmt_inventory_dis_mortgage_returnOrder_opinion()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_audit()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_appStore_store_dis_mortgage_returnOrder_process()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    step_mgmt_inventory_dis_mortgage_returnOrder_inspect()
    step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": returnOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": returnOrder_detail["orderSn"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
            for i in r.json()["data"]["list"]:                     
                assert i["dealTypeName"] == "押货退货"
                assert i["recordType"] == 5 # 款项类型
                assert i["recordTypeName"] == "无" # 款项类型名称
                assert i["diffMoney"] == returnOrder_detail["returnRealAmount"] # 交易金额 
                assert i["bankAccount"] == None # 银行账号
                assert i["payTypeName"] is None # 支付方式
                assert i["remark"] == None # 备注
                assert i["mortgageOrderNo"] == returnOrder_detail["orderSn"] # 关联单号
                assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 2, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": returnOrder_detail["storeCode"], # 服务中心编号
            "productCode": returnOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == returnOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -returnOrder_detail["productList"][0]["returnNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 2, # 出入库：1入库 2出库
            "bizType": 2, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": returnOrder_detail["storeCode"], # 服务中心编号
            "productCode": returnOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == returnOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -returnOrder_detail["productList"][1]["returnNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()

# 完美后台-套装组合拆分-店铺-套装组合

@allure.title("85云商-店铺+完美后台-套装拆分组合")
@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgage/returnOrder/mortgageReturn")
def test_combine_split(login_store_85):
    
    combine_page = None # 分页查询套装组合列表
    combine_forward = None # 套装组合展示
    diffNum = 1 # 组合数量
    inventory_combine = None # 套装组合
    combine_detail = None # 分页查询套装组合明细
    
    split_page = None # 查询套装拆分列表
    split_forward = None # 拆分单个套装确认页
    record_page_id = None # 查询套装拆分记录列表
    split_detail = None # 套装拆明细
    access_token = os.environ["access_token_2"]
    store_token = os.environ["store_token_85"]

    # 完美运营后台-组合
    @allure.step("分页查询套装组合列表")
    def step_mgmt_dis_inventory_combine_page():
        
        nonlocal combine_page
        params = {
            "combineState": None,
            "companyCode": None, # 分公司编号
            "product": ACC05, # 产品编号/名称
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "combineBegin": None,
            "combineEnd": None,
            "pageNum": 1,
            "pageSize": 10,
        }
        with _mgmt_dis_inventory_combine_page(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                combine_page = r.json()["data"]["list"][0]

    @allure.step("套装组合展示")
    def step_mgmt_dis_inventory_combine_forward():
        
        nonlocal combine_forward
        params = {
            "productCode": combine_page["productCode"], # 产品编号
            "storeCode": combine_page["storeCode"], # 服务中心编号
        }
        with _mgmt_dis_inventory_combine_forward(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combine_forward = r.json()["data"]

    @allure.step("套装组合")    
    def step_mgmt_dis_inventory_combine():
        
        nonlocal inventory_combine
        data = {
            "combineNum": diffNum, # 组合数量
            "productCode": combine_page["productCode"], # 产品编号/名称
            "storeCode": combine_page["storeCode"], # 服务中心编号
        }
        with _mgmt_dis_inventory_combine(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            inventory_combine = r.json()["data"]

    @allure.step("分页查询套装组合明细")     
    def step_mgmt_dis_inventory_combine_detail():
        
        nonlocal combine_detail
        data = {
            "combineIds": [inventory_combine["combineId"]],
            "pageNum": 1,
            "pageSize": 100000
        }
        with _mgmt_dis_inventory_combine_detail(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combine_detail = r.json()["data"]["list"]

    # 完美运营后台-拆分    
    @allure.step("查询套装拆分列表")
    def step_mgmt_dis_inventory_split_page():
        
        nonlocal split_page
        data = {
            "product": ACC05,
            "splitBegin": "",
            "splitEnd": "",
            "productCode": None,
            "stopTime": [],
            "pageNum": 1,
            "pageSize": 10
        }
        with _mgmt_dis_inventory_split_page(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                split_page = r.json()["data"]["list"][0]

    @allure.step("拆分单个套装确认页")
    def step_mgmt_dis_inventory_split_forward():
        
        nonlocal split_forward
        params = {
            "productCode": split_page["productCode"], # 产品编号
        }
        with _mgmt_dis_inventory_split_forward(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            split_forward = r.json()["data"]

    @allure.step("套装拆分")    
    def test_mgmt_dis_inventory_split():
       
        data = {
            "productCodes": [split_page["productCode"]]
        }
        with _mgmt_dis_inventory_split(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["successCount"] > 0
            assert r.json()["data"]["failCount"] == 0
    
    @allure.step("查询套装拆分记录列表")             
    def step_mgmt_dis_inventory_split_record_page():
        
        nonlocal record_page_id
        data = {
            "product": split_page["productCode"], # 商品编号
            "stopTime": [],
            "splitBegin": "",
            "splitEnd": "",
            "productCode": None,
            "pageNum": 1,
            "pageSize": 10
        }
        with _mgmt_dis_inventory_split_record_page(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            record_page_id = r.json()["data"]["list"][0]["id"]
   
    @allure.step("套装拆明细")     
    def step_mgmt_dis_inventory_split_detail():
        
        nonlocal split_detail
        data = {
            "id": record_page_id,
            "pageNum": 1,
            "pageSize": 100000
        }
        with _mgmt_dis_inventory_split_detail(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            split_detail = r.json()["data"]["list"]

    # 店铺运营后台-组合 
    @allure.step("套装组合列表")    
    def step_appStore_dis_inventory_combine_page():
        
        nonlocal combine_page
        params = {
            "pageNum": 1,
            "pageSize": 20,
            "product": ACC05 
        }
        with _appStore_dis_inventory_combine_page(params, store_token) as r:
            assert r.status_code == 200 
            assert r.json()["code"] == 200           
            if r.json()["data"]["list"]:
                combine_page = r.json()["data"]["list"][0]

    @allure.step("套装组合预览")
    def step_appStore_dis_inventory_combine_preview():
        
        nonlocal combine_forward
        params = {
            "combineNum": diffNum, # 套装组合数量
            "productCode": combine_page["productCode"]  # 产品编号
        }
        with _appStore_dis_inventory_combine_preview(params, store_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            combine_forward = r.json()["data"]
                
    @allure.step("套装组合")    
    def step_appStore_dis_inventory_combine_confirm():
        
        data = {
            "combineId": "",
            "combineNum": int(diffNum), # 套装组合数量
            "productCode": combine_page["productCode"]  # 产品编号
        }
        with _appStore_dis_inventory_combine_confirm(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("套装组合记录列表")             
    def step_appStore_dis_inventory_combine_record_page():
        
        nonlocal record_page_id
        params = {
            "pageNum": 1,
            "pageSize": 20,
            "combineBegin": "",
            "combineEnd": "",
            "product": combine_page["productCode"]
        }
        with _appStore_dis_inventory_combine_record_page(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            record_page_id = r.json()["data"]["list"][0]["id"]

    @allure.step("套装组合明细")     
    def step_appStore_dis_inventory_combine_detail():
        
        nonlocal combine_detail
        params = {
            "id": record_page_id
        }
        with _appStore_dis_inventory_combine_detail(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            combine_detail = r.json()["data"]
        
    # 产品下架
    listVersion = None # 商品信息
    versionId = None # 待审核商品id
    @allure.step("商品版本列表：acc")
    def step_01_mgmt_product_item_listVersion():
        
        nonlocal  listVersion
        data = {
            "versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
            "pageNum": 1,
            "pageSize": 10,
            "serialNo": ACC, # 商品编码
            "title": None, # 商品名称
            "catalogId": None, # 类型id
            "saleCompanyId": None, # 销售主体id
            "orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
            "directSale": None, # 是否直销，1-是，0-否
            "orderWay": None, # 下单方式 1-自购,2-代购
            "deliverWay": None, # 交付方式 1-公司交付,2-门店交付
            "startTime": "", # 开始时间时间戳
            "endTime": "" # 结束时间时间戳
        }
        with _mgmt_product_item_listVersion(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listVersion = r.json()["data"]["list"][0]

    @allure.step("商品版本列表：acc05")
    def step_mgmt_product_item_listVersion():
        
        nonlocal  listVersion
        data = {
            "versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
            "pageNum": 1,
            "pageSize": 10,
            "serialNo": ACC05, # 商品编码
            "title": None, # 商品名称
            "catalogId": None, # 类型id
            "saleCompanyId": None, # 销售主体id
            "orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
            "directSale": None, # 是否直销，1-是，0-否
            "orderWay": None, # 下单方式 1-自购,2-代购
            "deliverWay": None, # 交付方式 1-公司交付,2-门店交付
            "startTime": "", # 开始时间时间戳
            "endTime": "" # 结束时间时间戳
        }
        with _mgmt_product_item_listVersion(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            listVersion = r.json()["data"]["list"][0]

    @allure.step("下架")    
    def step_mgmt_product_item_offSaleVersion():
            
        params = {
            "productId": listVersion["productId"], # 商品id
        }                   
        with _mgmt_product_item_offSaleVersion(params, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "下架成功"

    @allure.step("待产品审核商品版本列表")     
    def step_mgmt_product_ctrl_listInfoAudit():
        
        nonlocal versionId
        data = {
            "auditStauts": "2", # 审核状态 1-所有，2-待审核，3-已通过，4-未通过
            "pageNum": 1,
            "pageSize": 10,
            "serialNo": ACC05, # 商品编码
            "title": None,
            "startTime": "", # 开始时间时间戳 1648742400000,本月第一天
            "endTime": "" # 结束时间时间戳,本月当天
        }
        with _mgmt_product_ctrl_listInfoAudit(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["statusNote"] == "待审核" # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
            versionId = r.json()["data"]["list"][0]["id"]
    
    @allure.step("产品审核商品版本")  
    def step_mgmt_product_ctrl_infoAudit():
        
        data = {
            "versionId": versionId, # 版本id
            "auditResult": 1, # 审核结果 1-通过，2-不通过
            "remarks": "同意此产品通过审核" # 说明
        }
        with _mgmt_product_ctrl_infoAudit(data, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
    
    # 产品上架
    @allure.step("上架") 
    def step_mgmt_product_item_onSaleVersion():
        "商品版本上架"
        
        params = {
            "productId": listVersion["productId"]
        }
        with _mgmt_product_item_onSaleVersion(params, os.environ["access_token"]) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "上架成功"
    
    # 押货-ACC
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage
        params = {
            "keyword": ACC, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == ACC:
                    searchProductPage = d
                    break  

    @allure.step("获取启用中的拼箱费上限")  
    def step_appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling
        with _appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("推送购物车数据")  
    def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
        
        data = [ # 85押货单下单商品明细
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage["productCode"] # 押货商品编码
            },
        ] 
        with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("店铺是否处于交通管控")  
    def step_appStore_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        with _appStore_common_isStoreInTrafficControl(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")      
    def step_appStore_store_dis_mortgageOrder_mortgage():
        
        nonlocal id
        data = {
            "isDelivery": True, # 是否发货
            "productList": [
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage["productCode"] # 押货商品编码
                }
            ],
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编码
            "transId": f'KEY_{login_store_85["data"]["storeCode"]}_{uuid.uuid1()}' # 业务id
        }
        with _appStore_store_dis_mortgageOrder_mortgage(data, store_token) as r:
            id = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("获取购物车数据")  
    def step_appStore_store_dis_mortgageOrder_searchCartProducts():
        
        nonlocal searchCartProducts
        with _appStore_store_dis_mortgageOrder_searchCartProducts(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            searchCartProducts = r.json()["data"]

    @allure.step("押货单详情")  
    def step_appStore_store_dis_mortgageOrder_detail_id():
        
        nonlocal mortgageOrder_detail
        params = {
            "id": id # 押货单id
        }
        with _appStore_store_dis_mortgageOrder_detail_id(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            mortgageOrder_detail = r.json()["data"]

    @allure.step("查询店铺押货余额与限额")  
    def step_appStore_store_dis_mortgageOrder_getMortgageAmount():
        
        nonlocal getMortgageAmount
        with _appStore_store_dis_mortgageOrder_getMortgageAmount(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]

    @allure.step("押货单支付前的金额校验")                  
    def step_01_appStore_store_dis_mortgageOrder_prePayCheck():
        
        data = {
            "orderId": id, # 押货单id
            "oweDepositAmount": -getMortgageAmount["depositAvailableAmount"] if getMortgageAmount["depositAvailableAmount"] < 0 else 0, # 押货保证金欠额
            # "payAmount": None # 需支付金额
        }
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("获取服务中心可用押货保证金余额")  
    def step_appStore_store_deposit_msg():
        
        nonlocal balance
        params = {
            "storeCode": login_store_85["data"]["storeCode"]
        }
        with _appStore_store_deposit_msg(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            balance = r.json()["data"]["balance"]
            
    @allure.step("获取签约银行列表")  
    def step_appStore_store_getSignBankAccountList():
        
        nonlocal getSignBankAccountList
        params = {
            "isSigned": 1 # 是否已签约，1/是，2/否
        }            
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getSignBankAccountList = r.json()["data"]

    @allure.step("押货单支付前的金额校验")                  
    def step_02_appStore_store_dis_mortgageOrder_prePayCheck():
        
        data = {
            "orderId": id, # 押货单id
            "oweDepositAmount": -getMortgageAmount["depositAvailableAmount"] if getMortgageAmount["depositAvailableAmount"] < 0 else 0, # 押货保证金欠额
            "payAmount": mortgageOrder_detail["payAmount"] # 需支付金额
        }
        with _appStore_store_dis_mortgageOrder_prePayCheck(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            
    @allure.step("支付")              
    def step_appStore_api_wallet_pay():
        
        nonlocal payOrderNo
        data = {
            "accountName": getSignBankAccountList[0]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance":balance,
                    "payAmount": mortgageOrder_detail["payAmount"],
                    "payWays":[
                        {
                            "name":getSignBankAccountList[0]["accountBank"],
                            "payAmount": mortgageOrder_detail["payAmount"],
                            "data":{
                                "accountName":getSignBankAccountList[0]["accountName"],
                                "account":getSignBankAccountList[0]["account"],
                                "accountBank":getSignBankAccountList[0]["accountBank"],
                                "accountType":getSignBankAccountList[0]["accountType"],
                                "isSigned":getSignBankAccountList[0]["isSigned"]
                            }
                        }
                    ]
                }
            ), # 扩展参数
            "payAmount": mortgageOrder_detail["payAmount"],
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 2, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
            "pxAmount": mortgageOrder_detail["pieceBoxCost"], # 拼箱费
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "uniqueFlagNo": id, # 订单唯一标识
            "userId": login_store_85["data"]["userId"], # 用户ID
            "yfAmount": mortgageOrder_detail["freightCost"] # 运费
        }
        with _appStore_api_wallet_pay(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["payStatus"] == 2
            payOrderNo = r.json()["data"]["payOrderNo"]

    @allure.step("押货单发货")  
    def step_esb_third_mortgage_syncDeliveryInfo():
        
        data = {
            "deliveryCode": f"hw{int(round(time.time() * 1000))}", # 发货单号，不能重复
            "mortgageItemReqDtoList": [
                {
                    "itemCode": searchProductPage["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                },
            ],
            "mortgageOrderNo": mortgageOrder_detail["orderSn"], # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
    

    # 押货保证金详情表-组合
    @allure.step("押货保证金详情表-组合")
    def step_01_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": combine_detail[0]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": combine_detail[0]["orderNo"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if combine_detail[0]["productCode"] == ACC05:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == combine_detail[0]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == combine_detail[0]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
            else:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货退货"
                    assert i["recordType"] == 5 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == combine_detail[0]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] is None # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == combine_detail[0]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    @allure.step("押货保证金详情表-组合")
    def step_02_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": combine_detail[1]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": combine_detail[1]["orderNo"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if combine_detail[1]["productCode"] == ACC05:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == combine_detail[1]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == combine_detail[1]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
            else:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货退货"
                    assert i["recordType"] == 5 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == combine_detail[1]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] is None # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == combine_detail[1]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表-组合
    @allure.step("查询库存明细-组合")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": combine_detail[0]["storeCode"], # 服务中心编号
            "productCode": combine_detail[0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if combine_detail[0]["productCode"] == ACC05:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail[0]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == combine_detail[0]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))  
            else:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail[0]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == combine_detail[0]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细-组合")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": combine_detail[1]["storeCode"], # 服务中心编号
            "productCode": combine_detail[1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if combine_detail[1]["productCode"] == ACC05:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail[1]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == combine_detail[1]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))  
            else:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail[1]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == combine_detail[1]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
  
    # 押货保证金详情表-拆分
    @allure.step("押货保证金详情表-拆分")
    def step_11_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": split_detail[0]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": split_detail[0]["orderNo"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if split_detail[0]["productCode"] == ACC05:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货退货"
                    assert i["recordType"] == 5 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == split_detail[0]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] is None # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == split_detail[0]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
            else:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == split_detail[0]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == split_detail[0]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    @allure.step("押货保证金详情表-拆分")
    def step_12_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": split_detail[1]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": split_detail[1]["orderNo"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if split_detail[1]["productCode"] == ACC05:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货退货"
                    assert i["recordType"] == 5 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == split_detail[1]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] is None # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == split_detail[1]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
            else:
                assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用"]
                for i in r.json()["data"]["list"]:                     
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    assert i["diffMoney"] == split_detail[1]["amount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"] == split_detail[1]["orderNo"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表-拆分
    @allure.step("查询库存明细-拆分")
    @stepreruns(times=30)
    def step_11_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": split_detail[0]["storeCode"], # 服务中心编号
            "productCode": split_detail[0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if split_detail[0]["productCode"] == ACC05:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == split_detail[0]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == split_detail[0]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            else:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == split_detail[0]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == split_detail[0]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))                

    @allure.step("查询库存明细-拆分")
    def step_12_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": split_detail[1]["storeCode"], # 服务中心编号
            "productCode": split_detail[1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if split_detail[1]["productCode"] == ACC05:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == split_detail[1]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == split_detail[1]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            else:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == split_detail[1]["orderNo"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == split_detail[1]["adjustNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))  
                
    # 押货保证金详情表-组合-店铺
    @allure.step("押货保证金详情表-组合-店铺")
    def step_21_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": combine_detail["mortgageCode"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for item in combine_detail["items"]:
                if item["productCode"] == ACC05:
                    assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用"]
                    for i in r.json()["data"]["list"]:                     
                        assert i["dealTypeName"] == "押货使用"
                        assert i["recordType"] == 4 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        assert i["diffMoney"] == -item["securityPrice"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] is None # 备注
                        assert i["mortgageOrderNo"] == combine_detail["mortgageCode"] # 关联单号
                        assert i["businessNo"] == "无" # 流水号

    @allure.step("押货保证金详情表-组合-店铺")
    def step_22_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": combine_detail["mortgageReturnCode"], # 押货单号or流水号
            "pageNum": 1,
            "pageSize": 10,
            "reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
            "moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
            "startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
            "endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        }                     
        with _mgmt_inventory_deposit_storeDepositDetail(data, access_token) as r: 
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for item in combine_detail["items"]:
                if item["productCode"] == ACC:
                    assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货退货"]
                    for i in r.json()["data"]["list"]:                     
                        assert i["dealTypeName"] == "押货退货"
                        assert i["recordType"] == 5 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        assert i["diffMoney"] == item["securityPrice"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] is None # 支付方式
                        assert i["remark"] is None # 备注
                        assert i["mortgageOrderNo"] == combine_detail["mortgageReturnCode"] # 关联单号
                        assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表-组合-店铺
    @allure.step("查询库存明细-组合-店铺")
    def step_21_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "productCode": combine_detail["items"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if combine_detail["items"][0]["productCode"] == ACC05:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail["mortgageCode"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == combine_detail["items"][0]["diffNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))  
            else:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail["mortgageReturnCode"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == -combine_detail["items"][0]["diffNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细-组合-店铺")
    def step_22_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "productCode": combine_detail["items"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if combine_detail["items"][1]["productCode"] == ACC05:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail["mortgageCode"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == combine_detail["items"][1]["diffNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))  
            else:
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == combine_detail["mortgageReturnCode"] # 单号
                assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == -combine_detail["items"][1]["diffNum"] # 押货数量              
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
              
    step_01_mgmt_product_item_listVersion() # 确保ACC 上架
    if listVersion["versionStatus"] == 8:
        step_mgmt_product_item_onSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()
    elif listVersion["versionStatus"] == 2: # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit() 
        
    step_mgmt_product_item_listVersion() # 确保ACC05 上架
    if listVersion["versionStatus"] == 8:
        step_mgmt_product_item_onSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()
    elif listVersion["versionStatus"] == 2: # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit() 
        
    step_mgmt_dis_inventory_combine_page()
    if combine_page is None: # ACC押货
        step_appStore_store_dis_mortgage_common_fetchFreightTemplate()
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_common_isStoreInTrafficControl()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_appStore_store_dis_mortgageOrder_searchCartProducts()
        step_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_dis_mortgageOrder_getMortgageAmount()
        step_01_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_getSignBankAccountList()
        step_02_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_api_wallet_pay()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_detail_id()
        step_esb_third_mortgage_syncDeliveryInfo()        

    # 完美运营后台-组合
    step_mgmt_dis_inventory_combine_page()
    step_mgmt_dis_inventory_combine_forward()
    step_mgmt_dis_inventory_combine()
    step_mgmt_dis_inventory_combine_detail()
    # 查看报表数据
    step_01_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表-组合
    step_02_mgmt_inventory_deposit_storeDepositDetail()
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表-组合
    step_02_mgmt_dis_inventory_detail()  
    # 下架
    step_mgmt_product_item_listVersion()
    if listVersion["versionStatus"] == 7: # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        step_mgmt_product_item_offSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()
    elif listVersion["versionStatus"] == 2: # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()
    # 完美运营后台-拆分
    step_mgmt_dis_inventory_split_page()
    step_mgmt_dis_inventory_split_forward()    
    test_mgmt_dis_inventory_split()    
    step_mgmt_dis_inventory_split_record_page()
    step_mgmt_dis_inventory_split_detail()
    # 查看报表数据
    step_11_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表-拆分
    step_12_mgmt_inventory_deposit_storeDepositDetail()
    step_11_mgmt_dis_inventory_detail() # 库存增减明细表-拆分
    step_12_mgmt_dis_inventory_detail()  
    # 上架
    step_mgmt_product_item_listVersion()
    if listVersion["versionStatus"] == 8:
        step_mgmt_product_item_onSaleVersion()
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()
    elif listVersion["versionStatus"] == 2: # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit() 
    # 店铺运营后台-组合
    step_appStore_dis_inventory_combine_page()
    step_appStore_dis_inventory_combine_preview() 
    step_appStore_dis_inventory_combine_confirm() 
    step_appStore_dis_inventory_combine_record_page() 
    step_appStore_dis_inventory_combine_detail()     
    # 查看报表数据
    step_21_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表-组合
    step_22_mgmt_inventory_deposit_storeDepositDetail()
    step_21_mgmt_dis_inventory_detail() # 库存增减明细表-组合
    step_22_mgmt_dis_inventory_detail() 
                               

        
    
    
    





