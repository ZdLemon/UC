# coding:utf-8

from api.mall_mgmt_application._mgmt_cms_community_getCommunityWorksList import data, _mgmt_cms_community_getCommunityWorksList # 生活社区—查询素材作品列表
from api.mall_mgmt_application._mgmt_cms_community_communityWorksAudit import _mgmt_cms_community_communityWorksAudit # 生活社区-作品审核

from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
import uuid
            

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/cms/community/communityWorksAudit")
class TestClass02:
    """
    生活社区-作品审核
    /mgmt/cms/community/communityWorksAudit
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("生活社区-作品审核-成功路径: 待资格审核状态审核通过检查")
    def test_01_mgmt_cms_community_communityWorksAudit(self):
        
        getCommunityWorksList = []
        
        @allure.step("生活社区—查询素材作品列表:获取id")
        def step_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 3
            data["pageSize"] = 100              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getCommunityWorksList.append(i["id"])

        @allure.step("生活社区-作品审核")
        def step_mgmt_cms_community_communityWorksAudit():
            
            data = {
                "id": id,
                "remarks": "资格审核通过了资格审核通过了资格审核通过了",
                "worksStatus": 5 # 审核状态 2:人工审核不通过 3:(人工审核通过)待资格审核; 4:资格审核不通过 5:(资格审核通过)待初审;6:初审不通过 7:(初审通过)待复审;8:复审不通过 9:审核通过
            }             
            with _mgmt_cms_community_communityWorksAudit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_cms_community_getCommunityWorksList()
        if getCommunityWorksList:
            for id in getCommunityWorksList:               
                step_mgmt_cms_community_communityWorksAudit()
               
    @allure.severity(P2)
    @allure.title("生活社区-作品审核-成功路径: 待初审状态审核通过检查")
    def test_02_mgmt_cms_community_communityWorksAudit(self):
        
        getCommunityWorksList = []
        
        @allure.step("生活社区—查询素材作品列表:获取id")
        def step_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 5
            data["pageSize"] = 100              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getCommunityWorksList.append(i["id"])

        @allure.step("生活社区-作品审核")
        def step_mgmt_cms_community_communityWorksAudit():
            
            data = {
                "id": id,
                "remarks": "待初审通过待初审通过待初审通过待初审通过",
                "worksStatus": 7 # 审核状态 2:人工审核不通过 3:(人工审核通过)待资格审核; 4:资格审核不通过 5:(资格审核通过)待初审;6:初审不通过 7:(初审通过)待复审;8:复审不通过 9:审核通过
            }             
            with _mgmt_cms_community_communityWorksAudit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_cms_community_getCommunityWorksList()
        if getCommunityWorksList:
            for id in getCommunityWorksList:               
                step_mgmt_cms_community_communityWorksAudit()
    
    @allure.severity(P2)
    @allure.title("生活社区-作品审核-成功路径: 待复审审核通过检查")
    def test_03_mgmt_cms_community_communityWorksAudit(self):
        
        getCommunityWorksList = []
        
        @allure.step("生活社区—查询素材作品列表:获取id")
        def step_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 7
            data["pageSize"] = 100              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        getCommunityWorksList.append(i["id"])

        @allure.step("生活社区-作品审核")
        def step_mgmt_cms_community_communityWorksAudit():
            
            data = {
                "id": id,
                "remarks": "待复审通过待复审通过待复审通过待复审通过待复审通过",
                "worksStatus": 9 # 审核状态 2:人工审核不通过 3:(人工审核通过)待资格审核; 4:资格审核不通过 5:(资格审核通过)待初审;6:初审不通过 7:(初审通过)待复审;8:复审不通过 9:审核通过
            }             
            with _mgmt_cms_community_communityWorksAudit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_cms_community_getCommunityWorksList()
        if getCommunityWorksList:
            for id in getCommunityWorksList:               
                step_mgmt_cms_community_communityWorksAudit()
  