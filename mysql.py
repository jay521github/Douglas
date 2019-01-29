import pymysql
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# 打开数据库连接
db = pymysql.connect(host="172.17.15.63",port=3306,user="bwol_qsteach_dev",passwd="bwol_qsteach_dev",db="bwol_qsteach_dev",charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#sql查询
sql="SELECT CLASS_NAME_CN FROM `bwol_qsteach_dev`.`classes` WHERE `JW_SCHOOL_ID` = '2' LIMIT 0, 5"
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       LOGIN_NAME = row[0]
#       PASSWORD = row[0]
#        # 打印结果
#       print("账号%S"%LOGIN_NAME,"密码%s"%PASSWORD)
# except:
#    print ("Error: unable to fetch data")
cursor.execute(sql)
data=cursor.fetchall()
print(data)

# 关闭数据库连接
db.close()