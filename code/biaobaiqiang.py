#coding:utf-8
import pymysql
import json
"""
抓取表白强信息
"""
conn = pymysql.connect(host='127.0.0.1', port=3306, db='mooc',
                       user='root', password='13452078118')
cusor = conn.cursor()
file = '/Users/piwenjing/Desktop/10'
str = open(file,'r').read()
d = json.loads(str)
list = d['photoList']
shoottime = []
desc = []
for item in list:
    shoottime.append(item['shoottime'])
    desc.append(item['desc'])

sql = 'INSERT INTO biaobaiqiang (upload_time,detail) VALUES (%s,%s)'

for i in range(len(shoottime)):
    data = (shoottime[i],desc[i])
    cusor.execute(sql,data)
    conn.commit()


cusor.close()
conn.close()
