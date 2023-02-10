# coding:utf-8

from api.mall_mgmt_application._mgmt_product_cfg_menu_catalog import _mgmt_product_cfg_menu_catalog # 菜单列表-产品类型
from api.mall_mgmt_application._mgmt_product_cfg_menu_show import _mgmt_product_cfg_menu_show # 菜单列表-前端展示
from api.mall_mgmt_application._mgmt_product_cfg_menu_brand import _mgmt_product_cfg_menu_brand # 菜单列表-产品品牌
from api.mall_mgmt_application._mgmt_product_cfg_menu_company import _mgmt_product_cfg_menu_company # 菜单列表-销售主体
from api.mall_mgmt_application._mgmt_product_cfg_menu_tag import _mgmt_product_cfg_menu_tag # 菜单列表-产品标签
from api.mall_mgmt_application._mgmt_product_cfg_getPrice import _mgmt_product_cfg_getPrice # 价格参数查询
from api.mall_center_sys._mgmt_sys_getCarriList import _mgmt_sys_getCarriList # 查询所有的运费模板
from api.mall_center_sys._mgmt_sys_lclFee_list import _mgmt_sys_lclFee_list # 获取拼箱费列表
from api.basic_services._storage_upload import files, _storage_upload # 上传商品图片

from api.mall_mgmt_application._mgmt_product_item_saveVersion import data, _mgmt_product_item_saveVersion

from setting import P1, P2, P3, productCode_qg, productCode_qg_title, productCode_zh, productCode_zh_title, productCode, productCode_title, productCode_ys, productCode_ys_title

