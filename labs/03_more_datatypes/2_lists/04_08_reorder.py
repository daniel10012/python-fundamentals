i = 0
list = []

while i < 10:
    list.append(int(input("input a number")))
    i += 1



# l = [1,2,3,4,5,6,7,8,9,10]


l1 = (list[1::2])
l2 = (list[8::-2])

l3 = l1 + l2

print (*l3, sep = ", ")



'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''