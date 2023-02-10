# coding:utf-8

from api.mall_store_application._appStore_store_info import _appStore_store_info # 服务中心查看基础信息
from api.mall_store_application._appStore_store_getSignBankAccountList import _appStore_store_getSignBankAccountList # 获取签约银行列表
from api.mall_store_application._appStore_invest import _appStore_invest # 充值

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import _mgmt_inventory_dis_mortgage_order_searchProductPage # 关键字搜索可押货商品分页  
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_fetchFreightTemplate import _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate # 获取最新的运费计算模板
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_getMortgageAmount import _mgmt_inventory_dis_mortgage_order_getMortgageAmount # 查询店铺押货余额与限额
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling import _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling # 获取启用中的拼箱费上限  
from api.mall_mgmt_application._mgmt_inventory_common_isStoreInTrafficControl import _mgmt_inventory_common_isStoreInTrafficControl # 店铺是否处于交通管控
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import _mgmt_inventory_dis_mortgage_order_mortgage # 押货下单
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit # 查询押货单是否超出库存限额
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_audit import _mgmt_inventory_dis_mortgage_order_audit # 押货单审核
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_modify import _mgmt_inventory_dis_mortgage_order_modify # 押货单修改
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_stopDeliver import _mgmt_inventory_dis_mortgage_order_stopDeliver # 押货单欠货停发
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_batchCancel import _mgmt_inventory_dis_mortgage_order_batchCancel # 押货单批量取消
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detailForModify_id import _mgmt_inventory_dis_mortgage_order_detailForModify_id # 押货单详情(修改)
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detail_id import _mgmt_inventory_dis_mortgage_order_detail_id # 押货单详情
from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo # 押货单发货

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
from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay # 支付
from api.mall_center_esb._esb_third_mortgage_syncDeliveryInfo import _esb_third_mortgage_syncDeliveryInfo # 押货单发货

from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_pageList import _mgmt_inventory_disManualInputRemit_pageList # 85折手工录入流水分页搜索列表
from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import _mgmt_inventory_disManualInputRemit_getStoreWalletMsg # 1:3押货余额及85折保证金余额查询
from api.mall_mgmt_application._mgmt_store_getStoreByCode import _mgmt_store_getStoreByCode # 根据服务中心编号获取服务中心
from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_add import _mgmt_inventory_disManualInputRemit_add # 85折手工录入流水
from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_verify import _mgmt_inventory_disManualInputRemit_verify # 85折手工录入流水单个审核
    
from api.mall_mgmt_application._mgmt_inventory_deposit_storeDepositDetail import _mgmt_inventory_deposit_storeDepositDetail # 85折账款管理 -- 服务中心押货保证详情
from api.mall_mgmt_application._mgmt_inventory_disBankRemit_pageList import _mgmt_inventory_disBankRemit_pageList # 85折银行流水分页搜索列表
from api.mall_mgmt_application._mgmt_pay_verifyAcct_querytob import _mgmt_pay_verifyAcct_querytob # 查询对公支付对账结果信息
from api.mall_mgmt_application._mgmt_inventory_disChargeDetail_pageList import _mgmt_inventory_disChargeDetail_pageList # 分页列表-手续费明细表
from api.mall_mgmt_application._mgmt_dis_inventory_detail import _mgmt_dis_inventory_detail # 查询库存明细

from util.stepreruns import stepreruns
from setting import store_85, AG, AG2
import os
import allure
import pytest
from copy import deepcopy
import time
import uuid

# 充值-工行签约代扣-建行签约代扣
# 押货-（后台押货，后台押货批量取消，后台-押货-修改，后台-押货-欠货停发）
# 押货-（后台押货-仅调账不发货，后台押货批量取消-仅调账不发货，后台-押货-修改-仅调账不发货，后台-押货-欠货停发-仅调账不发货）
# 押货-（# 店铺押货-保证金，店铺押货-工行，店铺押货-建行，店铺押货-工行+保证金，店铺押货-建行+保证金，店铺押货-工行-批量取消，店铺押货-工行-修改，店铺押货-工行-欠货停发）

# 85折充值 2->工行签约代扣 3->建行签约代扣

