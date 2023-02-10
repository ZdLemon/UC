# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_coupon_getListPage import params ,_mgmt_prmt_coupon_getListPage # 优惠券列表
from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity # 获取所有顾客身份类型
from api.mall_mgmt_application._mgmt_prmt_couponGrant_clearImportMember import _mgmt_prmt_couponGrant_clearImportMember # 清除缓存里导入的派发用户
from api.mall_mgmt_application._mgmt_prmt_coupon_getBasicInfo import _mgmt_prmt_coupon_getBasicInfo # 优惠券详情
from api.mall_mgmt_application._mgmt_prmt_selectMemberByCard import _mgmt_prmt_selectMemberByCard # 根据会员卡号去会员中心搜索会员信息
from api.mall_mgmt_application._mgmt_prmt_couponGrant_addUser import _mgmt_prmt_couponGrant_addUser # 手动新增派发顾客
from api.mall_mgmt_application._mgmt_prmt_couponGrant_getImportMemberPage import _mgmt_prmt_couponGrant_getImportMemberPage # 分页查询导入用户(导入时)
from api.mall_mgmt_application._mgmt_prmt_couponGrant_addCouponGrant import _mgmt_prmt_couponGrant_addCouponGrant # 新增优惠券派发记录
from api.mall_mgmt_application._mgmt_prmt_couponGrant_examineGrant import _mgmt_prmt_couponGrant_examineGrant # 优惠券派发审核
from api.mall_mgmt_application._mgmt_prmt_couponGrant_getCouponGrantList import params as params02, _mgmt_prmt_couponGrant_getCouponGrantList # 优惠券派发列表

