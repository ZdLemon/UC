
from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, CHANNEL01, Authorization, USERNAME, PASSWORD, TIMEOUT, VERIFY, URL

import requests
import time
from urllib.parse import urlencode



data = {
    "id": 109,
    "executorParam": {
        "startDate": f'{time.strftime("%Y-%m-%d",time.localtime(time.time()))} 00:00:00', # "2022-04-07 00:00:00"
        "endDate": f'{time.strftime("%Y-%m-%d",time.localtime(time.time()))} 23:59:59', # "2022-04-08 23:59:59"
    },
    "addressList": ""
}


def _jobinfo_trigger(data=data, cookie=""):
    """定时调度任务秒返券生效
    """  
    url = f"{URL}/jobinfo/trigger"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "cookie": cookie}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:  
        logger.debug(data_msg(r, data))       
        return r


