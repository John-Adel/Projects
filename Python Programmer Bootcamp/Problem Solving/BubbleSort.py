def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

import random

# generate a list of 200 random numbers between 1 and 1000
numbers = [random.randint(1, 1000) for _ in range(200)]

print(numbers[:20])  # just preview the first 20
print(bubble_sort(numbers))