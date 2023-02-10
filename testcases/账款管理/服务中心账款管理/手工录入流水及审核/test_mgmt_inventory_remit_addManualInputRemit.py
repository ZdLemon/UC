# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
from api.mall_mgmt_application._mgmt_store_getBankAccountList import _mgmt_store_getBankAccountList # 通过storeCode获取银行账户资料信息
from api.mall_mgmt_application._mgmt_inventory_remit_addManualInputRemit import _mgmt_inventory_remit_addManualInputRemit # 手工录入流水
from setting import P1, P2, P3, username, mobile, username_vip, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/remit/addManualInputRemit")
class TestClass:
    """
    手工录入流水
    /mgmt/inventory/remit/addManualInputRemit
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("手工录入流水-成功路径: 手工增押货款检查")
    def test_mgmt_inventory_remit_addManualInputRemit(self):
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        getBankAccountList = None # 通过storeCode获取银行账户资料信息
        remitMoney = 1000 # 金额
        
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
                "remitMoney": remitMoney, # 汇款金额
                "account": getBankAccountList[0]["account"], # 付款账号
                "bankName": getBankAccountList[0]["accountBank"], # 付款银行名称
                "remark": f"录入手工增押货款{remitMoney}元", # 备注
                "receiptAccount": getAccountList[0]["account"], # 收款账号
                "receiptBankName": getAccountList[0]["bankType"] # 收款银行名称
            }           
            with _mgmt_inventory_remit_addManualInputRemit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"] is True
    
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()
        step_mgmt_store_getBankAccountList()
        step_mgmt_inventory_remit_addManualInputRemit()

        

