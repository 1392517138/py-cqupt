#coding:utf-8
import pymysql
import json
import requests
"""
获取交叉通识课程
"""
conn = pymysql.connect(host='127.0.0.1', port=3306, db='mooc',
                       user='root', password='13452078118')
cusor = conn.cursor()
url = "http://cc.cqupt.edu.cn/getAllJctsk"
data = {
    "unifyCode":1,
    "page":1,
    "count":12
}
headers = {
    "cookie": "JSESSIONID=8843793488DCD16629CCB6B9FF4988C9"
}
tpurl = []
kcbh = []
kcpf = []
kcjs = []
kkxymc = []
xs = []
kcmc = []
xf = []
jysmc = []


#遍历所有页
for i in range (1,28):
    data["page"] = i
    r = requests.post(url, data=data, headers=headers)

    text = json.loads(r.text)
    courseList = text['data']['courseList']


    for item in courseList:
        try:
            if (item['tpurl'] == ""):
                tpurl.append("null")
            else:
                tpurl.append("http://cc.cqupt.edu.cn/upload/PIC/"+item['tpurl'])

            kcbh.append(item['kcbh'])
            kcpf.append(item['kcpf'])
            kcjs.append(item['kcjs'])
            kkxymc.append(item['kkxymc'])
            xs.append(item['xs'])
            xf.append(item['xf'])
            jysmc.append(item['jysmc'])
            kcmc.append(item['kcmc'])
        except BaseException:
            print("-----keyError")


sql = 'insert into all_jctsk (kcbh,kcmc,kcpf,kcjs,kkxymc,xs,xf,jysmc,tpurl) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# print(len(kcbh))
# print(len(kcmc))
# print(len(kcpf))
# print(len(kcjs))
# print(len(kkxymc))
# print(len(xs))
# print(len(xf))
# print(len(jysmc))
# print(len(tpurl))
#
for i in range(len(xf)):
    data = (kcbh[i],kcmc[i],kcpf[i],kcjs[i],kkxymc[i],xs[i],xf[i],jysmc[i],tpurl[i])
    cusor.execute(sql,data)
    conn.commit()


cusor.close()
conn.close()
