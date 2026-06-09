# a=[10,20,30,40,2,44,22,22,45,67,2]
def high_ele(a):
    m=0
    for i in range(len(a)):
        if a[i]>m:
            m=a[i]
    print(m)

# a=[10,20,30,40,2,44,22,22,45,2]
# high_ele(a)

def prime(a,b):
    for i in range(a,b+1):
        # print(i)
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(i)