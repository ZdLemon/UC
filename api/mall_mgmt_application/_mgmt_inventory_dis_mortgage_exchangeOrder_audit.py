# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"id": "317", # 押货换货单id
	"exchangeType": 3, # 换货类型 1先退后换 2秒换 3只换不退 4先换后退
	"auditFileUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/202207061621062n2CL.jpg", # 审批附件
	"auditFileName": "202207061621062n2CL.jpg", # 审批附件名称
	"auditRemark": "3333333333", # 审核备注
	"auditResult": "1", # 审批意见 0不通过 1通过
	"disposalType": "1", # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
	"reasonFirst": "其他原因换货", # 一级原因
	"reasonFirstRemark": "11111111111111111111111", # 一级原因备注
	"reasonSecond": "其他原因换货", # 二级原因
	"reasonSecondRemark": "22222222222222222", # 二级原因备注
	"productList": [{
		"id": "358",
		"exchangeNum": 2, # 数量
		"dailyUseType": None, # 日常使用时间 1早上 2中午 3晚上
		"firstUseTime": "", # 第一次使用的时间
		"happenType": None, # 物品问题发生状态 1初次开封使用发现 2使用过程中发现
		"productBatch": "12345", # 批次号
		"problemDesc": "进水了", # 问题描述
		"productionDate": "20220101", # 物品生产日期
		"productSn": "", # 物品序列号/二维码
		"disposalType": 1, # 旧品处理方式 1服务中心报废 2分公司报废 3退货中转仓
		"productCode": "AG" # 商品编号
	}],
	"returnAddress": "广州仓" # 退回地址信息
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_audit(data, access_token=access_token):
    """
    审批
    /mgmt/inventory/dis/mortgage/exchangeOrder/audit
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/audit"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
