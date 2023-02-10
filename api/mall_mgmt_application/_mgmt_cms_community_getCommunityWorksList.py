# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "pageNum": 1,
    "pageSize": 10,
    "worksSerial": None,
    "categoryId": None, # 品类id
    "materialType": None,
    "title": None,
    "worksStatus": None, # 审核状态 -1：审核中 0:系统审核不通过;1:待人工审核；2:人工审核不通过;3:待资格审核;4:资格审核不通过;5:待初审;6:初审不通过;7:待复审;8:复审不通过;9:审核通过
    "userName": None,
    "cardNo": None,
    "awards": None, # 是否获奖 -1:入围作品；0：人气作品; 1:获奖作品
    "startTime": "",
    "endTime": ""
}


def _mgmt_cms_community_getCommunityWorksList(data=data, access_token=access_token):
    """
    生活社区—查询素材作品列表
    /mgmt/cms/community/getCommunityWorksList
    """

    url = f"{BASE_URL}/mgmt/cms/community/getCommunityWorksList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
