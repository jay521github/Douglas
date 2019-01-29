import pymysql
db=pymysql.connect(host="172.17.15.63",port=3306,user="bwol_qsteach_dev",passwd="bwol_qsteach_dev",db="bwol_qsteach_dev",charset="utf8")
cursor=db.cursor()
sql="SELECT * FROM teacher WHERE NAME_CN='商超'"
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    for row in data:
        LOGIN_NAME=row[4]
        PASSWORD=row[5]
        print("账号：%s"%LOGIN_NAME ,"密码:%s"%PASSWORD)
except:
    print("Error :%s"% '没有这位老师 ')

db.close()