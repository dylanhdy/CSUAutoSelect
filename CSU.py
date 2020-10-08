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
    #username=raw_input('用户名:')
    #password=raw_input('密码:')
    username='8208200412'
    password='36010220021019121X'

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
    print('成功登录')

respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_WDXK')

respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=45803CD452A342E6997F6B19E62CB96C')

id = '202020211002751'

def work(id):
    respond = session.get(REQUEST_URL + '?jx0404id=' + id)
    #respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?jx0404id=202020211002751')
    #print(respond.text)
    while not re.search('true', respond.text):
        respond = session.get(REQUEST_URL + '?jx0404id=' + id)
        time.sleep(0.1)
        print('正在尝试')
    else:
        print('选课成功')
    return True

work(id)




