list = []
i = 0

while i < 10:
    
    list.append(int(input("input a new number")))
        i += 1

print (list)


print (max(list))


x = 1

for number in list:
    x *= number

print (x)





'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
