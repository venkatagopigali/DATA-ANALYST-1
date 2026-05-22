# class overriding:
#     def cam(self):
#         print("50 pixcel")
#         print("zoom 50meters")
#     def cam(self):
#         print("100 pixcel")
#         print("zoom 100 meters")
# ovr=overriding()
# ovr.cam()


# class dark:
#     def theme(self):
#         print("entire device in dark")
# class white(dark):
#     def theme(self):
#         print("entire device in white")
# print("1.white\n2.dark")
# op=int(input("enter your option"))
# if op==1:
#     a=white()
#     a.theme()
# elif op==2:
#     a=dark()
#     a.theme()



# print(10+20)
# print((10).__add__(20))
# print((10).__sub__(20))   #10-20


class dunder:
    def __init__(self,a):
        self.a=a
        print(self.a)
    def __add__(self,other):
        print(self.a-other.a)
    def __sub__(self,other):
        print(self.a*other.a)
    def __mul__(self,other):
        print(self.a+other.a)
    def __gt__(self,other):
        print(self.a>other.a)
    def __ge__(self,other):
        print(self.a>=other.a)
obj1=dunder(1100)
obj2=dunder(20)
print(obj1>=obj2)

