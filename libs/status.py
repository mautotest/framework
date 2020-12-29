# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: status.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site:
# @Time: 12月 21, 2020
# -----------------------------------------------------
class Status(object):

    def __init__(self):
        self.status = StatusType.ONELINE
        self.status_list = []


class StatusType:
    ONELINE = "online"
    OFFLINE = "offline"
    PENDING = "pending"


s = Status()
