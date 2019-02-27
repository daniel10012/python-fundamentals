'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

a = 1
b = 100

sum_numbers=0

for i in range(a,b+1):
    sum_numbers += i

print(sum_numbers)