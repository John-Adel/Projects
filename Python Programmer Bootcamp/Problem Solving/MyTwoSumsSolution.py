# Two Sum problem
# You have an list of integers, return the indices of the pair of integers that add up to a given target
# Each input has one solution,
# Example [8,6,11,3] target 9 return [1,3]

def two_sum_list(num_list, target):
    for i in range(len(num_list)):
        if target - num_list[i] in num_list[:i] or target - num_list[i] in num_list[i + 1: ]:
            return [i, num_list.index(target - num_list[i])]
    return -1

print(two_sum_list([-4, -1, 2, 7], -5))
