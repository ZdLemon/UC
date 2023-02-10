# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_getSecondCouponGetDetailSum import data, _mgmt_fin_voucher_getSecondCouponGetDetailSum
from api.mall_mgmt_application._mgmt_fin_voucher_getSecondCouponGetDetail import data as data01, _mgmt_fin_voucher_getSecondCouponGetDetail
from setting import P1, P2, P3, username, mysql_host, mysql_passwd, mysql_port, mysql_user, store

from copy import deepcopy
import os
import allure
import pytest
import time
import pymysql
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/getSecondCouponGetDetailSum")
class TestClass:
    """
    秒返券获券合计
    /mgmt/fin/voucher/getSecondCouponGetDetailSum
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data01 = deepcopy(data01)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 查询会员卡号检查")
    def test_02_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, db_mall_center_finance):
        

        
        data = deepcopy(self.data)
        data["cardNo"] = username 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail where card_no = {username} and get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum = db.fetchall()[0][0]
               
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 单选查询顾客类型检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["vip顾客", "云商", "微店"])
    def test_03_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, memberType, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail where member_type = {memberType} and get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum = db.fetchall()[0][0]
                
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 查询来源订单检查")
    def test_04_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["sourceOrderNo"] = "SG942437220325000008" 
        data["getStartTime"] = ""
        data["getEndTime"] = ""
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail where source_order_no = 'SG942437220325000008';"
        db.execute(sql)
        datasum = db.fetchall()[0][0]
              
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] ==  datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 单选查询交易类型检查")
    @pytest.mark.parametrize("getType", [1, 2], ids=["购物获得", "月结更新"])
    def test_05_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, getType, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["getType"] = getType 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail where get_type = {getType} and get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum = db.fetchall()[0][0]
              
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计: 仅支持精确查询服务中心编号检查")
    def test_06_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store   
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail where source_store_code = {store} and get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum = db.fetchall()[0][0]
   
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 查询券状态检查")
    @pytest.mark.parametrize("couponStatus", [1, 2, 3, 4], ids=["待生效", "已生效", "退货失效", "月结失效"])
    def test_07_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, couponStatus, db_mall_center_finance):
               
        data = deepcopy(self.data)
        data["couponStatus"] = couponStatus 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail where coupon_status = {couponStatus} and get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum = db.fetchall()[0][0]
              
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 查询生成时间,默认本月检查")
    def test_08_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, db_mall_center_finance):
         
        data = deepcopy(self.data) 
               
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail \
            where get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
               
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券获券合计-成功路径: 查询业绩月份检查")
    def test_09_mgmt_fin_voucher_getSecondCouponGetDetailSum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["transMonthEnd"] = time.strftime("%Y%m",time.localtime(time.time()))
        data["transMonthStart"] = time.strftime("%Y%m",time.localtime(time.time()))   
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon_getdetail \
                where get_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%' and source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
             
        with _mgmt_fin_voucher_getSecondCouponGetDetailSum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["data"] == datasum
        