from copy import deepcopy
import os
import allure
import time
import pytest
import datetime


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/saveVersion")
@pytest.mark.skip("仅创建产品一次")
class TestClass:
    """
    添加商品
    /mgmt/product/item/saveVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.files = deepcopy(files)
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("添加组合产品")
    def test_01_mgmt_product_item_saveVersion(self):
        
        fileUrlKey = [] # 上传图片存储url
        
        @allure.title("上传商品图片1")
        def step_storage_upload():
            
            nonlocal fileUrlKey
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-store", # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:  
                fileUrlKey.append(r.json()["datas"]["fileUrlKey"])          
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"

        @allure.title("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 3,
                "productId": "",
                "versionStatus": 2,
                "serialNo": productCode_zh,
                "discountBoxNum": None,
                "catalogTitle": "化妆品(玛丽艳美容护肤品)",
                "catalogId": "3",
                "showIds": ["3"],
                "title": productCode_zh_title,
                "brandTitle": "玛丽艳",
                "brandId": "3",
                "meterUnit": "盒",
                "packing": "84瓶/盒*5盒",
                "boxNum": "420",
                "saleCompanyTitle": "完美中国",
                "saleCompanyId": "2",
                "propertyRights": "",
                "processMode": 1,
                "orderType": 1,
                "shippingTpl": "按订单金额收取运费",
                "shippingId": "1217978678543324234",
                "directSale": 0,
                "guarantee": "",
                "tags": [],
                "bundleProducts": [
                    {
                        "amount": 5,
                        "productId": "232",
                        "serialNo": productCode,
                        "title": productCode_title,
                        "retailPrice": 480,
                        "versionId": "4237",
                        "pv": 410,
                        "subId": "232",
                        "subVerId": "4237"
                    }
                ],
                "customProducts": [],
                "lclFeeId": "",
                "retailPrice": "1440",
                "securityPrice": 480,
                "groupPrice": 1123,
                "pv": "1230",
                "orderPrice": 1224,
                "activityPrice": "",
                "preDepositPrice": "",
                "depositDiscountPrice": "",
                "discountPrice": "",
                "attrs": "{}",
                "verMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey[0]
                    }, 
                ],
                "videoMedais": [],
                "imgMedais": [
                    {
                    "mediaType": 1,
                    "sort": 1,
                    "storageType": 1,
                    "url": fileUrlKey[0]
                    }, 
                ],
                "webContent": "",
                "appContent": "",
                "serveContent": "<p><span id=\"_mce_caret\" data-mce-bogus=\"1\" data-mce-type=\"format-caret\"><strong></strong></span></p><p><br data-mce-bogus=\"1\"></p>",
                "stopBatType": None,
                "stopBatTime": None,
                "isStopBat": 0,
                "isStopSale": 0,
                "isStopDiscountBat": 0,
                "isStopDiscountTransfer": 0,
                "isExchangeProduct": 0,
                "isInstall": 0,
                "isRepair": 0,
                "isReturnRepair": 0,
                "isConsumeStock": 0,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "isActivateItem": 0,
                "isPreProduct": 0,
                "isIdentityLimit": 0,
                "isLimitNum": 0,
                "orderWay": 1,
                "deliverWay": 1,
                "saleTimeType": 1,
                "upSaleTime": None,
                "downSaleTime": None,
                "customerIdentityTypes": [],
                "customerCardTypes": []
            }
            
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P1)
    @allure.title("添加抢购活动产品")
    def test_02_mgmt_product_item_saveVersion(self):
        
        fileUrlKey = [] # 上传图片存储url
        id = None
        
        @allure.title("上传商品图片1")
        def step_storage_upload():
            
            nonlocal fileUrlKey
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-store", # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey.append(r.json()["datas"]["fileUrlKey"]) 

        @allure.title("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            nonlocal id
            data = {
                "id": "",
                "productType": 1,
                "productId": "",
                "versionStatus": 2,
                "serialNo": productCode_qg,
                "discountBoxNum": None,
                "catalogTitle": "化妆品(玛丽艳美容护肤品)",
                "catalogId": "3",
                "showIds": ["3"],
                "title": productCode_qg_title,
                "brandTitle": "玛丽艳",
                "brandId": "3",
                "meterUnit": "瓶",
                "packing": "100ml/瓶",
                "boxNum": "12",
                "saleCompanyTitle": "完美中国",
                "saleCompanyId": "2",
                "propertyRights": "",
                "processMode": 1,
                "orderType": 1,
                "shippingTpl": "按订单金额收取运费",
                "shippingId": "1217978678543324234",
                "directSale": 1,
                "guarantee": "365",
                "tags": [],
                "bundleProducts": [],
                "customProducts": [],
                "lclFeeId": "",
                "retailPrice": "300",
                "securityPrice": 100,
                "groupPrice": 150,
                "pv": "280",
                "orderPrice": "255",
                "activityPrice": "260",
                "preDepositPrice": "",
                "depositDiscountPrice": "",
                "discountPrice": "",
                "attrs": "{}",
                "verMedais": [{
                    "mediaType": 1,
                    "sort": 1,
                    "storageType": 1,
                    "url": fileUrlKey[0]
                }],
                "videoMedais": [],
                "imgMedais": [{
                    "mediaType": 1,
                    "sort": 1,
                    "storageType": 1,
                    "url": fileUrlKey[0]
                }],
                "webContent": "",
                "appContent": "",
                "serveContent": "",
                "stopBatType": None,
                "stopBatTime": None,
                "isStopBat": 0,
                "isStopSale": 0,
                "isStopDiscountBat": 0,
                "isStopDiscountTransfer": 0,
                "isExchangeProduct": 0,
                "isInstall": 0,
                "isRepair": 0,
                "isReturnRepair": 0,
                "isConsumeStock": 0,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "isActivateItem": 0,
                "isPreProduct": 0,
                "isIdentityLimit": 0,
                "isLimitNum": 0,
                "orderWay": 99,
                "deliverWay": 1,
                "saleTimeType": 1,
                "upSaleTime": None,
                "downSaleTime": None,
                "customerIdentityTypes": [],
                "customerCardTypes": []
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
                id = r.json()["data"]
        
        step_storage_upload()
        step_mgmt_product_item_saveVersion()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/saveVersion")
@pytest.mark.skip("以测试发版上线")
class TestClass02:
    """
    添加商品-提交待审核
    /mgmt/product/item/saveVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.files = deepcopy(files)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("添加商品-成功路径: 禁止85折押货+禁止85折转分立即生效检查")
    def test_01_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 0, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": None, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 0, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": None, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P2)
    @allure.title("添加商品-成功路径: 禁止85折押货+禁止85折转分定时生效检查")
    def test_02_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 1, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 1, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 禁止85折押货定时生效+禁止85折转分立即生效检查")
    def test_03_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 1, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 2, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 禁止85折押货立即生效+禁止85折转分定时生效检查")
    def test_04_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 2, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 1, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折押货立即生效检查")
    def test_05_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 2, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 0, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": None, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折押货定时生效检查")
    def test_06_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 1, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 0, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": None, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折转分立即生效检查")
    def test_07_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 0, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": None, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 2, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折转分定时生效检查")
    def test_08_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 2, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 0, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": None, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 1, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/saveVersion")
