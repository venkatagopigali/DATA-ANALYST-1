# class father:
#     def weight(self):
#         print("70 kgs")
#     def color(self):
#         print("black")
# class mother:
#     def height(self):
#         print("5.8 ft")
#     def hobbies(self):
#         print("watching tv")
#     def color(self):
#         print("white")
# class child(mother,father):
#     def game(self):
#         print("he likes cricket")

# c=child()
# c.game()
# c.hobbies()
# c.color()
# c=child()
# c.game()
# c.height()
# c.color()

# m=mother()
# m.height()




# class parent:
#     def color(self):
#         print("black")
#     def height(self):
#         print("5.8 ft")
# class child1(parent):
#     def hobbies(self):
#         print("playing games")
# class child2(parent):
#     def weight(self):
#         print("65 kgs")

# c1=child1()
# c1.hobbies()
# c1.color()

# c2=child2()
# c2.weight()
# c2.height()

class A:
    def one(self):
        print("first method")
class B(A):
    def two(self):
        print("second method")
class C(A):
    def three(self):
        print("third method")
class D(C,B):
    def four(self):
        print("fouth method")

# obj=D()
# obj.four()
# obj.three()
# obj.two()
# obj.one()


o=B()
o.two()