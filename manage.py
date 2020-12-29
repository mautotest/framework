# -*- coding: utf-8 -*-
# ---------------------------------------------
# @Software: PyCharm
# @File: manage.py
# @Author: majiayang
# @Institution: nanma, China
# @E-mail: 609921831.com
# @Site: 
# @Time: 12月 29, 2020
# ---------------------------------------------
from app import create_app
from config import SERVER_PORT

def main():
    app = create_app()
    app.run(port=SERVER_PORT)

if __name__ == '__main__':
    main()
