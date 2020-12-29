# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: apis.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 12月 29, 2020
# ---------------------------------------------
from flask_restful import Resource
from libs.status import s
from libs.result import Result
from flask import current_app,request

class Hello(Resource):
    def get(self):
        current_app.logger.info('Hello World!')
        return Result({"hello status:":s.status}).bulid_success()

class Heart(Resource):
    def post(self):
        current_app.logger.info('rev heart:{}'.format(request.get_json()))
        return Result().bulid_success()