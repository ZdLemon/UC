# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "storeCode" : "",  # str服务中心编号
    "name" : "",   # str服务中心名称
    "leaderCardNo": "", # str总店负责人卡号
    "address" : "",  # 地址关键字，模糊搜索
    "leaderName" : "",  # str负责人姓名
    "shopType" : None,  # int网点类型1、微店 2、微店(账务未清)3、微店(办理结店中)4、微店(结店)5、冻结资格6、办理结点中7、取消（账务未结清）8、新批未运作9、正式网点10、结店（保店二年1、结店12、结店（保店一年13、结店（保店三年）
    "shopkeeperName" : "",  # 分店管理员姓名
    "shopkeeperNo" : "",  # 分店管理员卡号
    "isMainShop" : None,  # int是否总店 0总店 1分店
    "level" : None,  # int星级
    "companyCode" : "",  # str所属分公司编号
    "isServiceShop" : None,  # int是否服务网店
    "isSignContract" : None,  # int是否签订合同
    "areaCode" : "",  # str区县code
    "cityCode" : "",  # str城市code
    "provinceCode" : "",  # str省份code
    "ratifyDate" : "",  # str批准最早时间
    "ratifyDate" : "",  #  str批准最晚时间
    "regionCode" : "",   #
    "ratifyEndTime" : "",  #
    "ratifyStartTime" : "",   #
    "pageNum": 1,  # int页码
    "pageSize": 20,  # int页数量
    "businessMode": None # 保证金类型，1/1:3，2/85%
}

def _mgmt_store_listStore(params=params, access_token=access_token):
    """
    获取服务中心列表
    /mgmt/store/listStore
    """

    url = f"{BASE_URL}/mgmt/store/listStore"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
