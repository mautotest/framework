# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: app.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site:
# @Time: 12月 21, 2020
# -----------------------------------------------------
from flask import Flask, request
from common.status import s
from common.result import Result
import logging
import os

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.info('Hello World!')
    return 'Hello World:' + s.status


@app.route('/heart', methods=["POST"])
def heart():
    app.logger.info('rev heart:{}'.format(request.get_json()))
    return Result().bulid_success()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='## %Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    server_port = os.environ.get("MTEST_SERVER_PORT", 5021)
    app.run(port=server_port)
