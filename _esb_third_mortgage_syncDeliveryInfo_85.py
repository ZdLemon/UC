# coding:utf-8

from util.login_rsakey import login_rsakey
from util.msg import data_msg
from util.logger import logger
from setting import CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY

import requests
import time

BASE_URL = "https://uc-test.perfect99.com/api"


def _login(username=USERNAME, password=PASSWORD, channel=CHANNEL01):
    """登录接口

    Args:
        username (_type_, optional): _description_. Defaults to username.
        password (_type_, optional): _description_. Defaults to password.
        channel (_type_, optional): _description_. Defaults to CHANNEL01.
        authorization

    Returns:
        _type_: _description_
    """  
    url = f"{BASE_URL}/login"
    headers = {"Authorization": Authorization}
    data = login_rsakey(username, password, channel)

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:  
        logger.debug(data_msg(r, data))       
        return r


data = {
	# "deliveryCode": f"shunfeng85{int(round(time.time() * 1000))}", # 发货单号，不能重复
 	"deliveryCode": f"test12078501", # 发货单号，不能重复
	"mortgageItemReqDtoList": [
		{
			"itemCode": "AG2", # 商品编号
			"num": 2, # 数量
			"skuCode": ""
		},
		# {
		# 	"itemCode": "FA", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "AG2", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "DMP", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "DST", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "FIS", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "LSP", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "NB", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "PSG", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
		# {
		# 	"itemCode": "PSN", # 商品编号
		# 	"num": 1, # 数量
		# 	"skuCode": ""
		# },
	],
	"mortgageOrderNo": "YH8590220822120001", # 押货单号
	"optime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
	"status": 2,
	"type": 5 # 1:3是2,85折是5
}
access_token = _login().json()["data"]["access_token"]


def _esb_third_mortgage_syncDeliveryInfo(data=data, access_token=access_token):
    """
    同步仓库中心的发货信息
    /esb/third/mortgage/syncDeliveryInfo
    """

    url = f"{BASE_URL}/esb/third/mortgage/syncDeliveryInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


_esb_third_mortgage_syncDeliveryInfo() 