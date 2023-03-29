# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
@Time : 2022/8/24 20:21
@Author : 张继成
@Site : laozhang
@File : 111.py
@Software: PyCharm
============================
"""

import selenium.webdriver
#driver=selenium.webdriver.Chrome('/Users/zhangjicheng/PycharmProjects/demo/webdriver/chromedriver')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def dirver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    print(driver.title)
    driver.close()



if __name__ == '__main__':
    dirver()
