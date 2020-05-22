import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, db='mooc',
                       user='root', password='13452078118')
cusor = conn.cursor()
sql = "select detail from biaobaiqiang"
cusor.execute(sql)
all = cusor.fetchall()
timelist = []
data = open("detail.txt", "w+")
for i in range(len(all)):
    print(all[i][0], file=data)
data.close()

cusor.close()
conn.close()
