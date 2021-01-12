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

def login():
    username=raw_input("用户名:")
    password=raw_input("密码:")

    s1 = base64.b64encode(username)
    s2 = base64.b64encode(password)

    data = {'encoded': s1 + '%%%' + s2}

    respond = session.post(LOGIN_URL, data)
    respond = session.get(MAIN_URL)
    return respond
    
respond = login()

while respond.status_code != requests.codes.ok:
    print('用户名或密码错误，请重试')
    respond = login()
else:
    print('成功登录教务系统')

num = int(input('需要选的课程数量为:'))

list = []

for i in range(1, num+1):
    id = raw_input('第 %d 门课的课程 ID:' %i)
    list.append('202020212'+id)

respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxk/xklc_list')

#print(respond.content)

while True:
    key = re.findall('href="(.+?)" target="blank">进入选课', respond.content)
    #print(key)
    if len(key) >= 1:
        break
    time.sleep(0.5)

respond = session.get('http://csujwc.its.csu.edu.cn' + key[0])

print('成功进入选课页面')

def work(id):
    respond = session.get(REQUEST_URL + '?jx0404id=' + id)
    print('正在尝试')
    #print(respond.content)
    if re.search('true', respond.content):
        return True
    if re.search('null', respond.content):
        print("没有该 ID 所对应的课程")
    else:
        print re.search('"选课失败：(.+)"', respond.content).group(1)
    return False

for i in range(0, num):
    print('第 {} 门课选课开始，课程 ID: {}'.format(i, list[i]))
    while not work(list[i]):
        time.sleep(0.5)
    else:
        print("成功抢到第 %d 门课")

raw_input('输入回车以结束程序')