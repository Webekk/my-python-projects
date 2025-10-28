import collections
from itertools import count
from typing import Collection

my_list = [10, 20, 30, 40, 50]
print(my_list[4])
print(f"Length of the list: {len(my_list)}")
if len(my_list) == 0:
    print("Empty list")
else:
    print("List is not empty")

my_list[2] = 200
print(f"After changing second element {my_list}")
my_list.append(600)
print(f"After appending 600: {my_list}")
my_list.insert(2, 300)
print(f"After inserting 400: {my_list}")
my_list.remove(600)
print(f"After removing 600 (by value): {my_list}")
del my_list[0]
print(f"After removing element at index 0: {my_list}")

my_second_list = [10, 20, 30, 40, 50]
adding = 0
for item in my_second_list:
    adding += item
print("Sum: ", adding)
print(f"Average: {adding / len(my_second_list)}")

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

numbers = [1,2,3,4,5,6,7]
result = []
for number in numbers:
   result.append(number * number)

print(result)


data = [8, 2, 15, 1, 9]

print(f"Largest number:{max(data)}" )
print(f"Smallest number:{min(data)}" )

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']

print(sports.count("Football"))

number_list = [5,2,8,1,9]
print(f"Original list: {number_list}")
number_list.sort()
print(f"Sorted list: {number_list}")

list_copy = [10,20,30]
copy_of_a_list = list_copy.copy()
copy_of_a_list[0] = 23
print(list_copy)
print(copy_of_a_list)

third_copy = list_copy[:]

third_copy.append(100)
print(third_copy)

list_a = [1,2]
list_b = [3,4]
list_c = list_a + list_b

print(list_c)


combined_list_unpacking = [*list_a, *list_b]
print(combined_list_unpacking)

def empty_space(empty):
    return empty != ""

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
filtered_list1 = filter(empty_space,list1)
print(list(filtered_list1))

res = list(filter(None, list1))
print(res)

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
no_duplicates = set(list_with_duplicates)
list_with_duplicates = list(no_duplicates)
print(list_with_duplicates)


def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]


list_occurences = [20, 5, 20, 15, 20, 25, 50, 20]
occurence = remove_value(list_occurences, 20)
print(occurence)

for occurence in list_occurences:
    if occurence == 20:
        list_occurences.remove(occurence)
print(list_occurences)
print("Sprawdz wynik")


numbers = [1,2,3,4,5,6,7]
squares = [n * n for n in numbers]
print(numbers)
print(squares)

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
only_numbers_list = [numbers for numbers in my_list if isinstance(numbers, (int, float)) ]
print(only_numbers_list)


nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print(nested_list[1][1])
print("Yo" + str(5))