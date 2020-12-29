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
class Result(object):

    def __init__(self, result={}, code=0, desc="success"):
        self.result = result
        self.code = code
        self.desc = desc

    def bulid_success(self):
        return {
            "result": self.result,
            "code": self.code,
            "desc": self.desc
        }

    def bulid_fail(self):
        return {
            "result": self.result,
            "code": 1,
            "desc": "fail"
        }
