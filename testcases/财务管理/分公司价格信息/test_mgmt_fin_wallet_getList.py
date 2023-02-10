# coding:utf-8

from api.mall_mgmt_application._mgmt_product_filiale_getFilialePriceList import data ,_mgmt_product_filiale_getFilialePriceList
from setting import P1, P2, P3, username, mobile

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/filiale/getFilialePriceList")
class TestClass:
    """
    分公司价格信息列表查询
    /mgmt/product/filiale/getFilialePriceList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
   
    @allure.severity(P2)
    @allure.title("分公司价格信息列表查询-成功路径: 支持模糊查询产品编号检查")
    def test_01_mgmt_product_filiale_getFilialePriceList(self):
        
        getFilialePriceList = None # 分公司价格信息列表查询
        
        @allure.step("分公司价格信息列表查询: 获取产品编号")
        def step_01_mgmt_product_filiale_getFilialePriceList():
            
            nonlocal getFilialePriceList
            data = deepcopy(self.data)              
            with _mgmt_product_filiale_getFilialePriceList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getFilialePriceList = r.json()["data"]["list"][0]["serialNo"]
       
        @allure.step("分公司价格信息列表查询: 精确查询产品编号检查")
        def step_02_mgmt_product_filiale_getFilialePriceList():
            
            data = deepcopy(self.data)
            data["serialNo"] = getFilialePriceList               
            with _mgmt_product_filiale_getFilialePriceList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getFilialePriceList in set(d["serialNo"] for d in r.json()["data"]["list"])

        @allure.step("分公司价格信息列表查询: 模糊查询产品编号检查")
        def step_03_mgmt_product_filiale_getFilialePriceList():
            
            data = deepcopy(self.data)
            data["serialNo"] = getFilialePriceList[:-1]               
            with _mgmt_product_filiale_getFilialePriceList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert getFilialePriceList[:-1] in set(d["serialNo"] for d in r.json()["data"]["list"])
        
        step_01_mgmt_product_filiale_getFilialePriceList()
        step_02_mgmt_product_filiale_getFilialePriceList()
        step_03_mgmt_product_filiale_getFilialePriceList()


 