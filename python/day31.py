# class a:
#     def add(self):
#         print("add method")
#     def __sub(self):
#         print("sub method")
# class b(a):
#     def mul(self):
#         print("mul method")
#     def div(self):
#         print("div method")

# obj = b()
# obj.add()
# obj.__sub()



# class A:
#     b=10               # public
#     def add(self):
#         print("same calss same method ",A.b)
#     def sub(self):
#         pass
# class B:
#     def mul(self):
#         print("differnt calss different method ",A.b)
# obj1=A()
# obj2=B()
# obj1.add()
# obj2.mul()
# print("out of class",obj1.b)

# class A:
#     _b=10                # protected     
#     def add(self):
#         print("same calss same method ",A._b)
#     def sub(self):
#         pass
# class B(A):
#     def mul(self):
#         print("differnt calss different method ",A._b)
# obj1=A()
# obj2=B()
# obj1.add()
# obj2.mul()

# class A:
#     __b=10                # private  
#     def add(self):
#         print("same calss same method ",A.__b)
#     def sub(self):
#         pass
# class B(A):
#     def mul(self):
#         print("differnt calss different method ",A.__b)
# obj1=A()
# obj2=B()
# obj1.add()
# obj2.mul()



# class A:
#     __b=10                # private  
#     def add(self):
#         print("same calss same method ",A.__b)
#     def sub(self):
#         pass
# class B(A):
#     def mul(self):
#         print("differnt calss different method ",A._A__b)     # name mangling
# obj1=A()
# obj2=B()
# obj1.add()
# obj2.mul()


# class iphone:
#     def cam(self):
#         print("cam features")
#     def __security(self):
#         print("security ferauers")
# class dummy(iphone):
#     def camera(self):
#         print("new fetaure")
# d=dummy()
# d.cam()
# d.__security()