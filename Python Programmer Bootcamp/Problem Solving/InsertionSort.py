def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j != - 1:
            if key < unsorted_list[j]:
                unsorted_list.insert(j, unsorted_list.pop(unsorted_list.index(key)))
            j -= 1

    return unsorted_list
l = [42, 7, 99, 18, 3, 56, 23, 81, 12, 37]
print(insertion_sort(l))