from setting import P1, P2, P3, couponName, couponNumber, username_85, store_85, username, username_vip, store
from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/couponGrant/examineGrant")
class TestClass:
    """
    优惠券派发审核
    /mgmt/prmt/couponGrant/examineGrant
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("优惠券派发审核-成功路径: 45722864派发10张优惠券检查")
    def test_01_mgmt_prmt_couponGrant_examineGrant(self):
        
        getCouponGrantList = [] # 已有的待审核id集合
        id = None # 优惠券id
        getBasicInfo = None # 优惠券详情
        selectMemberByCard = None # 会员信息
        addCouponGrant = None # 待审核派发id
        
        @allure.step(" 优惠券派发列表:确保没有待审核申请")
        def step_01_mgmt_prmt_couponGrant_getCouponGrantList():
            
            nonlocal getCouponGrantList
            params = deepcopy(self.params02)
            params["state"] = 1 # 状态1待审核2派发中3已完成4已驳回5草稿6已停止
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        getCouponGrantList.append(d["id"])
        
        @allure.step("优惠券派发审核")
        def step_01_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": id, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                
        @allure.step("优惠券列表:获取id")
        def step_mgmt_prmt_coupon_getListPage():
            
            nonlocal id
            params = deepcopy(self.params)
            params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("获取所有顾客身份类型")                   
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == [
                    {
                        "code": 1,
                        "typeName": "会员"
                    }, 
                    {
                        "code": 2,
                        "typeName": "VIP会员"
                    }, 
                    {
                        "code": 3,
                        "typeName": "云商"
                    }, 
                    {
                        "code": 4,
                        "typeName": "微店"
                    }
                ]

        @allure.step("清除缓存里导入的派发用户")                   
        def step_mgmt_prmt_couponGrant_clearImportMember():
                           
            with _mgmt_prmt_couponGrant_clearImportMember(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("优惠券详情-基础信息")                   
        def step_mgmt_prmt_coupon_getBasicInfo():
            
            nonlocal getBasicInfo
            params ={"id": id}               
            with _mgmt_prmt_coupon_getBasicInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getBasicInfo = r.json()["data"]
        
        @allure.step("根据会员卡号去会员中心搜索会员信息")                   
        def step_mgmt_prmt_selectMemberByCard():
            
            nonlocal selectMemberByCard
            params ={"cardNo": username}               
            with _mgmt_prmt_selectMemberByCard(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                selectMemberByCard = r.json()["data"]

        @allure.step("手动新增派发顾客")                   
        def step_mgmt_prmt_couponGrant_addUser():
            
            data = {
                "cardNo": selectMemberByCard["cardNo"], # 会员卡号
                "mobile": selectMemberByCard["mobile"], # 会员手机号
                "realName": selectMemberByCard["realName"], # 会员姓名
                "everyCount": 10, # 派发数量
                "type": 1, # 派发方式1等量2按需
                "code": None, # 使用门店
                "couponId": id # 优惠券id
            }               
            with _mgmt_prmt_couponGrant_addUser(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("分页查询导入用户(导入时)")                   
        def step_mgmt_prmt_couponGrant_getImportMemberPage():
            
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "grantId": None,
                "user": None
            }               
            with _mgmt_prmt_couponGrant_getImportMemberPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("新增优惠券派发记录")                   
        def step_mgmt_prmt_couponGrant_addCouponGrant():
            
            nonlocal addCouponGrant
            data = {
                "type": 1, # 导入方式1等量派发2按需派发
                "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
                "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
                "everyCount": 1, # 每人发放数量
                "fixedTime": "", # 定时派发时间(yyyy-MM-dd HH:mm:ss)
                "grantStartTime": None, # 定时派发开始时间(yyyy-MM-dd HH:mm:ss)
                "grantEndTime": None, # 定时派发结束时间(yyyy-MM-dd HH:mm:ss)
                "memberIdentities": [], # 用户身份集合
                "memberLevelList": [], # 顾客等级:0.新用户,1.一星优惠客户,2.二星优惠客户,3.三星优惠客户,4.四星优惠客户,5.客户代表,6.客户经理,7.中级客户经理,8.客户总监,9.高级客户总监,10.资深客户总监,11.客户总经理
                "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
                "limitMemberLevel": False, # 是否限制顾客等级
                "limitOrderTime": 0, # 限制购货月份:0-不限制,1-限制,2-从未购货
                "limitCardTime": 0, # 是否限制开卡时间0否1是2限制注册时间
                "limitRegTime": 0, # 是否限制注册月份:0-不限制,1-限制
                "startTime": None, # 开卡时间起(yyyy-MM)
                "endTime": None, # endTime
                "regStartTime": None, # 注册月份起区(yyyy-MM)
                "regEndTime": None, # 注册月份止区(yyyy-MM)
                "orderStartTime": None, # 购货月份起区(yyyy-MM)
                "orderEndTime": None, # 购货月份止区(yyyy-MM)
                "couponId": id, # 优惠券id
                "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
            }               
            with _mgmt_prmt_couponGrant_addCouponGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addCouponGrant = r.json()["data"]

        @allure.step("优惠券派发审核")
        def step_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": addCouponGrant, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_01_mgmt_prmt_couponGrant_getCouponGrantList()
        if getCouponGrantList:
            for id in getCouponGrantList:
                step_01_mgmt_prmt_couponGrant_examineGrant()               
        step_mgmt_prmt_coupon_getListPage()
        step_mgmt_prmt_getMemberIdentity()
        step_mgmt_prmt_couponGrant_clearImportMember()
        step_mgmt_prmt_coupon_getBasicInfo()
        step_mgmt_prmt_selectMemberByCard()
        step_mgmt_prmt_couponGrant_addUser()
        step_mgmt_prmt_couponGrant_getImportMemberPage()
        step_mgmt_prmt_couponGrant_addCouponGrant()
        step_mgmt_prmt_couponGrant_examineGrant()

    @allure.severity(P1)
    @allure.title("优惠券派发审核-成功路径: 14498218派发10张优惠券检查")
    def test_02_mgmt_prmt_couponGrant_examineGrant(self):
        
        getCouponGrantList = [] # 已有的待审核id集合
        id = None # 优惠券id
        getBasicInfo = None # 优惠券详情
        selectMemberByCard = None # 会员信息
        addCouponGrant = None # 待审核派发id
        
        @allure.step(" 优惠券派发列表:确保没有待审核申请")
        def step_01_mgmt_prmt_couponGrant_getCouponGrantList():
            
            nonlocal getCouponGrantList
            params = deepcopy(self.params02)
            params["state"] = 1 # 状态1待审核2派发中3已完成4已驳回5草稿6已停止
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        getCouponGrantList.append(d["id"])
        
        @allure.step("优惠券派发审核")
        def step_01_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": id, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("优惠券列表:获取id")
        def step_mgmt_prmt_coupon_getListPage():
            
            nonlocal id
            params = deepcopy(self.params)
            params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("获取所有顾客身份类型")                   
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == [
                    {
                        "code": 1,
                        "typeName": "会员"
                    }, 
                    {
                        "code": 2,
                        "typeName": "VIP会员"
                    }, 
                    {
                        "code": 3,
                        "typeName": "云商"
                    }, 
                    {
                        "code": 4,
                        "typeName": "微店"
                    }
                ]

        @allure.step("清除缓存里导入的派发用户")                   
        def step_mgmt_prmt_couponGrant_clearImportMember():
                           
            with _mgmt_prmt_couponGrant_clearImportMember(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("优惠券详情-基础信息")                   
        def step_mgmt_prmt_coupon_getBasicInfo():
            
            nonlocal getBasicInfo
            params ={"id": id}               
            with _mgmt_prmt_coupon_getBasicInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getBasicInfo = r.json()["data"]
        
        @allure.step("根据会员卡号去会员中心搜索会员信息")                   
        def step_mgmt_prmt_selectMemberByCard():
            
            nonlocal selectMemberByCard
            params ={"cardNo": username_85}               
            with _mgmt_prmt_selectMemberByCard(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                selectMemberByCard = r.json()["data"]

        @allure.step("手动新增派发顾客")                   
        def step_mgmt_prmt_couponGrant_addUser():
            
            data = {
                "cardNo": selectMemberByCard["cardNo"], # 会员卡号
                "mobile": selectMemberByCard["mobile"], # 会员手机号
                "realName": selectMemberByCard["realName"], # 会员姓名
                "everyCount": 10, # 派发数量
                "type": 1, # 派发方式1等量2按需
                "code": None, # 使用门店
                "couponId": id # 优惠券id
            }               
            with _mgmt_prmt_couponGrant_addUser(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("分页查询导入用户(导入时)")                   
        def step_mgmt_prmt_couponGrant_getImportMemberPage():
            
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "grantId": None,
                "user": None
            }               
            with _mgmt_prmt_couponGrant_getImportMemberPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("新增优惠券派发记录")                   
        def step_mgmt_prmt_couponGrant_addCouponGrant():
            
            nonlocal addCouponGrant
            data = {
                "type": 1, # 导入方式1等量派发2按需派发
                "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
                "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
                "everyCount": 1, # 每人发放数量
                "fixedTime": "", # 定时派发时间(yyyy-MM-dd HH:mm:ss)
                "grantStartTime": None, # 定时派发开始时间(yyyy-MM-dd HH:mm:ss)
                "grantEndTime": None, # 定时派发结束时间(yyyy-MM-dd HH:mm:ss)
                "memberIdentities": [], # 用户身份集合
                "memberLevelList": [], # 顾客等级:0.新用户,1.一星优惠客户,2.二星优惠客户,3.三星优惠客户,4.四星优惠客户,5.客户代表,6.客户经理,7.中级客户经理,8.客户总监,9.高级客户总监,10.资深客户总监,11.客户总经理
                "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
                "limitMemberLevel": False, # 是否限制顾客等级
                "limitOrderTime": 0, # 限制购货月份:0-不限制,1-限制,2-从未购货
                "limitCardTime": 0, # 是否限制开卡时间0否1是2限制注册时间
                "limitRegTime": 0, # 是否限制注册月份:0-不限制,1-限制
                "startTime": None, # 开卡时间起(yyyy-MM)
                "endTime": None, # endTime
                "regStartTime": None, # 注册月份起区(yyyy-MM)
                "regEndTime": None, # 注册月份止区(yyyy-MM)
                "orderStartTime": None, # 购货月份起区(yyyy-MM)
                "orderEndTime": None, # 购货月份止区(yyyy-MM)
                "couponId": id, # 优惠券id
                "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
            }               
            with _mgmt_prmt_couponGrant_addCouponGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addCouponGrant = r.json()["data"]

        @allure.step("优惠券派发审核")
        def step_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": addCouponGrant, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_01_mgmt_prmt_couponGrant_getCouponGrantList()
        if getCouponGrantList:
            for id in getCouponGrantList:
                step_01_mgmt_prmt_couponGrant_examineGrant()  
        step_mgmt_prmt_coupon_getListPage()
        step_mgmt_prmt_getMemberIdentity()
        step_mgmt_prmt_couponGrant_clearImportMember()
        step_mgmt_prmt_coupon_getBasicInfo()
        step_mgmt_prmt_selectMemberByCard()
        step_mgmt_prmt_couponGrant_addUser()
        step_mgmt_prmt_couponGrant_getImportMemberPage()
        step_mgmt_prmt_couponGrant_addCouponGrant()
        step_mgmt_prmt_couponGrant_examineGrant()

    @allure.severity(P1)
    @allure.title("优惠券派发审核-成功路径: 26712599派发5张902804优惠券检查")
    def test_03_mgmt_prmt_couponGrant_examineGrant(self):
        
        getCouponGrantList = [] # 已有的待审核id集合
        id = None # 优惠券id
        getBasicInfo = None # 优惠券详情
        selectMemberByCard = None # 会员信息
        addCouponGrant = None # 待审核派发id
        
        @allure.step(" 优惠券派发列表:确保没有待审核申请")
        def step_01_mgmt_prmt_couponGrant_getCouponGrantList():
            
            nonlocal getCouponGrantList
            params = deepcopy(self.params02)
            params["state"] = 1 # 状态1待审核2派发中3已完成4已驳回5草稿6已停止
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        getCouponGrantList.append(d["id"])
        
        @allure.step("优惠券派发审核")
        def step_01_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": id, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("优惠券列表:获取id")
        def step_mgmt_prmt_coupon_getListPage():
            
            nonlocal id
            params = deepcopy(self.params)
            params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("获取所有顾客身份类型")                   
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == [
                    {
                        "code": 1,
                        "typeName": "会员"
                    }, 
                    {
                        "code": 2,
                        "typeName": "VIP会员"
                    }, 
                    {
                        "code": 3,
                        "typeName": "云商"
                    }, 
                    {
                        "code": 4,
                        "typeName": "微店"
                    }
                ]

        @allure.step("清除缓存里导入的派发用户")                   
        def step_mgmt_prmt_couponGrant_clearImportMember():
                           
            with _mgmt_prmt_couponGrant_clearImportMember(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("优惠券详情-基础信息")                   
        def step_mgmt_prmt_coupon_getBasicInfo():
            
            nonlocal getBasicInfo
            params ={"id": id}               
            with _mgmt_prmt_coupon_getBasicInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getBasicInfo = r.json()["data"]
        
        @allure.step("根据会员卡号去会员中心搜索会员信息")                   
        def step_mgmt_prmt_selectMemberByCard():
            
            nonlocal selectMemberByCard
            params ={"cardNo": username_vip}               
            with _mgmt_prmt_selectMemberByCard(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                selectMemberByCard = r.json()["data"]

        @allure.step("手动新增派发顾客")                   
        def step_mgmt_prmt_couponGrant_addUser():
            
            data = {
                "cardNo": selectMemberByCard["cardNo"], # 会员卡号
                "mobile": selectMemberByCard["mobile"], # 会员手机号
                "realName": selectMemberByCard["realName"], # 会员姓名
                "everyCount": 5, # 派发数量
                "type": 1, # 派发方式1等量2按需
                "code": store, # 使用门店
                "couponId": id # 优惠券id
            }               
            with _mgmt_prmt_couponGrant_addUser(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("分页查询导入用户(导入时)")                   
        def step_mgmt_prmt_couponGrant_getImportMemberPage():
            
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "grantId": None,
                "user": None
            }               
            with _mgmt_prmt_couponGrant_getImportMemberPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("新增优惠券派发记录")                   
        def step_mgmt_prmt_couponGrant_addCouponGrant():
            
            nonlocal addCouponGrant
            data = {
                "type": 1, # 导入方式1等量派发2按需派发
                "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
                "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
                "everyCount": 1, # 每人发放数量
                "fixedTime": "", # 定时派发时间(yyyy-MM-dd HH:mm:ss)
                "grantStartTime": None, # 定时派发开始时间(yyyy-MM-dd HH:mm:ss)
                "grantEndTime": None, # 定时派发结束时间(yyyy-MM-dd HH:mm:ss)
                "memberIdentities": [], # 用户身份集合
                "memberLevelList": [], # 顾客等级:0.新用户,1.一星优惠客户,2.二星优惠客户,3.三星优惠客户,4.四星优惠客户,5.客户代表,6.客户经理,7.中级客户经理,8.客户总监,9.高级客户总监,10.资深客户总监,11.客户总经理
                "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
                "limitMemberLevel": False, # 是否限制顾客等级
                "limitOrderTime": 0, # 限制购货月份:0-不限制,1-限制,2-从未购货
                "limitCardTime": 0, # 是否限制开卡时间0否1是2限制注册时间
                "limitRegTime": 0, # 是否限制注册月份:0-不限制,1-限制
                "startTime": None, # 开卡时间起(yyyy-MM)
                "endTime": None, # endTime
                "regStartTime": None, # 注册月份起区(yyyy-MM)
                "regEndTime": None, # 注册月份止区(yyyy-MM)
                "orderStartTime": None, # 购货月份起区(yyyy-MM)
                "orderEndTime": None, # 购货月份止区(yyyy-MM)
                "couponId": id, # 优惠券id
                "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
            }               
            with _mgmt_prmt_couponGrant_addCouponGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addCouponGrant = r.json()["data"]

        @allure.step("优惠券派发审核")
        def step_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": addCouponGrant, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_01_mgmt_prmt_couponGrant_getCouponGrantList()
        if getCouponGrantList:
            for id in getCouponGrantList:
                step_01_mgmt_prmt_couponGrant_examineGrant()  
        step_mgmt_prmt_coupon_getListPage()
        step_mgmt_prmt_getMemberIdentity()
        step_mgmt_prmt_couponGrant_clearImportMember()
        step_mgmt_prmt_coupon_getBasicInfo()
        step_mgmt_prmt_selectMemberByCard()
        step_mgmt_prmt_couponGrant_addUser()
        step_mgmt_prmt_couponGrant_getImportMemberPage()
        step_mgmt_prmt_couponGrant_addCouponGrant()
        step_mgmt_prmt_couponGrant_examineGrant()

    @allure.severity(P1)
    @allure.title("优惠券派发审核-成功路径: 26712599派发5张902208优惠券检查")
    def test_04_mgmt_prmt_couponGrant_examineGrant(self):
        
        getCouponGrantList = [] # 已有的待审核id集合
        id = None # 优惠券id
        getBasicInfo = None # 优惠券详情
        selectMemberByCard = None # 会员信息
        addCouponGrant = None # 待审核派发id
        
        @allure.step(" 优惠券派发列表:确保没有待审核申请")
        def step_01_mgmt_prmt_couponGrant_getCouponGrantList():
            
            nonlocal getCouponGrantList
            params = deepcopy(self.params02)
            params["state"] = 1 # 状态1待审核2派发中3已完成4已驳回5草稿6已停止
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_couponGrant_getCouponGrantList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        getCouponGrantList.append(d["id"])
        
        @allure.step("优惠券派发审核")
        def step_01_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": id, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("优惠券列表:获取id")
        def step_mgmt_prmt_coupon_getListPage():
            
            nonlocal id
            params = deepcopy(self.params)
            params["couponState"] = 3 # 状态1待审核2待生效3生效中4已失效5已禁用6已驳回7草稿
            params["couponNumber"] = couponNumber
            with _mgmt_prmt_coupon_getListPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("获取所有顾客身份类型")                   
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == [
                    {
                        "code": 1,
                        "typeName": "会员"
                    }, 
                    {
                        "code": 2,
                        "typeName": "VIP会员"
                    }, 
                    {
                        "code": 3,
                        "typeName": "云商"
                    }, 
                    {
                        "code": 4,
                        "typeName": "微店"
                    }
                ]

        @allure.step("清除缓存里导入的派发用户")                   
        def step_mgmt_prmt_couponGrant_clearImportMember():
                           
            with _mgmt_prmt_couponGrant_clearImportMember(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("优惠券详情-基础信息")                   
        def step_mgmt_prmt_coupon_getBasicInfo():
            
            nonlocal getBasicInfo
            params ={"id": id}               
            with _mgmt_prmt_coupon_getBasicInfo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getBasicInfo = r.json()["data"]
        
        @allure.step("根据会员卡号去会员中心搜索会员信息")                   
        def step_mgmt_prmt_selectMemberByCard():
            
            nonlocal selectMemberByCard
            params ={"cardNo": username_vip}               
            with _mgmt_prmt_selectMemberByCard(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                selectMemberByCard = r.json()["data"]

        @allure.step("手动新增派发顾客")                   
        def step_mgmt_prmt_couponGrant_addUser():
            
            data = {
                "cardNo": selectMemberByCard["cardNo"], # 会员卡号
                "mobile": selectMemberByCard["mobile"], # 会员手机号
                "realName": selectMemberByCard["realName"], # 会员姓名
                "everyCount": 5, # 派发数量
                "type": 1, # 派发方式1等量2按需
                "code": store_85, # 使用门店
                "couponId": id # 优惠券id
            }               
            with _mgmt_prmt_couponGrant_addUser(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("分页查询导入用户(导入时)")                   
        def step_mgmt_prmt_couponGrant_getImportMemberPage():
            
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "grantId": None,
                "user": None
            }               
            with _mgmt_prmt_couponGrant_getImportMemberPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
               
        @allure.step("新增优惠券派发记录")                   
        def step_mgmt_prmt_couponGrant_addCouponGrant():
            
            nonlocal addCouponGrant
            data = {
                "type": 1, # 导入方式1等量派发2按需派发
                "grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
                "grantTarget": 4, # 派发对象1所有人2身份3等级4导入
                "everyCount": 1, # 每人发放数量
                "fixedTime": "", # 定时派发时间(yyyy-MM-dd HH:mm:ss)
                "grantStartTime": None, # 定时派发开始时间(yyyy-MM-dd HH:mm:ss)
                "grantEndTime": None, # 定时派发结束时间(yyyy-MM-dd HH:mm:ss)
                "memberIdentities": [], # 用户身份集合
                "memberLevelList": [], # 顾客等级:0.新用户,1.一星优惠客户,2.二星优惠客户,3.三星优惠客户,4.四星优惠客户,5.客户代表,6.客户经理,7.中级客户经理,8.客户总监,9.高级客户总监,10.资深客户总监,11.客户总经理
                "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
                "limitMemberLevel": False, # 是否限制顾客等级
                "limitOrderTime": 0, # 限制购货月份:0-不限制,1-限制,2-从未购货
                "limitCardTime": 0, # 是否限制开卡时间0否1是2限制注册时间
                "limitRegTime": 0, # 是否限制注册月份:0-不限制,1-限制
                "startTime": None, # 开卡时间起(yyyy-MM)
                "endTime": None, # endTime
                "regStartTime": None, # 注册月份起区(yyyy-MM)
                "regEndTime": None, # 注册月份止区(yyyy-MM)
                "orderStartTime": None, # 购货月份起区(yyyy-MM)
                "orderEndTime": None, # 购货月份止区(yyyy-MM)
                "couponId": id, # 优惠券id
                "state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
            }               
            with _mgmt_prmt_couponGrant_addCouponGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                addCouponGrant = r.json()["data"]

        @allure.step("优惠券派发审核")
        def step_mgmt_prmt_couponGrant_examineGrant():
            
            data = {
                "enclosureVos":[], # 附件集合
                "examine": 3, # 审核是否通过3通过4不通过
                "grantId": addCouponGrant, # 优惠券派发id
                "remark": "同意发放优惠券" # 备注
            }               
            with _mgmt_prmt_couponGrant_examineGrant(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_01_mgmt_prmt_couponGrant_getCouponGrantList()
        if getCouponGrantList:
            for id in getCouponGrantList:
                step_01_mgmt_prmt_couponGrant_examineGrant()  
        step_mgmt_prmt_coupon_getListPage()
        step_mgmt_prmt_getMemberIdentity()
        step_mgmt_prmt_couponGrant_clearImportMember()
        step_mgmt_prmt_coupon_getBasicInfo()
        step_mgmt_prmt_selectMemberByCard()
        step_mgmt_prmt_couponGrant_addUser()
        step_mgmt_prmt_couponGrant_getImportMemberPage()
        step_mgmt_prmt_couponGrant_addCouponGrant()
        step_mgmt_prmt_couponGrant_examineGrant()










