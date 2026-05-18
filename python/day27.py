# class first:
#     def add(self):
#         print("adding numbers")
#         a=10
#         b=20
#         print(a+b)
#     def mul(self):
#         print("mul numbers")
#         a=10
#         b=20
#         print(a*b)

# class second:
#     def sub(self):
#         print("sub numbers")
#         a=10
#         b=20
#         print(a-b)
#     def div(self):
#         print("div numbers")
#         a=10
#         b=20
#         print(a/b)

# obj=first()
# obj.add()
# obj.mul()

# sec=second()
# sec.div()
# sec.sub()

## single level
'''
class whatsapp:      # sof1
    def chatting(self):
        print('code of chatting')
    def status(self):
        print("code for status")
class bussiness(whatsapp):       # sof2
    # def chatting(self):
    #     print('code of chatting')
    # def status(self):
    #     print("code for status")
    def avaible_time(self):
        print("code for availability time")'''

# w=whatsapp()
# w.chatting()
# w.status()

# b=bussiness()
# b.chatting()
# b.status()
# b.avaible_time()

# w=whatsapp()
# w.chatting()
# w.status()
# w.avaible_time()


## multi level

'''class grand_parent:
    def color(self):
        print("white")
    def height(self):
        print('6.0 height')
class parent(grand_parent):
    def hobbies(self):
        print("playing games")
    def weight(self):
        print("70kgs ")
class child(parent):
    def eye(self):
        print("black eyes")'''

# g=grand_parent()
# g.color()
# g.height()
# g.weight()   -- raise error
# g.eye()      -- raise error

# p=parent()
# p.weight()
# p.height()
# p.eye()  -- raising error


# c=child()
# c.eye()
# c.hobbies()
# c.color()

