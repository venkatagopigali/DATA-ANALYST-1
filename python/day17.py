

# a=[1,2,3,4,5,6,'python','java']
# print(a[6])
# print(a[-5])


# a=[1,2,3,4,5,6,'python','java']
# print(a[2:7:2])
# print(a[1::3])

# a=[1,2,3,[10,11,12],67,[99,88]]
# print(a[-2])
# print(a[4])
# print(a[3][0])
# print(a[5][1])


# l=[1,2,3,66,77]
# l.append(100)
# print(l)


# l=[1,2,3,66,77]
# l.extend([55,88,99])
# print(l)

# a=[1,2,3,66,77]
# a.append([55,88,99])
# print(a)

# a=[1,2,3,66,77]
# a.insert(2,88)
# print(a)


# l=[10,20,30,40,50]
# l.insert(1,'python')
# l.insert(-3,'java')
# l.insert(-4,'hello')
# print(l)

# a=[10,20,30,40]
# a.insert(3,['python','java','hello'])
# print(a)

# a=[10,20,30,40,'hello']
# a.remove('hello')
# a.pop()
# a.pop(2)
# print(a)

# a=[10,20,30,40,'hello',89,90,77,22]  #22,77,90,89
# a.reverse()
# print(a)
# print(len(a))

# l=[10,20,30,30,50,30,'hello',77]
# print(l.count(88))

a=[10,20,30,5,6,7,66,33]
h=0
for i in a:
    if i>h:
        h=i
print(h)