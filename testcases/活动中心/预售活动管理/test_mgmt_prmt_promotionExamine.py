# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_deleteCacheMember import _mgmt_prmt_deleteCacheMember # 删除缓存的活动用户
from api.mall_mgmt_application._mgmt_prmt_selectPromotionCode import _mgmt_prmt_selectPromotionCode # 查询活动编码是否已经存在
from api.mall_mgmt_application._mgmt_prmt_getProductListByCodeOrName import _mgmt_prmt_getProductListByCodeOrName # 根据产品编码或名称搜索产品
from api.mall_mgmt_application._mgmt_prmt_getMemberIdentity import _mgmt_prmt_getMemberIdentity # 获取所有顾客身份类型
from api.mall_mgmt_application._mgmt_prmt_addPromotion import _mgmt_prmt_addPromotion # 保存新建的活动
from api.mall_mgmt_application._mgmt_prmt_promotionExamine import _mgmt_prmt_promotionExamine # 活动审核

from setting import P1, P2, P3, couponName, promotionName, promotionCode, productCode_ys, productCode_qg, promotionCode_qg, promotionName_qg

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/promotionExamine")
class TestClass:
    """
    活动审核
    /mgmt/prmt/promotionExamine
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("新建预售活动")
    def test_01_mgmt_prmt_promotionExamine(self):
        
        getProductListByCodeOrName = None # 活动产品信息
        code = 200 # 活动产品如果不可添加，则返回500
        id = None # 新建活动id
        
        @allure.step("删除缓存的活动用户")
        def step_mgmt_prmt_deleteCacheMember():
            
            data = {
                "id": None
            }                  
            with _mgmt_prmt_deleteCacheMember(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询活动编码是否已经存在")
        def step_mgmt_prmt_selectPromotionCode():
            
            nonlocal code
            params = {
                "promotionCode": promotionCode, # 活动编码
                "promotionId": None,
            }                  
            with _mgmt_prmt_selectPromotionCode(params, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]
        
        @allure.step("根据产品编码或名称搜索产品")
        def step_mgmt_prmt_getProductListByCodeOrName():
            
            nonlocal getProductListByCodeOrName, code
            params = {
                "id": None, # 活动id
                "type": 4, # 搜索来源:1活动 2换购 3加购 4预售 None优惠券
                "productCode": productCode_ys, # 产品编码
            }                
            with _mgmt_prmt_getProductListByCodeOrName(params, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]
                if r.json()["code"] == 200:
                    getProductListByCodeOrName = r.json()["data"][0]

        @allure.step("获取所有顾客身份类型")
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("保存新建的活动")
        def step_mgmt_prmt_addPromotion():
            
            nonlocal id
            data = {
                "startTime": None, # 开始时间时间戳1651507200000
                "endTime":  None, # 结束时间1651507200000
                "expireOption": 1, # 定金支付时效配置项:0-自定义,1-15分钟,2-30分钟,3-1小时
                "customDays": None, # 定金支付时效自定义(天)
                "customHours": None, # 定金支付时效自定义(时)
                "customMinutes": None, # 定金支付时效自定义(分)
                "payStartTime":  None, # 尾款支付开始时间1651507200000
                "payEndTime":  None, # 尾款支付结束时间1653926400000
                "remarks": "", 
                "configDto": {
                    "cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
                    "limitNumber": 1, # 限购数量(-1不限,-2按需分配)
                    "isNotice": 1, # 是否预告0预告1不预告
                    "limitCustomer": 1, # 参与顾客设置1所有2顾客身份3顾客等级4导入
                    "noticeTime": "", # 预告时间
                    "limitType": 1, # 限购方式1不限量2独立限量3统一限量4按需导入5按阶梯配置独立限量6按阶梯配置统一限量
                    "startCardTime": None,
                    "endCardTime": None,
                    "limitCardTime": 0,
                    "limitMemberLevel": False, # 是否限制顾客等级
                    "limitOrderTime": 0,
                    "limitRegTime": 0,
                    "memberLevelList": [],
                    "regEndTime": None,
                    "regStartTime": None,
                    "orderEndTime": None,
                    "orderStartTime": None
                },
                "productDtos": [getProductListByCodeOrName], # 活动商品信息
                "promotionCode": promotionCode, # 活动编码
                "promotionName": promotionName, # 活动名称
                "promotionState": 1, # 活动状态1待审核2待开始3进行中4已结束5已驳回6草稿
                "promotionType": 4, # 活动类型:1-活动,2-换购,4-预售
                "memberIdentities": []
            }                          
            with _mgmt_prmt_addPromotion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]
       
        @allure.step("活动审核")
        def step_mgmt_prmt_promotionExamine():
            
            data = {
                "promotionId": id, # 活动id
                "examine": 3, # 审核是否通过3通过4不通过
                "remarks": "同意执行该活动", # 备注
                "enclosureVos": [] # 附件集合
            }                          
            with _mgmt_prmt_promotionExamine(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
       
        step_mgmt_prmt_deleteCacheMember()
        step_mgmt_prmt_selectPromotionCode()
        if code != 500:
            step_mgmt_prmt_getProductListByCodeOrName()
            if code != 500:
                step_mgmt_prmt_getMemberIdentity()
                step_mgmt_prmt_addPromotion()
                step_mgmt_prmt_promotionExamine()
        
    @allure.severity(P1)
    @allure.title("新建抢购活动")
    def test_02_mgmt_prmt_promotionExamine(self):
        
        getProductListByCodeOrName = None # 活动产品信息
        code = 200 # 活动产品如果不可添加，则返回500
        id = None # 新建活动id
        
        @allure.step("删除缓存的活动用户")
        def step_mgmt_prmt_deleteCacheMember():
            
            data = {
                "id": None
            }                  
            with _mgmt_prmt_deleteCacheMember(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询活动编码是否已经存在")
        def step_mgmt_prmt_selectPromotionCode():
            
            nonlocal code
            params = {
                "promotionCode": promotionCode, # 活动编码
                "promotionId": None,
            }                  
            with _mgmt_prmt_selectPromotionCode(params, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]
        
        @allure.step("根据产品编码或名称搜索产品")
        def step_mgmt_prmt_getProductListByCodeOrName():
            
            nonlocal getProductListByCodeOrName, code
            params = {
                "id": None, # 活动id
                "type": 1, # 搜索来源:1活动 2换购 3加购 4预售 None优惠券
                "productCode": productCode_qg, # 产品编码
            }                
            with _mgmt_prmt_getProductListByCodeOrName(params, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]
                if r.json()["code"] == 200:
                    getProductListByCodeOrName = r.json()["data"][0]

        @allure.step("获取所有顾客身份类型")
        def step_mgmt_prmt_getMemberIdentity():
                           
            with _mgmt_prmt_getMemberIdentity(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("保存新建的活动")
        def step_mgmt_prmt_addPromotion():
            
            nonlocal id
            data = {
                "remarks": "",
                "configDto": {
                    "isNewCard": 0,
                    "showEndTime": 0,
                    "limitNumber": "",
                    "payLimitTime": 1,
                    "appPosterImg": "",
                    "isNotice": 1,
                    "limitCustomer": 1,
                    "noticeContent": None,
                    "noticeTime": "",
                    "pcPosterImg": "",
                    "day": 0,
                    "hour": 0,
                    "minute": 0,
                    "payMinute": 0,
                    "limitType": 1,
                    "limitCardTime": 0
                },
                "endTime": None,
                "productDtos": [getProductListByCodeOrName],
                "promotionCode": productCode_qg,
                "promotionName": promotionName_qg,
                "promotionState": 1,
                "promotionType": 1,
                "roleIds": [],
                "startTime": int(round(time.time() * 1000)), # 1651579235000 13位时间戳
                "memberIdentities": [],
                "couponIds": [],
                "serialNos": []
            }                          
            with _mgmt_prmt_addPromotion(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]
       
        @allure.step("活动审核")
        def step_mgmt_prmt_promotionExamine():
            
            data = {
                "promotionId": id, # 活动id
                "examine": 3, # 审核是否通过3通过4不通过
                "remarks": "同意执行该活动", # 备注
                "enclosureVos": [] # 附件集合
            }                          
            with _mgmt_prmt_promotionExamine(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
       
        step_mgmt_prmt_deleteCacheMember()
        step_mgmt_prmt_selectPromotionCode()
        if code != 500:
            step_mgmt_prmt_getProductListByCodeOrName()
            if code != 500:
                step_mgmt_prmt_getMemberIdentity()
                step_mgmt_prmt_addPromotion()
                step_mgmt_prmt_promotionExamine()
        
        
         
        
        



            
