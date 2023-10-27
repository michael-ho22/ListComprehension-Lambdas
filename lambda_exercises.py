''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = list(filter(lambda num: (num % 2 == 0), num_list))
print(even_nums)

odd_nums = list(filter(lambda num: (num % 2 != 0), num_list))
print(odd_nums)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


filtered_days = list(filter(lambda days: len(days) == 6, weekdays))
print(filtered_days)






''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']

filtered_list = list(filter(lambda word: word != 'orange' and word != 'black', original_list))
print(filtered_list)

# or

# original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
# remove_words = ['orange', 'black']
#  filtered_list = list(filter(lambda word: word not in remove, original_list))
# print(filtered_list)







''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list(filter(lambda nums: nums not in list2, list1))
print(new_list)




''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

original_list = ['red', 'black', 'white', 'green', 'orange']

fun_filters = list(filter(lambda color: 'ack' in color, original_list))
print(fun_filters)

fun_filters = list(filter(lambda color: 'abc' in color, original_list))
print(fun_filters)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"


verify = lambda string: any([y.isupper() for y in string] and 
                            [y.islower() for y in string] and 
                            [y.isdigit() for y in string] and 
                            [len(string) > 7])
print(verify(str1))








''' 7)
Write a Python program to sort a list of tuples using Lambda.

lambda with sort

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

original_scores.sort(key=lambda x: x[1])
print(original_scores)