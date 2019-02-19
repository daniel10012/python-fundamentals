



'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string =input ("input string")

list = string.split(" ")

print(list)

max_oc = 0

for word in list:
    occurences = list.count(word)
    if occurences > max_oc:
        max_oc = occurences
        max_word = word

print(max_word)