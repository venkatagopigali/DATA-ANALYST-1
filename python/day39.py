import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='gopi@1234',
    database='py_sql_project'
)
# print(conn)
cur=conn.cursor()   # read the command

# def add_trainer():

def add_student():
    s=int(input("Enter sno of student   :"))
    n=input("Enter student name         :")
    e=input("enter student email        :")
    c=input("enter course               :")
    p=input("enter student password     :")
    ph=input("Enter student phone number:")
    cur.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(s,n,e,c,p,ph))
    conn.commit()
    print("Successfully a new student added")

def see_stu():
    cur.execute("select * from student")
    for i in cur:
        print(i)
    conn.commit()

def delete_student():
    s=int(input("Enter student id     :"))
    cur.execute("delete from student where s_id=%s",(s))
    conn.commit()
    print("successfully student deleted")



while True:
    try:
        print("========================================")
        print("              MyDream                   ")
        print("========================================")
        print("1.Admin\n2.Trainer\n3.Student")
        op=int(input("Who are you     :"))
        if op==1:
            print("================================================")
            print("               WELCOME ADMIN PORTAL")
            print("================================================")
            print("1.add_trainer\n2.delete trainer\n3.see trainer details\n4.add_student\n5.delete student\n6.see student detail")
            op=int(input("Choose which opeartion you want to do   :"))
            if op==1:
                pass
            elif op==2:
                pass
            elif op==3:
                pass
            elif op==4:
                add_student()
            elif op==5:
                delete_student()
            elif op==6:
                see_stu()
            else:
                print("choose correct option   ")
        elif op==2:
            print("================================================")
            print("               WELCOME TRAINER PORTAL")
            print("================================================")
            print("1.add student\n2,see student details")
            op=int(input("Choose your option   :"))
            if op==1:
                add_student()
            elif op==2:
                see_stu()
            else:
                print("choose correct option  :")
        elif op==3:
            print("================================================")
            print("               WELCOME STUDENT PORTAL")
            print("================================================")
        else:
            print("choose correct option    ")
    except Exception as e:
        print(e)