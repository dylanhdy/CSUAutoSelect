# coding=utf-8

import random
import re
import time
import requests
import base64

global username, password

LOGIN_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
MAIN_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/framework/xsMain.jsp'
REQUEST_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper'

session = requests.Session()

respond = session.get(LOGIN_URL)
# print(respond.text)

def login():
    username=raw_input('用户名:')
    password=raw_input('密码:')

    s1 = base64.b64encode(username)
    s2 = base64.b64encode(password)

    data = {'encoded': s1 + '%%%' + s2}

    respond = session.post(LOGIN_URL, data)
    #print(respond.text)
    respond = session.get(MAIN_URL)
    return respond
    
respond = login()

#print(respond.status_code)

while respond.status_code != requests.codes.ok:
    print('用户名或密码错误，请重试')
    respond = login()
else:
    print('成功登录教务系统')

num = int(raw_input('需要选的课程数量为:'))
list = []

for i in range(1, num+1):
    id = raw_input('第 %d 门课的课程ID:' %i)
    list.append(id)

respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxk/xklc_list')

#print(respond.text)

while True:
    key = re.findall('href="(.+)" target="blank">进入选课', respond.text)
    print(str(key))
    if len(key) == 1:
        break
    time.sleep(0.1)

#respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=45803CD452A342E6997F6B19E62CB96C')
respond = session.get('http://jwxt.sustc.edu.cn' + key[0])

print('成功进入选课页面')
#id = raw_input('课程ID:')
#id = '202020212017376' 台球

def work(id):
    respond = session.get(REQUEST_URL + '?jx0404id=' + id)
    #respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?jx0404id=202020211002751')
    #print(respond.text)
    while not re.search('true', respond.text):
        respond = session.get(REQUEST_URL + '?jx0404id=' + id)
        time.sleep(0.1)
        print('正在尝试')
    return True

for i in range(0, num):
    print('第 {} 门课选课开始，课程 ID: {}'.format(i, list[i]))
    if work(list[i]):
        print('成功抢到第 %d 门课')
