# t=(10,20,30,40)
# print(t)
# print(type(t))


# a=tuple((10,20,30,40))
# print(a)
# print(type(a))

# a=(10,20,'rahul','python','prasanna',30.6,'rahul',20)
# a[1]=200
# print(a[-5])
# print(a[2:7:1])

a=(10,20,'rahul','python','prasanna',30.6,'rahul',20)
# print(a.index(10))
# print(a.index(30.6))
# print(a.index('rahul'))
# print(a.count(10))
# print(a.count('rahul'))
# print(a.count('prasanna'))


# s=set((10,20,30,40))
# print(s)
# print(type(s))

# s={10,20,30,40}
# print(type(s))

# a={10,20,10.6,'rahul','prasanna',True,10+2j,10,10,10,20,'rahul'}
# for i in a:
#     print(i)


# a={10,20,30,40}
# a.add('python')
# print(a)


a='rahul'  #RAHUL

# print(ord('a'))
# print(ord('A'))
# print(ord('r'))   # -- R  
# print(ord("R"))

# print(ord('a'))
# print(ord("z"))

# print(ord('A'))
# print(ord("Z"))


a='rahul'
s=""
for i in a:
    num=ord(i)
    num=num-32
    s=s+chr(num)
print(s)


# print(ord('r'))
# print(ord('R'))