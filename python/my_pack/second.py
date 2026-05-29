class Student:
    def cap(self,s):
        s=s.upper()
        print(s)
    def number(self,a,b):
        c=0
        for i in range(a,b):
            if i%2==0:
                c=c+1
        print(c)
