# class ploy:
#     def data(self,a,b):
#         print(a+b)
# obj=ploy()
# obj.data(10,20)              # addition
# obj.data('python','java')    # str concatination
# obj.data([10,20,30],[40,50,60]) #extend



## duck typing

# class duck:
#     def color(self):
#         print("white color")
#     def hobbies(self):
#         print("swimming")
# class bird:
#     def color(self):
#         print("balck color")
#     def hobbies(self):
#         print("flying")

# ### obj=class_name()
# def duck_typing(obj):
#     obj.color()
#     obj.hobbies()
# duck_typing(duck())
# duck_typing(bird())

## overloading

# class overloading:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
#     def add(self,a,b,c,d):
#         print(a+b+c+d)
# ovl=overloading()
# ovl.add(10,20,30,40)
# ovl.add(10,20)

# in java 
#add(10,20)
#add(10,20,30)
#add(10,20,3040)


# a=10
# b=20
# a=30
# print(a)


# def over(*a):
#     print(a)
# over(10,20)
# over(10,20,30)

class loading:
    def add(self,*a):
        s=0
        for i in a:
            s=s+i
        print(s)
l=loading()
l.add(10,20)
l.add(10,20)
l.add(10,20,30)
l.add(10,20,30,40)