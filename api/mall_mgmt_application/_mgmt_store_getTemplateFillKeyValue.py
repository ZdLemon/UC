# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "storeCode": "902063", # 服务中心编号
    "templateNo": "MB164491049756884", # 模板编号
}

def _mgmt_store_getTemplateFillKeyValue(params=params, access_token=access_token):
    """
    根据服务中心及模板编号获取填充字段-对应值
    /mgmt/store/getTemplateFillKeyValue
    """

    url = f"{BASE_URL}/mgmt/store/getTemplateFillKeyValue"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
