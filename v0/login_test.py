#!/usr/bin/env python
#_*_coding:utf-8_*_

import json
from selenium import webdriver
import conf

from selenium.webdriver.common.proxy import Proxy, ProxyType

def login_test():
    """
    测试登录
    """
    try:
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = "10.211.55.4:808"
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')
        chrome_options.add_argument('--window-size=1024,768')
        driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options, service_args=["--verbose", "--log-path=driver.log"], desired_capabilities=capabilities)
        driver.get(conf.url)
        name=driver.find_element_by_xpath('//*[@id="username"]')
        name.send_keys(conf.username)
        password=driver.find_element_by_xpath('//*[@id="pwd"]')
        password.send_keys(conf.password)
        login=driver.find_element_by_xpath('//*[@id="loginform"]/button')
        login.click()
        #driver.get_screenshot_as_file("./tmp.png")
        if not isinstance(driver.get_cookies(), list):
            conf.logger.error("cookie is not list")
            exit(-1)
        has_right_sid = False
        for item in driver.get_cookies():
            if isinstance(item, dict) and item.has_key('name') and item['name'] == 'JSESSIONID' and item.has_key("value") and len(item['value']) == 32:
                has_right_sid = True
        if not has_right_sid:
            conf.logger.error("jsessionid is wrong: {}".format(json.dumps(driver.get_cookies())))
            exit(-1)
        conf.logger.info("LOGIN TEST PASS")
        return driver
    except Exception as e:
        conf.logger.exception(e)
        exit(-1)


