# -*- coding: utf-8 -*-

# gunicorn gengleiming.wsgi:application --blind 0.0.0.0:33000

# 设置进程名，方便在supervisor里管理
proc_name = 'gengleiming'
# sync/gevent
worker_class = 'gevent'
bind = ['0.0.0.0:33000']
workers = 1
# timeout = 1800
# for debug
# accesslog = '-'
# loglevel = 'debug'
# debug=True
