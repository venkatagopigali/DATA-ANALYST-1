def example(a):
    c=0
    for i in a:
        c=c+1
    print(c)

def even(a):
    # print(a)
    l1=[]
    for i in a:
        if i%2==0:
            l1.append(i)
    print(l1)

# l=[10,20,30,40,11,33,23]
# even(l)

# l=[10,20,30,40,11,21]
# for i in l:
#     if i%2==0:
#         print(i)

def highest(a):      #a=[10,20,30,40,50,60,70]
    m=0
    for i in a:
        if type(i)==int or type(i)==float:
            if i>m:
                m=i
    print(m)

# l=[10,20,11,12,40,50,9]
# highest(l)

















# def example(a,b):
#     print(a+b)
# l=10
# l1=20
# example(l,l1)
