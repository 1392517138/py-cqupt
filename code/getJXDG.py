# @Time    : 2020/5/9 7:42 下午
# @Author  : Aaron
# @Email   : 1392517138@qq.com
# @Desc    : None
import pymysql
import requests
import oss2
import json

# 我自己的备用表
conn = pymysql.connect(host='localhost', port=3306, db='mooc',
                       user='root', password='root')
cusor = conn.cursor()

# kaoyan表
conn1 = pymysql.connect(host='localhost', port=3306, db='graduate',
                        user='root', password='root')
cusor1 = conn1.cursor()

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
# 教学大纲
data1 = {
    "unifyCode": 1,
    "courseNo": "",
    "place": 2
}
data2 = {
    "unifyCode": 1,
    "courseNo": "",
    "type": 1,  # 1是ksdg,5是zsdtx,2是dxfa
    "place": 2
}
# 教学大纲
url1 = 'http://cc.cqupt.edu.cn/queryJXDG'
# 考试大纲、导学方案、知识点体系
url2 = 'http://cc.cqupt.edu.cn/queryAttachment'
# pdf文件url
url3 = 'http://cc.cqupt.edu.cn/CquptCourseCenter/pages/classInfShow/docs/CourseCenterAttachment/'
# 图片地址前缀
url4 = 'https://smart-house-img.oss-cn-beijing.aliyuncs.com/shujuku/course/'
# 插入课程的附件 jxdg/ksdg/zsdtx/dxfa
sql11 = 'insert into jxdg (kcbh,jxdgid) values (%s,%s)'
sql22 = 'insert into ksdg (kcbh,ksdgid) values (%s,%s)'
sql33 = 'insert into zsdtx (kcbh,zsdtxid) values (%s,%s)'
sql44 = 'insert into dxfa (kcbh,dxfaid) values (%s,%s)'

# 插入resource 附件表
sql2 = 'insert into resource (course_id,resource_type,resource_name)  values (%s,%s,%s)'
# pdf - mp4 - other附件表
sql3 = 'insert into pdf (resource_id,pdf_url) values (%s,%s)'
sql4 = 'insert into other (resource_id,other_url) values (%s,%s)'

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('<>', '<>')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, '<>', '<>')

# requests.get返回的是一个可迭代对象（Iterable），此时Python SDK会通过Chunked Encoding方式上传。
# input = requests.get('')
# a = bucket.put_object('shujuku/course/' + '', input)

'''
1.  获取考试大纲
2.  获取考试大纲
3.  获取知识点体系
4.  获取导学方案
'''
type = 'pdf'
jxdgUrl = ''
ksdgUrl = ''
zsdtxUrl = ''
dxfaUrl = ''
originName = ''
resource_id = ''

def kzdMethod(b):
    try:
        global text, originName, input, url, type, digital1, resource_id, digital2, ksdgUrl, zsdtxUrl, dxfaUrl
        r = requests.post(url2, data=data2, headers=headers)
        text = json.loads(r.text)
        #获得一个list
        a = text['data']['list']
        numName = []
        originName = []
        for num in a:
            numName.append(num['fileName'])
            originName.append(num['originName'])
        for i,value in enumerate(numName):
            input = requests.get(url3 + value)
            bucket.put_object('shujuku/course/' + originName[i], input)
            url = url4 + originName[i]
            input = requests.get(url3 + value)
            bucket.put_object('shujuku/course/' + originName[i], input)
            if (a == 1):
                ksdgUrl = url
            elif (a == 5):
                zsdtxUrl = url
            elif (a == 2):
                dxfaUrl = url
            if (originName[i].endswith('.pdf')):
                type = 'pdf'
                digital1 = (item, type, originName[i])
                cusor1.execute(sql2, digital1)
                resource_id = conn1.insert_id()
                conn1.commit()

                digital2 = (resource_id, url)
                cusor1.execute(sql3, digital2)
                conn1.commit()
            else:
                type = 'other'
                digital1 = (item, type, originName[i])
                cusor1.execute(sql2, digital1)
                resource_id = conn1.insert_id()
                conn1.commit()

                digital2 = (resource_id, url)
                cusor1.execute(sql4, digital2)
                conn1.commit()

            if (b == 1):
                cusor.execute(sql22,(item,resource_id))
                conn.commit()
            elif (b == 5):
                cusor.execute(sql33, (item, resource_id))
                conn.commit()
            elif (b == 2):
                cusor.execute(sql44, (item, resource_id))
                conn.commit()
    except BaseException:
        print("--------error----")

# 跳过所有异常

for item in kcbh:
    try:
        # 1. 获取教学大纲
        data1['courseNo'] = item
        r1 = requests.post(url1, data=data1, headers=headers)
        text = json.loads(r1.text)
        jxdgNumName = text['data']['fileName']
        jxdgOriginName = text['data']['originName']
        input = requests.get(url3 + jxdgNumName)
        bucket.put_object('shujuku/course/' + jxdgOriginName, input)
        jxdgUrl = url4 + jxdgOriginName
        if (jxdgOriginName.endswith('.pdf')):
            type = 'pdf'
            digital1 = (item, type, jxdgOriginName)
            cusor1.execute(sql2, digital1)
            resource_id = conn1.insert_id()
            print('---'+str(resource_id))
            conn1.commit()
            digital2 = (resource_id, jxdgUrl)
            cusor1.execute(sql3, digital2)
            conn1.commit()

        else:
            type = 'other'
            digital1 = (item, type, jxdgOriginName)
            cusor1.execute(sql2, digital1)
            resource_id = conn1.insert_id()
            conn1.commit()
            digital2 = (resource_id, jxdgUrl)
            cusor1.execute(sql4, digital2)
            conn1.commit()

        cusor.execute(sql11,(item,resource_id))
        conn.commit()

        data2['courseNo'] = item
        # 2.  获取考试大纲
        data2['type'] = 1
        kzdMethod(1)
        # 3.  获取知识点体系
        data2['type'] = 5
        kzdMethod(5)
        # 4.  获取导学方案
        data2['type'] = 2
        kzdMethod(2)
    except BaseException:
        print("eroor 1111 -------")



# except BaseException:
#     print("error!")


cusor.close()
conn.close()
cusor1.close()
conn1.close()
