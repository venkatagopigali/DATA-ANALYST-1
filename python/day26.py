
# #
# a=10                       # global variable
# class example:
#     def __init__(self):
#         print("welcome to oops")
#         print("inside class ",a)
#     def add(self):              # methods
#         print("it is method")
#         print("inside methods",a)

# def nice():      # function
#     print("this is function")
#     print("inside function",a)

# o=example()
# o.add()
# #function calling
# nice()
# print("outside class mrthod and function",a)



## local variable
# class example1:
#     def add(self):
#         b=20         # local variable
#         print(b)
#     def sub(self):
#         b=40
#         print(b)

# def hello():
#     a=10
#     print("inside function",a)
# hello()

# obj=example1()
# obj.add()
# obj.sub()


## class variable

# class example2:
#     a=10            # class variable
#     def add(self):
#         print(example2.a)
#     def sub(self):
#         print(example2.a)
#     print('outside methods',a)
# obj=example2()
# obj.add()
# obj.sub()


## instance variable
# name="python"          # global variable
# class example3:
#     c=50                   # class variable
#     def add(self,a,b):
#         self.a=a         # instance variable
#         self.b=b         # instance variable
#         d=90             # local variable
#         print("in add block")
#         print(self.a)
#         print(self.b)
#         print(example3.c)
#         print(d)
#     def sub(self):
#         print("in sub block")
#         print(self.a)
#         print(self.b)
#         print(example3.c)
#     print("outside metods",c)
# obj=example3()
# obj.add(10,20)
# obj.sub()