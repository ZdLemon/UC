# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _appStore_store_dis_mortgage_common_fetchProductShowList(access_token=access_token):
    """
    获取商品前端分类列表
    /appStore/store/dis/mortgage/common/fetchProductShowList
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgage/common/fetchProductShowList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
