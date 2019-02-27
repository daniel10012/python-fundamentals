'''
Print out every prime number between 1 and 100.

'''

# for i in range(1,101):
#     for j in range(2,i):
#         if i%j == 0:
#             break


def isprime(number):

    if number<2:
        return(false)
    prime_flag= True
    for i in range(2,number):
        if number%i == 0:
            prime_flag = False
            break

    return(prime_flag)



for i in range(2,101):
    if isprime(i):
        print(i)
