# try:
#     a=int(input("enter a values     :"))
#     print(a)
# except Exception as e:   # exception is raised
#     print(e)
# else:
#     print("congratulation there will be no errors")
# finally:
#     print("success")


import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='gopi@1234',
    database='analyst'
)
# print(conn)

cur=conn.cursor()       # will helps to read the commands
cur.execute("select * from emp")  # will excecute commands

for i in cur:
    print(i)
conn.commit()
