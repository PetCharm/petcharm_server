#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64

# 接口地址
# 情感分析 https://ltpapi.xfyun.cn/v2/sa
# 关键词提取 http://ltpapi.xfyun.cn/v1/ke
# url ="https://ltpapi.xfyun.cn/v2/sa"
# 开放平台应用ID
x_appid = "2f64dd66"
# 开放平台应用接口秘钥
api_key = "3c2b387672dd5f7568edf0ec804f9180"


# 语言文本
# TEXT="soto重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。天生丽质难自弃，一朝选在君王侧。"

def ner(TEXT):
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request("http://ltpapi.xfyun.cn/v1/ke", body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    if json.loads(result.decode('utf-8'))['code'] != 0:
        return ''
    # print(result.decode('utf-8'))
    keywords = ''
    for i in json.loads(result.decode('utf-8'))['data']['ke']:
        keywords += i['word'] + '|'
    return keywords[:-1]


def senti(TEXT):
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request("https://ltpapi.xfyun.cn/v2/sa", body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    # print(result.decode('utf-8'))
    if json.loads(result.decode('utf-8'))['code'] != 0:
        return '0'
    return json.loads(result.decode('utf-8'))['data']['score']

# if __name__ == '__main__':
#     print(senti("soto重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。天生丽质难自弃，一朝选在君王侧。"))
#     print(ner("soto重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。天生丽质难自弃，一朝选在君王侧。"))
