# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import _mgmt_inventory_remit_getSourceTypeByRemitType # 按银行流水类型获取款项映射列表
from api.mall_mgmt_application._mgmt_inventory_common_getStoreInfo import _mgmt_inventory_common_getStoreInfo # 获取服务中心信息
from api.mall_center_sys._mgmt_sys_getAccountList import _mgmt_sys_getAccountList # 查询分公司银行账号
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_getMortgageAmountByStore import _mgmt_inventory_mortgageAmount_getMortgageAmountByStore # 根据storeCode查询押货余额主表数据
from setting import P1, P2, P3, username, mobile, username_vip, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/mortgageAmount/getMortgageAmountByStore")
class TestClass:
    """
    根据storeCode查询押货余额主表数据
    /mgmt/inventory/mortgageAmount/getMortgageAmountByStore
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("根据storeCode查询押货余额主表数据: 手工录入流水时检查")
    def test_mgmt_inventory_mortgageAmount_getMortgageAmountByStore(self):
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        getStoreInfo = None # 获取服务中心信息
        getAccountList = None # 查询分公司银行账号
        getMortgageAmountByStore = None # 根据storeCode查询押货余额主表数据
        
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
  
        step_mgmt_inventory_remit_getSourceTypeByRemitType()
        step_mgmt_inventory_common_getStoreInfo()
        step_mgmt_sys_getAccountList()
        step_mgmt_inventory_mortgageAmount_getMortgageAmountByStore()

        

