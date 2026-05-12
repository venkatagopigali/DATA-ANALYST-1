# def cal(a=10,b=30):
#     print(a)
#     print(b)
#     print(a*b)
#     print(a/b)

# cal(90)


# def cal(a,b):
#     print(a)
#     print(b)
# cal(b=20,a=10)

'''def cal(*a):
    print(a)
    print(sum(a))
cal(30,40,10,40,'prasanna')'''


# a=(30,40,10,40,'prasanna',30.9)
# s=0
# for i in a:
#     if type(i)==int or type(i)==float:
#         s=s+i
# print(s)


# def cal(*a):
#     print(a)
#     s=0
#     for i in a:
#         if type(i)==int or type(i)==float:
#             s=s+i
#     print(s)
# cal(30,40,10,40,'prasanna')

# cal(10,'prasanna','rahul','ramesh','suresh')

# cal(10,20,40,6,55,5)



def dic(**a):
    # print(a.items())
    d={}
    for i,j in a.items():
        d[j]=i
    print(d)
dic(name='rahul',age=28,location='USA')
dic(name='prasanna',course='data science')
dic(a=1,b=2,c=3,d=4,e=5)