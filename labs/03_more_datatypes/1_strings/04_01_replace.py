
string = input("input a string")
symbol = input("input a symbol")

first_letter = string[:1]


new_string = string.replace(first_letter,symbol)

print new_string

'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

