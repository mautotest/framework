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
from libs.result import bulid_success, bulid_fail
from libs.scheduler import APScheduler
from libs.emuns import Codes
from .uris import JOB_LIST, JOB_ADD, JOB_REMOVE, JOB_RESUME, JOB_PAUSE


def hello(a, b):
    print("hello 12345,{} {}".format(a, b))


class Jobs(Resource):
    """jobs 相关的接口"""

    def __init__(self):
        self.apsc = APScheduler()

    @login_wrapper
    def get(self):
        current_app.logger.info('requst path: {}'.format(request.path))
        if JOB_LIST == request.path:
            jobs = self.apsc.get_jobs()
            result = []
            for job in jobs:
                result.append({
                    "job_id": job.id,
                    "name": job.name,
                    "func": job.func_ref,
                    "args": job.args,
                    "kwargs": job.kwargs,
                    # "trigger": job.trigger
                })
            return bulid_success(result=result)
        else:
            return bulid_fail()

    @login_wrapper
    def post(self):
        current_app.logger.info('requst path: {}'.format(request.path))
        if JOB_ADD == request.path:
            job = {
                'func': 'apps.apis.jobs:hello',
                'args': (1, 2),
                'trigger': 'interval',
                'seconds': 10
            }
            j = self.apsc.add_job(job)
            if True:
                self.apsc.pause_job(j.id)
            return bulid_success(result={"job_id": j.id})
        job_id = request.form.get("job_id")
        if JOB_PAUSE == request.path:
            self.job_check(job_id)
            self.apsc.pause_job(job_id)
        if JOB_RESUME == request.path:
            self.job_check(job_id)
            self.apsc.resume_job(job_id)
        if JOB_REMOVE == request.path:
            self.job_check(job_id)
            self.apsc.remove_job(job_id)
        current_app.logger.info('job_id:{}, done!'.format(job_id))
        return bulid_success()

    def job_check(self, job_id):
        if not job_id:
            return bulid_fail(Codes.JOB_ID_CAN_NOT_NULL)
        if not self.apsc.get_job(job_id):
            return bulid_fail(Codes.JOB_ID_NOT_FOUND)
