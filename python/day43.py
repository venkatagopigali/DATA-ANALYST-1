import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='gopi@1234',
    database='company'
)
cur=conn.cursor()
while True:
    print("=================================")
    print("           COMPANY               ")
    print("=================================")
    print("1.Admin\n2.Manager\n3.Employee")
    # print("1.Admin")
    # print("2.Manager")
    # print("3.Employee")
    try:
        op=int(input("Enter option   :"))
        if op==1:
            print("=================================")
            print("           ADMIN              ")
            print("=================================")
            print("1.Add manager\n2.Update manager\n3.delete manager\n4.add employee\n5.update employee\n6.delete employee")
            a=int(input("Enter Which want to perform   :"))
            if a==1:
                i=int(input("enter manger id    :"))
                n=input("Enter manager name     :")
                a=int(input("enter manager age  :"))
                d=input("Enter Manager department:")
                cur.execute("insert into manager values(%s,%s,%s,%s)",(i,n,a,d))
                conn.commit()
                print("new manager added")
            elif a==2:
                i=int(input("Eeter manager id      :"))
                n=input("Entee Manager new name    : ")
                cur.execute("update manager set m_name=%s where m_id=%s",(n,i))
                conn.commit()
                print("manager details successfully updated")
            elif a==3:
                i=int(input("Enter your id   :"))
                cur.execute("delete from manager where m_id=%s",(i))
                conn.commit()
                print("manager deleted")            
            elif a==4:
                print("new emp added")
            elif a==5:
                print("updated emp details")
            elif a==6:
                print("emp deleted")
            else:
                print("enter valid option")
        elif op==2:
            print("=================================")
            print("           MANAGER               ")
            print("=================================")
        elif op==3:
            print("=================================")
            print("           EMPLOYEE               ")
            print("=================================")
        else:
            print("please enter valid option")
    except Exception as e:
        print(e)
