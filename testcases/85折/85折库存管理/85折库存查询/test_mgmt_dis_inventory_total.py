# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_total import params ,_mgmt_dis_inventory_total

from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter

# TODO
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/total")
class TestClass:
    """
    库存合计
    /mgmt/dis-inventory/total
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("库存合计-成功路径: 查询默认条件检查")
    def test_01_mgmt_dis_inventory_total(self, db_mall_center_finance):
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}' \
                        and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
            
        params = deepcopy(self.params)                 
        with _mgmt_dis_inventory_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("库存合计-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_dis_inventory_total(self, companyCode, db_mall_center_finance):
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}' \
                        and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
            
        params = deepcopy(self.params) 
        params["companyCode"] = companyCode                
        with _mgmt_dis_inventory_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("库存合计-成功路径: 查询服务中心编号检查")
    def test_03_mgmt_dis_inventory_total(self, db_mall_center_finance):
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}' \
                        and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
            
        params = deepcopy(self.params) 
        params["storeCode"] = store_85                 
        with _mgmt_dis_inventory_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("库存合计-成功路径: 查询当前库存检查")
    @pytest.mark.parametrize("stockOperator,stock,ids", [
        (0, 10, "库存=10"), 
        (1, 10, "库存>=10"), 
        (2, 10, "库存>10"), 
        (3, 10, "库存<=10"), 
        (4, 10, "库存<10")
    ])
    def test_04_mgmt_dis_inventory_total(self, stockOperator, stock, ids, db_mall_center_finance):
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}' \
                        and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
            
        params = deepcopy(self.params)
        params["stockOperator"] = stockOperator
        params["stock"] = stock
        with _mgmt_dis_inventory_total(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200


