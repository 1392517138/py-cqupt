# @Time    : 2020/5/9 10:16 上午
# @Author  : Aaron
# @Email   : 1392517138@qq.com
# @Desc    : None
# coding:utf-8
import pymysql
import json
import requests

"""
获取默认课程
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
# 先拿到所有专业号,放入zyh
sql = 'select zyh from zy'
zyh = []
cusor.execute(sql)
tmp = cusor.fetchall()
for item in tmp:
    zyh.append(item[0])
conn.commit()
url = 'http://cc.cqupt.edu.cn/getAllKcByZyh'

tpurl = []
DQZT = []
kcbh = []
kcpf = []
kcjs = []
kkxymc = []
xs = []
kcmc = []
xf = []
jysmc = []
major = []

for bh in zyh:
    # 1.设置编号
    data['zyh'] = bh
    # print(bh)
    # 2.遍历页码
    # for pageI in range(1, 11):
    #     data['page'] = pageI
    r = requests.post(url, data=data, headers=headers)
    # 3.变成字典
    text = json.loads(r.text)
    r = text['data']['courseList']
    for item in r:
        try:
            if (item['tpurl'] == ""):
                tpurl.append("null")
            else:
                tpurl.append("http://cc.cqupt.edu.cn/upload/PIC/" + item['tpurl'])
            kcbh.append(item['kcbh'])
            kcpf.append(item['kcpf'])
            kcjs.append(item['kcjs'])
            kkxymc.append(item['kkxymc'])
            xs.append(item['xs'])
            xf.append(item['xf'])
            jysmc.append(item['jysmc'])
            kcmc.append(item['kcmc'])
            DQZT.append(item['DQZT'])
            major.append(','.join(item['major']))
        except BaseException:
            print("2th problem happen!")

# except BaseException:
#     print("no enough page --> "+str(pageI))
#     #停止页码上加
#     break
print(major)
sql = 'insert into moren_kc (kcbh,DQZT,kcmc,kcpf,kcjs,kkxymc,xs,xf,jysmc,tpurl,major) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# print(len(kcbh))
# print(len(kcmc))
# print(len(kcpf))
# print(len(kcjs))
# print(len(kkxymc))
# print(len(xs))
# print(len(xf))
# print(len(jysmc))
# print(len(tpurl))
# print(len(DQZT))
# print(len(major))
for i in range(len(xf)):
    try:
        data = (kcbh[i], DQZT[i], kcmc[i], kcpf[i], kcjs[i], kkxymc[i], xs[i], xf[i], jysmc[i], tpurl[i], major[i])
        cusor.execute(sql, data)
        conn.commit()
    except BaseException:
        print("---Duplicate entry---")

cusor.close()
conn.close()
