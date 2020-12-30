# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: scheduler.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site: 
# @Time: 12月 21, 2020
# -----------------------------------------------------
from flask import current_app
import random
import string


class APScheduler(object):
    """调度器控制方法"""

    def add_job(self, job={}):

        """
        添加任务
        :param args:  元祖 -> （1，2）
        :param jobstore:  存储位置
        :param trigger:
                        data ->  run_date   datetime表达式
                        cron ->  second/minute/day_of_week
                        interval ->  seconds 延迟时间
                        next_run_time ->  datetime.datetime.now() + datetime.timedelta(seconds=12))
        :return:
        """
        job_def = dict(job)
        if "id" in job_def:
            self.remove_job(job_def["id"])  # 删除原job
        else:
            job_def["id"] = "".join(random.sample(string.ascii_letters + string.digits, 20))
        return current_app.apscheduler.scheduler.add_job(**job_def)

    def remove_job(self, jobid, jobstore=None):
        """删除任务"""
        return current_app.apscheduler.remove_job(jobid, jobstore=jobstore)

    def resume_job(self, jobid, jobstore=None):
        """恢复任务"""
        return current_app.apscheduler.resume_job(jobid, jobstore=jobstore)

    def pause_job(self, jobid, jobstore=None):
        """暂停任务"""
        return current_app.apscheduler.pause_job(jobid, jobstore=jobstore)
