# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar



def _mgmt_product_cfg_menu_brand(access_token=access_token):
    """
    菜单列表-产品品牌
    /mgmt/product/cfg/menu/brand
    """

    url = f"{BASE_URL}/mgmt/product/cfg/menu/brand"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
