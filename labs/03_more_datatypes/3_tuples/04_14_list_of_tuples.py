'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

string = "hello world"

words = string.split(" ")

print (words)


result =[]
for word in words:
    letters = []
    for letter in word:
        letters.append(letter)
        t = tuple(letters)
    result.append(t)

print (result)