import datetime
from time import sleep
import requests

# response = requests.get("https://github.com")
# if response.status_code == 200:
#     print("All good")
# print(datetime.datetime.now())
# sleep(10)


# Read files
# my_file = open("testhost.txt")
# print(list(my_file.readlines()))
# my_file.seek(0)
# for line in my_file.readlines():
#     print(line.strip())


# Write files

# def save_name(names):
#     my_file = open(names, "a")
#     current_name = input("Please enter name")
#     my_file.write(current_name + "\n")
#     my_file.close()
#
#
# def show_name(names):
#     my_file = open(names, 'r')
#     for name in my_file.readlines():
#         print(name, end="")
#     my_file.close()
#
#
# for i in range(5):
#     save_name('names.txt')
# show_name('names.txt')

# Open configuration file
# import ast
# my_file = open("config.json")
# c = dict(ast.literal_eval(my_file.read()))
# if c["name"] == "Leon":
#     print("Success")

# With fuction
# with open("names.txt") as my_file:
#     for name in my_file.readlines():
#         print(name.strip())

# Errors
# import requests
# print("moshe")
# try:
#     f = int(input("Please enter number: "))
#     r = 5 / 0
# except ZeroDivisionError:
#     print("Could not divide by zero")
# except ValueError:
#     print("Enter a legal number")
# except Exception as e:
#     print("Something went wrong, here is the error")
#     print(e.args)
# print("haim")

# Raising Exceptions
# def get_age():
#     age = int(input("Please enter you age\n"))
#     if age < 0:
#         raise ValueError("age can not be negative")
#
# try:
#     get_age()
# except Exception as e:
#     if e.args[0] == "age can not be negative":
#         print("Its the age")
#     else:
#         print(e)

# Artifex
from artifex2 import get_number
from artifex import sub,addition
#
# a = get_number()
# b = get_number()
# c = addition(a, b)
# d = sub(c, a)
# print(c)
# print(d)

# Decorators
import datetime


def dec(func_name):
    def wrapper():
        print(datetime.datetime.now())
        func_name()
        print(datetime.datetime.now())
    return wrapper

@dec
def print_something():
    print("something")


print_something()


def dima(ruslan):
    print("petsa")
