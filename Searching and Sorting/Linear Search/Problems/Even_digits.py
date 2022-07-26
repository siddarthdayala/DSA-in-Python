# Leetcode link - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if int(math.log(i,10)+1)%2 == 0:    #log10 returns the number of digits in a number
                count+=1
        return count
