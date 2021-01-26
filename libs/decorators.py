# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: decorators.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 1月 12, 2021
# ---------------------------------------------
from flask import request, current_app
from functools import wraps
from .result import bulid_fail
from libs.emuns import Codes
from itsdangerous import base64_decode
import zlib


def login_wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # 校验session
        try:
            compressed = False
            s = request.cookies.get("session")
            if s.startswith('.'):
                compressed = True
                s = s[1:]
            d = s.split(".")[0]
            d = base64_decode(d)
            if compressed:
                d = zlib.decompress(d)
            cookies_d = eval(str(d,"utf-8"))
            if cookies_d.get("username"):
                return func(*args, **kwargs)
            else:
                return bulid_fail(code=Codes.NOT_LOGIN)
        except Exception as e:
            current_app.logger.error("something error: {}".format(e))
            return bulid_fail()

    return inner
