# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: request.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site: 
# @Time: 12月 22, 2020
# -----------------------------------------------------
import requests


# params：字典或字节序列，作为参数增加到url中
# kv = {"k":"v"}
def request_get(cls, url, **kwargs):
    return requests.request("GET", url, **kwargs)


# data：字典、字节序列或文件对象，作为Request的对象
# kv = {"k":"v"}
# json：JSON格式的数据，作为Request的内容
# kv = {"k":"v"}
# files：字典类型，传输文件
# kv = {"file":open("1.txt","rb")}
def request_post(cls, url, **kwargs):
    if kwargs.get("isCookies") == True:
        kwargs["cookies"] = cls.cookies
    r = requests.request("POST", url, **kwargs)
    if kwargs.get("isCookies") == True:
        cookies = r.cookies
        cls.cookies = requests.utils.dict_from_cookiejar(cookies)
    return r
