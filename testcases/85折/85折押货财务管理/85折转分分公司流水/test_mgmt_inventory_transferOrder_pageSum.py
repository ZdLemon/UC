# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_transferOrder_pageSum import data, _mgmt_inventory_transferOrder_pageSum

from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/transferOrder/pageSum")
class TestClass:
    """
    分页列表统计列-85折转分分公司流水
    /mgmt/inventory/transferOrder/pageSum
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计: 默认查询当月检查")
    def test_01_mgmt_inventory_transferOrder_pageSum(self, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)            
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_transferOrder_pageSum(self, companyCode, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and company_code = {companyCode};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode                       
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:            
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计-成功路径: 查询审核时间检查")
    def test_03_mgmt_inventory_transferOrder_pageSum(self, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and verify_time LIKE '{time.strftime('%Y-%m-%d',time.localtime(time.time()))}%';"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["verifyStartDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        data["verifyEndDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))                   
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:            
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额
   
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("customerCardNo", [username_85, username_85[:-1]], ids=["正确的会员卡号", "会员卡号的一部分"])
    def test_04_mgmt_inventory_transferOrder_pageSum(self, customerCardNo, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and customer_card_no = {customerCardNo};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["customerCardNo"] = customerCardNo                      
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计: 仅支持精确查询开单人卡号检查")
    @pytest.mark.parametrize("openOrderCardNo", [username_85, username_85[:-1]], ids=["正确的开单人卡号", "开单人卡号的一部分"])
    def test_05_mgmt_inventory_transferOrder_pageSum(self, openOrderCardNo, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and open_order_card_no = {openOrderCardNo};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = openOrderCardNo                      
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额
                
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_06_mgmt_inventory_transferOrder_pageSum(self, storeCode, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and store_code = {storeCode};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode                
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额

    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计: 下拉选项查询开单人类型检查")
    @pytest.mark.parametrize("openOrderManType", [3, 4], ids=["云商", "微店"])
    def test_07_mgmt_inventory_transferOrder_pageSum(self, openOrderManType, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and open_order_man_type = {openOrderManType};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["openOrderManType"] = openOrderManType                     
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额

    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表合计: 下拉选项查询开单人类型检查")
    @pytest.mark.parametrize("orderType", [1, 2], ids=["报单", "退单"])
    def test_08_mgmt_inventory_transferOrder_pageSum(self, orderType, db_mall_center_inventory):
        
        db = db_mall_center_inventory
        # 优惠券，电子礼券，运费补贴券，活动优惠，实付金额，秒返券，应付金额
        sql = f"SELECT sum(coupon_amount), sum(electronic_gift_amount), sum(freight_bt_amount), sum(promotion_action_amount), sum(realpay_amount), sum(second_return_amount), sum(should_pay_amount)\
            FROM dis_deposit_transfer_order where month = {time.strftime('%Y%m',time.localtime(time.time()))} and order_type = {orderType};"
        db.execute(sql)
        sumCouponAmount, sumElectronicGiftAmount, sumFreightBtAmount, sumPromotionActionAmount, sumRealpayAmount, sumSecondReturnAmount, sumShouldPayAmount =  db.fetchall()[0]
        
        data = deepcopy(self.data)
        data["orderType"] = orderType                     
        with _mgmt_inventory_transferOrder_pageSum(data, self.access_token) as r:
            assert r.json()["data"]["sumCouponAmount"] is None or r.json()["data"]["sumCouponAmount"] == float(sumCouponAmount) # 优惠券
            assert r.json()["data"]["sumElectronicGiftAmount"] is None or r.json()["data"]["sumElectronicGiftAmount"] == float(sumElectronicGiftAmount) # 电子礼券
            assert r.json()["data"]["sumFreightBtAmount"] is None or r.json()["data"]["sumFreightBtAmount"] == float(sumFreightBtAmount) # 运费补贴券
            assert r.json()["data"]["sumPromotionActionAmount"] is None or r.json()["data"]["sumPromotionActionAmount"] == float(sumPromotionActionAmount) # 活动优惠
            assert r.json()["data"]["sumRealpayAmount"] is None or r.json()["data"]["sumRealpayAmount"] == float(sumRealpayAmount) # 实付金额
            assert r.json()["data"]["sumSecondReturnAmount"] is None or r.json()["data"]["sumSecondReturnAmount"] == float(sumSecondReturnAmount) # 使用购物礼券
            assert r.json()["data"]["sumShouldPayAmount"] is None or r.json()["data"]["sumShouldPayAmount"] == float(sumShouldPayAmount) # 应付金额