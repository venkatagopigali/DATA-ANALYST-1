# print("HELLO")
# try:
#     a=int(input("enter a number    :"))
#     b=int(input("enter a nubrer    :"))
#     print(a/b)
# except ZeroDivisionError:
#     print("plese check denominator")
# except ValueError:
#     print("please check the datatypes")
# print("further logic")


# name='Prasanna'
# try:
#     print(name)
# except NameError:
#     print("please check the spelling")
# print("furthor logic")


# from module_name import function

# import pandas as pd
# try:
#     data=pd.read_csv(r"C:\Users\hp\Desktop\BOOTCAMP\Orders_2024_Jan_Jun.csv")
#     print(data.to_string())
# except FileNotFoundError:
#     print("please check the file location or file name")

# try:
#     a=[10,20,30,40,50]
#     print(a[5])
# except IndexError:
#     print("please check index position")
# print("running next code")

# try:
#     d={"name":'rahul','age':27}
#     print(d['location'])
# except KeyError:
#     print("please check the keys")
# print("next block of code")
try:
    a=int(input("enter a vlaue"))
    # print(b)
    c=[10,20,30,40]
    print(c[2])
    print(10/0)
except Exception as e:
    print(e)
# except ZeroDivisionError:
#     print("zero")
# except ValueError:
#     print('value')
# except IndexError:
#     print("index")
# except NameError:
#     print('name')