'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}


dict_3 = dict_1



for key, value in dict_2.items():
    if key in dict_1:
        dict_3[key] = value + dict_1[key]

    else: dict_3[key] = value

print (dict_3)

