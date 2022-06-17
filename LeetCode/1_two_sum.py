# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums) - 1):
            for y in range(i + 1, len(nums)):
                if nums[i] + nums[y] == target:
                    answer.append(i)
                    answer.append(y)
                    return answer


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([3, 2, 3], 6))
