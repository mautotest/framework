# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: emuns.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 1月 12, 2021
# ---------------------------------------------
from enum import Enum


class Codes(Enum):
   SUCCESS = 0
   FAIL = 1
   NOT_LOGIN = 101
   USER_PAW_ERROR = 102