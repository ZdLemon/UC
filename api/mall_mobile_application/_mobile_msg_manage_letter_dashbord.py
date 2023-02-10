# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "systemId": 1, 
    "usrId": 1270780218333982428, # 用户id
}

def _mobile_msg_manage_letter_dashbord(params=params, access_token=access_token):
    """
    用户站内信列表,按消息类型分类
    /mobile/msg/manage/letter/dashbord/{usrId}/{systemId}
    """

    url = f"{BASE_URL}/mobile/msg/manage/letter/dashbord/{params['usrId']}/{params['systemId']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
