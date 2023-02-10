# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "id": "595",
    "remarks": "资格审核通过了资格审核通过了资格审核通过了",
    "worksStatus": 5 # 审核状态 2:人工审核不通过 3:(人工审核通过)待资格审核; 4:资格审核不通过 5:(资格审核通过)待初审;6:初审不通过 7:(初审通过)待复审;8:复审不通过 9:审核通过
}


def _mgmt_cms_community_communityWorksAudit(data=data, access_token=access_token):
    """
    生活社区-作品审核
    /mgmt/cms/community/communityWorksAudit
    """

    url = f"{BASE_URL}/mgmt/cms/community/communityWorksAudit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
