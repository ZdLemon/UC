# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


data = {
    "bankNo":"622123654753", # 银行卡号
    "bankOpenName":"招行银行解放路支行", # 开户银行名称
    "bankOpenType":"06", # 开户银行类型
    "cardNo":"3000003428", # 会员卡号
    "province":"110000000000", # 地址省份
    "city":"110100000000", # 地址市
    "memberId":"1270780218333983582", # 用户id
    "realname":"证件啦啦啦", # 姓名
    "provideType":2, # 发放类型：1->直销员；2->客户经理
    "platform":5, # 代邦银行卡平台,1、商城运营后台平台,2、店铺运营平台,3、app服务中心平台,4、油葱极速版
    "status":2 # 银行卡状态 1->汇退；2->正常；3->无账号
}


def _mobile_member_addorUpdateMerberBank(data=data, access_token=access_token):
    """
    绑定劳务发放数据
    /mobile/member/addorUpdateMerberBank
    """

    url = f"{BASE_URL}/mobile/member/addorUpdateMerberBank"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
