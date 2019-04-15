#!/usr/bin/env python
#_*_coding:utf-8_*_

import logging
import logging.handlers
from cloghandler import ConcurrentRotatingFileHandler

# logger config
logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
file_handler = ConcurrentRotatingFileHandler('test.log', "a", 512*1024*1024, 10, encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(filename)s: ' + \
        '%(funcName)s - %(lineno)s - %(levelname)s - %(thread)s - %(message)s'))
logger.addHandler(file_handler)

# login test config
#url = "http://122.229.31.227:340"
url = 'http://10.44.206.125:81/'
username = 'root'
password = '123456'

# DB config
dbhost = ''
dbport = 3306
dbuser = ''
dbpassword = ''
dbname = ''

if __name__ == "__main__":
    pass
