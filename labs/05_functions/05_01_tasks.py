'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

def isdivboth(number):
    if number % 4 == 0 and number % 7 == 0:
        div = True
    else:
        div = False

    return div

def isdivor(number):
    if number % 4 == 0 or number % 7 == 0:
        div = True
    else:
        div = False

    return div

def isdivex(number):
    if (number % 4 == 0 and number % 7 != 0) or (number % 4 != 0 and number % 7 == 0) :
        div = True
    else:
        div = False

    return div



print(isdivboth(57))
print(isdivor(49))
print(isdivex(256))