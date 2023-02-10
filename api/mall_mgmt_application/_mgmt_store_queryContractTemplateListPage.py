# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "pageNum": 0,
    "pageSize": 0,
    "templateStatus": 2, # 模板状态，1：停用；2：启用
    "contractType": 2, # 合同类型，1/经营合同，2/协议
    "isOnline": 1, # 是否是线上模板，1/线上，2、线下
    "customerType": 1, # 客户类型，1/服务中心(默认)，2/服务公司
}

def _mgmt_store_queryContractTemplateListPage(params=params, access_token=access_token):
    """
    分页查询合同模板列表
    /mgmt/store/queryContractTemplateListPage
    """

    url = f"{BASE_URL}/mgmt/store/queryContractTemplateListPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
