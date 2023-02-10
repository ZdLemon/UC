# coding:utf-8

from setting import BASE_URL
from functools import wraps
import time


def stepreruns(counts=3, times=10):
    """
    step断言失败后重复执行counts次, 每次休息times秒
    """
    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 1
            status = True
            while status and count < counts:
                try:
                    time.sleep(times + count)
                    func(*args, **kwargs)
                except:
                    status = True
                    count += 1
                else:
                    status = False
            if status:
                func(*args, **kwargs)
        return wrapper
    return decorate