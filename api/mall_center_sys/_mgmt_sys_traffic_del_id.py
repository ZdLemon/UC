# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {"id": None}


def _mgmt_sys_traffic_del_id(params, access_token=access_token):
    """
    删除更新交通管制
    /mgmt/sys/traffic/del/{id}
    """

    url = f"{BASE_URL}/mgmt/sys/traffic/del/{params['id']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.delete(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
