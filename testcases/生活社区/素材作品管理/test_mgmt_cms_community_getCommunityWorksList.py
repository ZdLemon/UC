# coding:utf-8

from api.mall_mgmt_application._mgmt_cms_community_getCommunityWorksList import data, _mgmt_cms_community_getCommunityWorksList # 生活社区—查询素材作品列表
from api.mall_mgmt_application._mgmt_cms_community_getCommunityCategoryList import _mgmt_cms_community_getCommunityCategoryList # 生活社区—查询品类列表
from api.mall_mgmt_application._mgmt_inventory_common_getCompanyList import _mgmt_inventory_common_getCompanyList # 获取分公司列表

from util.stepreruns import stepreruns
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
import uuid


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/cms/community/getCommunityWorksList")
class TestClass:
    """
    生活社区—查询素材作品列表
    /mgmt/cms/community/getCommunityWorksList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询编号检查")
    def test_01_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取编号")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询编号检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["worksSerial"] = getCommunityWorksList["worksSerial"]              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["worksSerial"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["worksSerial"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询品类检查")
    def test_02_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityCategoryList = {}
        
        @allure.step("生活社区—查询品类列表")
        def step_mgmt_cms_community_getCommunityCategoryList():
            
            nonlocal getCommunityCategoryList             
            with _mgmt_cms_community_getCommunityCategoryList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityCategoryList = r.json()["data"]

        @allure.step("生活社区—查询素材作品列表:查询品类检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["categoryId"] = categoryId["id"]              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["categoryId"] for d in r.json()["data"]["list"]):
                        assert i == categoryId["id"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_cms_community_getCommunityCategoryList()
        for categoryId in getCommunityCategoryList:             
            step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询类型检查")
    @pytest.mark.parametrize("materialType", [1, 2], ids=["图文", "视频"])
    def test_03_mgmt_cms_community_getCommunityWorksList(self, materialType):
            
        data = deepcopy(self.data)
        data["materialType"] = materialType             
        with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["materialType"] for d in r.json()["data"]["list"]):
                    assert i == materialType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询标题检查")
    def test_04_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取标题")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询标题检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["worksSerial"] = getCommunityWorksList["title"]              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["title"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["title"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
                  
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询状态检查")
    @pytest.mark.parametrize("worksStatus", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ids=["系统审核不通过", "待人工审核", "人工审核不通过", "待资格审核", "资格审核不通过", "待初审", "初审不通过", "待复审", "复审不通过", "核通过"])
    def test_05_mgmt_cms_community_getCommunityWorksList(self, worksStatus):
            
        data = deepcopy(self.data)
        data["worksStatus"] = worksStatus # 审核状态 -1：审核中 0:系统审核不通过;1:待人工审核；2:人工审核不通过;3:待资格审核;4:资格审核不通过;5:待初审;6:初审不通过;7:待复审;8:复审不通过;9:审核通过            
        with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["worksStatus"] for d in r.json()["data"]["list"]):
                    assert i == worksStatus
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询发布人姓名检查")
    def test_06_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取发布人姓名")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询发布人姓名检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["userName"] = getCommunityWorksList["userName"]              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["userName"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["userName"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询发布人卡号检查")
    def test_07_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取发布人卡号")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询发布人卡号检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["cardNo"] = getCommunityWorksList["cardNo"]              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["cardNo"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询提交时间检查")
    def test_08_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取提交时间")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:查询提交时间检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["startTime"] = f'{getCommunityWorksList["commitTime"][:10]} 00:00:00'
            data["endTime"] = f'{getCommunityWorksList["commitTime"][:10]} 23:59:59'             
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["commitTime"][:10] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["commitTime"][:10]
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询作品类型检查")
    @pytest.mark.parametrize("awards", [-1, 0, 1], ids=["入围作品", "人气作品", "获奖作品"])
    def test_09_mgmt_cms_community_getCommunityWorksList(self, awards):
            
        data = deepcopy(self.data)
        data["awards"] = awards # 是否获奖 -1:入围作品；0：人气作品; 1:获奖作品             
        with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert str(awards) in i["awards"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询品类检查")
    def test_10_mgmt_cms_community_getCommunityWorksList(self):
        
        getCompanyList = {}
        
        @allure.step("获取分公司列表")
        def step_mgmt_inventory_common_getCompanyList():
            
            nonlocal getCompanyList             
            with _mgmt_inventory_common_getCompanyList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCompanyList = r.json()["data"]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询编号检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["regionCode"] = Community["code"]              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["companyArea"] for d in r.json()["data"]["list"]):
                        assert i in Community["name"][:-3]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_inventory_common_getCompanyList()
        for Community in getCompanyList:             
            step_02_mgmt_cms_community_getCommunityWorksList()
               

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/cms/community/getCommunityWorksList")
class TestClass02:
    """
    生活社区—查询素材作品列表：待人工审核tab
    /mgmt/cms/community/getCommunityWorksList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询编号检查")
    def test_01_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取编号")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 1              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询编号检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["worksSerial"] = getCommunityWorksList["worksSerial"] 
            data["worksStatus"] = 1             
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["worksSerial"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["worksSerial"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询品类检查")
    def test_02_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityCategoryList = {}
        
        @allure.step("生活社区—查询品类列表")
        def step_mgmt_cms_community_getCommunityCategoryList():
            
            nonlocal getCommunityCategoryList             
            with _mgmt_cms_community_getCommunityCategoryList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityCategoryList = r.json()["data"]

        @allure.step("生活社区—查询素材作品列表:查询品类检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["categoryId"] = categoryId["id"] 
            data["worksStatus"] = 1             
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["categoryId"] for d in r.json()["data"]["list"]):
                        assert i == categoryId["id"]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_cms_community_getCommunityCategoryList()
        for categoryId in getCommunityCategoryList:             
            step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询类型检查")
    @pytest.mark.parametrize("materialType", [1, 2], ids=["图文", "视频"])
    def test_03_mgmt_cms_community_getCommunityWorksList(self, materialType):
            
        data = deepcopy(self.data)
        data["materialType"] = materialType 
        data["worksStatus"] = 1            
        with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["materialType"] for d in r.json()["data"]["list"]):
                    assert i == materialType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询标题检查")
    def test_04_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取标题")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 1              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询标题检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["worksSerial"] = getCommunityWorksList["title"]
            data["worksStatus"] = 1              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["title"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["title"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
                  
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询发布人姓名检查")
    def test_06_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取发布人姓名")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 1              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询发布人姓名检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["userName"] = getCommunityWorksList["userName"]
            data["worksStatus"] = 1              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["userName"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["userName"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 仅支持精确查询发布人卡号检查")
    def test_07_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取发布人卡号")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data) 
            data["worksStatus"] = 1             
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询发布人卡号检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["cardNo"] = getCommunityWorksList["cardNo"] 
            data["worksStatus"] = 1             
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["cardNo"] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["cardNo"] 
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询提交时间检查")
    def test_08_mgmt_cms_community_getCommunityWorksList(self):
        
        getCommunityWorksList = {}
        
        @allure.step("生活社区—查询素材作品列表:获取提交时间")
        def step_01_mgmt_cms_community_getCommunityWorksList():
            
            nonlocal getCommunityWorksList
            data = deepcopy(self.data)
            data["worksStatus"] = 1              
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCommunityWorksList = r.json()["data"]["list"][0]

        @allure.step("生活社区—查询素材作品列表:查询提交时间检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["startTime"] = f'{getCommunityWorksList["commitTime"][:10]} 00:00:00'
            data["endTime"] = f'{getCommunityWorksList["commitTime"][:10]} 23:59:59' 
            data["worksStatus"] = 1            
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["commitTime"][:10] for d in r.json()["data"]["list"]):
                    assert i == getCommunityWorksList["commitTime"][:10]
        
        step_01_mgmt_cms_community_getCommunityWorksList()               
        step_02_mgmt_cms_community_getCommunityWorksList()
               
    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询作品类型检查")
    @pytest.mark.parametrize("awards", [-1, 0, 1], ids=["入围作品", "人气作品", "获奖作品"])
    def test_09_mgmt_cms_community_getCommunityWorksList(self, awards):
            
        data = deepcopy(self.data)
        data["awards"] = awards # 是否获奖 -1:入围作品；0：人气作品; 1:获奖作品
        data["worksStatus"] = 1             
        with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in r.json()["data"]["list"]:
                    assert str(awards) in i["awards"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("生活社区—查询素材作品列表: 查询品类检查")
    def test_10_mgmt_cms_community_getCommunityWorksList(self):
        
        getCompanyList = {}
        
        @allure.step("获取分公司列表")
        def step_mgmt_inventory_common_getCompanyList():
            
            nonlocal getCompanyList             
            with _mgmt_inventory_common_getCompanyList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCompanyList = r.json()["data"]

        @allure.step("生活社区—查询素材作品列表:仅支持精确查询编号检查")
        def step_02_mgmt_cms_community_getCommunityWorksList():
            
            data = deepcopy(self.data)
            data["regionCode"] = Community["code"]
            data["worksStatus"] = 1               
            with _mgmt_cms_community_getCommunityWorksList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["companyArea"] for d in r.json()["data"]["list"]):
                        assert i in Community["name"][:-3]
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_inventory_common_getCompanyList()
        for Community in getCompanyList:             
            step_02_mgmt_cms_community_getCommunityWorksList()
               