@allure.title("85云商-店铺系统-工行充值2元")
@allure.feature("mall_store_application")
@allure.story("/appStore/invest")
def test_appStore_invest_2(login_store_85):
    
    store_info = None # 服务中心查看基础信息
    getSignBankAccountList = None # 签约银行列表
    payAmount = 2 # 充值金额
    payOrderNo = None # 充值流水号
    store_token = os.environ["store_token_85"] 
    access_token = os.environ["access_token_2"]   

    @allure.step("服务中心查看基础信息")    
    def step_appStore_store_info():
        
        nonlocal store_info                 
        with _appStore_store_info(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            store_info = r.json()["data"]
    
    @allure.step("获取签约银行列表")
    def step_appStore_store_getSignBankAccountList():
        
        nonlocal getSignBankAccountList 
        params = {
            "isSigned": 1 # 是否已签约，1/是，2/否
        }         
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["accountBank"] == "工商银行":
                    getSignBankAccountList = d

    @allure.step("充值")    
    def step_appStore_invest():

        nonlocal payOrderNo
        data = {
            "accountName": getSignBankAccountList["accountName"], # 户名不能为空
            "bankAccount": getSignBankAccountList["account"], # 代扣账户不能为空
            "bankName": getSignBankAccountList["accountBank"], # 开户银行名称
            "businessType": 3, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "payAmount": payAmount, # 充值金额
            "payChannel": "WEB", # 充值渠道 WEB/APP
            "payType": 2, # 2->工行签约代扣 3->建行签约代扣
            "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
            "userId": login_store_85["data"]["userId"] # 用户ID
        }                
        with _appStore_invest(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            payOrderNo = r.json()["data"]["payOrderNo"]

    step_appStore_store_info()
    step_appStore_store_getSignBankAccountList()
    step_appStore_invest()

    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": None, # 押货单号or流水号
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
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款" # 交易类型
            assert r.json()["data"]["list"][0]["recordType"] == 1 # 款项类型
            assert r.json()["data"]["list"][0]["recordTypeName"] == "汇押货款" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == payAmount # 交易金额
            assert r.json()["data"]["list"][0]["bankAccount"] == getSignBankAccountList["account"] # 银行账号
            assert r.json()["data"]["list"][0]["payTypeName"] == "工行代扣" # 支付方式
            assert r.json()["data"]["list"][0]["remark"] == None # 备注
            assert r.json()["data"]["list"][0]["mortgageOrderNo"] == "无" # 关联单号
            assert r.json()["data"]["list"][0]["businessNo"] == payOrderNo # 流水号

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType":None, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == login_store_85["data"]["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == login_store_85["data"]["companyNo"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "前端充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": store_info["comInfo"]["code"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 14, # 支付渠道 14工行代扣 15建行
            "status": None, # 平账状态
            "storeCode": store_info["storeInfo"]["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == store_info["comInfo"]["fullName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_info["storeInfo"]["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] is None # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == payAmount # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "工行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 0 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账


@allure.title("85云商-店铺系统-建行充值3元")
@allure.feature("mall_store_application")
@allure.story("/appStore/invest")
def test_appStore_invest_3(login_store_85):
    
    store_info = None # 服务中心查看基础信息
    getSignBankAccountList = None # 签约银行列表
    payAmount = 3 # 充值金额
    payOrderNo = None # 充值流水号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token_2"]      

    @allure.step("服务中心查看基础信息")    
    def step_appStore_store_info():
        
        nonlocal store_info                 
        with _appStore_store_info(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            store_info = r.json()["data"]

    @allure.step("获取签约银行列表")    
    def step_appStore_store_getSignBankAccountList():
        
        nonlocal getSignBankAccountList
        params = {
            "isSigned": 1 # 是否已签约，1/是，2/否
        }                  
        with _appStore_store_getSignBankAccountList(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]:
                if d["accountBank"] == "建设银行":
                    getSignBankAccountList = d

    @allure.step("充值")     
    def step_appStore_invest():

        nonlocal payOrderNo
        data = {
            "accountName": getSignBankAccountList["accountName"], # 户名不能为空
            "bankAccount": getSignBankAccountList["account"], # 代扣账户不能为空
            "bankName": getSignBankAccountList["accountBank"], # 开户银行名称
            "businessType": 3, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "payAmount": payAmount, # 充值金额
            "payChannel": "WEB", # 充值渠道 WEB/APP
            "payType": 3, # 2->工行签约代扣 3->建行签约代扣
            "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
            "userId": login_store_85["data"]["userId"] # 用户ID
        }                
        with _appStore_invest(data, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            payOrderNo = r.json()["data"]["payOrderNo"]

    step_appStore_store_info()
    step_appStore_store_getSignBankAccountList()
    step_appStore_invest()
        
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": login_store_85["data"]["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": None, # 押货单号or流水号
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
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款" # 交易类型
            assert r.json()["data"]["list"][0]["recordType"] == 1 # 款项类型
            assert r.json()["data"]["list"][0]["recordTypeName"] == "汇押货款" # 款项类型
            assert r.json()["data"]["list"][0]["diffMoney"] == payAmount # 交易金额
            assert r.json()["data"]["list"][0]["bankAccount"] == getSignBankAccountList["account"] # 银行账号
            assert r.json()["data"]["list"][0]["payTypeName"] == "建行代扣" # 支付方式
            assert r.json()["data"]["list"][0]["remark"] == None # 备注
            assert r.json()["data"]["list"][0]["mortgageOrderNo"] == "无" # 关联单号
            assert r.json()["data"]["list"][0]["businessNo"] == payOrderNo # 流水号

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType":None, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == login_store_85["data"]["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == login_store_85["data"]["companyNo"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] ==  payAmount # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "前端充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": store_info["comInfo"]["code"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 15, # 支付渠道 14工行代扣 15建行
            "status": None, # 平账状态
            "storeCode": store_info["storeInfo"]["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == store_info["comInfo"]["fullName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_info["storeInfo"]["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] == payAmount # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == payAmount # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "建行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 1 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 手续费明细表
    totalPage = 1 # 有多少页
    @allure.step("分页列表-手续费明细表:获取页数")
    def step_01_mgmt_inventory_disChargeDetail_pageList():
        
        nonlocal totalPage
        data = {
            "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "companyCode": [store_info["comInfo"]["code"]], # 分公司
            "storeCode": store_info["storeInfo"]["storeCode"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10
        }          
        with _mgmt_inventory_disChargeDetail_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            totalPage = r.json()["data"]["totalPage"]

    @allure.step("分页列表-手续费明细表")
    def step_02_mgmt_inventory_disChargeDetail_pageList():
        
        data = {
            "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "companyCode": [store_info["comInfo"]["code"]], # 分公司
            "storeCode": store_info["storeInfo"]["storeCode"], # 服务中心编号
            "pageNum": totalPage,
            "pageSize": 10
        }          
        with _mgmt_inventory_disChargeDetail_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert str(r.json()["data"]["list"][-1]["month"]) == time.strftime("%Y%m",time.localtime(time.time())) # 所属月份
            assert r.json()["data"]["list"][-1]["storeCode"] == store_info["storeInfo"]["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][-1]["storeName"] == store_info["storeInfo"]["storeName"] # 服务中心名称
            assert r.json()["data"]["list"][-1]["leaderName"] == store_info["storeInfo"]["leaderName"] # 服务中心负责人
            assert r.json()["data"]["list"][-1]["companyCode"] == store_info["comInfo"]["code"] # 分公司编号
            assert r.json()["data"]["list"][-1]["changeTypeExcel"] == "建行签约代扣" # 手续费类型
            assert r.json()["data"]["list"][-1]["rate"] is None # 费率
            assert r.json()["data"]["list"][-1]["balance"] == payAmount # 金额
            assert r.json()["data"]["list"][-1]["charge"] == 0.5 # 手续费
            assert r.json()["data"]["list"][-1]["orderSn"] is None # 押货单号
            assert r.json()["data"]["list"][-1]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][-1]["payTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付时间

    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_inventory_disChargeDetail_pageList() # 手续费明细表
    step_02_mgmt_inventory_disChargeDetail_pageList()
    
# 完美运营后台-85折押货-仅调账不发货-修改押货单-批量取消-欠货停发

@allure.title("85云商-完美运营后台-押货")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 1, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

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
                {
                    "itemCode": searchProductPage02["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                },
            ],
            "mortgageOrderNo": order_detailForModify["orderSn"], # 押货单号
            "optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    step_esb_third_mortgage_syncDeliveryInfo()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-批量取消")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_batchCancel(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 1, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

    @allure.step("押货单批量取消") 
    def step_mgmt_inventory_dis_mortgage_order_batchCancel():
        
        data = {
            "orderSn": order_detailForModify["orderSn"], # 押货单号
        }           
        with _mgmt_inventory_dis_mortgage_order_batchCancel(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_batchCancel()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用"]
            for i in r.json()["data"]["list"][:3]: 
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

            for i in r.json()["data"]["list"][3:]: 
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-押货单修改")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_modify(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 1, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

    @allure.step("押货单修改") 
    def step_mgmt_inventory_dis_mortgage_order_modify():

        data = {
            "orderSn": order_detailForModify["orderSn"], # 押货单编号
            "productList": [
                {
                    "mortgageNum": order_detailForModify["productList"][0]["mortgageNum"] - 1, # 押货商品数量
                    "mortgagePrice": order_detailForModify["productList"][0]["mortgagePrice"], # 商品押货价
                    "productCode": order_detailForModify["productList"][0]["productCode"] # 商品编码
                }
            ]
        }           
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_modify()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用", "其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号 
                elif i["remark"] == "押货调整":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-欠货停发")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_stopDeliver(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 1, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

    @allure.step("押货单修改") 
    def step_mgmt_inventory_dis_mortgage_order_modify():
        
        data = {
            "orderSn": order_detailForModify["orderSn"], # 押货单编号
            "productList": [
                {
                    "mortgageNum": order_detailForModify["productList"][0]["mortgageNum"] - 1, # 押货商品数量
                    "mortgagePrice": order_detailForModify["productList"][0]["mortgagePrice"], # 商品押货价
                    "productCode": order_detailForModify["productList"][0]["productCode"] # 商品编码
                }
            ]
        }           
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单欠货停发") 
    def step_mgmt_inventory_dis_mortgage_order_stopDeliver():
        
        params = {
            "orderSn": order_detailForModify["orderSn"], # 押货单编号
        }           
        with _mgmt_inventory_dis_mortgage_order_stopDeliver(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 押货单修改
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_modify()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 欠货停发
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_stopDeliver()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_01_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": None, # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"][:3]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货退货"]
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"][:3]:
                    if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                        assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                        assert i["recordType"] == 10 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        assert i["diffMoney"] == order_detailForModify["freightCost"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] == "运费" # 备注
                        assert i["mortgageOrderNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 关联单号
                        assert i["businessNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 流水号
                    elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                        assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                        assert i["recordType"] == 10 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        assert i["diffMoney"] == order_detailForModify["pieceBoxCost"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] == "拼箱费" # 备注
                        assert i["mortgageOrderNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 关联单号
                        assert i["businessNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 流水号
                    else:                       
                        assert i["dealTypeName"] == "押货退货"
                        assert i["recordType"] == 5 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        assert i["diffMoney"] == order_detailForModify["mortgageAmount"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] == None # 备注
                        assert i["mortgageOrderNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 关联单号
                        assert i["businessNo"] == "无" # 流水号 

    @allure.step("押货保证金详情表")
    def step_02_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用", "其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == order_detailForModify["orderSn"] # 流水号 
                elif i["remark"] == "押货调整":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            assert r.json()["data"]["page"]["list"][1]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][1]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][1]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][1]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            
    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            assert r.json()["data"]["page"]["list"][1]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][1]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][1]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][1]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_01_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_02_mgmt_inventory_deposit_storeDepositDetail()  
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-仅调账不发货")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_isDelivery(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 0, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
      
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用"]
            for i in r.json()["data"]["list"]:                    
                assert i["dealTypeName"] == "押货使用"
                assert i["recordType"] == 4 # 款项类型
                assert i["recordTypeName"] == "无" # 款项类型名称
                for d in order_detailForModify["operationLogList"]:
                    if d["logType"] == 1:
                        assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                assert i["bankAccount"] == None # 银行账号
                assert i["payTypeName"] == "保证金" # 支付方式
                assert i["remark"] == None # 备注
                assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-仅调账不发货-批量取消")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_isDelivery_batchCancel(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 0, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

    @allure.step("押货单批量取消") 
    def step_mgmt_inventory_dis_mortgage_order_batchCancel():
        
        data = {
            "orderSn": order_detailForModify["orderSn"], # 押货单号
        }           
        with _mgmt_inventory_dis_mortgage_order_batchCancel(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_batchCancel()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用", "押货使用"]
            for i in r.json()["data"]["list"]:
                if i["remark"] == "押货调整":
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
                else:                    
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-仅调账不发货-押货单修改")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_isDelivery_modify(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 0, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

    @allure.step("押货单修改") 
    def step_mgmt_inventory_dis_mortgage_order_modify():

        data = {
            "orderSn": order_detailForModify["orderSn"], # 押货单编号
            "productList": [
                {
                    "mortgageNum": order_detailForModify["productList"][0]["mortgageNum"] - 1, # 押货商品数量
                    "mortgagePrice": order_detailForModify["productList"][0]["mortgagePrice"], # 商品押货价
                    "productCode": order_detailForModify["productList"][0]["productCode"] # 商品编码
                }
            ]
        }           
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_modify()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": order_detailForModify["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用", "押货使用"]
            for i in r.json()["data"]["list"]:
                if i["remark"] == "押货调整":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in order_detailForModify["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-完美运营后台-押货-仅调账不发货-欠货停发")
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/mortgage")
def test_order_mortgage_isDelivery_stopDeliver(login_store_85):
 
    searchStore = None # 查询店铺信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    searchProductPage = None, # 商品信息
    searchProductPage02 = None, # 商品信息
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    getMortgageAmount = None # 查询店铺押货余额与限额
    checkIsAuditAmountOverLimit = True # 是否超出库存限额
    mortgageNum = 2 # 押货数量
    orderId = None # 押货单id
    order_detailForModify = None # 押货单详情
    access_token = os.environ["access_token"]

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

    @allure.step("关键字搜索可押货商品")    
    def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "storeCode": searchStore["storeCode"],
            "keyword": AG, # 关键字
            "pageSize": 20,
            "pageNum": 1
        }              
        with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break 
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
                    break 

    @allure.step("获取最新的运费计算模板")  
    def step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate             
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token) as r:          
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            ffetchFreightTemplate =  r.json()["data"]["intervalList"][0]

    @allure.step("获取启用中的拼箱费上限")  
    def step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling():
        
        nonlocal fetchPieceBoxCostCeiling                
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchPieceBoxCostCeiling = r.json()["data"]

    @allure.step("查询店铺押货余额与限额") 
    def step_mgmt_inventory_dis_mortgage_order_getMortgageAmount():
        
        nonlocal getMortgageAmount
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_dis_mortgage_order_getMortgageAmount(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getMortgageAmount = r.json()["data"]["depositAvailableAmount"]

    @allure.step("店铺是否处于交通管控") 
    def step_mgmt_inventory_common_isStoreInTrafficControl():
        
        nonlocal isStoreInTrafficControl
        params = {
            "storeCode" : searchStore["storeCode"],  # 服务中心编号
        }                   
        with _mgmt_inventory_common_isStoreInTrafficControl(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            isStoreInTrafficControl = r.json()["data"]["isTrafficControl"]

    @allure.step("押货下单")                 
    def step_mgmt_inventory_dis_mortgage_order_mortgage():
        "押货下单"
        
        nonlocal orderId
        data = {
            "storeCode": searchStore["storeCode"], 
            "isDelivery": 0, # 是否发货
            "remarks": "", # 押货单备注
            "productList": [
                { # 押货单商品列表信息
                "productCode": searchProductPage["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                { 
                "productCode": searchProductPage02["productCode"], # 押货商品编码
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "mortgageNum": mortgageNum # 押货商品数量
                },
                ],
            "transId": f"{searchStore['storeCode']}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
        }
        with _mgmt_inventory_dis_mortgage_order_mortgage(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            orderId = r.json()["data"]
            
    @allure.step("查询押货单是否超出库存限额")       
    def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
        
        nonlocal checkIsAuditAmountOverLimit
        params = {
            "orderId" : orderId,  # 押货单id
        }              
        with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, access_token) as r:
            checkIsAuditAmountOverLimit = r.json()["data"]
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("审核通过押货单")      
    def step_mgmt_inventory_dis_mortgage_order_audit():
        
        data = {
            "auditRemarks": "同意押货单申请", # 审批备注
            "auditResult": 1, # 审批结果 0不通过 1通过
            "orderId": orderId # 押货单id
        }
        with _mgmt_inventory_dis_mortgage_order_audit(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]

    @allure.step("押货单修改") 
    def step_mgmt_inventory_dis_mortgage_order_modify():
        
        data = {
            "orderSn": order_detailForModify["orderSn"], # 押货单编号
            "productList": [
                {
                    "mortgageNum": order_detailForModify["productList"][0]["mortgageNum"] - 1, # 押货商品数量
                    "mortgagePrice": order_detailForModify["productList"][0]["mortgagePrice"], # 商品押货价
                    "productCode": order_detailForModify["productList"][0]["productCode"] # 商品编码
                }
            ]
        }           
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单欠货停发") 
    def step_mgmt_inventory_dis_mortgage_order_stopDeliver():
        
        params = {
            "orderSn": order_detailForModify["orderSn"], # 押货单编号
        }           
        with _mgmt_inventory_dis_mortgage_order_stopDeliver(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单详情") 
    def step_mgmt_inventory_dis_mortgage_order_detail_id():
        
        nonlocal order_detailForModify
        params = {"id": orderId}           
        with _mgmt_inventory_dis_mortgage_order_detail_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            order_detailForModify = r.json()["data"]
            
    step_mgmt_inventory_dis_mortgage_common_searchStore()
    step_mgmt_inventory_dis_mortgage_order_searchProductPage()
    step_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate()
    step_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling()
    step_mgmt_inventory_dis_mortgage_order_getMortgageAmount()
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_mortgage()
    step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
    step_mgmt_inventory_dis_mortgage_order_audit()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 押货单修改
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_modify()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 欠货停发
    step_mgmt_inventory_common_isStoreInTrafficControl()
    step_mgmt_inventory_dis_mortgage_order_stopDeliver()
    step_mgmt_inventory_dis_mortgage_order_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_01_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": None, # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"][:3]] == ["押货退货", "押货使用", "押货使用"]
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"][:3]:
                    if i["dealTypeName"] == "押货退货":                       
                        assert i["dealTypeName"] == "押货退货"
                        assert i["recordType"] == 5 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        assert i["diffMoney"] == order_detailForModify["mortgageAmount"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] == None # 备注
                        assert i["mortgageOrderNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 关联单号
                        assert i["businessNo"] == "无" # 流水号 
                    elif i["remark"] == "押货调整":                       
                        assert i["dealTypeName"] == "押货使用"
                        assert i["recordType"] == 4 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        for d in order_detailForModify["operationLogList"]:
                            if d["logType"] == 5:
                                assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] == "押货调整" # 备注
                        assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                        assert i["businessNo"] == "无" # 流水号 
                    else:                       
                        assert i["dealTypeName"] == "押货使用"
                        assert i["recordType"] == 4 # 款项类型
                        assert i["recordTypeName"] == "无" # 款项类型名称
                        for d in order_detailForModify["operationLogList"]:
                            if d["logType"] == 1:
                                assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                        assert i["bankAccount"] == None # 银行账号
                        assert i["payTypeName"] == "保证金" # 支付方式
                        assert i["remark"] == None # 备注
                        assert i["mortgageOrderNo"] == order_detailForModify["orderSn"] # 关联单号
                        assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            assert r.json()["data"]["page"]["list"][1]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][1]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][1]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][1]["diffNum"] == order_detailForModify["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            
    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": order_detailForModify["storeCode"], # 服务中心编号
            "productCode": order_detailForModify["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"][:14] == F'TYH{order_detailForModify["orderSn"][2:13]}' # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            assert r.json()["data"]["page"]["list"][1]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][1]["bizNo"] == order_detailForModify["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][1]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][1]["diffNum"] == order_detailForModify["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_01_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()

# 店铺系统-85折押货-保证金-工行-建行-工行+保证金-建行+保证金

@allure.title("85云商-店铺运营后台-押货-工行代扣")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_2(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                {
                    "itemCode": searchProductPage02["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": mortgageOrder_detail["orderSn"], # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
    
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
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "工行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 14, # 支付渠道 工行代扣
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] is None # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "工行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 0 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-店铺运营后台-押货-建行代扣")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_3(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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
            "accountName": getSignBankAccountList[1]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[1]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[1]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance":balance,
                    "payAmount": mortgageOrder_detail["payAmount"],
                    "payWays":[
                        {
                            "name":getSignBankAccountList[1]["accountBank"],
                            "payAmount": mortgageOrder_detail["payAmount"],
                            "data":{
                                "accountName":getSignBankAccountList[1]["accountName"],
                                "account":getSignBankAccountList[1]["account"],
                                "accountBank":getSignBankAccountList[1]["accountBank"],
                                "accountType":getSignBankAccountList[1]["accountType"],
                                "isSigned":getSignBankAccountList[1]["isSigned"]
                            }
                        }
                    ]
                }
            ), # 扩展参数
            "payAmount": mortgageOrder_detail["payAmount"],
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 3, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
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
                {
                    "itemCode": searchProductPage02["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": mortgageOrder_detail["orderSn"], # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"
    
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
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "建行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[1]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[1]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 15, # 支付渠道 14工行代扣 15建行
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "建行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 1 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 手续费明细表
    totalPage = 1 # 有多少页
    @allure.step("分页列表-手续费明细表:获取页数")
    def step_01_mgmt_inventory_disChargeDetail_pageList():
        
        nonlocal totalPage
        data = {
            "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "companyCode":[mortgageOrder_detail["companyCode"]], # 分公司
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10
        }          
        with _mgmt_inventory_disChargeDetail_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            totalPage = r.json()["data"]["totalPage"]

    @allure.step("分页列表-手续费明细表")
    def step_02_mgmt_inventory_disChargeDetail_pageList():
        
        data = {
            "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "companyCode":[mortgageOrder_detail["companyCode"]], # 分公司
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum": totalPage,
            "pageSize": 10
        }          
        with _mgmt_inventory_disChargeDetail_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert str(r.json()["data"]["list"][-1]["month"]) == time.strftime("%Y%m",time.localtime(time.time())) # 所属月份
            assert r.json()["data"]["list"][-1]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][-1]["storeName"] == mortgageOrder_detail["storeName"] # 服务中心名称
            assert r.json()["data"]["list"][-1]["leaderName"] == mortgageOrder_detail["leader"] # 服务中心负责人
            assert r.json()["data"]["list"][-1]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司编号
            assert r.json()["data"]["list"][-1]["changeTypeExcel"] == "建行签约代扣" # 手续费类型
            assert r.json()["data"]["list"][-1]["rate"] is None # 费率
            assert r.json()["data"]["list"][-1]["balance"] == mortgageOrder_detail["payRecord"]["payMoney"] # 金额
            assert r.json()["data"]["list"][-1]["charge"] == 0.5 # 手续费
            assert r.json()["data"]["list"][-1]["orderSn"] == mortgageOrder_detail["orderSn"] # 押货单号
            assert r.json()["data"]["list"][-1]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][-1]["payTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付时间
            
    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()
    step_01_mgmt_inventory_disChargeDetail_pageList() # 手续费明细表
    step_02_mgmt_inventory_disChargeDetail_pageList()


@allure.title("85云商-店铺运营后台-押货-保证金")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_1(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号

    disManualInputRemit_pageList = [] # 85折手工录入流水分页搜索列表:是否有待审核的申请
    remitMoney = 0 # 录入金额
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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
            "accountName": "", # 户名(仅钱包支付不用传)
            "bankAccount": "", # 代扣账户(仅钱包支付不用传)
            "bankName": "", # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str( # 扩展参数
                {
                    "balance":balance,
                    "payAmount":mortgageOrder_detail["payAmount"],
                    "payWays":[
                        {
                            "name":"押货保证金支付",
                            "payAmount":mortgageOrder_detail["payAmount"],
                            "data":None
                        }
                    ]
                }), 
            "payAmount": mortgageOrder_detail["payAmount"],
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 1, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
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
                {
                    "itemCode": searchProductPage02["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": mortgageOrder_detail["orderSn"], # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"

    # 保证金调整
    @allure.step("根据服务中心编号获取服务中心信息")
    def step_mgmt_store_getStoreByCode():
        
        nonlocal getStoreByCode
        params = {
            "code" : login_store_85["data"]["storeCode"],  # 服务中心编号
        }                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreByCode = r.json()["data"]
      
    @allure.step("85折手工录入流水分页搜索列表:是否有待审核的申请")
    def step_01_mgmt_inventory_disManualInputRemit_pageList():
        
        nonlocal disManualInputRemit_pageList
        data = {
            "monthrange": None,
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "companyCode": None, # 分公司code
            "sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "payAccountBankName": None, # 付款银行
            "verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
            "verifyStatus": 0, # 审核状态 0 待审核 1 已审核
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    disManualInputRemit_pageList.append(i["id"])

    @allure.step("85折手工录入流水单个审核:拒绝待审核的申请")
    def step_01_mgmt_inventory_disManualInputRemit_verify():
        
        params = {
            "id": disManualInputRemit_id, # 主键id
            "verifyRemark": "", # 审核备注
            "verifyResult": 2 # 1->通过 2-> 拒绝
        }                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
              
    @allure.step("查询分公司银行账号")
    def step_mgmt_sys_getAccountList():
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreByCode["store"]["companyCode"],  # 公司编码
        }
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getAccountList = r.json()["data"]
                
    @allure.step("通过storeCode获取银行账户资料信息")
    def step_mgmt_store_getBankAccountList():
        
        nonlocal getBankAccountList
        params = {
            "storeCode" : getStoreByCode["store"]["code"],  # 服务中心编号
        }             
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBankAccountList = r.json()["data"]
                        
    @allure.step("1:3押货余额及85折保证金余额查询")
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        
        nonlocal getStoreWalletMsg
        params = {
            "storeCode" : getStoreByCode["store"]["code"],  # 服务中心编号
        }                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreWalletMsg = r.json()["data"]
                
    @allure.step("85折手工录入流水")
    def step_mgmt_inventory_disManualInputRemit_add(): 
                
        data = {
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "storeName": getStoreByCode["store"]["name"], # 店铺名称
            "companyCode": getStoreByCode["store"]["companyCode"], # 分公司code
            "companyName": getAccountList[0]["accountName"], # 分公司名称
            "leaderName": getStoreByCode["user"]["realname"],
            "changeReason": "其他",
            "payAccount": "", # 付款账号
            "payAccountBankName": "", # 付款银行名称
            "receiptAccount": "",  # 收款账号
            "receiptBankName": "", # 收款银行名称
            "remitMoney": remitMoney, # 款项金额
            "sourceType": 3, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "inputRemark": "小何录入款项" # 录入备注
        } 
        if remitMoney > 0: # 服务中心付款
            data["payAccount"] = getBankAccountList[0]["account"]
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"]
            data["receiptBankName"] = getAccountList[0]["bankType"]
        elif remitMoney < 0: # 公司付款
            data["payAccount"] = getAccountList[0]["account"]
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"]
            data["receiptBankName"] = getBankAccountList[0]["branch"]             
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    @allure.step("85折手工录入流水分页搜索列表,获取id")
    def step_mgmt_inventory_disManualInputRemit_pageList():
        
        nonlocal disManualInputRemit_pageList
        data = {
            "monthrange": None,
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "companyCode": None, # 分公司code
            "sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "payAccountBankName": None, # 付款银行
            "verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
            "verifyStatus": 0, # 审核状态 0 待审核 1 已审核
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            disManualInputRemit_pageList = r.json()["data"]["list"][0]["id"]
            
    @allure.step("85折手工录入流水单个审核")
    def step_mgmt_inventory_disManualInputRemit_verify():
        
        params = {
            "id": disManualInputRemit_pageList, # 主键id
            "verifyRemark": "", # 审核备注
            "verifyResult": 1 # 1->通过 2-> 拒绝
        }                  
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
    
    step_appStore_store_dis_mortgage_common_fetchFreightTemplate()
    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_common_isStoreInTrafficControl()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_appStore_store_dis_mortgageOrder_searchCartProducts()
    step_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_dis_mortgageOrder_getMortgageAmount() # 查询店铺押货余额与限额
    if getMortgageAmount["depositAvailableAmount"] < mortgageOrder_detail["payAmount"]:
        remitMoney = mortgageOrder_detail["payAmount"] - getMortgageAmount["depositAvailableAmount"]
        # 保证金调整
        step_mgmt_store_getStoreByCode()
        step_01_mgmt_inventory_disManualInputRemit_pageList() # 拒绝所有待申请的手工录入款
        if disManualInputRemit_pageList:
            for disManualInputRemit_id in disManualInputRemit_pageList:
                step_01_mgmt_inventory_disManualInputRemit_verify()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add()
        step_mgmt_inventory_disManualInputRemit_pageList()
        step_mgmt_inventory_disManualInputRemit_verify()
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

    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == "" # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == mortgageOrder_detail["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == "" # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == mortgageOrder_detail["orderSn"] # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == "" # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-店铺运营后台-押货-工行代扣+保证金")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_4(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号

    disManualInputRemit_pageList = [] # 85折手工录入流水分页搜索列表:是否有待审核的申请
    remitMoney = 0 # 录入金额
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                    "balance": balance,
                    "payAmount": mortgageOrder_detail["payAmount"],
                    "payWays":[
                        {
                            "name":"押货保证金支付",
                            "payAmount":balance,
                            "data":None
                        },
                        {
                            "name":getSignBankAccountList[0]["accountBank"],
                            "payAmount":mortgageOrder_detail["payAmount"]-balance,
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
            "payType": 4, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
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
                {
                    "itemCode": searchProductPage02["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": mortgageOrder_detail["orderSn"], # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"

    # 保证金调整
    @allure.step("根据服务中心编号获取服务中心信息")
    def step_mgmt_store_getStoreByCode():
        
        nonlocal getStoreByCode
        params = {
            "code" : login_store_85["data"]["storeCode"],  # 服务中心编号
        }                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreByCode = r.json()["data"]
      
    @allure.step("85折手工录入流水分页搜索列表:是否有待审核的申请")
    def step_01_mgmt_inventory_disManualInputRemit_pageList():
        
        nonlocal disManualInputRemit_pageList
        data = {
            "monthrange": None,
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "companyCode": None, # 分公司code
            "sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "payAccountBankName": None, # 付款银行
            "verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
            "verifyStatus": 0, # 审核状态 0 待审核 1 已审核
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    disManualInputRemit_pageList.append(i["id"])

    @allure.step("85折手工录入流水单个审核:拒绝待审核的申请")
    def step_01_mgmt_inventory_disManualInputRemit_verify():
        
        params = {
            "id": disManualInputRemit_id, # 主键id
            "verifyRemark": "", # 审核备注
            "verifyResult": 2 # 1->通过 2-> 拒绝
        }                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
              
    @allure.step("查询分公司银行账号")
    def step_mgmt_sys_getAccountList():
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreByCode["store"]["companyCode"],  # 公司编码
        }
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getAccountList = r.json()["data"]
                
    @allure.step("通过storeCode获取银行账户资料信息")
    def step_mgmt_store_getBankAccountList():
        
        nonlocal getBankAccountList
        params = {
            "storeCode" : getStoreByCode["store"]["code"],  # 服务中心编号
        }             
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBankAccountList = r.json()["data"]
                        
    @allure.step("1:3押货余额及85折保证金余额查询")
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        
        nonlocal getStoreWalletMsg
        params = {
            "storeCode" : getStoreByCode["store"]["code"],  # 服务中心编号
        }                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreWalletMsg = r.json()["data"]
                
    @allure.step("85折手工录入流水")
    def step_mgmt_inventory_disManualInputRemit_add(): 
                
        data = {
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "storeName": getStoreByCode["store"]["name"], # 店铺名称
            "companyCode": getStoreByCode["store"]["companyCode"], # 分公司code
            "companyName": getAccountList[0]["accountName"], # 分公司名称
            "leaderName": getStoreByCode["user"]["realname"],
            "changeReason": "其他",
            "payAccount": "", # 付款账号
            "payAccountBankName": "", # 付款银行名称
            "receiptAccount": "",  # 收款账号
            "receiptBankName": "", # 收款银行名称
            "remitMoney": remitMoney, # 款项金额
            "sourceType": 3, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "inputRemark": "小何录入款项" # 录入备注
        } 
        if remitMoney > 0: # 服务中心付款
            data["payAccount"] = getBankAccountList[0]["account"]
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"]
            data["receiptBankName"] = getAccountList[0]["bankType"]
        elif remitMoney < 0: # 公司付款
            data["payAccount"] = getAccountList[0]["account"]
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"]
            data["receiptBankName"] = getBankAccountList[0]["branch"]             
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    @allure.step("85折手工录入流水分页搜索列表,获取id")
    def step_mgmt_inventory_disManualInputRemit_pageList():
        
        nonlocal disManualInputRemit_pageList
        data = {
            "monthrange": None,
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "companyCode": None, # 分公司code
            "sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "payAccountBankName": None, # 付款银行
            "verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
            "verifyStatus": 0, # 审核状态 0 待审核 1 已审核
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            disManualInputRemit_pageList = r.json()["data"]["list"][0]["id"]
            
    @allure.step("85折手工录入流水单个审核")
    def step_mgmt_inventory_disManualInputRemit_verify():
        
        params = {
            "id": disManualInputRemit_pageList, # 主键id
            "verifyRemark": "", # 审核备注
            "verifyResult": 1 # 1->通过 2-> 拒绝
        }                  
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
    
    step_appStore_store_dis_mortgage_common_fetchFreightTemplate()
    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_common_isStoreInTrafficControl()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_appStore_store_dis_mortgageOrder_searchCartProducts()
    step_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_dis_mortgageOrder_getMortgageAmount() # 查询店铺押货余额与限额
    if getMortgageAmount["depositAvailableAmount"] <= 0 or getMortgageAmount["depositAvailableAmount"] >= mortgageOrder_detail["payAmount"]:
        remitMoney = mortgageOrder_detail["payAmount"]/2 - getMortgageAmount["depositAvailableAmount"]
        # 保证金调整
        step_mgmt_store_getStoreByCode()
        step_01_mgmt_inventory_disManualInputRemit_pageList() # 拒绝所有待申请的手工录入款
        if disManualInputRemit_pageList:
            for disManualInputRemit_id in disManualInputRemit_pageList:
                step_01_mgmt_inventory_disManualInputRemit_verify()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add()
        step_mgmt_inventory_disManualInputRemit_pageList()
        step_mgmt_inventory_disManualInputRemit_verify()
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

    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "工行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 14, # 支付渠道 工行代扣
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] is None # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "工行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 0 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-店铺运营后台-押货-建行代扣+保证金")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_5(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号

    disManualInputRemit_pageList = [] # 85折手工录入流水分页搜索列表:是否有待审核的申请
    remitMoney = 0 # 录入金额
    getStoreWalletMsg = None # 现有押货余额及保证金信息
    getAccountList = None # 分公司银行账号信息
    getStoreByCode = None # 服务中心信息
    getBankAccountList = None # 服务中心银行账号信息
    
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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
            "accountName": getSignBankAccountList[1]["accountName"], # 户名(仅钱包支付不用传)
            "bankAccount": getSignBankAccountList[1]["account"], # 代扣账户(仅钱包支付不用传)
            "bankName": getSignBankAccountList[1]["accountBank"], # 开户银行名称(仅钱包支付不用传)
            "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
            "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
            "extJson": str(
                {
                    "balance": balance,
                    "payAmount": mortgageOrder_detail["payAmount"],
                    "payWays":[
                        {
                            "name":"押货保证金支付",
                            "payAmount":balance,
                            "data":None
                        },
                        {
                            "name":getSignBankAccountList[1]["accountBank"],
                            "payAmount":mortgageOrder_detail["payAmount"]-balance,
                            "data":{
                                "accountName":getSignBankAccountList[1]["accountName"],
                                "account":getSignBankAccountList[1]["account"],
                                "accountBank":getSignBankAccountList[1]["accountBank"],
                                "accountType":getSignBankAccountList[1]["accountType"],
                                "isSigned":getSignBankAccountList[1]["isSigned"]
                            }
                        }
                    ]
                }
            ), # 扩展参数
            "payAmount": mortgageOrder_detail["payAmount"],
            "payChannel": "WEB", # 支付渠道 WEB/APP
            "payType": 5, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
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
                {
                    "itemCode": searchProductPage02["productCode"], # 商品编号
                    "num": mortgageNum, # 数量
                    "skuCode": ""
                }
            ],
            "mortgageOrderNo": mortgageOrder_detail["orderSn"], # 押货单号
            "optime": time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "status": 2,
            "type": 5 # 1:3是2,85折是5
        }
        with _esb_third_mortgage_syncDeliveryInfo(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["resultMsg"] == "success"

    # 保证金调整
    @allure.step("根据服务中心编号获取服务中心信息")
    def step_mgmt_store_getStoreByCode():
        
        nonlocal getStoreByCode
        params = {
            "code" : login_store_85["data"]["storeCode"],  # 服务中心编号
        }                 
        with _mgmt_store_getStoreByCode(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreByCode = r.json()["data"]
      
    @allure.step("85折手工录入流水分页搜索列表:是否有待审核的申请")
    def step_01_mgmt_inventory_disManualInputRemit_pageList():
        
        nonlocal disManualInputRemit_pageList
        data = {
            "monthrange": None,
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "companyCode": None, # 分公司code
            "sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "payAccountBankName": None, # 付款银行
            "verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
            "verifyStatus": 0, # 审核状态 0 待审核 1 已审核
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    disManualInputRemit_pageList.append(i["id"])

    @allure.step("85折手工录入流水单个审核:拒绝待审核的申请")
    def step_01_mgmt_inventory_disManualInputRemit_verify():
        
        params = {
            "id": disManualInputRemit_id, # 主键id
            "verifyRemark": "", # 审核备注
            "verifyResult": 2 # 1->通过 2-> 拒绝
        }                 
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
              
    @allure.step("查询分公司银行账号")
    def step_mgmt_sys_getAccountList():
        
        nonlocal getAccountList
        params = {
            "companyCode" : getStoreByCode["store"]["companyCode"],  # 公司编码
        }
        params["companyCode"] = getStoreByCode["store"]["companyCode"]                    
        with _mgmt_sys_getAccountList(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getAccountList = r.json()["data"]
                
    @allure.step("通过storeCode获取银行账户资料信息")
    def step_mgmt_store_getBankAccountList():
        
        nonlocal getBankAccountList
        params = {
            "storeCode" : getStoreByCode["store"]["code"],  # 服务中心编号
        }             
        with _mgmt_store_getBankAccountList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getBankAccountList = r.json()["data"]
                        
    @allure.step("1:3押货余额及85折保证金余额查询")
    def step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg():
        
        nonlocal getStoreWalletMsg
        params = {
            "storeCode" : getStoreByCode["store"]["code"],  # 服务中心编号
        }                  
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            getStoreWalletMsg = r.json()["data"]
                
    @allure.step("85折手工录入流水")
    def step_mgmt_inventory_disManualInputRemit_add(): 
                
        data = {
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "storeName": getStoreByCode["store"]["name"], # 店铺名称
            "companyCode": getStoreByCode["store"]["companyCode"], # 分公司code
            "companyName": getAccountList[0]["accountName"], # 分公司名称
            "leaderName": getStoreByCode["user"]["realname"],
            "changeReason": "其他",
            "payAccount": "", # 付款账号
            "payAccountBankName": "", # 付款银行名称
            "receiptAccount": "",  # 收款账号
            "receiptBankName": "", # 收款银行名称
            "remitMoney": remitMoney, # 款项金额
            "sourceType": 3, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "inputRemark": "小何录入款项" # 录入备注
        } 
        if remitMoney > 0: # 服务中心付款
            data["payAccount"] = getBankAccountList[0]["account"]
            data["payAccountBankName"] = getBankAccountList[0]["branch"]
            data["receiptAccount"] = getAccountList[0]["account"]
            data["receiptBankName"] = getAccountList[0]["bankType"]
        elif remitMoney < 0: # 公司付款
            data["payAccount"] = getAccountList[0]["account"]
            data["payAccountBankName"] = getAccountList[0]["bankType"]
            data["receiptAccount"] = getBankAccountList[0]["account"]
            data["receiptBankName"] = getBankAccountList[0]["branch"]             
        with _mgmt_inventory_disManualInputRemit_add(data, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True

    @allure.step("85折手工录入流水分页搜索列表,获取id")
    def step_mgmt_inventory_disManualInputRemit_pageList():
        
        nonlocal disManualInputRemit_pageList
        data = {
            "monthrange": None,
            "storeCode": getStoreByCode["store"]["code"], # 店铺编号
            "companyCode": None, # 分公司code
            "sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
            "payAccountBankName": None, # 付款银行
            "verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
            "verifyStatus": 0, # 审核状态 0 待审核 1 已审核
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_inventory_disManualInputRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            disManualInputRemit_pageList = r.json()["data"]["list"][0]["id"]
            
    @allure.step("85折手工录入流水单个审核")
    def step_mgmt_inventory_disManualInputRemit_verify():
        
        params = {
            "id": disManualInputRemit_pageList, # 主键id
            "verifyRemark": "", # 审核备注
            "verifyResult": 1 # 1->通过 2-> 拒绝
        }                  
        with _mgmt_inventory_disManualInputRemit_verify(params, access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"] is True
    
    step_appStore_store_dis_mortgage_common_fetchFreightTemplate()
    step_appStore_store_dis_mortgageOrder_searchProductPage()
    step_appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling()
    step_appStore_store_dis_mortgageOrder_pushProductsToCart()
    step_appStore_common_isStoreInTrafficControl()
    step_appStore_store_dis_mortgageOrder_mortgage()
    step_appStore_store_dis_mortgageOrder_searchCartProducts()
    step_appStore_store_dis_mortgageOrder_detail_id()
    step_appStore_store_dis_mortgageOrder_getMortgageAmount() # 查询店铺押货余额与限额
    if getMortgageAmount["depositAvailableAmount"] <= 0 or getMortgageAmount["depositAvailableAmount"] >= mortgageOrder_detail["payAmount"]:
        remitMoney = mortgageOrder_detail["payAmount"]/2 - getMortgageAmount["depositAvailableAmount"]
        # 保证金调整
        step_mgmt_store_getStoreByCode()
        step_01_mgmt_inventory_disManualInputRemit_pageList() # 拒绝所有待申请的手工录入款
        if disManualInputRemit_pageList:
            for disManualInputRemit_id in disManualInputRemit_pageList:
                step_01_mgmt_inventory_disManualInputRemit_verify()
        step_mgmt_sys_getAccountList()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_disManualInputRemit_getStoreWalletMsg()
        step_mgmt_inventory_disManualInputRemit_add()
        step_mgmt_inventory_disManualInputRemit_pageList()
        step_mgmt_inventory_disManualInputRemit_verify()
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

    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[1]["account"] # 银行账号
                    assert i["payTypeName"] == "建行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[1]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[1]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 15, # 支付渠道 14工行代扣 15建行
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "建行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 1 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 手续费明细表
    totalPage = 1 # 有多少页
    @allure.step("分页列表-手续费明细表:获取页数")
    def step_01_mgmt_inventory_disChargeDetail_pageList():
        
        nonlocal totalPage
        data = {
            "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "companyCode":[mortgageOrder_detail["companyCode"]], # 分公司
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum": 1,
            "pageSize": 10
        }          
        with _mgmt_inventory_disChargeDetail_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            totalPage = r.json()["data"]["totalPage"]

    @allure.step("分页列表-手续费明细表")
    def step_02_mgmt_inventory_disChargeDetail_pageList():
        
        data = {
            "month": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "companyCode":[mortgageOrder_detail["companyCode"]], # 分公司
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum": totalPage,
            "pageSize": 10
        }          
        with _mgmt_inventory_disChargeDetail_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert str(r.json()["data"]["list"][-1]["month"]) == time.strftime("%Y%m",time.localtime(time.time())) # 所属月份
            assert r.json()["data"]["list"][-1]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][-1]["storeName"] == mortgageOrder_detail["storeName"] # 服务中心名称
            assert r.json()["data"]["list"][-1]["leaderName"] == mortgageOrder_detail["leader"] # 服务中心负责人
            assert r.json()["data"]["list"][-1]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司编号
            assert r.json()["data"]["list"][-1]["changeTypeExcel"] == "建行签约代扣" # 手续费类型
            assert r.json()["data"]["list"][-1]["rate"] is None # 费率
            assert r.json()["data"]["list"][-1]["balance"] == mortgageOrder_detail["payRecord"]["payMoney"] # 金额
            assert r.json()["data"]["list"][-1]["charge"] == 0.5 # 手续费
            assert r.json()["data"]["list"][-1]["orderSn"] == mortgageOrder_detail["orderSn"] # 押货单号
            assert r.json()["data"]["list"][-1]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][-1]["payTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付时间
            
    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()
    step_01_mgmt_inventory_disChargeDetail_pageList() # 手续费明细表
    step_02_mgmt_inventory_disChargeDetail_pageList()


@allure.title("85云商-店铺运营后台-押货-工行代扣-批量取消")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_2_batchCancel(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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

    # 批量取消押货单
    
    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        params = {"id": id}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单批量取消") 
    def step_mgmt_inventory_dis_mortgage_order_batchCancel():
        
        data = {
            "orderSn": mortgageOrder_detail["orderSn"], # 押货单号
        }           
        with _mgmt_inventory_dis_mortgage_order_batchCancel(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 批量取消押货单
    step_mgmt_inventory_dis_mortgage_order_batchCancel() 
    step_appStore_store_dis_mortgageOrder_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"][:3]: 
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == mortgageOrder_detail["orderSn"] # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == mortgageOrder_detail["orderSn"] # 流水号 
                else:                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

            for i in r.json()["data"]["list"][3:]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "工行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 14, # 支付渠道 工行代扣
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] is None # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "工行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 0 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-店铺运营后台-押货-工行代扣-押货单修改")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_2_modify(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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

    # 押货单修改
    
    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        params = {"id": id}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单修改") 
    def step_mgmt_inventory_dis_mortgage_order_modify():

        data = {
            "orderSn": mortgageOrder_detail["orderSn"], # 押货单编号
            "productList": [
                {
                    "mortgageNum": mortgageOrder_detail["productList"][0]["mortgageNum"] - 1, # 押货商品数量
                    "mortgagePrice": mortgageOrder_detail["productList"][0]["mortgagePrice"], # 商品押货价
                    "productCode": mortgageOrder_detail["productList"][0]["productCode"] # 商品编码
                }
            ]
        }           
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 押货单修改
    step_mgmt_inventory_dis_mortgage_order_modify() 
    step_appStore_store_dis_mortgageOrder_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用", "其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["remark"] == "押货调整" and i["remark"] == "押货调整":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "工行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 14, # 支付渠道 工行代扣
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] is None # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "工行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 0 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))

    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": 1, # 出入库：1入库 2出库
            "bizType": 1, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))      
    
    step_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()


@allure.title("85云商-店铺运营后台-押货-工行代扣-欠货停发")
@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
def test_wallet_pay_2_stopDeliver(login_store_85):
    
    fetchFreightTemplate = None # 获取最新的运费计算模板
    fetchPieceBoxCostCeiling = None # 获取启用中的拼箱费上限
    searchProductPage = None # 商品信息
    searchProductPage02 = None # 商品信息
    isStoreInTrafficControl = None # 店铺是否处于交通管控
    mortgageNum = 2 # 押货数量
    id = None # 押货单id
    searchCartProducts = None # 获取购物车数据
    mortgageOrder_detail = None # 押货单详情
    getMortgageAmount = None # 查询店铺押货余额与限额
    balance = None # 保证金余额
    getSignBankAccountList = None # 签约银行信息
    payOrderNo = None # 支付-流水号
    store_token = os.environ["store_token_85"]
    access_token = os.environ["access_token"]

    @allure.step("获取最新的运费计算模板")  
    def step_appStore_store_dis_mortgage_common_fetchFreightTemplate():
        
        nonlocal fetchFreightTemplate
        with _appStore_store_dis_mortgage_common_fetchFreightTemplate(store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            fetchFreightTemplate = r.json()["data"]

    @allure.step("关键字搜索可押货商品分页,获取商品信息")            
    def step_appStore_store_dis_mortgageOrder_searchProductPage():
        
        nonlocal searchProductPage, searchProductPage02
        params = {
            "keyword": AG, # 搜索关键字
            "pageNum": 1,
            "pageSize": 20
        }
        with _appStore_store_dis_mortgageOrder_searchProductPage(params, store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG:
                    searchProductPage = d
                    break  
            for d in r.json()["data"]["list"]:
                if d["productCode"] == AG2:
                    searchProductPage02 = d
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
            {
                "mortgageNum": mortgageNum, # 押货商品数量
                "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                "productCode": searchProductPage02["productCode"] # 押货商品编码
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
                },
                {
                    "mortgageNum": mortgageNum, # 押货商品数量
                    "mortgagePrice": searchProductPage02["mortgagePrice"], # 商品押货价
                    "productCode": searchProductPage02["productCode"] # 押货商品编码
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

    # 押货单欠货停发
    
    @allure.step("押货单详情(修改)") 
    def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
        
        params = {"id": id}           
        with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单修改") 
    def step_mgmt_inventory_dis_mortgage_order_modify():

        data = {
            "orderSn": mortgageOrder_detail["orderSn"], # 押货单编号
            "productList": [
                {
                    "mortgageNum": mortgageOrder_detail["productList"][0]["mortgageNum"] - 1, # 押货商品数量
                    "mortgagePrice": mortgageOrder_detail["productList"][0]["mortgagePrice"], # 商品押货价
                    "productCode": mortgageOrder_detail["productList"][0]["productCode"] # 商品编码
                }
            ]
        }           
        with _mgmt_inventory_dis_mortgage_order_modify(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("押货单欠货停发") 
    def step_mgmt_inventory_dis_mortgage_order_stopDeliver():
        
        params = {
            "orderSn": mortgageOrder_detail["orderSn"], # 押货单编号
        }           
        with _mgmt_inventory_dis_mortgage_order_stopDeliver(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

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
    step_mgmt_inventory_dis_mortgage_order_detailForModify_id() # 押货单欠货停发
    step_mgmt_inventory_dis_mortgage_order_modify()
    step_mgmt_inventory_dis_mortgage_order_stopDeliver() 
    step_appStore_store_dis_mortgageOrder_detail_id()
    
    # 押货保证金详情表
    @allure.step("押货保证金详情表")
    def step_01_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": None, # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"][:3]] == ["其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货退货"]
            for i in r.json()["data"]["list"][:3]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 6:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] is None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 关联单号
                    assert i["businessNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 6:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] is None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 关联单号
                    assert i["businessNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 流水号 
                else:                                            
                    assert i["dealTypeName"] == "押货退货"
                    assert i["recordType"] == 5 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 6:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] is None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] is None # 备注
                    assert i["mortgageOrderNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 关联单号
                    assert i["businessNo"] == "无" # 流水号 

    @allure.step("押货保证金详情表")
    def step_02_mgmt_inventory_deposit_storeDepositDetail():
            
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "mortgageOrderNoOrBusinessNo": mortgageOrder_detail["orderSn"], # 押货单号or流水号
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
            assert [i["dealTypeName"] for i in r.json()["data"]["list"]] == ["押货使用", "其他扣款(运费和拼箱费)", "其他扣款(运费和拼箱费)", "押货使用", "汇押货款"]
            for i in r.json()["data"]["list"]:
                if i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "运费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffFreightCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "运费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号
                elif i["dealTypeName"] == "其他扣款(运费和拼箱费)" and i["remark"] == "拼箱费":
                    assert i["dealTypeName"] == "其他扣款(运费和拼箱费)"
                    assert i["recordType"] == 10 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffPieceBoxCost"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "拼箱费" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                elif i["remark"] == "押货调整" and i["remark"] == "押货调整":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 5:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == None # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == "押货调整" # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == "无" # 流水号 
                elif i["dealTypeName"] == "押货使用":                       
                    assert i["dealTypeName"] == "押货使用"
                    assert i["recordType"] == 4 # 款项类型
                    assert i["recordTypeName"] == "无" # 款项类型名称
                    for d in mortgageOrder_detail["operationLogList"]:
                        if d["logType"] == 1:
                            assert i["diffMoney"] == -d["diffMortgageAmount"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "保证金" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == str(int(payOrderNo) + 1) # 流水号 
                else:                       
                    assert i["dealTypeName"] == "汇押货款"
                    assert i["recordType"] == 1 # 款项类型
                    assert i["recordTypeName"] == "汇押货款" # 款项类型名称
                    assert i["diffMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 交易金额 
                    assert i["bankAccount"] == getSignBankAccountList[0]["account"] # 银行账号
                    assert i["payTypeName"] == "工行代扣" # 支付方式
                    assert i["remark"] == None # 备注
                    assert i["mortgageOrderNo"] == mortgageOrder_detail["orderSn"] # 关联单号
                    assert i["businessNo"] == payOrderNo # 流水号 

    # 银行汇款流水查询
    @allure.step("85折银行流水分页搜索列表")
    def step_mgmt_inventory_disBankRemit_pageList():
        
        data = {
            "storeCode": mortgageOrder_detail["storeCode"], # 店铺编号
            "companyCode":None, # 分公司code
            "payAccountBankName":None, # 付款银行
            "handleType": 1, # 手工/自动类型 1、自动处理 2、手工处理
            "pageNum":1,
            "pageSize":10,
            "sourceType":[1], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
        }            
        with _mgmt_inventory_disBankRemit_pageList(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["waterNo"] == payOrderNo # 流水号
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["companyCode"] == mortgageOrder_detail["companyCode"] # 分公司
            assert r.json()["data"]["list"][0]["remitMoney"] == mortgageOrder_detail["payRecord"]["payMoney"] # 款项金额
            assert r.json()["data"]["list"][0]["sourceType"] == 1 # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
            assert r.json()["data"]["list"][0]["sourceTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["dealType"] == 1 # # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
            assert r.json()["data"]["list"][0]["dealTypeName"] == "汇押货款"
            assert r.json()["data"]["list"][0]["bankPaymentTime"] == None # 银行到账时间
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["systemPaymentTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 系统到账时间
            assert r.json()["data"]["list"][0]["payAccountBankName"] == getSignBankAccountList[0]["accountBank"] # 付款银行
            assert r.json()["data"]["list"][0]["payAccount"] == getSignBankAccountList[0]["account"] # 付款账号
            assert r.json()["data"]["list"][0]["handleType"] == 1 # 手工/自动类型 1、自动处理 2、手工处理
            assert r.json()["data"]["list"][0]["handleTypeName"] == "自动处理"
            assert r.json()["data"]["list"][0]["inputRemark"] == "支付充值" # 录入备注
            assert r.json()["data"]["list"][0]["verifyer"] == None # 审核人
            assert r.json()["data"]["list"][0]["dealTime"] == None # 审核时间
            assert r.json()["data"]["list"][0]["verifyRemark"] == None # 审核备注    

    # 支付渠道对账
    @allure.step("查询对公支付对账结果信息")
    def step_mgmt_pay_verifyAcct_querytob():
        
        data = {
            "tradeTimeOrder": "DESC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
            "companyNo": mortgageOrder_detail["companyCode"], # 分公司编号
            "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
            "channelCode": 14, # 支付渠道 工行代扣
            "status": None, # 平账状态
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "pageNum":1,
            "pageSize":10
        }           
        with _mgmt_pay_verifyAcct_querytob(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["bankSeq"] is not None # 银行流水号
            assert r.json()["data"]["list"][0]["companyName"] == mortgageOrder_detail["companyName"][10:] # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == mortgageOrder_detail["storeCode"] # 服务中心编号
            assert r.json()["data"]["list"][0]["payNo"] == payOrderNo # 支付流水号
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["list"][0]["tradeTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time())) # 支付完成时间
            assert r.json()["data"]["list"][0]["bankAmount"] is None # 银行回调金额
            assert r.json()["data"]["list"][0]["amount"] == mortgageOrder_detail["payRecord"]["payMoney"] # 订单交易金额
            assert r.json()["data"]["list"][0]["channelName"] == "工行签约代扣" # 支付渠道
            assert r.json()["data"]["list"][0]["tradeType"] == "交易" # 类型
            assert r.json()["data"]["list"][0]["status"] == 0 # 平账状态: 0-未对账,1-正常,2-异常
            assert r.json()["data"]["list"][0]["remark"] is None # 备注  

    # 库存增减明细表
    @allure.step("查询库存明细")
    def step_01_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][0]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            assert r.json()["data"]["page"]["list"][1]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][1]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][1]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][1]["diffNum"] == mortgageOrder_detail["productList"][0]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            
    @allure.step("查询库存明细")
    def step_02_mgmt_dis_inventory_detail():
            
        params = {
            "type": None, # 出入库：1入库 2出库
            "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
            "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
            "storeCode": mortgageOrder_detail["storeCode"], # 服务中心编号
            "productCode": mortgageOrder_detail["productList"][1]["productCode"], # 产品编号
            "pageNum": 1,
            "pageSize": 10
        }             
        with _mgmt_dis_inventory_detail(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["page"]["list"][0]["bizType"] == 2 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][0]["bizNo"][:14] == F'TYH{mortgageOrder_detail["orderSn"][2:13]}' # 单号
            assert r.json()["data"]["page"]["list"][0]["type"] == 2 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][0]["diffNum"] == -mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
            assert r.json()["data"]["page"]["list"][1]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
            assert r.json()["data"]["page"]["list"][1]["bizNo"] == mortgageOrder_detail["orderSn"] # 单号
            assert r.json()["data"]["page"]["list"][1]["type"] == 1 # 出入库：1入库 2出库
            assert r.json()["data"]["page"]["list"][1]["diffNum"] == mortgageOrder_detail["productList"][1]["mortgageNum"] # 押货数量              
            assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][1]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))    
    
    step_01_mgmt_inventory_deposit_storeDepositDetail() # 押货保证金详情表
    step_02_mgmt_inventory_deposit_storeDepositDetail()
    step_mgmt_inventory_disBankRemit_pageList() # 银行汇款流水查询
    step_mgmt_pay_verifyAcct_querytob() # 支付渠道对账
    step_01_mgmt_dis_inventory_detail() # 库存增减明细表
    step_02_mgmt_dis_inventory_detail()





