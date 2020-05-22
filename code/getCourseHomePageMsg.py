# @Time    : 2020/5/9 2:22 下午
# @Author  : Aaron
# @Email   : 1392517138@qq.com
# @Desc    : None
#coding:utf-8
import pymysql
import json
import requests

"""
获取teacher表、老师课程关系表
"""
conn = pymysql.connect(host='127.0.0.1', port=3306, db='mooc',
                       user='root', password='13452078118')
cusor = conn.cursor()
url = "http://cc.cqupt.edu.cn/getAllJctsk"
data = {
    "unifyCode": 1,
    "zyh": 1,
    "count": 100,
    "page": 1
}
headers = {
    "cookie": "JSESSIONID=8843793488DCD16629CCB6B9FF4988C9"
}
# 先拿到所有课程号,放入kcbn
sql = 'select kcbh from moren_kc'
kcbh = []
cusor.execute(sql)
tmp = cusor.fetchall()
for item in tmp:
    kcbh.append(item[0])
conn.commit()
data = {
    "unifyCode": 1,
    "kcbh": "A1040040"
}
url = 'http://cc.cqupt.edu.cn/getTeachingTeamPageMsg'
sql1 = 'insert into teacher (xm,xymc) values (%s,%s)'
sql2 = 'insert into tc_kc (teacherid,kcbh,jslx) values (%s,%s,%s)'
for item in kcbh:
    try:
        data['kcbh'] = item
        r = requests.post(url, data=data)
        text = json.loads(r.text)
        team = text['data']['member']
        for one in team:
            try:
                #1.插入teacher表
                te = (one['xm'],one['xymc'])
                cusor.execute(sql1,te)
                teacherid = conn.insert_id()
                conn.commit()
                #2.插入teacher与课程的关系表
                te2 = (teacherid,item,one['jslx'])
                cusor.execute(sql2,te2)
                conn.commit()
            except BaseException:
                print("---Duplicate entry---")
    except BaseException:
        pass




cusor.close()
conn.close()
