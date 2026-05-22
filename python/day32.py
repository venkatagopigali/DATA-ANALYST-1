# class A:
#     def add(self):
#         # self.a=a
#         print("first class method")
#     def sub(self):
#         print("outside method",self.a)
# class B(A):
#     def mul(self):
#         super().add()
#         print("mul")
# # obj=A()
# # obj.add(10)
# # obj.sub()

# obj=B()
# obj.mul()
# # obj.add(10)
# # obj.sub()


# class phone:
#     def security(self):   # instanec metod
#         print("verifying the password")
# class apps(phone):
#     def instagram(self):
#         super().security()
#         print("open insta")
#     def whatsapp(self):
#         super().security()
#         print("open whats app")
#     def cam(self):
#         print('open camera')

# o=apps()
# o.instagram()  
# o.whatsapp()
# o.cam()


# class bank:
#     username="rahul"
#     password=12345

#     @classmethod        
#     def update(cls):
#         cls.password=345678
#         cls.username='RAHUL'


#     def display(self):
#         print("username     :",bank.username)
#         print("password     :",bank.password)
# b=bank()
# b.update()
# b.display()

# class sta:

#     @staticmethod
#     def add(a,b):
#         # self.a=a
#         # self.b=b
#         # print("inside method ",self.a+self.b)
#         print(a+b)
#     # def sub(self):
#     #     print("outside method",self.a+self.b)
# s=sta()
# s.add(10,20)
# # s.sub()


class A:
    def sub(self):
        print("a class method")
class B:
    def add(self):
        print(" b class method")
class c(B,A):
    def mul(self):
        print("c class method")
obj=c()
print(c.mro())
print(c.__mro__)