# @Time    : 2020/5/9 5:54 下午
# @Author  : Aaron
# @Email   : 1392517138@qq.com
# @Desc    : 获得课程适合的专业
# coding:utf-8
import pymysql
import json
import requests

conn = pymysql.connect(host='127.0.0.1', port=3306, db='mooc',
                       user='root', password='13452078118')
cusor = conn.cursor()
url = "http://cc.cqupt.edu.cn/getCourseMajor"
data = {
    "unifyCode": 1,
    "zyh": 1,
    "count": 100,
    "page": 1
}
headers = {
    "cookie": "JSESSIONID=8843793488DCD16629CCB6B9FF4988C9"
}
# 先拿到所有课程号,放入kcbh
sql = 'select kcbh from moren_kc'
kcbh = []
cusor.execute(sql)
tmp = cusor.fetchall()
for item in tmp:
    kcbh.append(item[0])
conn.commit()
data = {
    "unifyCode": 1,
    "courseNo": "A1040040"
}

url = 'http://cc.cqupt.edu.cn/getCourseMajor'
sql = 'insert into course_major (kcbh,zyh,xyh) values (%s,%s,%s)'
for item in kcbh:
    try:
        data['courseNo'] = item
        r = requests.post(url, data=data)
        text = json.loads(r.text)
        team = text['data']
        for one in team:
            zy = one['zy']
            xyh = one['xyh']
            for two in zy:
                try:
                    # 1.插入teacher表
                    te = (item, two['zyh'], xyh)
                    cusor.execute(sql, te)
                    conn.commit()
                except BaseException:
                    print("2th problem happen!")
    except BaseException:
        print("---1th problem happen!")

cusor.close()
conn.close()
