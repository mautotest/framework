# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: login_service.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 1月 14, 2021
# ---------------------------------------------
from apps.modles.login import User


def check_pwd(user, pwd):
    r = User.query.filter_by(name=user).first()
    if r is None:
        return False
    else:
        return r.password == pwd
