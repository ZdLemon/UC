# coding:utf-8

from api.mall_mgmt_application._mgmt_order_totalOrderSettlement import params, _mgmt_order_totalOrderSettlement

from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
import uuid


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/totalOrderSettlement")
@pytest.mark.skip()
class TestClass:
    """
    交付结算列表合计
    /mgmt/order/totalOrderSettlement
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("交付结算列表合计-成功路径: 查询业绩月份默认本月检查")
    def test_01_mgmt_order_totalOrderSettlement(self, db_mall_center_finance):
        
        params = deepcopy(self.params) 
        
        "查询数据库数据"
        db = db_mall_center_finance
        sql = f"SELECT sum(second_coupon_amount) as datasum FROM fin_second_coupon \
                where source_order_month = '{time.strftime('%Y%m',time.localtime(time.time()))}' \
                        and effect_time LIKE '{time.strftime('%Y-%m',time.localtime(time.time()))}%';"
        db.execute(sql)
        datasum =  db.fetchall()[0][0]
                  
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r:
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验

    @allure.severity(P2)
    @allure.title("交付结算列表合计-成功路径: 查询服务中心编号检查")
    def test_02_mgmt_order_totalOrderSettlement(self, db_mall_center_finance):
        
        params = deepcopy(self.params)
        params["storeCode"] = store_85                
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r:
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验
               
    @allure.severity(P2)
    @allure.title("交付结算列表合计-成功路径: 查询负责人卡号检查")
    def test_03_mgmt_order_totalOrderSettlement(self, db_mall_center_finance):
        
        params = deepcopy(self.params)
        params["cardNo"] =  username_85                    
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r:
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验
        
    @allure.severity(P2)
    @allure.title("交付结算列表合计 -成功路径: 查询负责人检查")
    def test_04_mgmt_order_totalOrderSettlement(self, db_mall_center_finance):
        
        params = deepcopy(self.params)
        params["realName"] = name_85                   
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r: 
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验

    @allure.severity(P2)
    @allure.title("交付结算列表合计-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_05_mgmt_order_totalOrderSettlement(self, companyCode, db_mall_center_finance):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r:            
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验

    @allure.severity(P2)
    @allure.title("交付结算列表合计: 下拉选项查询本期交付差额是否为负检查")
    @pytest.mark.parametrize("isDifference,ids", [(0, "否"), (1, "是")])
    def test_06_mgmt_order_totalOrderSettlement(self, isDifference, ids, db_mall_center_finance):
        
        params = deepcopy(self.params)
        params["isDifference"] = isDifference                     
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r:
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验
    @allure.severity(P2)
    @allure.title("交付结算列表合计: 下拉选项查询差额校验是否为零检查")
    @pytest.mark.parametrize("isDifCheck,ids", [(0, "否"), (1, "是")])
    def test_06_mgmt_order_totalOrderSettlement(self, isDifCheck, ids, db_mall_center_finance):
        
        params = deepcopy(self.params)
        params["isDifCheck"] = isDifCheck                     
        with _mgmt_order_totalOrderSettlement(params, self.access_token) as r:
            assert r.json()["data"]["retailPrice"] == None # 零售价
            assert r.json()["data"]["securityAmount"] == None # 押货价
            assert r.json()["data"]["payDifference"] == None # 店应补差额
            assert r.json()["data"]["orderAmount"] == None # 应付金额
            assert r.json()["data"]["returnAmount"] == None # 返还金额
            assert r.json()["data"]["secCouponAmount"] == None # 秒返券金额
            assert r.json()["data"]["giftCouponAmount"] == None # 电子礼券
            assert r.json()["data"]["couponAmount"] == None # 优惠券
            assert r.json()["data"]["expressSubsidyAmount"] == None # 运费补贴券
            assert r.json()["data"]["promotionDiscount"] == None # 活动优惠
            assert r.json()["data"]["totalAmount"] == None # 实付金额
            assert r.json()["data"]["receiveAmount"] == None # 店应收回款
            assert r.json()["data"]["difAmount"] == None # 本期交付差额
            assert r.json()["data"]["deliveryNum"] == None # 交付数量
            assert r.json()["data"]["deliveryReturn"] == None # 交付退回
            assert r.json()["data"]["securityTotal"] == None # 交付总量对应的押货价合计
            assert r.json()["data"]["difCheck"] == None # 差额校验


