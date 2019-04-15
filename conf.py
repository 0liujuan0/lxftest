#!/usr/bin/env python
#_*_coding:utf-8_*_

import logging
import logging.handlers
from cloghandler import ConcurrentRotatingFileHandler
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# logger config
logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
file_handler = ConcurrentRotatingFileHandler('test.log', "a", 512*1024*1024, 10, encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(filename)s: ' + \
        '%(funcName)s - %(lineno)s - %(levelname)s - %(thread)s - %(message)s'))
logger.addHandler(file_handler)

# login test config
login_url = 'http://10.44.206.125:81/'
username = 'root'
password = '123456'

def get_driver(proxy=False):
    if proxy:
        #set up proxy
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = "10.211.55.4:808"
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)
    else:
        capabilities = webdriver.DesiredCapabilities.CHROME
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')
    chrome_options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options, desired_capabilities=capabilities)
    return driver


if __name__ == "__main__":
    pass
