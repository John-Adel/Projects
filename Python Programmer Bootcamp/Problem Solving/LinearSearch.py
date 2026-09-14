def linear_search(element, the_list):
    count = 0
    for i in the_list:
        if i == element:
            print(count)
            return True
        count += 1
    print(count)
    return False

numbers = [3, 8, 15, 27, 42, 56, 72, 91]
target_in = 42     # ✅ exists in the list
target_out = 100   # ❌ not in the list

print(linear_search(target_in, numbers))
print(linear_search(target_out, numbers))