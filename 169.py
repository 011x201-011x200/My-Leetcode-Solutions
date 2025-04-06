"""169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = 0
        c = None
        for num in nums:
            if n == 0:
                c = num
            n += (1 if num == c else -1)
        return c