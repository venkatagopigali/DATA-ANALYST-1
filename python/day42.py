import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='gopi@1234',
    database='analyst'
)
## cursor :-- will read the command
cur=conn.cursor()
## excecute :-- will run the query
# cur.execute("select * from stu") 
# print(cur)
# for i in cur:
#     print(i)
# conn.commit()
while True:
    print("1.insert\n2.update\n3.delete\n4.view")
    op=int(input("enter your option : "))
    if op==1:
        s=int(input("Enter your sno  :"))
        n=input("Enter your name     :")
        a=int(input("Entre your age  :"))
        l=input("Enter your location :")
        cur.execute("insert into stu values(%s,%s,%s,%s)",(s,n,a,l))
        conn.commit()
        print("data inserted")
    elif op==2:
        s=int(input("Enter your sno   :--"))
        new_name=input("Enter your new_name   :--")
        cur.execute("update stu set name=%s where sno=%s",(new_name,s))
        conn.commit()
        print("data updated")
    elif op==3:
        s=int(input("Entre your sno   :-- "))
        cur.execute("delete from stu where sno=%s",(s))
        conn.commit()
        print("data deleted")
    elif op==4:
        cur.execute("select * from stu")
        for i in cur:
            print(i)
        conn.commit()
        print("view")