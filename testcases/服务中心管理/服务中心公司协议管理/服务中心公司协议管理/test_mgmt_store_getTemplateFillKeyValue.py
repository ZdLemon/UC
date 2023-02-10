# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getTemplateFillKeyValue import params, _mgmt_store_getTemplateFillKeyValue
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据服务中心及模板编号获取填充字段-对应值
    /mgmt/store/getTemplateFillKeyValue
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/store/getTemplateFillKeyValue")
    @allure.severity(P2)
    @allure.title("根据服务中心及模板编号获取填充字段-对应值-成功路径: 服务中心+线上协议模板编号检查")
    def test_01_mgmt_store_getTemplateFillKeyValue(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = "902063"
        params["templateNo"] = "MB164491049756884"        
        with _mgmt_store_getTemplateFillKeyValue(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == [
                {"name":"负责人手机号码","value":"15913029179","required":True},
                {"name":"法人身份证号码","value":"445122197908242221","required":True},
                {"name":"邮编","value":"515644","required":True},
                {"name":"服务中心电子邮箱","value":"02574@perfect99.com","required":True},
                {"name":"服务中心经营地址","value":"广东省潮州市潮安区彩塘镇骊塘三村龙华路41幢11号","required":True},
                {"name":"服务中心名称","value":"潮州市潮安区彩塘镇新能保健食品咨询服务部2","required":True}
            ]

