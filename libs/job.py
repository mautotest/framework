# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: libs.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site:
# @Time: 12月 21, 2020
# -----------------------------------------------------
from common.status import s
from common.job_tool import jobs
from common.request_tool import RequestTool
import os

# 工作任务
# 传入文件名执行
def push_work_job(**kwargs):
    current_app = get_current_app()
    test_queue = kwargs.get("test_queue")
    if test_queue.empty():
        current_app.logger.info("nothing to run!")
        return
    test_queue.get()
    server_ip = os.environ.get("MTEST_SERVER_IP", "127.0.0.1")
    server_port = os.environ.get("MTEST_SERVER_PORT", 5021)
    url = "http://{}:{}/heart".format(server_ip, server_port)
    current_app.logger.debug('send heart:{},status:{}'.format(url, s.status))
    RequestTool.request_post(url, json={"status": s.status})


def start_push(date, test_queue):
    return jobs.add_date_job(push_work_job, data=date, test_queue=test_queue)
