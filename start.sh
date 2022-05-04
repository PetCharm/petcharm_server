#!/bin/bash

#1.生成数据库迁移文件
#python3 manage.py makemigrations
#2.根据数据库迁移文件来修改数据库
#python3 manage.py migrate
#3.用uwsgi启动django服务，不再使用python3 manage.py runserver
uwsgi --http :8000 --chdir /var/www/petcharm/petcharm_server/ --wsgi-file /var/www/petcharm/petcharm_server/back/wsgi.py
