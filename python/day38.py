import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='gopi@1234',
    database='analyst'
)
print(conn)  
cur=conn.cursor()    # to read the commands 
# cur.execute("select * from stu")   # tuple
# for i in cur:
#     print(i)
# conn.commit()
while True:
    print("1.insert data\n2.update data\n3.delete data\n4.view details")
    op=int(input("Enter your optipn   :"))
    if op==1:
        s=int(input("Enter your Sno     :"))
        n=input("Enter your Name     :")
        a=int(input("Enter your Age    :"))
        ad=input("Enter your address     :")
        p=int(input("Enter your phone   :"))

        cur.execute("insert into practice values(%s,%s,%s,%s,%s)",(s,n,a,ad,p))

        conn.commit()     # to store the data periminently
    elif op==2:
        s=int(input("Enter sno which one you want update   :"))
        a=input("Enter your new address : ")

        cur.execute("update practice set address=%s where sno=%s",(a,s))

        conn.commit()
    elif op==3:
        s=int(input("Enter your Sno to delete  : "))

        cur.execute("delete from practice where sno=%s",(s))

        conn.commit()
    elif op==4:
        cur.execute("select * from practice")
        for i in cur:
            print(i)
        conn.commit()