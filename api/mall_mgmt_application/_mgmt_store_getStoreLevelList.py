# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests


params = {
    "storeCode": None,
    "level": None, # 网点等级 1服务中心 2五星服务中心 3五星旗舰服务中心 4无实体店，多个用逗号分隔
    "leaderNo": None, # 负责人卡号
    "provinceCode": None, # 省份编码
    "year": None, # 年份
    "cancelType": None, # 取消类型: 1、结点取消，2、转让取消，3、违规取消，4、不达标取消，5、冻结取消，6、转云取消
    "isCancel": None, # 是否取消: 1、是，0、否
    "pageNum": 1,
    "pageSize": 20
}


def _mgmt_store_getStoreLevelList(params=params, access_token=access_token):
    """
    查询网点等级列表
    /mgmt/store/getStoreLevelList
    """

    url = f"{BASE_URL}/mgmt/store/getStoreLevelList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
