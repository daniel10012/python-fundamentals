'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''


def isdivby3 (number):
    remainder = number%3
    if remainder == 0:
        print("yes")
    else:print("no")



isdivby3(27)