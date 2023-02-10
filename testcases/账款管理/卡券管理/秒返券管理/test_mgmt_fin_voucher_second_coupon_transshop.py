# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_transshop import data, _mgmt_fin_voucher_second_coupon_transshop
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryList import data as data02, _mgmt_fin_voucher_second_coupon_queryList

from api.mall_mgmt_application._mgmt_store_updatePermission import data as data03, _mgmt_store_updatePermission # 权限编辑
from api.mall_mgmt_application._mgmt_store_getByParms import params as params03, _mgmt_store_getByParms # 根据常用条件查询服务中心
from api.mall_mgmt_application._mgmt_store_listStore import params as params04, _mgmt_store_listStore # 获取服务中心权限列表
from api.mall_mgmt_application._mgmt_store_getStoreName import params as params05, _mgmt_store_getStoreName # 根据服务中心编号获取服务中心名称(正常服务中心)
from util.stepreruns import stepreruns

from setting import P1, P2, P3, username_vip, store13, store85, store

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/transshop")
@pytest.mark.usefixtures("updatePermission", "updatePermission_85")
class TestClass:
    """
    秒返券转店
    /mgmt/fin/voucher/second/coupon/transshop
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.params05 = deepcopy(params05)
        self.access_token = os.environ["access_token_2"]

    @allure.severity(P1)
    @allure.title("秒返券转店-成功路径: 仅一张未使用的秒返券转店检查")
    def test_01_mgmt_fin_voucher_second_coupon_transshop(self, updatePermission):      
        
        secondCouponId = None # 待转店的券Id
        sourceOrderNo = None # 待转店的券来源订单号
        storename = None # 服务中心信息  
        
        @allure.step("秒返券列表: 获取待转店的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId, sourceOrderNo
            data = deepcopy(self.data02)
            data["cardNo"] = username_vip
            data["couponStatusList"] = [2]
            data["sourceStoreCode"] = store     
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                if r.json()["data"]["list"]:
                    secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
                    sourceOrderNo = r.json()["data"]["list"][0]["sourceOrderNo"]
        
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal storename
            params = deepcopy(self.params05)
            params["storeCode"] = store13
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                storename = r.json()["data"]
                
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].append(secondCouponId)   
            data["targetShopCode"] = store13
            data["targetShopName"] = storename
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200

        @allure.step("秒返券列表: 查看是否转店成功")
        def step_02_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId, sourceOrderNo
            data = deepcopy(self.data02)
            data["sourceOrderNo"] = sourceOrderNo 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                ids = []
                for d in r.json()["data"]["list"]:
                    ids.append(d["secondCouponId"])
                
                assert secondCouponId in ids

        step_01_mgmt_fin_voucher_second_coupon_queryList()
        if secondCouponId:
            step_mgmt_store_getStoreName()
            step_mgmt_fin_voucher_second_coupon_transshop()
            step_02_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P1)
    @allure.title("秒返券转店-成功路径: 多张未使用的秒返券转店检查")
    def test_02_mgmt_fin_voucher_second_coupon_transshop(self, updatePermission_85):      
           
        secondCouponId = [] # 待转店的券Id
        sourceOrderNo = set() # 待转店的券来源订单号
        storename = None # 服务中心信息
        
        @allure.step("秒返券列表: 获取待转店的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId, sourceOrderNo
            data = deepcopy(self.data02)
            data["cardNo"] = username_vip
            data["couponStatusList"] = [2]
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                if r.json()["data"]["list"]:
                    secondCouponId.append(r.json()["data"]["list"][0]["secondCouponId"])
                    secondCouponId.append(r.json()["data"]["list"][1]["secondCouponId"])
                    sourceOrderNo.add(r.json()["data"]["list"][0]["sourceOrderNo"])
                    sourceOrderNo.add(r.json()["data"]["list"][1]["sourceOrderNo"])
        
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal storename
            params = deepcopy(self.params05)
            params["storeCode"] = store13  
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                storename = r.json()["data"]
                
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].extend(secondCouponId ) 
            data["targetShopCode"] = store13
            data["targetShopName"] = storename 
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200

        @allure.step("秒返券列表: 查看是否转店成功")
        def step_02_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId, sourceOrderNo
            data = deepcopy(self.data02)
            ids = []
            for s in sourceOrderNo:
                data["sourceOrderNo"] = s   
                with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                    for d in r.json()["data"]["list"]:
                        ids.append(d["secondCouponId"])
                
            assert secondCouponId <= ids

        step_01_mgmt_fin_voucher_second_coupon_queryList()
        if secondCouponId:
            step_mgmt_store_getStoreName()
            step_mgmt_fin_voucher_second_coupon_transshop()
            step_02_mgmt_fin_voucher_second_coupon_queryList()

    @allure.severity(P2)
    @allure.title("秒返券转店-失败路径: 仅未使用的秒返券可以转店检查")
    @pytest.mark.parametrize("couponStatus,couponStatusname", [(1, "已使用"), (3, "占用中"), (4, "已失效"), (5, "已撤回"), (6, "已提现"), (7, "提现中"), (8, "已锁定")])
    def test_03_mgmt_fin_voucher_second_coupon_transshop(self, couponStatus, couponStatusname, updatePermission):      
           
        secondCouponId = None # 待转店的券Id
        storename = None # 服务中心信息
        
        @allure.step("秒返券列表: 获取待转店的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data02)
            data["couponStatusList"] = [couponStatus]
            data["effectStartTimeStr"] = None
            data["effectEndTimeStr"] = None
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                if r.json()["data"]["list"]:
                    secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
        
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal storename
            params = deepcopy(self.params05)
            params["storeCode"] = store13
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                storename = r.json()["data"]
                
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].append(secondCouponId )
            data["targetShopCode"] = store13
            data["targetShopName"] = storename 
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 500
                assert r.status_code == 200
                assert r.json()["message"] == "部分秒返券非未使用状态，请刷新列表后重新选择"

        step_01_mgmt_fin_voucher_second_coupon_queryList()
        if secondCouponId:
            step_mgmt_store_getStoreName()
            step_mgmt_fin_voucher_second_coupon_transshop()

    @allure.severity(P2)
    @allure.title("秒返券转店-失败路径: 多张秒返券中有非未使用的秒返券转店检查")
    @pytest.mark.parametrize("couponStatus,couponStatusname", [(1, "已使用"), (3, "占用中"), (4, "已失效"), (5, "已撤回"), (6, "已提现"), (7, "提现中"), (8, "已锁定")])
    def test_04_mgmt_fin_voucher_second_coupon_transshop(self, couponStatus, couponStatusname, updatePermission):      
           
        secondCouponId = [] # 待转店的券Id
        storename = None # 服务中心信息
        
        @allure.step("秒返券列表: 获取非未使用的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data02)
            data["couponStatusList"] = [couponStatus]
            data["effectStartTimeStr"] = None
            data["effectEndTimeStr"] = None
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                if r.json()["data"]["list"]:
                    secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]

        @allure.step("秒返券列表: 获取未使用的秒返券Id")
        def step_02_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data02)
            data["couponStatusList"] = [2]
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                if r.json()["data"]["list"]:
                    secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
       
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal storename
            params = deepcopy(self.params05)
            params["storeCode"] = store13
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                storename = r.json()["data"]
                
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].extend(secondCouponId )
            data["targetShopCode"] = store13
            data["targetShopName"] = storename 
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 500
                assert r.status_code == 200
                assert r.json()["message"] == "部分秒返券非未使用状态，请刷新列表后重新选择"

        step_01_mgmt_fin_voucher_second_coupon_queryList()
        if secondCouponId:
            step_02_mgmt_fin_voucher_second_coupon_queryList()
            step_mgmt_store_getStoreName()
            step_mgmt_fin_voucher_second_coupon_transshop()

    @allure.severity(P2)
    @allure.title("秒返券转店-成功路径: 转店的服务中心可以和原有的关联服务中心一样检查")
    def test_05_mgmt_fin_voucher_second_coupon_transshop(self, updatePermission):      
        
        secondCouponId = None # 待转店的券Id
        storename = None # 服务中心信息
        
        @allure.step("秒返券列表: 获取待转店的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data02)
            data["cardNo"] = username_vip
            data["couponStatusList"] = [2]
            data["sourceStoreCode"] = store 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                if r.json()["data"]["list"]:
                    secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
        
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal storename
            params = deepcopy(self.params05)
            params["storeCode"] = store 
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200
                storename = r.json()["data"]
                
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].append(secondCouponId)   
            data["targetShopCode"] = store
            data["targetShopName"] = storename        
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200

        @allure.step("秒返券列表: 查看是否转店成功")
        def step_02_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId
            data = deepcopy(self.data02)
            data["cardNo"] = username_vip
            data["couponStatusList"] = [2]
            data["sourceStoreCode"] = store
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                ids = []
                for d in r.json()["data"]["list"]:
                    ids.append(d["secondCouponId"])
                
                assert secondCouponId in ids

        step_01_mgmt_fin_voucher_second_coupon_queryList()
        if secondCouponId:
            step_mgmt_store_getStoreName()
            step_mgmt_fin_voucher_second_coupon_transshop()
            step_02_mgmt_fin_voucher_second_coupon_queryList()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/second/coupon/transshop")
@pytest.mark.usefixtures("updatePermission", "updatePermission_85")
class TestClass02:
    """
    秒返券转店: 只允许转给非取消资格，门店类型为“正式网店，正式网店/申请微店中，正式网店（美容中心转），油葱微店”的服务中心
    /mgmt/fin/voucher/second/coupon/transshop
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.params05 = deepcopy(params05)
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("秒返券转店-成功路径: 非取消资格服务中心仅支持4种类型转店检查")
    @pytest.mark.parametrize("shopType,ids", [
        (1, "正式网点"),
        (2, "正式网点/申请微店中"),
        (3, "正式网点（美容中心转）"),
        (4, "油葱微店（已取消未结清账务）"),
        (5, "油葱微店测试"),
        (6, "油葱微店（结点/取消）"),
        (7, "油葱微店（冻结)"),
        (8, "油葱微店（办理中）"),
        (9, "油葱微店"),
        (10, "已取消（未结清账务）"),
        (11, "新批未运作"),
        (12, "结点/取消"),
        (13, "冻结资格/申请微店中"),
        (14, "冻结资格（美容中心转）"),
        (15, "冻结资格"),
        (16, "办理结点中"),])
    def test_01_mgmt_fin_voucher_second_coupon_transshop(self, shopType, ids):      
        
        secondCouponId = None # 待转店的券Id
        sourceOrderNo = None # 待转店的券来源订单号
        getByParms = None # 服务中心信息
        message = "此服务中心已被取消资格或者冻结/结点，请重新输入"
        
        @allure.step("根据常用条件查询服务中心")
        def step_mgmt_store_getByParms():
            
            nonlocal getByParms
            params = deepcopy(self.params03)
            params["storeCode"] = store13              
            with _mgmt_store_getByParms(params, self.access_token) as r:
                assert r.json()["data"][0]["code"] == store13
                getByParms = r.json()["data"][0]
        
        @allure.step("服务中心权限编辑修改")
        def step_mgmt_store_updatePermission():
            
            data = deepcopy(self.data03)
            data["storeCode"] = getByParms["code"]
            data["storeName"] = getByParms["name"]
            data["leaderName"] = getByParms["leaderName"]
            data["permission"] = "1,2,3,4,5" # 权限
            data["discountPermission"] = "" # 85折押货权限
            data["businessMode"] = 1 
            data["shopType"] = shopType # 网点类型
            if "冻结" in ids:
                data["frozenReason"] = "这个是冻结你的原因" # 冻结原因
                data["frozenTime"] = int(round(time.time()*1000)) # 冻结时间
                data["cancelTime"] = None # 取消时间
            elif "取消" in ids:
                data["frozenReason"] = "" # 冻结原因
                data["frozenTime"] = 0 # 冻结时间
                data["cancelTime"] = int(round(time.time()*1000)) # 取消时间
            else:
                data["frozenReason"] = "" # 冻结原因
                data["frozenTime"] = int(round(time.time()*1000)) # 冻结时间
                data["cancelTime"] = int(round(time.time()*1000)) # 取消时间
                        
            with _mgmt_store_updatePermission(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == True
                assert r.json()["message"] == "操作成功"
            
        @allure.step("获取服务中心权限列表：查看网点类型是否修改成功")
        @stepreruns()
        def step_mgmt_store_listStore():
            
            params = deepcopy(self.params04)
            params["storeCode"] = store13        
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"][0]["shopType"] == shopType
               
        @allure.step("秒返券列表: 获取待转店的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId, sourceOrderNo
            data = deepcopy(self.data02)
            data["couponStatusList"] = [2]    
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
                sourceOrderNo = r.json()["data"]["list"][0]["sourceOrderNo"]
        
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal message
            params = deepcopy(self.params05)
            params["storeCode"] = store13
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                if shopType in [1, 2, 3, 8, 9, 11]:
                    assert r.json()["code"] == 200
                    message = r.json()["message"]
                else:
                    assert r.json()["code"] == 500
                    assert r.json()["message"] == "此服务中心已被取消资格或者冻结/结点，请重新输入"
                               
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].append(secondCouponId)   
            data["targetShopCode"] = store13
            data["targetShopName"] = getByParms["name"]        
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200

        @allure.step("秒返券列表: 查看是否转店成功")
        def step_02_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data02)
            data["sourceOrderNo"] = sourceOrderNo 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:                
                assert r.json()["data"]["list"][0]["sourceStoreCode"] == store13
        
        step_mgmt_store_getByParms()
        step_mgmt_store_updatePermission()
        step_mgmt_store_listStore()
        step_01_mgmt_fin_voucher_second_coupon_queryList()
        step_mgmt_store_getStoreName()
        step_mgmt_fin_voucher_second_coupon_transshop()
        step_02_mgmt_fin_voucher_second_coupon_queryList()


    @allure.severity(P1)
    @allure.title("秒返券转店-成功路径: 非取消资格85折服务中心仅支持4种类型转店检查")
    @pytest.mark.parametrize("shopType,ids", [
        (1, "正式网点"),
        (2, "正式网点/申请微店中"),
        (3, "正式网点（美容中心转）"),
        (4, "油葱微店（已取消未结清账务）"),
        (5, "油葱微店测试"),
        (6, "油葱微店（结点/取消）"),
        (7, "油葱微店（冻结)"),
        (8, "油葱微店（办理中）"),
        (9, "油葱微店"),
        (10, "已取消（未结清账务）"),
        (11, "新批未运作"),
        (12, "结点/取消"),
        (13, "冻结资格/申请微店中"),
        (14, "冻结资格（美容中心转）"),
        (15, "冻结资格"),
        (16, "办理结点中"),])
    def test_02_mgmt_fin_voucher_second_coupon_transshop(self, shopType, ids):      
        
        secondCouponId = None # 待转店的券Id
        sourceOrderNo = None # 待转店的券来源订单号
        getByParms = None # 服务中心信息
        message = "此服务中心已被取消资格或者冻结/结点，请重新输入"
        
        @allure.step("根据常用条件查询服务中心")
        def step_mgmt_store_getByParms():
            
            nonlocal getByParms
            params = deepcopy(self.params03)
            params["storeCode"] = store85
            with _mgmt_store_getByParms(params, self.access_token) as r:
                assert r.json()["data"][0]["code"] == store85
                getByParms = r.json()["data"][0]
        
        @allure.step("服务中心权限编辑修改")
        def step_mgmt_store_updatePermission():
            
            data = deepcopy(self.data03)
            data["storeCode"] = getByParms["code"]
            data["storeName"] = getByParms["name"]
            data["leaderName"] = getByParms["leaderName"]
            data["permission"] = "1,2,3,5,8,9,4" # 权限
            data["discountPermission"] = "" # 85折押货权限
            data["businessMode"] = 2
            data["shopType"] = shopType # 网点类型
            if "冻结" in ids:
                data["frozenReason"] = "这个是冻结你的原因" # 冻结原因
                data["frozenTime"] = int(round(time.time()*1000)) # 冻结时间
                data["cancelTime"] = None # 取消时间
            elif "取消" in ids:
                data["frozenReason"] = "" # 冻结原因
                data["frozenTime"] = 0 # 冻结时间
                data["cancelTime"] = int(round(time.time()*1000)) # 取消时间
            else:
                data["frozenReason"] = None # 冻结原因
                data["frozenTime"] = None # 冻结时间
                data["cancelTime"] = int(round(time.time()*1000)) # 取消时间
                        
            with _mgmt_store_updatePermission(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == True
                assert r.json()["message"] == "操作成功"
            
        @allure.step("获取服务中心权限列表：查看网点类型是否修改成功")
        @stepreruns()
        def step_mgmt_store_listStore():
            
            params = deepcopy(self.params04)
            params["storeCode"] = store85            
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"][0]["shopType"] == shopType
               
        @allure.step("秒返券列表: 获取待转店的秒返券Id")
        def step_01_mgmt_fin_voucher_second_coupon_queryList():
            
            nonlocal secondCouponId, sourceOrderNo
            data = deepcopy(self.data02)
            data["couponStatusList"] = [2]    
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:
                secondCouponId = r.json()["data"]["list"][0]["secondCouponId"]
                sourceOrderNo = r.json()["data"]["list"][0]["sourceOrderNo"]
        
        @allure.step("根据服务中心编号获取服务中心名称(正常服务中心)")
        def step_mgmt_store_getStoreName():
            
            nonlocal message
            params = deepcopy(self.params05)
            params["storeCode"] = store85
            with _mgmt_store_getStoreName(params, self.access_token) as r:
                if shopType in [1, 2, 3, 8, 9, 11]:
                    assert r.json()["code"] == 200
                    message = r.json()["message"]
                else:
                    assert r.json()["code"] == 500
                    assert r.json()["message"] == "此服务中心已被取消资格或者冻结/结点，请重新输入"
                               
        @allure.step("秒返券转店")
        def step_mgmt_fin_voucher_second_coupon_transshop():
            
            data = deepcopy(self.data)
            data["secondCouponIdList"].append(secondCouponId)   
            data["targetShopCode"] = store85
            data["targetShopName"] = getByParms["name"]        
            with _mgmt_fin_voucher_second_coupon_transshop(data, self.access_token) as r:
                assert r.json()["code"] == 200
                assert r.status_code == 200

        @allure.step("秒返券列表: 查看是否转店成功")
        def step_02_mgmt_fin_voucher_second_coupon_queryList():
            
            data = deepcopy(self.data02)
            data["sourceOrderNo"] = sourceOrderNo 
            with _mgmt_fin_voucher_second_coupon_queryList(data, self.access_token) as r:                
                assert r.json()["data"]["list"][0]["sourceStoreCode"] == store85
        
        step_mgmt_store_getByParms()
        step_mgmt_store_updatePermission()
        step_mgmt_store_listStore()
        step_01_mgmt_fin_voucher_second_coupon_queryList()
        step_mgmt_store_getStoreName()
        step_mgmt_fin_voucher_second_coupon_transshop()
        step_02_mgmt_fin_voucher_second_coupon_queryList()
