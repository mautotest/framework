# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: login.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 1月 14, 2021
# ---------------------------------------------
from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
