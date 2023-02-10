# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests


params = {
    "customerType": 1, # 客户类型，1/服务中心，2/服务公司
    "storeCode": None, # 服务中心编号
    "companyName": None, # 企业认证名称
    "adminName": None, # 企业管理员名称
    "adminMobile": None, # 企业管理员手机号
    "creditNo": None, # 认证中统一社会信用代码
    "fddCreditNo": None, # 法大大统一社会信用代码
    "pageNum": 1,
    "pageSize": 10,
    "certStartTime": None, # 通过认证开始时间
    "certEndTime": None # 通过认证开始时间
}


def _mgmt_store_getCompanyCertList(params=params, access_token=access_token):
    """
    获取电子印章认证列表
    /mgmt/store/getCompanyCertList
    """

    url = f"{BASE_URL}/mgmt/store/getCompanyCertList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r

