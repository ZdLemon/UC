# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_transferOrder_pageList import data, _mgmt_inventory_transferOrder_pageList
from util.getBaseMonthlyReportData import getBaseMonthlyReportData
from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode, storeName_85, username_vip, name_vip

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/transferOrder/pageList")
class TestClass:
    """
    分页列表-85折转分分公司流水列表:搜索查询
    /mgmt/inventory/transferOrder/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表: 默认查询当月检查")
    def test_01_mgmt_inventory_transferOrder_pageList(self):
        
        data = deepcopy(self.data)            
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert time.strftime("%Y%m",time.localtime(d["createTime"]/1000)) == time.strftime("%Y%m",time.localtime(time.time()))
            else:
                assert r.json()["data"]["list"] == []
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_transferOrder_pageList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode                       
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert data["companyCode"] == i
            else:
                assert r.json()["data"]["list"] == []
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表-成功路径: 查询审核时间检查")
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_03_mgmt_inventory_transferOrder_pageList(self):
        
        data = deepcopy(self.data)
        data["verifyStartDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        data["verifyEndDay"] = time.strftime("%Y-%m-%d",time.localtime(time.time()))                   
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:            
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert time.strftime("%Y-%m-%d",time.localtime(d["verifyTime"]/1000)) == time.strftime("%Y-%m-%d",time.localtime(time.time()))
            else:
                assert r.json()["data"]["list"] == []
   
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表: 仅支持精确查询会员卡号检查")
    @pytest.mark.parametrize("customerCardNo", [username_85, username_85[:-1]], ids=["正确的负责人卡号", "负责人卡号的一部分"])
    def test_04_mgmt_inventory_transferOrder_pageList(self, customerCardNo):
        
        data = deepcopy(self.data)
        data["customerCardNo"] = customerCardNo                      
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["customerCardNo"] for d in r.json()["data"]["list"]):
                    assert i == customerCardNo
            else:
                assert r.json()["data"]["list"] == []
    
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表: 仅支持精确查询开单人卡号检查")
    @pytest.mark.parametrize("openOrderCardNo", [username_85, username_85[:-1]], ids=["正确的开单人卡号", "开单人卡号的一部分"])
    def test_05_mgmt_inventory_transferOrder_pageList(self, openOrderCardNo):
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = openOrderCardNo                      
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["openOrderCardNo"] for d in r.json()["data"]["list"]):
                    assert i == openOrderCardNo
            else:
                assert r.json()["data"]["list"] == []
                
    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表: 仅支持精确查询服务中心编号检查")
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["正确的服务中心编号", "服务中心编号的一部分"])
    def test_06_mgmt_inventory_transferOrder_pageList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode                
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表: 下拉选项查询开单人类型检查")
    @pytest.mark.parametrize("openOrderManType", [3, 4], ids=["云商", "微店"])
    def test_07_mgmt_inventory_transferOrder_pageList(self, openOrderManType):
        
        data = deepcopy(self.data)
        data["openOrderManType"] = openOrderManType                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["openOrderManType"] == openOrderManType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("85折转分分公司流水列表: 下拉选项查询开单人类型检查")
    @pytest.mark.parametrize("orderType", [1, 2], ids=["报单", "退单"])
    def test_08_mgmt_inventory_transferOrder_pageList(self, orderType):
        
        data = deepcopy(self.data)
        data["orderType"] = orderType                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["orderType"] == orderType
            else:
                assert r.json()["data"]["list"] == []


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/transferOrder/pageList")
class TestClass02:
    """
    分页列表-85折转分分公司流水列表:转分订单，退单流水检查
    /mgmt/inventory/transferOrder/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
       
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 转分订单自购流水检查")
    def test_01_mgmt_inventory_transferOrder_pageList(self, orderCommit_85):
        
        getOrderInfo = orderCommit_85
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_85 # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_85 # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 3 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 转分订单代购流水检查")
    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    def test_02_mgmt_inventory_transferOrder_pageList(self, orderCommit_85_vip):
        
        getOrderInfo = orderCommit_85_vip
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_vip # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_vip # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 2 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 转分订单退货流水检查")
    def test_03_mgmt_inventory_transferOrder_pageList(self, applyReturn_85):
        
        applyReturn, getOrderInfo = applyReturn_85
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == applyReturn # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_85 # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_85 # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 3 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 2 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == -getOrderInfo["orderAmount"] or 0 # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == -getOrderInfo["secCouponAmount"] or 0 # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == -getOrderInfo["giftCouponAmount"] or 0 # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == -getOrderInfo["couponAmount"] or 0 # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == -getOrderInfo["expressSubsidyAmount"] or 0 # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == -getOrderInfo["promotionDiscount"] or 0 # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == -getOrderInfo["totalAmount"] or 0 # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            
            
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/transferOrder/pageList")
@pytest.mark.skipif(getBaseMonthlyReportData() != 3, reason="不在公开补报时间内")
class TestClass03:
    """
    分页列表-85折转分分公司流水列表:转分结算前销售调整订单，退单流水检查
    /mgmt/inventory/transferOrder/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
       
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 转分结算前销售调整订单-自购流水检查")
    def test_01_mgmt_inventory_transferOrder_pageList(self, BB_orderCommit_85):
        
        getOrderInfo = BB_orderCommit_85
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_85 # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_85 # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 3 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 转分结算前销售调整订单-代购流水检查")
    def test_02_mgmt_inventory_transferOrder_pageList(self, BB_orderCommit_85_vip):
        
        getOrderInfo = BB_orderCommit_85_vip
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == getOrderInfo["orderNo"] # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_vip # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_vip # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 2 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 1 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == getOrderInfo["orderAmount"] # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == getOrderInfo["secCouponAmount"] # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == getOrderInfo["giftCouponAmount"] # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == getOrderInfo["couponAmount"] # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == getOrderInfo["expressSubsidyAmount"] # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == getOrderInfo["promotionDiscount"] # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == getOrderInfo["totalAmount"] # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 转分结算前销售调整订单退货流水检查")
    def test_03_mgmt_inventory_transferOrder_pageList(self, BB_applyReturn_85):
        
        applyReturn, getOrderInfo = BB_applyReturn_85
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == applyReturn # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_85 # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_85 # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 3 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 2 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == -getOrderInfo["orderAmount"] or 0 # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == -getOrderInfo["secCouponAmount"] or 0 # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == -getOrderInfo["giftCouponAmount"] or 0 # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == -getOrderInfo["couponAmount"] or 0 # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == -getOrderInfo["expressSubsidyAmount"] or 0 # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == -getOrderInfo["promotionDiscount"] or 0 # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == -getOrderInfo["totalAmount"] or 0 # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            
            
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/transferOrder/pageList")
@pytest.mark.skipif(time.localtime(time.time()).tm_mday > 8, reason="超过补报截止时间")
class TestClass04:
    """
    分页列表-85折转分分公司流水列表:补报截止日期前，退货上个月的订单流水算都算当天的流水检查
    /mgmt/inventory/transferOrder/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
       
    @allure.severity(P1)
    @allure.title("85折转分分公司流水列表: 补报截止日期前，退货上个月的订单流水检查")
    @pytest.mark.skip("仅支持5月1日起的订单退货")
    def test_01_mgmt_inventory_transferOrder_pageList(self, FGY_applyReturn_85):
        
        applyReturn, getOrderInfo = FGY_applyReturn_85
        
        data = deepcopy(self.data)
        data["openOrderCardNo"] = username_85                     
        with _mgmt_inventory_transferOrder_pageList(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["businessNo"] == applyReturn # 订单号
            assert r.json()["data"]["list"][0]["companyCode"] == "34000" # 分公司
            assert r.json()["data"]["list"][0]["storeCode"] == store_85 # 服务中心
            assert r.json()["data"]["list"][0]["openOrderCardNo"] == username_85 # 开单人卡号
            assert r.json()["data"]["list"][0]["openOrderManType"] == 3 # 开单人类型
            assert r.json()["data"]["list"][0]["openOrderManName"] == name_85 # 开单人姓名
            assert r.json()["data"]["list"][0]["customerCardNo"] == username_85 # 顾客卡号
            assert r.json()["data"]["list"][0]["customerName"] == name_85 # 顾客姓名
            assert r.json()["data"]["list"][0]["customerType"] == 3 # 顾客类型
            assert r.json()["data"]["list"][0]["orderType"] == 2 # 账款类型 1->报单 ，2->退单
            assert r.json()["data"]["list"][0]["shouldPayAmount"] == -getOrderInfo["orderAmount"] or 0 # 应付金额
            assert r.json()["data"]["list"][0]["secondReturnAmount"] == -getOrderInfo["secCouponAmount"] or 0 # 秒返券
            assert r.json()["data"]["list"][0]["electronicGiftAmount"] == -getOrderInfo["giftCouponAmount"] or 0 # 电子礼券
            assert r.json()["data"]["list"][0]["couponAmount"] == -getOrderInfo["couponAmount"] or 0 # 优惠券
            assert r.json()["data"]["list"][0]["freightBtAmount"] == -getOrderInfo["expressSubsidyAmount"] or 0 # 运费补贴券
            assert r.json()["data"]["list"][0]["promotionActionAmount"] == -getOrderInfo["promotionDiscount"] or 0 # 活动优惠
            assert r.json()["data"]["list"][0]["realpayAmount"] == -getOrderInfo["totalAmount"] or 0 # 实付金额
            assert r.json()["data"]["list"][0]["storeName"] == storeName_85 # 服务中心名称
            

                






