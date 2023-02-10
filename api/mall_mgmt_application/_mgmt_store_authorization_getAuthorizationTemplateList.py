# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "templateNo": None, # 授权书模板编号
    "templateName": None, # 授权书模板名称
    "status": None, # 状态，0：已失效，1：生效中
    "pageNum": 1,
    "pageSize": 10,
    "addStartTime": None, # 添加开始时间
    "addEndTime": None, # 添加结束时间
}


def _mgmt_store_authorization_getAuthorizationTemplateList(params=params, access_token=access_token):
    """
    获取授权书模板列表
    /mgmt/store/authorization/getAuthorizationTemplateList
    """

    url = f"{BASE_URL}/mgmt/store/authorization/getAuthorizationTemplateList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
