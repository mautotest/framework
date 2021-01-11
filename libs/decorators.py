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
from flask import session, request
from functools import wraps
from .result import bulid_fail
from libs.emuns import Codes
from config import SECRET_KEY
import base64


def login_wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # 校验session
        try:
            s = request.headers.get("Session")
            user = base64.b64decode(s.replace(SECRET_KEY, "")).decode()
            if s == session.get(user):
                return func(*args, **kwargs)
        except Exception:
            pass
        return bulid_fail(code=Codes.NOT_LOGIN)

    return inner
