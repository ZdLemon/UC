# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_book_total import params, _mgmt_inventory_book_total
from api.mall_mgmt_application._mgmt_product_cfg_menu_catalog import _mgmt_product_cfg_menu_catalog
from setting import P1, P2, P3, productCode, productCode_title, store, BASE_URL

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/book/total")
@pytest.mark.skip()
class TestClass:
    """
    查询实时库存台账合计合计
    /mgmt/inventory/book/total
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询实时库存台账合计-实时库存-成功路径: 查询默认条件检查")
    def test_01_mgmt_inventory_book_total(self, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 上期结存，期末库存，入库汇总（押货数量+），出库汇总
        sql = f"SELECT sum(prior_balance), sum(stock), sum(mortgage_num) + sum(order_return), sum(mortgage_return) + sum(order_num)\
            FROM dis_inventory;"
        db.execute(sql)
        priorBalance, productNum, stockIn, stockOut =  db.fetchall()[0]
            
        params = deepcopy(self.params)                 
        with _mgmt_inventory_book_total(params, self.access_token) as r:
            assert r.json()["data"]["priorBalance"] == priorBalance
            assert r.json()["data"]["productNum"] ==  productNum
            assert r.json()["data"]["stockIn"] == stockIn
            assert r.json()["data"]["stockOut"] == stockOut

    @allure.severity(P2)
    @allure.title("查询实时库存台账合计-实时库存-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_book_total(self, companyCode, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 上期结存，期末库存，入库汇总（押货数量+），出库汇总
        sql = f"SELECT sum(prior_balance), sum(stock), sum(mortgage_num) + sum(order_return), sum(mortgage_return) + sum(order_num)\
            FROM dis_inventory where company_code = '{companyCode}';"
        db.execute(sql)
        priorBalance, productNum, stockIn, stockOut =  db.fetchall()[0]
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode                
        with _mgmt_inventory_book_total(params, self.access_token) as r:
            assert r.json()["data"]["priorBalance"] == priorBalance
            assert r.json()["data"]["productNum"] ==  productNum
            assert r.json()["data"]["stockIn"] == stockIn
            assert r.json()["data"]["stockOut"] == stockOut

    @allure.severity(P2)
    @allure.title("查询实时库存台账合计-实时库存-成功路径: 查询服务中心编号检查")
    def test_03_mgmt_inventory_book_total(self, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 上期结存，期末库存，入库汇总（押货数量+），出库汇总
        sql = f"SELECT sum(prior_balance), sum(stock), sum(mortgage_num) + sum(order_return), sum(mortgage_return) + sum(order_num)\
            FROM dis_inventory where store_code = '{store}';"
        db.execute(sql)
        priorBalance, productNum, stockIn, stockOut =  db.fetchall()[0]
            
        params = deepcopy(self.params) 
        params["storeCode"] = store               
        with _mgmt_inventory_book_total(params, self.access_token) as r:
            assert r.json()["data"]["priorBalance"] == priorBalance
            assert r.json()["data"]["productNum"] ==  productNum
            assert r.json()["data"]["stockIn"] == stockIn
            assert r.json()["data"]["stockOut"] == stockOut
     
    @allure.severity(P2)
    @allure.title("查询实时库存台账合计-实时库存-成功路径: 支持模糊查询产品编码检查")
    @pytest.mark.parametrize("product", [productCode, productCode[:-1]], ids=["精确产品编码", "产品编码的一部分"])
    def test_05_mgmt_inventory_book_total(self, product, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 上期结存，期末库存，入库汇总（押货数量+），出库汇总
        sql = f"SELECT sum(prior_balance), sum(stock), sum(mortgage_num) + sum(order_return), sum(mortgage_return) + sum(order_num)\
            FROM dis_inventory where product_code LIKE '{product}%';"
        db.execute(sql)
        priorBalance, productNum, stockIn, stockOut =  db.fetchall()[0]
            
        params = deepcopy(self.params) 
        params["product"] = product             
        with _mgmt_inventory_book_total(params, self.access_token) as r:
            assert r.json()["data"]["priorBalance"] == priorBalance
            assert r.json()["data"]["productNum"] ==  productNum
            assert r.json()["data"]["stockIn"] == stockIn
            assert r.json()["data"]["stockOut"] == stockOut

    @allure.severity(P2)
    @allure.title("查询实时库存台账合计-实时库存-成功路径: 支持模糊查询产品名称检查")
    @pytest.mark.parametrize("product", [productCode_title, productCode_title[:-1]], ids=["精确产品名称", "产品名称的一部分"])
    def test_06_mgmt_inventory_book_total(self, product, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 上期结存，期末库存，入库汇总（押货数量+），出库汇总
        sql = f"SELECT sum(prior_balance), sum(stock), sum(mortgage_num) + sum(order_return), sum(mortgage_return) + sum(order_num)\
            FROM dis_inventory where product_code LIKE '{productCode}%';"
        db.execute(sql)
        priorBalance, productNum, stockIn, stockOut =  db.fetchall()[0]
            
        params = deepcopy(self.params) 
        params["product"] = product        
        with _mgmt_inventory_book_total(params, self.access_token) as r:
            assert r.json()["data"]["priorBalance"] == priorBalance
            assert r.json()["data"]["productNum"] ==  productNum
            assert r.json()["data"]["stockIn"] == stockIn
            assert r.json()["data"]["stockOut"] == stockOut


