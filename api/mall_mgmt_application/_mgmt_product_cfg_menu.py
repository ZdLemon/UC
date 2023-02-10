# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "type" : "company",  # type:show-前端展示,catalog-产品类型,company-销售主体,brand-产品品牌,tag-产品标签
}

def _mgmt_product_cfg_menu(params=params, access_token=access_token):
    """
    菜单列表
    /mgmt/product/cfg/menu/{type}
    """

    url = f"{BASE_URL}/mgmt/product/cfg/menu/{params['type']}"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
