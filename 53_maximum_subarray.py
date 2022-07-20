# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -999999999

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    if nums[i] > max_sum:
                        max_sum = nums[i]
                if max_sum + nums[j] > max_sum:
                    max_sum += nums[j]
        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5, 4, -1, 7, 8]))

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = -99999999

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums) + 1):
#                 sum_nums = sum(nums[i:j])
#                 if sum_nums > max_sum:
#                     max_sum = sum_nums
#         return max_sum
