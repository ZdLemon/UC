# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"promotionType": 4, # 活动类型:1-活动,2-换购,4-预售
    "pageNum": 1,
    "pageSize": 15,
}

def _mgmt_prmt_selectPromotionListPage(params=params, access_token=access_token):
    """
    活动分页列表
    /mgmt/prmt/selectPromotionListPage
    """

    url = f"{BASE_URL}/mgmt/prmt/selectPromotionListPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
