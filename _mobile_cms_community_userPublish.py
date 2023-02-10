# coding:utf-8

from api.basic_services._login import _login
from api.basic_services._login_oauth_token import _login_oauth_token
from api.mall_center_member._member_mgmt_getVipList import _member_mgmt_getVipList # 获取优惠顾客列表
from api.mall_center_member._member_mgmt_resetMemberPassword import _member_mgmt_resetMemberPassword # 重置会员密码
from api.mall_mobile_application._mobile_cms_community_getRegionList import _mobile_cms_community_getRegionList # 获取活动报名地区列表
from api.mall_mobile_application._mobile_cms_community_getUserInfo import _mobile_cms_community_getUserInfo # 获取用户信息
from api.mall_mobile_application._mobile_cms_community_communityRegister import _mobile_cms_community_communityRegister # 活动报名
from api.basic_services._storage_upload import files as files01, _storage_upload # 上传商品图片
from api.mall_mobile_application._mobile_cms_community_userPublish import _mobile_cms_community_userPublish # 用户作品发布

from copy import deepcopy
import time
import allure
import os

BASE_URL = "https://uc-test.perfect99.com/api"


def test_mobile_cms_community_userPublish():
    "生活社区-作品发布"

    getVipList = [] # 获取优惠顾客列表
    community_getRegionList = None # 获取活动报名地区列表
    getUserInfo = None # 获取用户信息 
    fileUrlKey_01 = {} # 上传图片存储url
    fileUrlKey_02 = {} # 上传图片存储url
    access_token = ""
    access_toke = "" # 

    @allure.step("登录完美运营后台,获取access_token")
    def step_01_login():

        nonlocal access_token
        with _login(username="test01") as r:
            assert r.status_code == 200
            access_token = r.json()["data"]["access_token"]

    @allure.step("获取优惠顾客列表")
    def step_member_mgmt_getVipList():
        
        nonlocal getVipList
        params = {
            "showType": 1,
            "pageNum": 2,
            "pageSize": 100,
            "cardNo": None,
            "mobile": None,
            "realname": None,
            "certificatesNo": None,
            "aboutMobile": None,
            "status": 0,
            "mobileVaildStatus": None,
            "selfIdCardVaildStatus": None,
            "spouseIdCardVaildStatus": None,
            "channel": None,
            "userSource": None,
            "registrationTime": None,
            "promotionTime": None,
            "promotionType": None,
            "registerMode": None,
            "openCardMode": None,
            "openCardStartTime": 1640361600000,
            "openCardEndTime": 1655999999999,
            "promotionTimeStart": None,
            "promotionTimeEnd": None,
        }          
        with _member_mgmt_getVipList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in r.json()["data"]["list"]:
                getVipList.append((i["memberId"], i["cardNo"]))

    @allure.step("重置会员密码")
    def step_member_mgmt_resetMemberPassword():
        
        data = {
            "id": id, # ID，主账号传会员ID，子账号传子账号ID
        }           
        with _member_mgmt_resetMemberPassword(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.step("登录PC商城，获取token")
    def step_02_login():
        
        nonlocal access_toke
        with _login_oauth_token(username=username) as r:
            assert r.status_code == 200
            access_toke = r.json()["data"]["access_token"]

    @allure.step("获取活动报名地区列表")
    def step_mobile_cms_community_getRegionList():
        
        nonlocal community_getRegionList            
        with _mobile_cms_community_getRegionList(access_toke) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            community_getRegionList = r.json()["data"]

    @allure.step("获取用户信息")
    def step_mobile_cms_community_getUserInfo():
        
        nonlocal getUserInfo             
        with _mobile_cms_community_getUserInfo(access_toke) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getUserInfo = r.json()["data"]

    @allure.step("活动报名")
    def step_mobile_cms_community_communityRegister():
        
        if getUserInfo["companyArea"] and getUserInfo["regionCode"]:
            data = {
                "userName": getUserInfo["userName"],
                "companyArea": getUserInfo["companyArea"],
                "regionCode": getUserInfo["regionCode"],
                "contactAddress":""
            }
        else:
            data = {
                "userName": getUserInfo["userName"],
                "companyArea": "广东",
                "regionCode": "02000",
                "contactAddress":""
            }         
        with _mobile_cms_community_communityRegister(data, access_toke) as r:
            assert r.status_code == 200

    @allure.step("上传商品图片")
    def step_01_storage_upload():
        
        nonlocal fileUrlKey_01
        files = deepcopy(files01)  
        files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
        files["clientKey"] = "mall-center-store" # str客户端Key(由管理员进行分配)
        files["file"] = "data/m7035501.png"
        with _storage_upload(files, access_toke) as r:     
            assert r.status_code == 200
            assert r.json()["datas"]["msg"] == "文件上传成功"
            fileUrlKey_01 = r.json()["datas"]

    @allure.step("上传商品图片")
    def step_02_storage_upload():
        
        nonlocal fileUrlKey_02
        files = deepcopy(files01)  
        files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
        files["clientKey"] = "mall-center-store" # str客户端Key(由管理员进行分配)
        files["file"] = "data/m7035501.png"
        with _storage_upload(files, access_toke) as r:     
            assert r.status_code == 200
            assert r.json()["datas"]["msg"] == "文件上传成功"
            fileUrlKey_02 = r.json()["datas"]
                        
    @allure.step("生活社区—查询素材作品列表:仅支持精确查询发布人卡号检查")
    def step_mobile_cms_community_userPublish():
        
        data = {
            "title": f"{getUserInfo['userName']}生活馆{int(time.time())}",
            "content": "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈",
            "categoryId": "3",
            "materialType": 1,
            "linkProductList": [
                {
                    "serialNo": "AG",
                    "title": "完美芦荟胶",
                    "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/202104021453563l40u.png",
                    "retailPrice": 40,
                    "underlinedPrice": 40,
                    "pv": 20,
                    "checked": True
                }, 
                {
                    "serialNo": "AG2",
                    "title": "完美芦荟胶礼盒",
                    "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402145642464FT.png",
                    "retailPrice": 51,
                    "underlinedPrice": 51,
                    "pv": 59,
                    "checked": True
                }
            ],
            "linkUrls": [
                {
                    "url": fileUrlKey_01["fileUrlKey"]
                }, 
                {
                    "url": fileUrlKey_02["fileUrlKey"]
                }
                ]
        }             
        time.sleep(1)
        with _mobile_cms_community_userPublish(data, access_toke) as r:
            assert r.status_code == 200

    step_01_login()
    step_member_mgmt_getVipList()
    for id, username in getVipList:
        step_member_mgmt_resetMemberPassword()
        step_02_login()
        step_mobile_cms_community_getRegionList()
        step_mobile_cms_community_getUserInfo() 
        step_mobile_cms_community_communityRegister()
        step_01_storage_upload()
        step_02_storage_upload() 
        for i in range(6):             
            step_mobile_cms_community_userPublish()

                
test_mobile_cms_community_userPublish()