class TestClass03:
    """
    添加商品-提交草稿
    /mgmt/product/item/saveVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.files = deepcopy(files)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("添加商品-成功路径: 禁止85折押货+禁止85折转分立即生效草稿检查")
    def test_01_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 0, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": None, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 0, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": None, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P2)
    @allure.title("添加商品-成功路径: 禁止85折押货+禁止85折转分定时生效草稿检查")
    def test_02_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 1, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 1, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 禁止85折押货定时生效+禁止85折转分立即生效草稿检查")
    def test_03_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 1, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 2, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 禁止85折押货立即生效+禁止85折转分定时生效草稿检查")
    def test_04_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 2, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 1, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折押货立即生效草稿检查")
    def test_05_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 2, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 0, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": None, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折押货定时生效草稿检查")
    def test_06_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 1, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": 1, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 0, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": None, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折转分立即生效草稿检查")
    def test_07_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 0, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": None, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 2, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": None, #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

    @allure.severity(P3)
    @allure.title("添加商品-成功路径: 仅禁止85折转分定时生效草稿检查")
    def test_08_mgmt_product_item_saveVersion(self):
        
        menu_catalog = [] # 菜单列表-产品类型
        menu_show = [] # 菜单列表-前端展示
        menu_brand = [] # 菜单列表-产品品牌
        menu_company = [] # 菜单列表-销售主体
        menu_tag = [] # 菜单列表-产品标签
        getPrice = {} # 价格参数查询
        getCarriList = [] # 查询所有的运费模板 
        lclFee_list = [] # 获取拼箱费列表
        fileUrlKey_01 = {} # 上传图片存储url
        fileUrlKey_02 = {} # 上传图片存储url
        fileUrlKey_03 = {} # 上传s视频存储url
        
        @allure.step("菜单列表-产品类型")
        def step_mgmt_product_cfg_menu_catalog():
            
            nonlocal menu_catalog
            with _mgmt_product_cfg_menu_catalog(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品类型"
                menu_catalog = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-前端展示")
        def step_mgmt_product_cfg_menu_show():
            
            nonlocal menu_show
            with _mgmt_product_cfg_menu_show(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "前端分类"
                menu_show = r.json()["data"]["childList"]

        @allure.step("菜单列表-产品品牌")
        def step_mgmt_product_cfg_menu_brand():
            
            nonlocal menu_brand
            with _mgmt_product_cfg_menu_brand(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品品牌"
                menu_brand = r.json()["data"]["childList"]

        @allure.step("菜单列表-销售主体")
        def step_mgmt_product_cfg_menu_company():
            
            nonlocal menu_company
            with _mgmt_product_cfg_menu_company(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "销售主体"
                menu_company = r.json()["data"]["childList"]
        
        @allure.step("菜单列表-产品标签")
        def step_mgmt_product_cfg_menu_tag():
            
            nonlocal menu_tag
            with _mgmt_product_cfg_menu_tag(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["title"] == "产品标签"
                menu_tag = r.json()["data"]["childList"]
  
        @allure.step("价格参数查询")
        def step_mgmt_product_cfg_getPrice():
            
            nonlocal getPrice
            with _mgmt_product_cfg_getPrice(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getPrice = r.json()["data"]
  
        @allure.step("查询所有的运费模板")
        def step_mgmt_sys_getCarriList():
            
            nonlocal getCarriList
            with _mgmt_sys_getCarriList(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCarriList = r.json()["data"]

        @allure.step("获取拼箱费列表")
        def step_mgmt_sys_lclFee_list():
            
            nonlocal lclFee_list
            with _mgmt_sys_lclFee_list(self.access_token) as r:           
                assert r.status_code == 200
                assert r.json()["code"] == 200
                lclFee_list = r.json()["data"]
                 
        @allure.step("上传商品图片")
        def step_01_storage_upload():
            
            nonlocal fileUrlKey_01
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035501.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_01 = r.json()["datas"]

        @allure.step("上传商品图片")
        def step_02_storage_upload():
            
            nonlocal fileUrlKey_02
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/m7035502.png"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_02 = r.json()["datas"]

        @allure.step("上传商品视频")
        def step_03_storage_upload():
            
            nonlocal fileUrlKey_03
            files = deepcopy(self.files)  
            files["storageType"] = "PublicCloud" # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
            files["clientKey"] = "mall-center-product" # str客户端Key(由管理员进行分配)
            files["file"] = "data/0610.mp4"
            with _storage_upload(files, self.access_token) as r:     
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"
                fileUrlKey_03 = r.json()["datas"]

        @allure.step("添加商品")
        def step_mgmt_product_item_saveVersion():
            
            data = {
                "id": "",
                "productType": 1, # 商品类型 1-商品，2-定制商品，3-组合商品
                "productId": "", # 商品id，新建版本时为空
                "versionStatus": 1, # 状态：1-草稿，2-待产品审核
                "serialNo": f"HW{str(round(time.time()))[-6:]}", # 商品编码
                "discountBoxNum": "5", # 85折装箱数量
                "catalogTitle": menu_catalog[7]["title"], # 类型名
                "catalogId": menu_catalog[7]["id"], # 类型id
                "showIds": [menu_show[5]["id"]], # 前端标签id
                "title": f"混沌青莲液{str(round(time.time()))[-6:]}号",
                "brandTitle": menu_brand[1]["title"], # 品牌名
                "brandId": menu_brand[1]["id"], # 品牌id
                "meterUnit": "瓶", # 计量单位
                "packing": "80ml/瓶", # 包装规格
                "boxNum": "12", # 装箱数量
                "saleCompanyTitle": menu_company[0]["title"], # 销售主体名
                "saleCompanyId": menu_company[0]["id"], # 销售主体id
                "propertyRights": "", # 产权
                "processMode": 1, # 加工方式，1-自制，2-外购
                "orderType": 1, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
                "shippingTpl": getCarriList[2]["carriageName"], # 运费模板名
                "shippingId": getCarriList[2]["id"], # 运费模板id
                "directSale": 1, # 是否直销，1-是，0-否
                "guarantee": "365", # 保质期
                "tags": [menu_tag[2]["id"]], # 标签id
                "bundleProducts": [], # 组合商品
                "customProducts": [], # 定制商品
                "lclFeeId": lclFee_list[1]["id"], # 85折拼箱费模板id
                "lclFeeTpl": lclFee_list[1]["feeName"], # 85折拼箱费模板名
                "retailPrice": "400", # 零售价
                "securityPrice": 133, # 1:3押货价
                "groupPrice": 200, # 团购价
                "pv": "380",
                "orderPrice": "340", # 85折押货价
                "activityPrice": "300", # 活动价
                "preDepositPrice": "", # 预售定金
                "depositDiscountPrice": "", # 定金优惠金额
                "discountPrice": "", # 折扣价
                "attrs": "{}",
                "verMedais": [ # 媒体信息
                    { 
                        "mediaType": 1, # 体类型，1-图片 2-视频
                        "sort": 1, # 排序
                        "storageType": 1, # 存储类型，1-FastDFS
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 2,
                        "sort": 3,
                        "storageType": 1,
                        "url": fileUrlKey_03["fileUrlKey"],
                        "name": "视频"
                    }
                ],
                "videoMedais": [{
                    "mediaType": 2, # 体类型，1-图片 2-视频
                    "sort": 3, # 排序
                    "storageType": 1, # 存储类型，1-FastDFS
                    "url": fileUrlKey_03["fileUrlKey"],
                    "name": "视频"
                }],
                "imgMedais": [
                    {
                        "mediaType": 1,
                        "sort": 1,
                        "storageType": 1,
                        "url": fileUrlKey_01["fileUrlKey"]
                    }, 
                    {
                        "mediaType": 1,
                        "sort": 2,
                        "storageType": 1,
                        "url": fileUrlKey_02["fileUrlKey"]
                    }
                    ],
                "webContent": "<p>我是pc端产品介绍哈哈哈</p>", # web富文本内容
                "appContent": "<p>我是移动端产品介绍哈哈哈<br data-mce-bogus=\"1\"></p>", # app富文本内容
                "serveContent": "<p>大伟仔为您提供一条龙服务！</p>", # 服务说明
                "shareCopy": "我是产品分享文案哈哈哈哈", # 分享文案
                "discussCopy": "我是朋友圈评论文案呀呀呀呀", # 评论文案
                "isExchangeProduct": 0, #? 是否换购商品 1-是，0-否 ！销售规则
                "isActivateItem": 0, #? 是否升级商品 1-是，0-否 ！销售规则
                "isPreProduct": 0, #? 是否预售产品 1-是，0-否 ！销售规则
                "isStopBat": 0, #! 是否停止押货 1-是，0-否 ！ 售前规则
                "stopBatType": None, #! 停止押货类型 1-定时，2-立即 ！ 售前规则
                "stopBatTime": None, #! 待停止押货时间 ！ 售前规则
                "isStopSale": 0, #! 是否停止销售 1-是，0-否 ！ 售前规则
                "isConsumeStock": 0, #! 是否消耗服务中心库存 1-是，0否 ！ 售前规则
                "isStopDiscountBat": 0, #TODO 是否禁止85折押货 1-是，0-否 ！ 售前规则
                "stopDiscountBatType": None, #TODO 停止85折押货类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountBatTime": None, #TODO 待停止85折押货时间 ！ 售前规则
                "isStopDiscountTransfer": 1, #TODO 是否禁止85折转分 1-是，0-否 ！ 售前规则
                "stopDiscountTransferType": 1, #TODO 停止85折转分类型 1-定时，2-立即 ！ 售前规则
                "stopDiscountTransferTime": int(round((datetime.datetime.now()+datetime.timedelta(hours=1)).timestamp() * 1000)), #TODO 待停止85折转分时间 ！ 售前规则
                "isInvoice": 1, #? 是否开发票 1-是，0-否 ！购买规则
                "isOneOrder": 0, #? 是否支持单独下单 1-是，0-否 ！购买规则
                "isDeliver": 1, #? 是否发货 1-是，0-否 ！购买规则
                "orderWay": 99, #? 下单方式 0-空, 1-自购,2-代购,99-全选 ！购买规则
                "deliverWay": 99, #? 交付方式 0-空, 1-公司交付,2-门店交付,99-全选 ！购买规则
                "isIdentityLimit": 0, #! 是否身份限购 1-是，0-否 ! 限购规则
                "isLimitNum": 0, #! 是否产品限购 1-是，0-否 ! 限购规则
                "customerIdentityTypes": [], #! 身份限购类型 1-普通顾客,2-优惠顾客,3-云商,4-微店 ! 限购规则
                "customerCardTypes": [], #! 会员卡限购类型 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效 ! 限购规则
                "isInstall": 0, #? 是否支持安装 1-是，0-否 ！售后规则
                "isRepair": 0, #? 是否支持维修 1-是，0-否 ！售后规则
                "isReturnRepair": 0, #? 是否支持返厂维修 1-是，0-否 ！售后规则
                "isProductReturn": 1, #? 是否支持可申请退货 1-是，0-否 ！售后规
                "saleTimeType": 1, # 上下架类型，1立即上架 2立即下架 3定时上架 4定时下架 5定时上下架
                "upSaleTime": None, # 待上架时间
                "downSaleTime": None, # 待下架时间
            }
            with _mgmt_product_item_saveVersion(data, self.access_token) as r:        
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "新增成功"
        
        step_mgmt_product_cfg_menu_catalog()
        step_mgmt_product_cfg_menu_show()
        step_mgmt_product_cfg_menu_brand()
        step_mgmt_product_cfg_menu_company()
        step_mgmt_product_cfg_menu_tag()
        step_mgmt_product_cfg_getPrice()
        step_mgmt_sys_getCarriList()
        step_mgmt_sys_lclFee_list()
        step_01_storage_upload()
        step_02_storage_upload()
        step_03_storage_upload()
        step_mgmt_product_item_saveVersion()

