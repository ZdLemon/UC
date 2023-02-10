# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

from requests_toolbelt import MultipartEncoder
import requests


files = {
    "storageType": "PublicCloud", # str存储类型（目前支持的类型:PrivateCloud 私有云，PublicCloud:公有云）
    "clientKey": "mall-center-store", # str客户端Key(由管理员进行分配)
    "file": "data/身份证正面.png"
}


def _storage_upload(files=files, access_token=access_token):
    """
    /storage/upload
    上传文件接口
    """
    

    url = f"{BASE_URL}/storage/upload"
   
    with open(files["file"], "rb") as f:
        index = files["file"].find(".")
        m = MultipartEncoder(
            fields={
                "storageType": files["storageType"],
                "clientKey": files["clientKey"],
                "file": (files["file"][5:index], f, 'text/plain')}
        )
        
        headers = {"Authorization": f"bearer {access_token}", 'Content-Type': m.content_type}

        with requests.post(url=url, headers=headers, data=m, timeout=TIMEOUT, verify=VERIFY) as r:
            logger.debug(data_msg(r, files))     
            return r
