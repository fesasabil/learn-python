# A list is exactly what it sounds like, a container that contains different Python objects, which could be integers, words, values, etc. It is the equivalent of an array in other programming languages. It is represented by square brackets (and this is one of the attributes that differentiates it from tuples, which are separated by parentheses). It is also mutable, that is, it can be modified or updated; unlike tuples, which are immutable.

# List slicing

list = [3, 22, 30, 5.3, 20]

# list[:] = [3, 22, 30, 5.3, 20]; # all the members of the list
# list[1:3] = [22, 30]; # members of the list from index 1 to index 3, without the member at index 3
# list[:4] = [3, 22, 30, 5.3]; # members of the list from index 0 to index 4, without the member at index 4
# list[2:-1] = [30, 5.3]; # members of the list from index 2, which is the third element, to the second to the last element in the list, which is 5.3

list[0] = 4
print(list)

del list[0]
# list.remove(3) or
# list.pop[0]
print(list)

list_1 = [3, 5, 7, 8, 9, 20]
list_1.append(3.33)
print(list_1)

list_1.append("cats")
print(list_1)

# List built-in functions (methods)
numbers = [2, 5, 7, 9]
print(len(numbers)) # len(list)

numbers = [2, 5, 7, 9]
print(max(numbers)) # max(list)

numbers = [2, 5, 7, 9]
print(min(numbers)) # min(list)

# animals = (cat, dog, fish, cow)
# print(list(animals)) # tuple(list)

numbers = [2, 5, 7, 9]
numbers.append(15)
print(numbers) # append(list)

numbers = [2, 5, 7, 9, 15]
numbers.pop(2)
print(numbers) # pop(list)

values = [2, 5, 7, 9]
values.remove(2)
print(values) # remove(list)

values = [2, 5, 7, 10]
values.reverse()
print(values) # reverse(list)

animals = ['cat', 'dog', 'fish', 'cow', 'goat']
fish_index = animals.index('fish')
print(fish_index) # index(list)

values = [2, 5, 10]
sum_of_values = sum(values)
print(sum_of_values) # sum(list)

values = [1, 7, 9, 3, 5]
# To sort the values in ascending order:
values.sort()
print(values) # sort(list)

values = [2, 10, 7, 14, 50]
# To sort the values in descending order:
values.sort(reverse = True)
print(values)

# to sort the list by length of the elements
strings = ['cat', 'mammal', 'goat', 'is']
sort_by_alphabet = strings.sort()
sort_by_length = strings.sort(key = len)
print(sort_by_alphabet)
print(sort_by_length)


# Looping through lists
list = [10, 20, 30, 40, 50, 60, 70]
for elem in list:
        elem = elem + 5
        print(elem)

for elem in list[:3]:
    list.remove(elem)
    print(elem)