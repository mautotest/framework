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
from flask import Flask
from flask_restful import Api
from apps.apis.hello import Hello, Heart

route_urls = {
    Hello: "/",
    Heart: "/heart"
}

def add_resource(api):
    for k, v in route_urls.items():
        api.add_resource(k, v)

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    api = Api(app)
    add_resource(api)
    return app