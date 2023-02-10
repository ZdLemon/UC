# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "signType": 2, # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
    "storeCode": None, # 服务中心编号
    "companyCode": None, # 分公司编号
    "companySignPerson": None, # 公司签署人
    "isSignOffline": None, # 是否线下签署
    "signStatus": None, # 签署状态，1/待提交，2/待店铺签署，3/待公司签署，4/签署完成，5/超时中止签署，6/拒签，7/已撤回，8/已作废，9/生成失败
    "pageNum": 1,
    "pageSize": 10,
    "minBillMonth": None, # 对账单月份最小值，格式: yyyymm
    "maxBillMonth": None, # 对账单月份最大值，格式: yyyymm
    "minSignStartDate": None, # 发起签署日期最小值，格式yyyy-MM-dd
    "maxSignStartDate": None, # 发起签署日期最大值，格式yyyy-MM-dd
    "minSignEndDate": None, # 店铺签署截止日期最小值，格式yyyy-MM-dd
    "maxSignEndDate": None, # 店铺签署截止日期最大值，格式yyyy-MM-dd
    "minStoreSignDate": None, # 店铺签署时间最小值，格式yyyy-MM-dd
    "maxStoreSignDate": None, # 店铺签署时间最大值，格式yyyy-MM-dd
} 

def _mgmt_store_contract_getStoreContractInvtBillList(params=params, access_token=access_token):
    """
    查询库存对账单合同列表
    /mgmt/store/contract/getStoreContractInvtBillList
    """

    url = f"{BASE_URL}/mgmt/store/contract/getStoreContractInvtBillList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
