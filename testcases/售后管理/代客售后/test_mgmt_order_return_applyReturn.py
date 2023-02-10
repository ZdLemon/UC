# coding:utf-8

from api.mall_mgmt_application._mgmt_order_return_getOrderReturnList import _mgmt_order_return_getOrderReturnList # 退货单列表
from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表
from api.mall_mgmt_application._mgmt_order_orderInfo import _mgmt_order_orderInfo # 订单信息
from api.mall_mgmt_application._mgmt_order_return_calcRefundAmount import _mgmt_order_return_calcRefundAmount # 计算订单退款金额
from api.mall_mgmt_application._mgmt_order_return_upgradeOrderVerify import _mgmt_order_return_upgradeOrderVerify # 升级单校验
from api.mall_center_sys._sys_api_getAllReturnReasonByType import _sys_api_getAllReturnReasonByType # 通过退换货类型获取 一级,二级层级原因
from api.mall_mgmt_application._mgmt_order_return_applyReturn import _mgmt_order_return_applyReturn # 申请退货
from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情
from api.mall_mgmt_application._mgmt_order_return_saveComment import _mgmt_order_return_saveComment # 新增/修改留言
from api.mall_mgmt_application._mgmt_order_return_auditOrderReturn import _mgmt_order_return_auditOrderReturn # 分公司退货审核

