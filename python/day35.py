# from my_pack.first import e_o_s
# from my_pack.second import Student
# l=[1,2,3,4,5,6,7,88,99,55,33,10,20]
# e_o_s(l)

# s="rahul"
# obj=Student()
# obj.cap(s)

# from my_pack.second import Student
# obj=Student()
# a=10
# b=100
# obj.number(a,b)


'''EXCEPTION HANDLING'''


# a=10
# if a>10
#     print("greter")


# a=int(input("Enter data    :"))
# print(a)
# print("next logic")

# a=10
# b=5
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divided with zero please verify")

# a=10
# if a==10:
#     print('same')


# a=10
# try:
#     print(a)
# except NameError:
#     print("please check variable")

try:
    a=int(input("Enter a values :"))
    print(a)
except ValueError:
    print("plase give correct data")