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


def bulid_fail(code=None):
    return {
        "code": code.value or Codes.FAIL.value,
        "desc": code.name or Codes.FAIL.name
    }
