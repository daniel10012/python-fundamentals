'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

def month(number):
    if number == 1:
        print("jan")
    elif number == 2:
        print("feb")
    elif number == 3:
        print("mar")
    else:
        print("other")


number = input("imput a number")

month(int(number))