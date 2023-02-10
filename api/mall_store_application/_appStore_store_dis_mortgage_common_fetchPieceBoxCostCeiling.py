# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


def _appStore_store_dis_mortgage_common_fetchPieceBoxCostCeiling(access_token=access_token):
    """
    获取启用中的拼箱费上限
    /appStore/store/dis/mortgage/common/fetchPieceBoxCostCeiling
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgage/common/fetchPieceBoxCostCeiling"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
