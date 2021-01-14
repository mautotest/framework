# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: jobs.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 1月 15, 2021
# ---------------------------------------------
from flask_restful import Resource
from libs.decorators import login_wrapper
from flask import current_app, request
from libs.result import bulid_success,bulid_fail
from .uris import JOB_LIST, JOB_ADD, JOB_REMOVE, JOB_RESUME, JOB_PAUSE


class Jobs(Resource):
    """jobs 相关的接口"""

    @login_wrapper
    def get(self):
        current_app.logger.info('requst path: {}'.format(request.path))
        if JOB_LIST == request.path:
            return bulid_success()
        else:
            return bulid_fail()


    @login_wrapper
    def post(self):
        current_app.logger.info('requst path: {}'.format(request.path))
        if JOB_ADD == request.path:
            r = "add"
        if JOB_PAUSE == request.path:
            r = "pause"
        if JOB_RESUME == request.path:
            r = "resume"
        if JOB_REMOVE == request.path:
            r = "remove"
        return r or bulid_fail()
