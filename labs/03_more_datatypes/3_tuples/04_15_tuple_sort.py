'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''




unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]



def second_element(t):
    return t[1]


sorted_list = sorted(unsorted_list, key = second_element)

print(sorted_list)

sorted_list = sorted(unsorted_list, key=lambda x: x[1])

print(sorted_list)







# for i in range(0,len(unsorted_list)):
#     number = unsorted_list[i][1]
#     for j in range(i+1,len(unsorted_list)):
#         if number <= unsorted_list[j][1]:
#             min_num =number
#         else:
#             min_num = unsorted_list[j][1]
#     sorted_list[i] = unsorted_list[i]
#     print(number)



