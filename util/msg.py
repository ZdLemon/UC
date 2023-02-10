# coding:utf-8

from setting import BASE_URL
import json


def params_msg(r, params=None):    
    # log request
    msg = f"\n====== request details ======\n"
    
    if params:
        request_msg = {"url": r.request.url, "method": r.request.method, "headers": dict(r.request.headers), "params": params}
    else:
        request_msg = {"url": r.request.url, "method": r.request.method, "headers": dict(r.request.headers)}
    
    msg += json.dumps(request_msg, indent=4, separators=(",", ":"), ensure_ascii=False)

    # log response
    msg += f"\n====== response details ======\n"
    
    try:
        response_msg = {"status_code": r.status_code, "headers": dict(r.headers), "body": dict(r.json())}
    except:
        response_msg = {"status_code": r.status_code, "headers": dict(r.headers), "body": r.text}
        
    msg += json.dumps(response_msg, indent=4, separators=(",", ":"), ensure_ascii=False)    
    msg += "\n"

    return msg


def data_msg(r, data=None):
    # log request
    msg = f"\n====== request details ======\n"
    if data:
        request_msg = {"url": r.request.url, "method": r.request.method, "headers": dict(r.request.headers), "data": data}
    else:
        request_msg = {"url": r.request.url, "method": r.request.method, "headers": dict(r.request.headers)}
    
    msg += json.dumps(request_msg, indent=4, separators=(",", ":"), ensure_ascii=False)

    # log response
    msg += f"\n====== response details ======\n"

    try:
        response_msg = {"status_code": r.status_code, "headers": dict(r.headers), "body": dict(r.json())}
    except:
        response_msg = {"status_code": r.status_code, "headers": dict(r.headers), "body": r.text}
    
    msg += json.dumps(response_msg, indent=4, separators=(",", ":"), ensure_ascii=False)
    msg += "\n"

    return msg