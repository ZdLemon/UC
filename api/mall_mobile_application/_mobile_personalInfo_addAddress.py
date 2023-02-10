# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


data = {
    "contactName":"小程", # 联系人姓名
    "mobile":"18928790109", # 手机号码
    "provinceCode":"110000000000", # 省份编码
    "province":"北京市", # 省份
    "cityCode":"110100000000", # 城市编码
    "city":"北京市", # 城市
    "districtCode":"110101000000", # 区编码
    "district":"东城区", # 区
    "streetCode":"110101001000", # 街道编码
    "street":"东华门街道办事处1", # 街道
    "address":"解放路1号", # 详细地址
    "isDefault":1 # 是否默认地址：0->不是；1->是
}


def _mobile_personalInfo_addAddress(data=data, access_token=access_token):
    """
    新建会员配送地址接口
    /mobile/personalInfo/addAddress
    """

    url = f"{BASE_URL}/mobile/personalInfo/addAddress"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r