# coding=utf-8

import re
import time
import base64
from selenium import webdriver

LOGIN_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
MAIN_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/framework/xsMain.jsp'
REQUEST_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper'

driver = webdriver.Chrome()

driver.get(LOGIN_URL)
time.sleep(2)
driver.quit()