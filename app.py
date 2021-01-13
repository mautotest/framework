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
from apps.apis.hello import Hello, Heart, Login
from flask_apscheduler import APScheduler
from config import db

"""URL配置"""
route_urls = {
    Hello: "/",
    Heart: "/heart",
    Login: "/login"
}


def add_resource(api):
    """注入URL"""
    for k, v in route_urls.items():
        api.add_resource(k, v)


def configure_scheduler(app):
    """Configure Scheduler"""
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()


def create_app():
    """创建app"""
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    api = Api(app)
    add_resource(api)
    configure_scheduler(app)
    db.init_app(app)
    return app
