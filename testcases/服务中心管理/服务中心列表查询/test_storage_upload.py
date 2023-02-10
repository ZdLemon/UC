# coding:utf-8

from api.basic_services._storage_upload import files, _storage_upload
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("basic_services")
class TestClass:
    """
    上传文件接口
    /storage/upload
    """
    def setup_class(self):
        self.files = deepcopy(files)
        self.access_token = os.environ["access_token"]

    @allure.story("/storage/upload")
    @allure.severity(P2)
    @allure.title("上传文件-成功路径: 上传png图片检查")
    def test_storage_upload(self):
        
        files = deepcopy(self.files)                   
        with _storage_upload(files, self.access_token) as r:            
                assert r.status_code == 200
                assert r.json()["datas"]["msg"] == "文件上传成功"

