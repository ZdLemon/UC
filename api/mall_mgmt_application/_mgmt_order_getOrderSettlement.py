# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


params = {
	"orderMonth": time.strftime("%Y%m",time.localtime(time.time())), # 业绩月份202204
	"storeCode": "", # 服务中心编号
	"cardNo": "", # 负责人卡号
	"realName": "", # 负责人
	"companyCode": "", # 分公司编号
	"isDifference": None, # 本期交付差额是否为负 0->否 1->
	"isDifCheck": None, # 差额校验是否为零 0->否 1->是
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_order_getOrderSettlement(params=params, access_token=access_token):
    """
    交付结算列表
    /mgmt/order/getOrderSettlement
    """

    url = f"{BASE_URL}/mgmt/order/getOrderSettlement"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