from setting import P1, P2, P3, username

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/order/return/applyReturn")
class TestClass:
    """
    申请退货
    /mgmt/order/return/applyReturn
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("申请退货-成功路径: 申请退货检查")
    def test_mgmt_order_return_applyReturn(self):
        
        orderNo = None # 订单编号
        calcRefundAmount = None # 计算订单退款金额
        upgradeOrderVerify = None # 升级单校验
        getAllReturnReasonByType = None # 通过退换货类型获取 一级,二级层级原因
        applyReturn = None # 退货单

        @allure.step("退货单列表：是否有待审核的退货单")
        def step_mgmt_order_return_getOrderReturnList():
                
            nonlocal orderNo, applyReturn
            params = {
                "returnType": 1, # 退货类型 1->当月退货 2->隔月退货
                "expressType": None, # 发货方式 1->服务中心自提 2->公司交付
                "applySource": None, # 申请来源 0->总公司代客售后 1->顾客申请 2->公司申请 3->商城1.0
                "companyCode": "", # 分公司编号
                "financeCompanyCode": "", # 财务分公司编号
                "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
                "storeCode": "", # 服务中心编号
                "customerCard": "", # 顾客卡号
                "creatorCard": username, # 开单人卡号
                "returnNo": "", # 退货单号
                "orderNo": "", # 订单号
                "isDeliver": None, # 是否发货 0->不发货 1->发货
                "isUpgrade": None, # 是否升级单 0->否 1->是
                "depositNo": "", # 对应定金订单号
                "currentPage": 1, 
                "pageSize": 10,
                "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
                "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
                "returnStatus": 1, # 服务状态 1->待审核 2->待退回 3->待验货 98->已取消 99->已完成
                "pageNum": 1,
            }           
            with _mgmt_order_return_getOrderReturnList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    orderNo = r.json()["data"]["list"][0]["orderNo"]
                    applyReturn = r.json()["data"]["list"][0]["returnNo"]   
       
        @allure.step("订单列表：获取订单编号")
        def step_mgmt_order_orderList():
                
            nonlocal orderNo
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
                "orderNo": "",
                "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
                "creatorCard": username, # 开单人卡号
                "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
                "isUpgrade": 0, # 是否升级单
                "commitStartTime": f"{time.strftime('%Y-%m', time.localtime(time.time()))}-01", # 开单开始时间
                "commitEndTime": time.strftime("%Y-%m-%d", time.localtime(time.time())), # 开单结束时间
            }           
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderNo = r.json()["data"]["list"][0]["orderNo"]   
       
        @allure.step("订单信息")
        def step_mgmt_order_orderInfo(): 
               
            params = {
                "orderNo": orderNo, # 订单编号
            }      
            with _mgmt_order_orderInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("计算订单退款金额")
        def step_mgmt_order_return_calcRefundAmount(): 
            
            nonlocal calcRefundAmount   
            params = {
                "orderNo": orderNo, # 订单编号
            }      
            with _mgmt_order_return_calcRefundAmount(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                calcRefundAmount = r.json()["data"]

        @allure.step("升级单校验")
        def step_mgmt_order_return_upgradeOrderVerify(): 
            
            nonlocal upgradeOrderVerify   
            data = {
                "orderNo": orderNo, 
                "applySource": 0,
            }     
            with _mgmt_order_return_upgradeOrderVerify(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["resultType"] != 2 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
                upgradeOrderVerify = r.json()["data"]["resultType"]
        
        @allure.step("通过退换货类型获取 一级,二级层级原因")
        def step_sys_api_getAllReturnReasonByType(): 
            
            nonlocal getAllReturnReasonByType   
            params = {
                "returnType": 1, # 退换货类型：1.商城退货，2.商城换货，3.服务中心押货退货，4.服务中心押货换货，5.展业包订货退货，6.展业包订货换货
            }   
            with _sys_api_getAllReturnReasonByType(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getAllReturnReasonByType = r.json()["data"]

        @allure.step("申请退货")
        def step_mgmt_order_return_applyReturn(): 
            
            nonlocal applyReturn 
            data = {
                "orderNo": orderNo, # 订单编号
                "reason1": getAllReturnReasonByType[1]["returnReason"], # 退货一级原因
                "reason1Id": getAllReturnReasonByType[1]["id"], # 退货一级原因id
                "reason1Remark": "我没钱了要退货", # 退货一级原因备注
                "reason2": getAllReturnReasonByType[1]["reasonList"][1]["returnReason"], # 退货二级原因
                "reason2Id": getAllReturnReasonByType[1]["reasonList"][1]["id"], # 退货二级原因id
                "reason2Remark": "给你特批退货吧", # 退货二级原因备注
                "applySource": 0 # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
            }   
            with _mgmt_order_return_applyReturn(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                applyReturn = r.json()["data"]

        @allure.step("退货详情")
        def step_mgmt_order_return_getOrderReturnDetails(): 
            
            params = {
                "returnNo": applyReturn, # 退货单号
            }
            with _mgmt_order_return_getOrderReturnDetails(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("新增或修改留言")
        def step_mgmt_order_return_saveComment(): 
            
            data = {
                "serviceNo": applyReturn, # 退货/换货单号
                "comment": "我同意这个代客售后申请", # 留言内容
                "id": "" # 留言id
            }
            with _mgmt_order_return_saveComment(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("升级单校验")
        def step_02_mgmt_order_return_upgradeOrderVerify(): 
            
            nonlocal upgradeOrderVerify   
            data = {
                "orderNo": orderNo, 
            }     
            with _mgmt_order_return_upgradeOrderVerify(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["resultType"] == 0 # 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
                upgradeOrderVerify = r.json()["data"]["resultType"]
        
        @allure.step("分公司退货审核")
        def step_mgmt_order_return_auditOrderReturn(): 
            
            data = {
                "serviceNo": applyReturn, # 售后单号
                "auditStatus": "1", # 审核状态 1->通过 2->不通过
                "remarks": "同意退款" # 审核意见
            }
            with _mgmt_order_return_auditOrderReturn(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_order_return_getOrderReturnList()
        if applyReturn: 
            step_mgmt_order_return_getOrderReturnDetails()
            step_mgmt_order_return_saveComment()
            step_02_mgmt_order_return_upgradeOrderVerify()
            step_mgmt_order_return_auditOrderReturn()        
        step_mgmt_order_orderList()
        step_mgmt_order_orderInfo()
        step_mgmt_order_return_calcRefundAmount()
        step_mgmt_order_return_upgradeOrderVerify()
        step_sys_api_getAllReturnReasonByType()
        step_mgmt_order_return_applyReturn()
        step_mgmt_order_return_getOrderReturnDetails()
        step_mgmt_order_return_saveComment()
        step_02_mgmt_order_return_upgradeOrderVerify()
        step_mgmt_order_return_auditOrderReturn()


