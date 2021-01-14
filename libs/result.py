# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: result.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site: 
# @Time: 12月 22, 2020
# -----------------------------------------------------
from libs.emuns import Codes


def bulid_success(**kwargs):
    return {
        "result": kwargs.get("result") or {},
        "code": Codes.SUCCESS.value,
        "desc": Codes.SUCCESS.name
    }


def bulid_fail(code=Codes.FAIL):
    return {
        "code": code.value,
        "desc": code.name
    }
