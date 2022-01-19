# https://leetcode.com/problems/find-peak-element/


# input
#  1, 2, 3, 1
#  1, 2, 1, 3, 5, 6, 4

num_array = [int(x) for x in input().split(", ")]

print(num_array.index(max(num_array)))
