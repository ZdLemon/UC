# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_querySum import data as data, _mgmt_fin_voucher_second_coupon_querySum
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryList import data as data02, _mgmt_fin_voucher_second_coupon_queryList

from setting import P1, P2, P3, username, store, username_vip, store_85
from util.stepreruns import stepreruns

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/querySum")
class TestClass:
    """
    秒返券列表金额合计金额合计
    /mgmt/fin/voucher/second/coupon/querySum
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token_2"]

    
    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询订单业绩月份合计检查")
    def test_01_mgmt_fin_voucher_second_coupon_querySum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["sourceOrderEndMonth"] = time.strftime("%Y%m",time.localtime(time.time()))
        data["sourceOrderStartMonth"] = time.strftime("%Y%m",time.localtime(time.time())) 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}' \
                        and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                         
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询会员卡号合计检查")
    def test_02_mgmt_fin_voucher_second_coupon_querySum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["cardNo"] = username
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where card_no = '{username}' and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                  
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum   

            
    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询会员手机号合计检查")
    def test_03_mgmt_fin_voucher_second_coupon_querySum(self, login_oauth_token, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["mobile"] = login_oauth_token["data"]["mobile"]
        mobile = login_oauth_token["data"]["mobile"]
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where mobile = '{mobile}' and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                            
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum 


    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 单选查询顾客类型合计检查")
    @pytest.mark.parametrize("memberType", [2, 3, 4], ids=["VIP顾客", "云商", "微店"])
    def test_04_mgmt_fin_voucher_second_coupon_querySum(self, memberType, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["memberType"] = memberType 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where member_type = '{memberType}' and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                         
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum 

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询来源订单号合计检查")
    def test_05_mgmt_fin_voucher_second_coupon_querySum(self, db_mall_center_finance):
        
        data = deepcopy(self.data02)
        data["sourceStoreCode"] = store 
                         
        with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
            sourceOrderNo =  r.json()["data"]["list"][0]["sourceOrderNo"]
               
        data = deepcopy(self.data)
        data["sourceOrderNo"] = sourceOrderNo
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_no = '{sourceOrderNo}' and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum  

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询提现批次号合计检查")
    def test_06_mgmt_fin_voucher_second_coupon_querySum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["withdrawBatch"] = f'{time.strftime("%Y%m",time.localtime(time.time()))}001'  
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where withdraw_batch = '{data['withdrawBatch']}' and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                        
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询服务中心编号合计检查")
    def test_07_mgmt_fin_voucher_second_coupon_querySum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["sourceStoreCode"] = store  
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_store_code = '{store}' and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                        
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询发放时间合计检查")
    def test_08_mgmt_fin_voucher_second_coupon_querySum(self, db_mall_center_finance):
        
        data = deepcopy(self.data)   
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where  effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                  
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 单选查询使用状态合计检查")
    @pytest.mark.parametrize("couponStatus", list(range(1, 9)), ids=["已使用", "未使用", "占用中", "已失效", "退货失效", "已提现", "提现中", "已锁定"])
    def test_09_mgmt_fin_voucher_second_coupon_querySum(self, couponStatus, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["couponStatusList"] = [couponStatus]
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where coupon_status = {couponStatus} and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                  
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum

    @allure.severity(P2)
    @allure.title("秒返券列表金额合计-成功路径: 查询是否已退货合计检查")
    @pytest.mark.parametrize("soReturnFlag,ids", [(True, "是"), (False,  "否")])
    def test_10_mgmt_fin_voucher_second_coupon_querySum(self, soReturnFlag, ids, db_mall_center_finance):
        
        data = deepcopy(self.data)
        data["soReturnFlag"] = soReturnFlag
        
        "查询数据库数据"
        db = db_mall_center_finance
        if soReturnFlag:
            sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                    where so_return_flag = {soReturnFlag} and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        else:
            sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                    where so_return_flag is Null and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                  
        with _mgmt_fin_voucher_second_coupon_querySum(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == datasum

