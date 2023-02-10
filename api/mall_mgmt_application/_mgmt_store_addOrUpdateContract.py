# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "contractType":2,
    "storeCode":"902063",
    "storeName":"潮州市潮安区彩塘镇新能保健食品咨询服务部2",
    "leaderId":"835606037",
    "leaderName":"吕丽琼",
    "leaderNo":"35606037",
    "spouseName":"陈泽民",
    "managerName":"吕丽琼",
    "managerCardNo":"445122197908242221",
    "socialCreditCode":"92445103MA54BR8980",
    "phone":"07686681289",
    "mobile":"15913029179",
    "certificatesNo":"445122197908242221",
    "email":"02574@perfect99.com",
    "address":"广东省潮州市潮安区彩塘镇骊塘三村龙华路41幢11号",
    "legalPerson":"吕丽琼",
    "legalInfo":"445122197908242221",
    "wechat":None,
    "fax":"",
    "postCode":"515644",
    "contactAddress":"",
    "customerType":1,
    "provinceName":"广东省",
    "cityName":"潮州市",
    "areaName":"潮安区",
    "contractStartDate":1646064000000,
    "customerId":"9746b0a8ee024f01902098fdc79f1821",
    "registerStatus":"已注册",
    "templateNo":"MB164491049756884",
    "signType":2,
    "expireMonth":1,
    "complete":True,
    "fieldMatch":"True",
    "year":"2022",
    "remark":"111",
    "id":None
}


def _mgmt_store_addOrUpdateContract(data, access_token=access_token):
    """
    添加合同/修改合同
    /mgmt/store/addOrUpdateContract
    """

    url = f"{BASE_URL}/mgmt/store/addOrUpdateContract"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
