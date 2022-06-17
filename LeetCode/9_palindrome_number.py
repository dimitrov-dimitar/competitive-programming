# https://leetcode.com/problems/palindrome-number/

from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
